import streamlit as st
from datetime import datetime
import pandas as pd
import io
import plotly.express as px

# --- 1. إعدادات الصفحة والستايل ---
st.set_page_config(page_title="KTS Master | Ahmed Mugali", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #000; color: #00ffcc; }
    .stApp { background-color: #000; }
    .shiny-text { animation: blinker 1.8s linear infinite alternate; color: #00ffcc; text-align: center; font-weight: bold; }
    @keyframes blinker { from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc; } to { opacity: 0.6; } }
    .st-expander { background-color: rgba(0, 255, 204, 0.05) !important; border: 1px solid #00ffcc !important; border-radius: 15px !important; margin-bottom: 10px !important; }
    .neon-card { background: rgba(0,255,204,0.1); border: 2px solid #00ffcc; border-radius: 20px; padding: 25px; text-align: center; margin: 20px 0; box-shadow: 0 0 25px rgba(0, 255, 204, 0.3); }
    .stButton>button { width: 100%; height: 75px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 24px; border-radius: 15px; box-shadow: 0 0 20px #00ffcc; border: none !important; }
    h3 { color: #00ffcc !important; border-bottom: 2px solid #00ffcc; padding-bottom: 5px; }
    label { color: #fff !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. الهيدر ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 50px;">KTS RIG MOVE MASTER</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>Ultimate Logistics Analytics by Ahmed Mugali © 2026</p>", unsafe_allow_html=True)

# --- 3. المدخلات الأساسية ---
col_m1, col_m2, col_m3 = st.columns(3)
rig_id = col_m1.text_input("Rig Name / ID")
distance = col_m2.number_input("One-Way Distance (KM)", value=0)
diesel_price = col_m3.number_input("Diesel Price", value=1.70, format="%.2f")

# --- SECTION 1: Trucks for rig move ---
with st.expander("➕ Trucks for rig move (flatbed and Lowbed)"):
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Transport Fleet")
        n_lb = st.number_input("Lowbed Qty", 0, key="lb_q")
        p_lb = st.number_input("Lowbed Rate (Trip)", 0, key="lb_p")
        n_fb = st.number_input("Flatbed Qty", 0, key="fb_q")
        p_fb = st.number_input("Flatbed Rate (Trip)", 0, key="fb_p")
    with c2:
        st.write("### Support & Tanker")
        n_ws = st.number_input("Workshop Team Qty", 0, key="ws_q")
        d_ws = st.number_input("Workshop Days", 0, key="ws_d")
        p_ws = st.number_input("Workshop Rate", 0, key="p_ws")
        n_dt = st.number_input("Diesel Tanker Qty", 0, key="dt_q")
        d_dt = st.number_input("Tanker Days", 0, key="dt_d")
        p_dt = st.number_input("Tanker Rate", 0, key="dt_p")
        f_dt = st.number_input("Tanker Fuel (L/Day)", 0, key="dt_f")

# --- SECTION 2: Equipment for old location ---
with st.expander("➕ Equipment for old location (crane rigger FL truck pusher safety)"):
    c3, c4 = st.columns(2)
    with c3:
        st.write("### Heavy Equipment")
        n_co = st.number_input("Crane Old Qty", 0, key="co_q")
        d_co = st.number_input("Crane Days", 0, key="co_d")
        p_co = st.number_input("Crane Rate", 0, key="co_p")
        f_co = st.number_input("Crane Fuel L/D", 225, key="co_f")
        n_lo = st.number_input("Loader/FL Old Qty", 0, key="lo_q")
        d_lo = st.number_input("Loader Days", 0, key="lo_d")
        p_lo = st.number_input("Loader Rate", 0, key="lo_p")
        f_lo = st.number_input("Loader Fuel L/D", 225, key="lo_f")
    with c4:
        st.write("### Personnel (Old)")
        n_tpo = st.number_input("Truck Pusher Qty", 0, key="tpo_q")
        d_tpo = st.number_input("TP Days", 0, key="tpo_d")
        p_tpo = st.number_input("TP Rate", 0, key="tpo_p")
        n_so = st.number_input("Safety Old Qty", 0, key="so_q")
        d_so = st.number_input("Safety Days", 0, key="so_d")
        p_so = st.number_input("Safety Rate", 0, key="so_p")
        n_ro = st.number_input("Rigger Old Qty", 0, key="ro_q")
        d_ro = st.number_input("Rigger Days", 0, key="ro_d")
        p_ro = st.number_input("Rigger Rate", 0, key="ro_p")

# --- SECTION 3: Equipment for new location ---
with st.expander("➕ Equipment for new location"):
    c6_1, c6_2 = st.columns(2)
    with c6_1:
        st.write("### New Loc Support")
        n_cnl = st.number_input("Crane New Qty", 0, key="cnl_q")
        d_cnl = st.number_input("Days", 0, key="cnl_d")
        p_cnl = st.number_input("Rate", 0, key="cnl_p")
        f_cnl = st.number_input("Fuel L/D", 225, key="cnl_f")
    with c6_2:
        n_lnl = st.number_input("Loader New Qty", 0, key="lnl_q")
        d_lnl = st.number_input("Days", 0, key="lnl_d")
        p_lnl = st.number_input("Rate", 0, key="lnl_p")
        f_lnl = st.number_input("Fuel L/D", 225, key="lnl_f")
    
    st.write("---")
    c7, c8 = st.columns(2)
    with c7:
        n_tpn = st.number_input("TP New Qty", 0, key="tpn_q")
        d_tpn = st.number_input("TP Days", 0, key="tpn_d")
        p_tpn = st.number_input("TP Rate", 0, key="tpn_p")
    with c8:
        n_sn = st.number_input("Safety New Qty", 0, key="sn_q")
        d_sn = st.number_input("Safety Days", 0, key="sn_d")
        p_sn = st.number_input("Safety Rate", 0, key="sn_p")

# --- SECTION 4: Equipment for rig up ---
with st.expander("➕ Equipment for rig up"):
    c5_1, c5_2 = st.columns(2)
    with c5_1:
        n_cru = st.number_input("Crane RigUp Qty", 0, key="cru_q")
        d_cru = st.number_input("Days (RigUp)", 0, key="cru_d")
        p_cru = st.number_input("Rate (RigUp)", 0, key="cru_p")
        f_cru = st.number_input("Fuel L/D (RigUp)", 225, key="cru_f")
    with c5_2:
        n_lru = st.number_input("Loader RigUp Qty", 0, key="lru_q")
        d_lru = st.number_input("Days (RigUp)", 0, key="lru_d")
        p_lru = st.number_input("Rate (RigUp)", 0, key="lru_p")
        f_lru = st.number_input("Fuel L/D (RigUp)", 225, key="lru_f")

# --- 4. الحسابات والرسوم البيانية ---
if st.button("🚀 CALCULATE & GENERATE ANALYTICS"):
    # وقود النقل (ذهاب وعودة)
    f_trans = ((n_lb * (distance * 2) * 1.57) + (n_fb * (distance * 2) * 1.39)) * diesel_price
    # وقود المعدات
    f_equip = ((n_dt*d_dt*f_dt) + (n_co*d_co*f_co) + (n_lo*d_lo*f_lo) + 
               (n_cru*d_cru*f_cru) + (n_lru*d_lru*f_lru) + (n_cnl*d_cnl*f_cnl) + (n_lnl*d_lnl*f_lnl)) * diesel_price
    total_fuel = f_trans + f_equip
    
    # الإيجارات
    rent_total = (n_lb*p_lb) + (n_fb*p_fb) + (n_ws*d_ws*p_ws) + (n_dt*d_dt*p_dt) + \
                 (n_co*d_co*p_co) + (n_lo*d_lo*p_lo) + (n_tpo*d_tpo*p_tpo) + (n_so*d_so*p_so) + (n_ro*d_ro*p_ro) + \
                 (n_cru*d_cru*p_cru) + (n_lru*d_lru*p_lru) + (n_cnl*d_cnl*p_cnl) + (n_lnl*d_lnl*p_lnl) + \
                 (n_tpn*d_tpn*p_tpn) + (n_sn*d_sn*p_sn)
    
    grand_total = total_fuel + rent_total

    st.markdown(f'<div class="neon-card"><h1>{grand_total:,.2f} SAR</h1><p>Grand Total Project Budget</p></div>', unsafe_allow_html=True)

    # --- الرسوم البيانية ---
    st.write("### 📊 Budget Breakdown")
    col_ch1, col_ch2 = st.columns(2)
    
    fig1 = px.pie(values=[total_fuel, rent_total], names=['Fuel Cost', 'Rental & Labor'], hole=0.4,
                 color_discrete_sequence=['#00ffcc', '#007bff'], title="Cost Distribution")
    fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    col_ch1.plotly_chart(fig1, use_container_width=True)

    sec_data = pd.DataFrame({
        "Section": ["Rig Move", "Old Loc", "New Loc", "Rig Up"],
        "Amount": [(f_trans + n_lb*p_lb + n_fb*p_fb), (n_co*d_co*p_co + n_lo*d_lo*p_lo), (n_cnl*d_cnl*p_cnl + n_lnl*d_lnl*p_lnl), (n_cru*d_cru*p_cru + n_lru*d_lru*p_lru)]
    })
    fig2 = px.bar(sec_data, x='Section', y='Amount', color='Section', title="Phase Spending Analysis")
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
    col_ch2.plotly_chart(fig2, use_container_width=True)

# --- التوقيع ---
st.markdown(f"<div style='text-align:center; border-top:2px solid #00ffcc; padding:20px;'><h1 class='shiny-text'>Ahmed Mugali</h1></div>", unsafe_allow_html=True)
