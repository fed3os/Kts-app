import streamlit as st

st.set_page_config(page_title="KTS Master | Ahmed Mugali", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #000; color: #00ffcc; }
    .stApp { background-color: #000; }
    .shiny-text { animation: blinker 1.8s linear infinite alternate; color: #00ffcc; text-align: center; font-weight: bold; }
    @keyframes blinker { from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc; } to { opacity: 0.6; } }
    .nav-card { background: rgba(0,255,204,0.1); border: 2px solid #00ffcc; border-radius: 20px; padding: 40px; text-align: center; margin: 20px; box-shadow: 0 0 25px rgba(0, 255, 204, 0.3); cursor: pointer; transition: all 0.3s; }
    .nav-card:hover { box-shadow: 0 0 40px rgba(0, 255, 204, 0.6); }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="shiny-text" style="font-size:55px;">KTS MASTER SYSTEM</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Ultimate Logistics & Driver Management | Ahmed Mugali © 2026</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class='nav-card'>
        <h2>🚛 KTS Rig Move Calculator</h2>
        <p style='color:white;'>حساب تكاليف نقل الحفارات والمعدات</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='nav-card'>
        <h2>📁 Driver Files System</h2>
        <p style='color:white;'>إدارة ملفات السائقين — رفع وتحميل</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; color:#00ffcc99; margin-top:40px;'>اختر من القائمة الجانبية للتنقل بين الصفحات</p>", unsafe_allow_html=True)
