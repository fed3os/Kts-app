import streamlit as st
from datetime import datetime
import pandas as pd
import io

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="KTS Legend | Ahmed Mugali", layout="centered")

# --- 2. التصميم الملكي (Neon Style) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #000; color: #00ffcc; }
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.92)), 
        url("data:image/svg+xml,%3Csvg width='150' height='150' viewBox='0 0 150 150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='30' fill='rgba(0, 255, 204, 0.12)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }
    .shiny-text { animation: blinker 1.8s linear infinite alternate; color: #00ffcc; text-align: center; font-weight: bold; }
    @keyframes blinker { from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc, 0 0 30px #00ffcc; } to { opacity: 0.6; } }
    .st-expander { background-color: rgba(0, 255, 204, 0.05) !important; border: 1px solid #00ffcc !important; border-radius: 15px !important; margin-bottom: 10px !important; }
    label { color: #ffffff !important; font-size: 16px !important; font-weight: bold !important; text-shadow: 2px 2px 4px #000; }
    .stNumberInput input, .stTextInput input { background-color: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; font-size: 18px !important; border-radius: 10px !important; }
    .neon-card { background: rgba(0,255,204,0.1); border: 2px solid #00ffcc; border-radius: 20px; padding: 25px; text-align: center; margin: 20px 0; box-shadow: 0 0 20px rgba(0, 255, 204, 0.2); }
    .stButton>button { width: 100%; height: 75px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 26px; border-radius: 15px; box-shadow: 0 0 25px #00ffcc; border: none !important; }
    h3 { color: #00ffcc !important; border-bottom: 1px solid #00ffcc; padding-bottom: 5px; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. الهيدر ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 55px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Exclusively Prepared by Ahmed Mugali © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. معلومات المشروع الأساسية ---
rig_name = st.text_input("Rig Name / Number", placeholder="Enter Rig Name")
location_name = st.text_input("Project Location", placeholder="Enter Destination")
dist = st.number_input("Rig Move Distance (KM)", value=0)
d_price = st.number_input("Diesel Price (Per Litre)", value=1.70, format="%.2f")

st.write("---")

# --- SECTION 1: RIG MOVE (الأسطول والورشة) ---
with st.expander("➕ SECTION 1: RIG MOVE (Fleet & Support)"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Transport Fleet")
        n_lowbed = st.number_input("Lowbed Quantity", value=0, key="lb_q")
        p_lowbed = st.number_input("Lowbed Rate (Trip)", value=0, key="lb_p")
        st.write("---")
        n_flat_move = st.number_input("Flatbed Quantity (Move)", value=0, key="fm_q")
        p_flat_move = st.number_input("Flatbed Rate (Move)", value=0, key="fm_p")
    with col2:
        st.write("### Workshop & Tanker")
        n_workshop = st.number_input("Workshop Team Qty", value=0, key="ws_q")
        d_workshop = st.number_input("Workshop Days", value=0, key="ws_d")
        p_workshop = st.number_input("Workshop Day Rate", value=0, key="ws_p")
        st.write("---")
        n_tanker = st.number_input("Diesel Tanker Qty", value=0, key="dt_q")
        d_tanker = st.number_input("Tanker Days", value=0, key="dt_d")
        p_tanker = st.number_input("Tanker Rate", value=0, key="dt_p")
        f_tanker = st.number_input("Tanker Fuel (L/Day)", value=0, key="dt_f")

# --- SECTION 2: OLD LOCATION (الموقع القديم) ---
with st.expander("➕ SECTION 2: OLD LOCATION"):
    col3, col4 = st.columns(2)
    with col3:
        st.write("### Equipment (Old)")
        n_crane_old = st.number_input("Crane Old Qty", value=0, key="co_q")
        d_crane_old = st.number_input("Crane Old Days", value=0, key="co_d")
        p_crane_old = st.number_input("Crane Old Rate", value=0, key="co_p")
        f_crane_old = st.number_input("Crane Fuel (L/Day)", value=225, key="co_f")
        st.write("---")
        n_loader_old = st.number_input("Loader/Forklift Qty (Old)", value=0, key="lo_q")
        d_loader_old = st.number_input("Loader Days (Old)", value=0, key="lo_d")
        p_loader_old = st.number_input("Loader Rate (Old)", value=0, key="lo_p")
        f_loader_old = st.number_input("Loader Fuel (L/Day)", value=225, key="lo_f")
    with col4:
        st.write("### Personnel (Old)")
        n_rigger_old = st.number_input("Rigger Old Qty", value=0, key="ro_q")
        d_rigger_old = st.number_input("Rigger Days (Old)", value=0, key="ro_d")
        p_rigger_old = st.number_input("Rigger Rate (Old)", value=0, key="ro_p")

# --- SECTION 3: NEW LOCATION (الموقع الجديد) ---
with st.expander("➕ SECTION 3: NEW LOCATION"):
    col5, col6 = st.columns(2)
    with col5:
        st.write("### Cranes (New)")
        n_crane_2_new = st.number_input("2 Cranes New Qty", value=0, key="c2n_q")
        d_crane_2_new = st.number_input("2 Cranes Days (New)", value=0, key="c2n_d")
        p_crane_2_new = st.number_input("2 Cranes Rate (New)", value=0, key="c2n_p")
        f_crane_2_new = st.number_input("2 Cranes Fuel (L/Day)", value=450, key="c2n_f")
        st.write("---")
        n_crane_1_new = st.number_input("1 Crane New Qty", value=0, key="c1n_q")
        d_crane_1_new = st.number_input("1 Crane Days (New)", value=0, key="c1n_d")
        p_crane_1_new = st.number_input("1 Crane Rate (New)", value=0, key="c1n_p")
        f_crane_1_new = st.number_input("1 Crane Fuel (L/Day)", value=225, key="c1n_f")
    with col6:
        st.write("### Support (New)")
        n_loader_new = st.number_input("Loader/Forklift Qty (New)", value=0, key="ln_q")
        d_loader_new = st.number_input("Loader Days (New)", value=0, key="ln_d")
        p_loader_new = st.number_input("Loader Rate (New)", value=0, key="ln_p")
        f_loader_new = st.number_input("Loader Fuel (L/Day)", value=225, key="ln_f")
        st.write("---")
        n_safety = st.number_input("Safety Man Qty", value=0, key="sn_q")
        d_safety = st.number_input("Safety Days", value=0, key="sn_d")
        p_safety = st.number_input("Safety Rate", value=0, key="sn_p")
        st.write("---")
        n_tp = st.number_input("Truck Pusher Qty", value=0, key="tn_q")
        d_tp = st.number_input("TP Days", value=0, key="tn_d")
        p_tp = st.number_input("TP Rate", value=0, key="tn_p")

# --- 5. منطق الحسابات ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE & GENERATE RIG MOVE REPORT"):
    # حساب إجمالي الديزل بناءً على المسافات واستهلاك كل معدة المدخل
    total_fuel_l = (n_lowbed * dist * 1.57) + (n_flat_move * dist * 1.39) + \
                   (n_tanker * d_tanker * f_tanker) + \
                   (n_crane_old * d_crane_old * f_crane_old) + \
                   (n_loader_old * d_loader_old * f_loader_old) + \
                   (n_crane_2_new * d_crane_2_new * f_crane_2_new) + \
                   (n_crane_1_new * d_crane_1_new * f_crane_1_new) + \
                   (n_loader_new * d_loader_new * f_loader_new)
    
    total_fuel_cost = total_fuel_l * d_price
    
    # حساب إجمالي الإيجارات
    total_rent = (n_lowbed*p_lowbed) + (n_flat_move*p_flat_move) + (n_workshop*d_workshop*p_workshop) + (n_tanker*d_tanker*p_tanker) + \
                 (n_crane_old*d_crane_old*p_crane_old) + (n_loader_old*d_loader_old*p_loader_old) + (n_rigger_old*d_rigger_old*p_rigger_old) + \
                 (n_crane_2_new*d_crane_2_new*p_crane_2_new) + (n_crane_1_new*d_crane_1_new*p_crane_1_new) + \
                 (n_loader_new*d_loader_new*p_loader_new) + (n_safety*d_safety*p_safety) + (n_tp*d_tp*p_tp)
    
    grand_total = total_fuel_cost + total_rent

    # عرض النتيجة النهائية
    st.markdown(f"""
        <div class="neon-card">
            <h2 style="color:#00ffcc; margin:0; font-size: 24px;">TOTAL PROJECT BUDGET</h2>
            <h1 style="font-size: 60px; color:#00ffcc; margin: 10px 0;">{grand_total:,.2f} SAR</h1>
            <p style="color:white; margin:0; font-size: 18px;">Total Fuel Required: {total_fuel_l:,.2f} Litres</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 6. تصدير تقرير إكسل تفصيلي ---
    report_items = {
        "Description": ["Rig Move Fleet", "Workshop Support", "Diesel Tanker Cost", "Old Location Costs", "New Location Costs", "Diesel Total Cost", "Grand Total Project"],
        "Details": [f"LB: {n_lowbed}, FB: {n_flat_move}", f"{d_workshop} Days", f"{d_tanker} Days", f"Crane & Loader & Rigger", f"Cranes & Personnel", f"{total_fuel_l:,.2f} L", f"{grand_total:,.2f} SAR"],
        "Total (SAR)": [(n_lowbed*p_lowbed + n_flat_move*p_flat_move), (n_workshop*d_workshop*p_workshop), (n_tanker*d_tanker*p_tanker), (n_crane_old*d_crane_old*p_crane_old + n_loader_old*d_loader_old*p_loader_old + n_rigger_old*d_rigger_old*p_rigger_old), (n_crane_2_new*d_crane_2_new*p_crane_2_new + n_crane_1_new*d_crane_1_new*p_crane_1_new + n_loader_new*d_loader_new*p_loader_new + n_safety*d_safety*p_safety + n_tp*d_tp*p_tp), total_fuel_cost, grand_total]
    }
    df = pd.DataFrame(report_items)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KTS_Summary')
    st.download_button("📥 DOWNLOAD DETAILED EXCEL REPORT", buffer.getvalue(), f"KTS_Report_{rig_name}.xlsx", "application/vnd.ms-excel")

# --- 7. التوقيع النهائي ---
st.write("<br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 3px solid #00ffcc; padding-top: 30px;'>
        <h1 class="shiny-text" style='font-size: 50px;'>Ahmed Mugali</h1>
        <p style='color: #ffffff; font-size: 16px; letter-spacing: 2px;'>KTS LOGISTICS MASTER SYSTEM © 2026</p>
    </div>
""", unsafe_allow_html=True)
