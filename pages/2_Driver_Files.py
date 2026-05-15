import streamlit as st
import sqlite3
import os
import zipfile
import io
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Driver Files | KTS", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #000; color: #00ffcc; }
    .stApp { background-color: #000; }
    .shiny-text { animation: blinker 1.8s linear infinite alternate; color: #00ffcc; text-align: center; font-weight: bold; }
    @keyframes blinker { from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc; } to { opacity: 0.6; } }
    .neon-card { background: rgba(0,255,204,0.1); border: 2px solid #00ffcc; border-radius: 20px; padding: 20px; text-align: center; margin: 10px 0; box-shadow: 0 0 25px rgba(0, 255, 204, 0.3); }
    .stButton>button { background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; border-radius: 10px; border: none !important; }
    .file-row { background: rgba(0,255,204,0.05); border: 1px solid #00ffcc33; border-radius: 10px; padding: 10px; margin: 5px 0; }
    h3 { color: #00ffcc !important; border-bottom: 2px solid #00ffcc; padding-bottom: 5px; }
    label { color: #fff !important; font-weight: bold !important; }
    .stDataFrame { border: 1px solid #00ffcc33; }
    </style>
""", unsafe_allow_html=True)

# ── Storage paths ──────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent / "driver_storage"
DB_PATH  = BASE_DIR / "drivers.db"
BASE_DIR.mkdir(exist_ok=True)

FILE_LABELS = [
    "رخصة القيادة",          # 1
    "الهوية الوطنية",        # 2
    "الإقامة",               # 3
    "الفحص الطبي",           # 4
    "عقد العمل",             # 5
    "السيرة الذاتية",        # 6
    "شهادة الخبرة",          # 7
    "تأمين المركبة",         # 8
    "صورة شخصية",            # 9
    "وثيقة إضافية",          # 10
]
MAX_FILES = 10

# ── Database setup ─────────────────────────────────────────────────────────────
def get_conn():
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS drivers (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                name      TEXT    NOT NULL,
                driver_id TEXT    NOT NULL UNIQUE,
                phone     TEXT,
                created   TEXT    NOT NULL
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS driver_files (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                driver_id  TEXT    NOT NULL,
                slot       INTEGER NOT NULL,
                label      TEXT    NOT NULL,
                filename   TEXT    NOT NULL,
                filepath   TEXT    NOT NULL,
                uploaded   TEXT    NOT NULL,
                UNIQUE(driver_id, slot)
            )
        """)

init_db()

# ── Helpers ────────────────────────────────────────────────────────────────────
def get_all_drivers():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM drivers ORDER BY name").fetchall()

def get_driver(driver_id):
    with get_conn() as conn:
        return conn.execute("SELECT * FROM drivers WHERE driver_id=?", (driver_id,)).fetchone()

def get_driver_files(driver_id):
    with get_conn() as conn:
        return conn.execute(
            "SELECT * FROM driver_files WHERE driver_id=? ORDER BY slot", (driver_id,)
        ).fetchall()

def add_driver(name, driver_id, phone):
    try:
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO drivers (name, driver_id, phone, created) VALUES (?,?,?,?)",
                (name, driver_id, phone, datetime.now().isoformat())
            )
        return True, "تم إضافة السائق بنجاح"
    except sqlite3.IntegrityError:
        return False, "رقم السائق موجود مسبقاً"

def delete_driver(driver_id):
    files = get_driver_files(driver_id)
    for f in files:
        try:
            os.remove(f["filepath"])
        except FileNotFoundError:
            pass
    with get_conn() as conn:
        conn.execute("DELETE FROM driver_files WHERE driver_id=?", (driver_id,))
        conn.execute("DELETE FROM drivers WHERE driver_id=?", (driver_id,))
    driver_dir = BASE_DIR / driver_id
    if driver_dir.exists() and not any(driver_dir.iterdir()):
        driver_dir.rmdir()

def save_file(driver_id, slot, label, uploaded_file):
    driver_dir = BASE_DIR / driver_id
    driver_dir.mkdir(exist_ok=True)
    ext = Path(uploaded_file.name).suffix
    safe_label = label.replace(" ", "_").replace("/", "-")
    filename = f"slot{slot:02d}_{safe_label}{ext}"
    filepath = driver_dir / filename
    filepath.write_bytes(uploaded_file.read())
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO driver_files (driver_id, slot, label, filename, filepath, uploaded)
            VALUES (?,?,?,?,?,?)
            ON CONFLICT(driver_id, slot) DO UPDATE SET
              label=excluded.label, filename=excluded.filename,
              filepath=excluded.filepath, uploaded=excluded.uploaded
        """, (driver_id, slot, label, filename, str(filepath), datetime.now().isoformat()))

def delete_file(driver_id, slot):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT filepath FROM driver_files WHERE driver_id=? AND slot=?", (driver_id, slot)
        ).fetchone()
        if row:
            try:
                os.remove(row["filepath"])
            except FileNotFoundError:
                pass
            conn.execute("DELETE FROM driver_files WHERE driver_id=? AND slot=?", (driver_id, slot))

def build_zip(driver_id):
    files = get_driver_files(driver_id)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            fp = Path(f["filepath"])
            if fp.exists():
                zf.write(fp, f"{f['slot']:02d}_{f['label']}{fp.suffix}")
    buf.seek(0)
    return buf

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<h1 class="shiny-text" style="font-size:42px;">ملفات السائقين</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>نظام إدارة ملفات السائقين | KTS © 2026</p>", unsafe_allow_html=True)

# ── Sidebar: stats ─────────────────────────────────────────────────────────────
drivers = get_all_drivers()
with st.sidebar:
    st.markdown("### إحصائيات")
    st.metric("إجمالي السائقين", len(drivers))
    if drivers:
        total_files = sum(
            len(get_driver_files(d["driver_id"])) for d in drivers
        )
        st.metric("إجمالي الملفات", total_files)
    st.markdown("---")

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab_browse, tab_add, tab_upload = st.tabs([
    "📁 تصفح السائقين",
    "➕ إضافة سائق",
    "⬆️ رفع ملفات",
])

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1 – BROWSE & DOWNLOAD
# ═══════════════════════════════════════════════════════════════════════════════
with tab_browse:
    st.markdown("### البحث عن سائق")
    search = st.text_input("ابحث بالاسم أو رقم السائق", placeholder="اكتب للبحث...")

    filtered = [
        d for d in drivers
        if not search
        or search.lower() in d["name"].lower()
        or search.lower() in d["driver_id"].lower()
    ]

    if not filtered:
        st.info("لا يوجد سائقون مطابقون.")
    else:
        st.markdown(f"**{len(filtered)} سائق**")
        for drv in filtered:
            files = get_driver_files(drv["driver_id"])
            file_count = len(files)
            with st.expander(f"🚗  {drv['name']}  —  {drv['driver_id']}  ({file_count}/{MAX_FILES} ملف)"):
                col_info, col_actions = st.columns([2, 1])

                with col_info:
                    st.markdown(f"**الاسم:** {drv['name']}")
                    st.markdown(f"**رقم السائق:** `{drv['driver_id']}`")
                    if drv["phone"]:
                        st.markdown(f"**الجوال:** {drv['phone']}")
                    st.markdown(f"**تاريخ الإضافة:** {drv['created'][:10]}")

                with col_actions:
                    # Download all as ZIP
                    if file_count > 0:
                        zip_buf = build_zip(drv["driver_id"])
                        st.download_button(
                            label=f"⬇️ تحميل جميع الملفات ({file_count})",
                            data=zip_buf,
                            file_name=f"{drv['driver_id']}_{drv['name']}_files.zip",
                            mime="application/zip",
                            key=f"zip_{drv['driver_id']}",
                        )
                    else:
                        st.warning("لا توجد ملفات بعد")

                # Individual file downloads
                if files:
                    st.markdown("#### الملفات الفردية")
                    for f in files:
                        fp = Path(f["filepath"])
                        if fp.exists():
                            file_bytes = fp.read_bytes()
                            ext = fp.suffix.lower()
                            mime = (
                                "application/pdf" if ext == ".pdf"
                                else "image/jpeg" if ext in (".jpg", ".jpeg")
                                else "image/png" if ext == ".png"
                                else "application/octet-stream"
                            )
                            fcol1, fcol2, fcol3 = st.columns([3, 2, 1])
                            fcol1.markdown(f"**{f['slot']:02d}. {f['label']}**")
                            fcol2.caption(f["filename"])
                            fcol3.download_button(
                                label="⬇️",
                                data=file_bytes,
                                file_name=f["filename"],
                                mime=mime,
                                key=f"dl_{drv['driver_id']}_{f['slot']}",
                            )

                # Danger zone
                with st.expander("⚠️ حذف السائق"):
                    st.warning("سيتم حذف السائق وجميع ملفاته نهائياً")
                    if st.button("تأكيد الحذف", key=f"del_{drv['driver_id']}"):
                        delete_driver(drv["driver_id"])
                        st.success("تم الحذف")
                        st.rerun()

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2 – ADD DRIVER
# ═══════════════════════════════════════════════════════════════════════════════
with tab_add:
    st.markdown("### إضافة سائق جديد")
    with st.form("add_driver_form", clear_on_submit=True):
        a1, a2, a3 = st.columns(3)
        new_name  = a1.text_input("اسم السائق *")
        new_id    = a2.text_input("رقم السائق *", placeholder="مثال: DRV-0001")
        new_phone = a3.text_input("رقم الجوال")
        submitted = st.form_submit_button("إضافة السائق")
        if submitted:
            if not new_name or not new_id:
                st.error("الاسم ورقم السائق مطلوبان")
            else:
                ok, msg = add_driver(new_name.strip(), new_id.strip(), new_phone.strip())
                if ok:
                    st.success(msg)
                    st.rerun()
                else:
                    st.error(msg)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3 – UPLOAD FILES
# ═══════════════════════════════════════════════════════════════════════════════
with tab_upload:
    st.markdown("### رفع ملفات السائق")

    if not drivers:
        st.info("أضف سائقاً أولاً من تبويب 'إضافة سائق'")
    else:
        driver_options = {f"{d['name']} — {d['driver_id']}": d["driver_id"] for d in drivers}
        selected_label = st.selectbox("اختر السائق", list(driver_options.keys()))
        sel_driver_id  = driver_options[selected_label]
        existing_files = {f["slot"]: f for f in get_driver_files(sel_driver_id)}

        st.markdown("---")
        st.markdown(f"**الملفات الحالية: {len(existing_files)}/{MAX_FILES}**")

        for slot, label in enumerate(FILE_LABELS, start=1):
            col_label, col_status, col_upload, col_del = st.columns([2, 1, 3, 1])
            col_label.markdown(f"**{slot:02d}. {label}**")

            if slot in existing_files:
                col_status.markdown("✅")
                col_upload.caption(existing_files[slot]["filename"])
                if col_del.button("🗑️", key=f"rm_{sel_driver_id}_{slot}", help="حذف الملف"):
                    delete_file(sel_driver_id, slot)
                    st.rerun()
            else:
                col_status.markdown("⬜")
                uploaded = col_upload.file_uploader(
                    f"رفع {label}",
                    key=f"up_{sel_driver_id}_{slot}",
                    label_visibility="collapsed",
                    type=["pdf", "jpg", "jpeg", "png", "doc", "docx"],
                )
                if uploaded:
                    save_file(sel_driver_id, slot, label, uploaded)
                    st.success(f"تم رفع: {label}")
                    st.rerun()

        st.markdown("---")
        updated_files = get_driver_files(sel_driver_id)
        if updated_files:
            zip_buf = build_zip(sel_driver_id)
            st.download_button(
                label=f"⬇️ تحميل جميع الملفات كـ ZIP ({len(updated_files)} ملف)",
                data=zip_buf,
                file_name=f"{sel_driver_id}_all_files.zip",
                mime="application/zip",
                key="zip_upload_tab",
            )

st.markdown("<div style='text-align:center; border-top:2px solid #00ffcc; padding:15px; color:#00ffcc;'>KTS Driver Files System © 2026</div>", unsafe_allow_html=True)
