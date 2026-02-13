import streamlit as st
from datetime import datetime
import pandas as pd
import io

# --- 1. إعدادات الشاشة (نفس الكود القديم) ---
st.set_page_config(page_title="KTS Ultimate | Ahmed Mugali", layout="centered")

# --- 2. تنسيق النيون والوميض (نفس التصميم بدون تغيير) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        background-color: #000000;
        color: #00ffcc;
    }

    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.88), rgba(0, 0, 0, 0.88)), 
        url("data:image/svg+xml,%3Csvg width='150' height='150' viewBox='0 0 150 150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='30' fill='rgba(0, 255, 204, 0.12)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }

    @keyframes blinker {
        from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc, 0 0 30px #00ffcc; }
        to { opacity: 0.6; text-shadow: 0 0 5px #00ffcc; }
    }

    .shiny-text {
        animation: blinker 1.8s linear infinite alternate;
        color: #00ffcc;
        font-weight: bold;
        text-align: center;
    }

    label {
        color: #ffffff !important;
        font-size: 20px !important;
        font-weight: bold !important;
        text-shadow: 2px 2px 5px #000;
    }

    .stNumberInput input, .stTextInput input {
        background-color: #111 !important;
        color: #00ffcc !important;
        border: 2px solid #00ffcc !important;
        font-size: 24px !important;
        border-radius: 12px !important;
    }

    .neon-card {
        background: rgba(0, 255, 204, 0.08);
        border: 2px solid #00ffcc;
        border-radius: 25px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
    }

    .stButton>button {
        width: 100%;
        height: 75px !important;
        background: linear-gradient(45deg, #00ffcc, #007bff) !important;
        color: #000 !important;
        font-weight: 900 !important;
        font-size: 26px !important;
        border-radius: 20px !important;
        box-shadow: 0 0 25px #00ffcc;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. الهيدر اللامع ---
st.markdown(f"<div class='shiny-text' style='font-size:24px; font-family:monospace;'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 55px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ffffff; font-size:18px;'>Ahmed Mugali Masterpiece © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. المدخلات الجديدة (إضافة اسم الريغ والمنطقة) ---
rig_name = st.text_input("Rig Name / Number", placeholder="Enter Rig Name")
location_name = st.text_input("Location", placeholder="Enter Destination")

# --- 5. المدخلات التشغيلية (نفس الأرقام والمعادلات) ---
dist = st.number_input("Distance KM | المسافة (كم)", value=0)
days = st.number_input("Work Days | عدد الأيام", value=1)

st.markdown("### 🏗️ Fleet & Rates | المعدات والأسعار")
col_fleet1, col_fleet2 = st.columns(2)

with col_fleet1:
    n_lowbed = st.number_input("Lowbed | لوبد", value=0)
    r_lowbed = st.number_input("Rent | سعر اللوبد", value=1500)
    st.write("---")
    n_crane = st.number_input("Crane | كرين", value=0)
    r_crane = st.number_input("Rent | سعر الكرين", value=5000)

with col_fleet2:
    n_flatbed = st.number_input("Flatbed | فلاتبد", value=0)
    r_flatbed = st.number_input("Rent | سعر الفلاتبد", value=900)
    st.write("---")
    n_loader = st.number_input("Loader | لودر", value=0)
    r_loader = st.number_input("Rent | سعر اللودر", value=1800)

st.write("---")
d_price = st.number_input("Diesel Rate | سعر الديزل", value=1.70, format="%.2f")

# --- 6. الحسابات والنتائج ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE | احسب الميزانية"):
    fuel_l = (n_lowbed * dist * 1.57) + (n_flatbed * dist * 1.39) + ((n_crane + n_loader) * days * 200)
    fuel_cost = fuel_l * d_price
    rent_total = (n_lowbed * r_lowbed) + (n_flatbed * r_flatbed) + ((n_crane * r_crane + n_loader * r_loader) * days)
    grand_total = fuel_cost + rent_total

    # العرض النهائي
    st.markdown(f"""
        <div class="neon-card" style="background: #00ffcc; color: #000; box-shadow: 0 0 40px #00ffcc;">
            <p style="color: #000; margin: 0; font-size: 22px; font-weight: bold;">GRAND TOTAL | الإجمالي الكلي</p>
            <h1 style="font-size: 55px; color: #000; margin: 0; font-weight: 900;">{grand_total:,.2f} SAR</h1>
        </div>
    """, unsafe_allow_html=True)

    # --- 7. ميزة الإكسل (بدون اسمك بالداخل) ---
    report_data = {
        "Description": ["Rig Name", "Location", "Distance (KM)", "Days", "Lowbed Qty", "Flatbed Qty", "Crane Qty", "Loader Qty", "Fuel (L)", "Fuel Cost", "Rental Cost", "Total Amount"],
        "Details": [rig_name, location_name, dist, days, n_lowbed, n_flatbed, n_crane, n_loader, f"{fuel_l:,.2f}", f"{fuel_cost:,.2f}", f"{rent_total:,.2f}", f"{grand_total:,.2f}"]
    }
    df = pd.DataFrame(report_data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KTS_Report')
    
    st.download_button(
        label="📥 DOWNLOAD EXCEL REPORT",
        data=buffer.getvalue(),
        file_name=f"KTS_{rig_name}_{datetime.now().strftime('%Y%m%d')}.xlsx",
        mime="application/vnd.ms-excel"
    )

    st.markdown(f'<div class="neon-card"><h2 class="shiny-text" style="margin:0;">FUEL: {fuel_l:,.2f} L</h2></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="neon-card"><h2 class="shiny-text" style="margin:0;">RENT: {rent_total:,.2f} SAR</h2></div>', unsafe_allow_html=True)

# --- 8. التوقيع النهائي (خارج ملف الإكسل) ---
st.write("<br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; border-top: 3px solid #00ffcc; padding-top: 30px;'>
        <h1 class="shiny-text" style='font-size: 40px;'>Ahmed Mugali</h1>
        <p style='color: #ffffff; font-size: 16px; letter-spacing: 2px;'>KTS LOGISTICS EXPERT © 2026</p>
    </div>
""", unsafe_allow_html=True)
