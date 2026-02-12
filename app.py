import streamlit as st
from datetime import datetime

# --- 1. إعدادات الشاشة ---
st.set_page_config(page_title="KTS Pro | Ahmed Mugali", layout="centered")

# --- 2. تنسيق النيون والوميض (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        background-color: #000000;
        color: #00ffcc;
    }

    /* خلفية KTS */
    .stApp {
        background-image: linear-gradient(rgba(0, 0, 0, 0.85), rgba(0, 0, 0, 0.85)), 
        url("data:image/svg+xml,%3Csvg width='150' height='150' viewBox='0 0 150 150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='30' fill='rgba(0, 255, 204, 0.1)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }

    /* تأثير الوميض (ينور ويطفي) */
    @keyframes blinker {
        from { opacity: 1.0; text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc; }
        to { opacity: 0.5; text-shadow: 0 0 5px #00ffcc; }
    }

    .blinking-text {
        animation: blinker 1.5s linear infinite alternate;
        color: #00ffcc;
        font-weight: bold;
        text-align: center;
    }

    /* مسميات واضحة جداً */
    label, .stMarkdown p {
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: bold !important;
        text-shadow: 2px 2px 4px #000000;
    }

    .stNumberInput input {
        background-color: #111 !important;
        color: #00ffcc !important;
        border: 1px solid #00ffcc !important;
        font-size: 22px !important;
    }

    /* كروت النتائج النيون */
    .neon-card {
        background: rgba(0, 255, 204, 0.05);
        border: 2px solid #00ffcc;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.2);
    }

    .stButton>button {
        width: 100%;
        height: 70px !important;
        background: #00ffcc !important;
        color: #000 !important;
        font-weight: bold !important;
        font-size: 24px !important;
        border-radius: 20px !important;
        box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. الهيدر اللامع ---
st.markdown(f"<div class='blinking-text' style='font-size:22px;'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="blinking-text" style="font-size: 50px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#ffffff; font-size:18px;'>Ahmed Mugali Edition © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. المدخلات ---
dist = st.number_input("Distance KM | المسافة الإجمالية", value=0)
days = st.number_input("Work Days | عدد الأيام", value=1)

with st.expander("🚚 الأسطول والأسعار"):
    n_lowbed = st.number_input("Lowbed | عدد اللوبد", value=0)
    n_flatbed = st.number_input("Flatbed | عدد الفلاتبد", value=0)
    n_crane = st.number_input("Crane | عدد الكرينات", value=0)
    n_loader = st.number_input("Loader | عدد اللودرات", value=0)
    st.write("---")
    d_price = st.number_input("Diesel Rate | سعر الديزل", value=1.70)

# --- 5. الحسابات والعرض المضيء ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE | احسب الآن"):
    fuel_l = (n_lowbed * dist * 1.57) + (n_flatbed * dist * 1.39) + ((n_crane + n_loader) * days * 200)
    fuel_cost = fuel_l * d_price
    rent_total = (n_lowbed * 1500) + (n_flatbed * 900) + ((n_crane * 5000 + n_loader * 1800) * days)
    grand_total = fuel_cost + rent_total

    st.markdown(f"""
        <div class="neon-card" style="background: #00ffcc; color: #000;">
            <p style="color: #000; margin: 0; font-size: 20px; text-shadow:none;">TOTAL BUDGET | الميزانية</p>
            <h1 style="font-size: 50px; color: #000; margin: 0; text-shadow:none;">{grand_total:,.2f} SAR</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="neon-card"><p class="blinking-text">FUEL: {fuel_l:,.2f} L</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="neon-card"><p class="blinking-text">RENTAL: {rent_total:,.2f} SAR</p></div>', unsafe_allow_html=True)

# --- 6. التوقيع ---
st.write("<br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; border-top: 2px solid #00ffcc; padding-top: 20px;'>
        <h2 class="blinking-text" style='color: #00ffcc;'>Ahmed Mugali</h2>
        <p style='color: #ffffff;'>KTS LOGISTICS SYSTEM © 2026</p>
    </div>
""", unsafe_allow_html=True)
