# FileName: app.py
# Created by: Ahmed Mugali (2026)
# Description: KTS Rig Move Cost Calculator - Mobile & Web Version

import streamlit as st
from datetime import datetime

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="KTS Rig Move | Ahmed Mugali", layout="centered")

# التنسيق الجمالي (اللمعان والخلفية)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #050505; color: white; }
    
    .stApp {
        background-image: linear-gradient(rgba(5, 5, 5, 0.9), rgba(5, 5, 5, 0.9)), 
        url("data:image/svg+xml,%3Csvg width='200' height='200' viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='40' fill='rgba(0, 212, 255, 0.1)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }

    .shiny-title {
        background: linear-gradient(90deg, #00d4ff, #ffffff, #00ffcc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        filter: drop-shadow(0 0 10px #00d4ff);
    }

    .stButton>button {
        width: 100%; height: 65px; border-radius: 20px;
        background: linear-gradient(45deg, #007bff, #00ffcc) !important;
        color: black !important; font-weight: bold; font-size: 22px;
        border: none; box-shadow: 0 0 20px rgba(0, 212, 255, 0.4);
    }
    
    .result-box {
        text-align: center; padding: 30px; 
        background: rgba(0, 212, 255, 0.05); 
        border: 2px solid #00d4ff; 
        border-radius: 30px; margin: 20px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# واجهة التطبيق
st.markdown(f"<div style='text-align:center; color:#00ffcc;'>{datetime.now().strftime('%I:%M %p')}</div>", unsafe_allow_html=True)
st.markdown('<div class="shiny-title">KTS RIG MOVE</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#aaa;'>Designed by: Ahmed Mugali © 2026</p>", unsafe_allow_html=True)

st.write("---")

# مدخلات المستخدم
dist = st.number_input("إجمالي المسافة (كم)", value=165)
days = st.number_input("عدد أيام العمل", value=1, min_value=1)

with st.expander("إعدادات الأسطول والأسعار"):
    n_lowbed = st.number_input("عدد اللوبد", value=0)
    n_flatbed = st.number_input("عدد الفلاتبد", value=0)
    n_crane = st.number_input("عدد الكرينات", value=0)
    n_loader = st.number_input("عدد اللودرات", value=0)
    st.write("---")
    diesel_p = st.number_input("سعر الديزل", value=1.70)

# الحسابات والنتائج
if st.button("🚀 احسب الآن"):
    fuel = (n_lowbed * dist * 1.57) + (n_flatbed * dist * 1.39) + ((n_crane + n_loader) * days * 200)
    rent = (n_lowbed * 1500) + (n_flatbed * 900) + ((n_crane * 5000 + n_loader * 1800) * days)
    total = (fuel * diesel_p) + rent

    st.markdown(f"""
        <div class="result-box">
            <p style="color: #aaa; margin: 0;">الإجمالي الكلي</p>
            <h1 style="font-size: 50px; color: #fff; margin: 0;">{total:,.2f} SAR</h1>
        </div>
    """, unsafe_allow_html=True)

# التذييل
st.markdown("<br><br><div style='text-align:center; border-top:1px solid #333; padding-top:20px;'><h2 style='color:#00d4ff;'>Ahmed Mugali</h2><p style='color:#555;'>KTS Logistics Support</p></div>", unsafe_allow_html=True)
