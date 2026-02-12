import streamlit as st
from datetime import datetime

# --- 1. إعدادات الشاشة المنسقة للجوال ---
st.set_page_config(
    page_title="KTS Mobile | Ahmed Mugali",
    layout="centered"
)

# --- 2. تنسيق CSS "خرافي" (اللمعان والخلفية) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif;
        background-color: #050505;
        color: white;
    }

    .stApp {
        background-image: linear-gradient(rgba(5, 5, 5, 0.93), rgba(5, 5, 5, 0.93)), 
        url("data:image/svg+xml,%3Csvg width='150' height='150' viewBox='0 0 150 150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='30' fill='rgba(0, 212, 255, 0.1)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }

    .shiny-title {
        font-size: 38px !important;
        background: linear-gradient(90deg, #00d4ff, #ffffff, #00ffcc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: bold;
        text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
    }

    .mobile-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 212, 255, 0.3);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin-bottom: 15px;
    }

    .stNumberInput > div > div > input {
        height: 55px !important;
        font-size: 20px !important;
    }
    
    .stButton>button {
        width: 100%;
        height: 65px !important;
        border-radius: 18px !important;
        font-size: 22px !important;
        background: linear-gradient(45deg, #007bff, #00ffcc) !important;
        color: black !important;
        font-weight: bold !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. الهيدر ---
st.markdown(f"<div style='text-align:center; color:#00ffcc; font-size:20px; font-family:monospace;'>{datetime.now().strftime('%I:%M %p')}</div>", unsafe_allow_html=True)
st.markdown('<div class="shiny-title">KTS RIG MOVE</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#aaa; font-size:16px;'>Ahmed Mugali Edition © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. المدخلات (تم تعديل المسافة لتبدأ بصفر) ---
dist = st.number_input("Distance KM | المسافة الإجمالية", value=0)  # تم التغيير لـ 0
days = st.number_input("Work Days | عدد الأيام", value=1)

with st.expander("🚚 Fleet Selection | اختيار المعدات"):
    n_lowbed = st.number_input("Lowbed | عدد اللوبد", value=0)
    n_flatbed = st.number_input("Flatbed | عدد الفلاتبد", value=0)
    n_crane = st.number_input("Crane | عدد الكرينات", value=0)
    n_loader = st.number_input("Loader | عدد اللودرات", value=0)

with st.expander("⛽ Setup Prices | إعدادات الأسعار"):
    d_price = st.number_input("Diesel Rate | سعر الديزل", value=1.70)
    r_lowbed = st.number_input("Lowbed Rent", value=1500)
    r_crane = st.number_input("Crane Rent", value=5000)

# --- 5. الحسابات والنتائج ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE | احسب الآن"):
    fuel_l = (n_lowbed * dist * 1.57) + (n_flatbed * dist * 1.39) + ((n_crane + n_loader) * days * 200)
    fuel_cost = fuel_l * d_price
    rent_total = (n_lowbed * r_lowbed) + (n_flatbed * 900) + ((n_crane * r_crane + n_loader * 1800) * days)
    grand_total = fuel_cost + rent_total

    st.markdown(f"""
        <div style="text-align: center; padding: 25px; background: rgba(0, 212, 255, 0.15); border: 2px solid #00d4ff; border-radius: 30px; margin: 20px 0;">
            <p style="color: #aaa; margin: 0; font-size: 16px;">TOTAL BUDGET | الميزانية</p>
            <h1 style="font-size: 45px; color: #fff; text-shadow: 0 0 20px #00d4ff; margin: 0;">{grand_total:,.2f} SAR</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="mobile-card"><p style="color:#888;">FUEL (L)</p><h2 style="color:#00ffcc;">{fuel_l:,.2f}</h2></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="mobile-card"><p style="color:#888;">RENTAL COST</p><h2 style="color:#00ffcc;">{rent_total:,.2f}</h2></div>', unsafe_allow_html=True)

# --- 6. التوقيع ---
st.write("<br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='text-align: center; border-top: 1px solid #333; padding-top: 20px;'>
        <h2 style='color: #00d4ff;'>Ahmed Mugali</h2>
        <p style='color: #555; font-size: 12px;'>KTS LOGISTICS SYSTEM © 2026</p>
    </div>
""", unsafe_allow_html=True)
