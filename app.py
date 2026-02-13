import streamlit as st
from datetime import datetime
import pandas as pd
import io
import plotly.express as px

# --- 1. Page Configuration ---
st.set_page_config(page_title="KTS Legend | Ahmed Mugali", layout="wide")

# --- 2. Royal Neon Styling (CSS) ---
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
    .neon-card { background: rgba(0,255,204,0.1); border: 2px solid #00ffcc; border-radius: 20px; padding: 25px; text-align: center; margin: 20px 0; box-shadow: 0 0 25px rgba(0, 255, 204, 0.3); }
    .stButton>button { width: 100%; height: 75px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 26px; border-radius: 15px; box-shadow: 0 0 25px #00ffcc; border: none !important; cursor: pointer; }
    h3 { color: #00ffcc !important; border-bottom: 2px solid #00ffcc; padding-bottom: 5px; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 55px; margin-bottom:0;">KTS RIG MOVE MASTER</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Professional Logistics Analytics by Ahmed Mugali © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. Main Settings ---
col_m1, col_m2, col_m3 = st.columns(3)
rig_name = col_m1.text_input("Rig Name / ID", placeholder="e.g. Rig-101")
dist = col_m2.number_input("One-Way Distance (KM)", value=0, help="Program will multiply by 2 for Round Trip fuel.")
d_price = col_m3.number_input("Diesel Price (Litre)", value=1.70, format="%.2f")

# --- SECTION 1: RIG MOVE ---
with st.expander("➕ SECTION 1: RIG MOVE (Fleet & Support)"):
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Transport Fleet")
        n_lb = st.number_input("Lowbed Quantity", 0, key="n_lb")
        p_lb = st.number_input("Lowbed Rate (Trip)", 0, key="p_lb")
        n_fb = st.number_input("Flatbed Move Qty", 0, key="n_fb")
        p_fb = st.number_input("Flatbed Rate (Trip)", 0, key="p_fb")
    with c2:
        st.write("### Workshop & Tanker")
        n_ws = st.number_input("Workshop Team Qty", 0, key="n_ws")
        d_ws = st.number_input("Workshop Days", 0, key="d_ws")
        p_ws = st.number_input("Workshop Day Rate", 0, key="p_ws")
        st.write("---")
        n_dt = st.number_input("Diesel Tanker Qty", 0, key="n_dt")
        d_dt = st.number_input("Tanker Days", 0, key="d_dt")
        p_dt = st.number_input("Tanker Rate", 0, key="p_dt")
        f_dt = st.number_input("Tanker Fuel (L/Day)", 0, key="f_dt")

# --- SECTION 2: OLD LOCATION ---
with st.expander("➕ SECTION 2: OLD LOCATION (Loadout Phase)"):
    c3, c4 = st.columns(2)
    with c3:
        st.write("### Heavy Equipment")
        n_co = st.number_input("Crane Old Qty", 0, key="n_co")
        d_co = st.number_input("Crane Days (Old)", 0, key="d_co")
        p_co = st.number_input("Crane Rate", 0, key="p_co")
        f_co = st.number_input("Crane Fuel (L/Day)", 225, key="f_co")
        st.write("---")
        n_lo = st.number_input("Loader/Forklift Old Qty", 0, key="n_lo")
        d_lo = st.number_input("Loader Days (Old)", 0, key="d_lo")
        p_lo = st.number_input("Loader Rate", 0, key="p_lo")
        f_lo = st.number_input("Loader Fuel (L/Day)", 225, key="f_lo")
    with c4:
        st.write("### Personnel (Old Loc)")
        n_tpo = st.number_input("Truck Pusher (Old) Qty", 0, key="n_tpo")
        d_tpo = st.number_input("TP Days (Old)", 0, key="d_tpo")
        p_tpo = st.number_input("TP Day Rate", 0, key="p_tpo")
        n_so = st.number_input("Safety Man (Old) Qty", 0, key="n_so")
        d_so = st.number_input("Safety Days (Old)", 0, key="d_so")
        p_so = st.number_input("Safety Day Rate", 0, key="p_so")
        n_ro = st.number_input("Rigger (Old) Qty", 0, key="n_ro")
        d_ro = st.number_input("Rigger Days (Old)", 0, key="d_ro")
        p_ro = st.number_input("Rigger Day Rate", 0, key="p_ro")

# --- SECTION 3: NEW LOCATION & RIG UP ---
with st.expander("➕ SECTION 3: NEW LOCATION & RIG UP (Offload Phase)"):
    c5, c6 = st.columns(2)
    with c5:
        st.write("### Rig Up Team")
        n_cru = st.number_input("Crane Rig-Up Qty", 0, key="n_cru")
        d_cru = st.number_input("Crane Days (Rig-Up)", 0, key="d_cru")
        p_cru = st.number_input("Crane Rate (Rig-Up)", 0, key="p_cru")
        f_cru = st.number_input("Fuel (L/Day)", 225, key="f_cru")
        st.write("---")
        n_lru = st.number_input("Loader Rig-Up Qty", 0, key="n_lru")
        d_lru = st.number_input("Loader Days (Rig-Up)", 0, key="d_lru")
        p_lru = st.number_input("Loader Rate (Rig-Up)", 0, key="p_lru")
        f_lru = st.number_input("Fuel (L/Day)", 225, key="f_lru")
    with c6:
        st.write("### New Loc Equipment")
        n_cnl = st.number_input("Crane New Loc Qty", 0, key="n_cnl")
        d_cnl = st.number_input("Crane Days (New Loc)", 0, key="d_cnl")
        p_cnl = st.number_input("Crane Rate (New Loc)", 0, key="p_cnl")
        f_cnl = st.number_input("Fuel (L/Day)", 225, key="f_cnl")
        st.write("---")
        n_lnl = st.number_input("Loader New Loc Qty", 0, key="n_lnl")
        d_lnl = st.number_input("Loader Days (New Loc)", 0, key="d_lnl")
        p_lnl = st.number_input("Loader Rate (New Loc)", 0, key="p_lnl")
        f_lnl = st.number_input("Fuel (L/Day)", 225, key="f_lnl")

    st.write("---")
    st.write("### Personnel (New Loc)")
    c7, c8 = st.columns(2)
    with c7:
        n_tpn = st.number_input("Truck Pusher (New) Qty", 0, key="n_tpn")
        d_tpn = st.number_input("TP Days (New)", 0, key="d_tpn")
        p_tpn = st.number_input("TP Day Rate", 0, key="p_tpn")
        n_rn = st.number_input("Rigger (New) Qty", 0, key="n_rn")
        d_rn = st.number_input("Rigger Days (New)", 0, key="d_rn")
        p_rn = st.number_input("Rigger Day Rate", 0, key="p_rn")
    with c8:
        n_sn = st.number_input("Safety Man (New) Qty", 0, key="n_sn")
        d_sn = st.number_input("Safety Days (New)", 0, key="d_sn")
        p_sn = st.number_input("Safety Day Rate", 0, key="p_sn")

# --- 5. Precision Logic & Charts ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE & GENERATE RIG MOVE ANALYTICS"):
    # Fuel Calculation (Distance * 2 for Round Trip)
    fuel_transport = ((n_lb * (dist * 2) * 1.57) + (n_fb * (dist * 2) * 1.39)) * d_price
    fuel_equip = ((n_dt*d_dt*f_dt) + (n_co*d_co*f_co) + (n_lo*d_lo*f_lo) + 
                  (n_cru*d_cru*f_cru) + (n_lru*d_lru*f_lru) + 
                  (n_cnl*d_cnl*f_cnl) + (n_lnl*d_lnl*f_lnl)) * d_price
    
    total_fuel_cost = fuel_transport + fuel_equip
    total_fuel_litres = total_fuel_cost / d_price if d_price > 0 else 0
    
    # Rental & Labor Calculation
    rent_rig_move = (n_lb*p_lb) + (n_fb*p_fb) + (n_ws*d_ws*p_ws) + (n_dt*d_dt*p_dt)
    rent_old_loc = (n_co*d_co*p_co) + (n_lo*d_lo*p_lo) + (n_tpo*d_tpo*p_tpo) + (n_so*d_so*p_so) + (n_ro*d_ro*p_ro)
    rent_new_loc = (n_cru*d_cru*p_cru) + (n_lru*d_lru*p_lru) + (n_cnl*d_cnl*p_cnl) + (n_lnl*d_lnl*p_lnl) + \
                   (n_tpn*d_tpn*p_tpn) + (n_sn*d_sn*p_sn) + (n_rn*d_rn*p_rn)
    
    total_rental_cost = rent_rig_move + rent_old_loc + rent_new_loc
    grand_total = total_fuel_cost + total_rental_cost

    # Display Results
    st.markdown(f"""
        <div class="neon-card">
            <h1 style="font-size: 65px; margin:0;">{grand_total:,.2f} SAR</h1>
            <p style="font-size: 22px; color:white;">Grand Total Budget for {rig_name}</p>
            <hr style="border: 1px solid #00ffcc;">
            <div style="display: flex; justify-content: space-around;">
                <div><p>Fuel Component</p><h3>{total_fuel_cost:,.2f} SAR</h3></div>
                <div><p>Rental/Labor Component</p><h3>{total_rental_cost:,.2f} SAR</h3></div>
                <div><p>Total Diesel</p><h3>{total_fuel_litres:,.2f} L</h3></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- Charts Section ---
    st.write("### 📊 Budget Distribution Analytics")
    col_chart1, col_chart2 = st.columns(2)
    
    # Chart 1: Fuel vs Rental
    pie_data = pd.DataFrame({"Category": ["Fuel Cost", "Rental & Labor"], "Value": [total_fuel_cost, total_rental_cost]})
    fig1 = px.pie(pie_data, values='Value', names='Category', hole=0.4, 
                 color_discrete_sequence=['#00ffcc', '#007bff'], title="Total Budget Split")
    fig1.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
    col_chart1.plotly_chart(fig1, use_container_width=True)
    
    # Chart 2: Section-wise Spending
    bar_data = pd.DataFrame({
        "Section": ["Rig Move Fleet", "Old Location", "New Location"],
        "Amount (SAR)": [rent_rig_move + fuel_transport, rent_old_loc, rent_new_loc]
    })
    fig2 = px.bar(bar_data, x='Section', y='Amount (SAR)', color='Section',
                 color_discrete_sequence=['#00ffcc', '#007bff', '#ff00ff'], title="Spending by Project Phase")
    fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
    col_chart2.plotly_chart(fig2, use_container_width=True)

    # --- Excel Export ---
    excel_data = {
        "Item Category": ["Grand Total", "Total Fuel", "Rig Move Phase", "Old Loc Phase", "New Loc Phase"],
        "Details": [f"{grand_total:,.2f} SAR", f"{total_fuel_litres:,.2f} Litres", f"{rent_rig_move:,.2f} SAR", f"{rent_old_loc:,.2f} SAR", f"{rent_new_loc:,.2f} SAR"]
    }
    df_excel = pd.DataFrame(excel_data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_excel.to_excel(writer, index=False, sheet_name='KTS_Summary')
    st.download_button("📥 DOWNLOAD DETAILED AUDIT REPORT (EXCEL)", buffer.getvalue(), f"KTS_Final_{rig_name}.xlsx", "application/vnd.ms-excel")

# --- 6. Final Signature ---
st.write("<br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 3px solid #00ffcc; padding-top: 30px;'>
        <h1 class="shiny-text" style='font-size: 55px;'>Ahmed Mugali</h1>
        <p style='color: #ffffff; font-size: 16px; letter-spacing: 2px;'>KTS LOGISTICS MASTER SYSTEM v4.0 © 2026</p>
    </div>
""", unsafe_allow_html=True)
