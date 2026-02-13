import streamlit as st
from datetime import datetime
import pandas as pd
import io

# --- 1. Page Configuration ---
st.set_page_config(page_title="KTS Organized | Ahmed Mugali", layout="centered")

# --- 2. Royal Neon Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #000; color: #00ffcc; }
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.92)), 
        url("data:image/svg+xml,%3Csvg width='150' height='150' viewBox='0 0 150 150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='30' fill='rgba(0,255,204,0.1)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }
    .shiny-text { animation: blinker 1.8s linear infinite alternate; color: #00ffcc; text-align: center; font-weight: bold; }
    @keyframes blinker { from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc; } to { opacity: 0.6; } }
    label { color: #ffffff !important; font-size: 19px !important; font-weight: bold !important; }
    .stNumberInput input, .stTextInput input { background-color: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; font-size: 20px !important; }
    .section-header { background: linear-gradient(90deg, rgba(0,255,204,0.2), transparent); border-left: 5px solid #00ffcc; padding: 10px; margin-top: 30px; color: #fff; font-size: 24px; font-weight: bold; border-radius: 5px; }
    .neon-card { background: rgba(0,255,204,0.08); border: 2px solid #00ffcc; border-radius: 20px; padding: 25px; text-align: center; margin: 20px 0; }
    .stButton>button { width: 100%; height: 70px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 24px; border-radius: 15px; box-shadow: 0 0 20px #00ffcc; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 50px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Logistics Master System © 2026</p>", unsafe_allow_html=True)

# --- 4. General Info ---
rig_name = st.text_input("Rig Name / Number")
location_name = st.text_input("General Location")
dist = st.number_input("Rig Move Distance (KM)", value=0)
d_price = st.number_input("Diesel Price (Litre)", value=1.70)

# --- SECTION 1: RIG MOVE ---
st.markdown("<div class='section-header'>SECTION 1: RIG MOVE (Fleet & Support)</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    n_lowbed = st.number_input("Lowbed Qty", value=0, key="lb_q")
    p_lowbed = st.number_input("Lowbed Rate (Trip)", value=0, key="lb_p")
    st.write("---")
    n_workshop = st.number_input("Workshop Team Qty", value=0, key="ws_q")
    d_workshop = st.number_input("Workshop Days", value=0, key="ws_d")
    p_workshop = st.number_input("Workshop Day Rate", value=0, key="ws_p")
with col2:
    n_flat_move = st.number_input("Flatbed Move Qty", value=0, key="fm_q")
    p_flat_move = st.number_input("Flatbed Move Rate", value=0, key="fm_p")
    st.write("---")
    n_tanker = st.number_input("Diesel Tanker Qty", value=0, key="dt_q")
    d_tanker = st.number_input("Tanker Days", value=0, key="dt_d")
    p_tanker = st.number_input("Tanker Day Rate", value=0, key="dt_p")

# --- SECTION 2: OLD LOCATION ---
st.markdown("<div class='section-header'>SECTION 2: OLD LOCATION</div>", unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    n_crane_old = st.number_input("One Crane (Old Loc) Qty", value=0, key="co_q")
    d_crane_old = st.number_input("Crane Old Loc Days", value=0, key="co_d")
    p_crane_old = st.number_input("Crane Old Loc Rate", value=0, key="co_p")
with col4:
    n_rigger_old = st.number_input("One Rigger (Old Loc) Qty", value=0, key="ro_q")
    d_rigger_old = st.number_input("Rigger Old Loc Days", value=0, key="ro_d")
    p_rigger_old = st.number_input("Rigger Old Loc Rate", value=0, key="ro_p")

# --- SECTION 3: NEW LOCATION ---
st.markdown("<div class='section-header'>SECTION 3: NEW LOCATION</div>", unsafe_allow_html=True)
col5, col6 = st.columns(2)
with col5:
    n_crane_2_new = st.number_input("2 Cranes (New Loc) Qty", value=0, key="c2n_q")
    d_crane_2_new = st.number_input("2 Cranes New Loc Days", value=0, key="c2n_d")
    p_crane_2_new = st.number_input("2 Cranes New Loc Rate", value=0, key="c2n_p")
    st.write("---")
    n_crane_1_new = st.number_input("One Crane (New Loc) Qty", value=0, key="c1n_q")
    d_crane_1_new = st.number_input("One Crane New Loc Days", value=0, key="c1n_d")
    p_crane_1_new = st.number_input("One Crane New Loc Rate", value=0, key="c1n_p")
    st.write("---")
    n_fl_new = st.number_input("One Flatbed (New Loc) Qty", value=0, key="fn_q")
    d_fl_new = st.number_input("Flatbed New Loc Days", value=0, key="fn_d")
    p_fl_new = st.number_input("Flatbed New Loc Rate", value=0, key="fn_p")
with col6:
    n_safety_new = st.number_input("One Safety Man Qty", value=0, key="sn_q")
    d_safety_new = st.number_input("Safety Man Days", value=0, key="sn_d")
    p_safety_new = st.number_input("Safety Man Day Rate", value=0, key="sn_p")
    st.write("---")
    n_tp_new = st.number_input("One Truck Pusher (TP) Qty", value=0, key="tn_q")
    d_tp_new = st.number_input("TP Days", value=0, key="tn_d")
    p_tp_new = st.number_input("TP Day Rate", value=0, key="tn_p")

# --- 5. Calculation Logic ---
if st.button("🚀 CALCULATE & GENERATE DETAILED REPORT"):
    # Fuel (Standards: LB 1.57, FL 1.39, Equipment 200L/day)
    fuel_l = (n_lowbed * dist * 1.57) + (n_flat_move * dist * 1.39) + \
             ((n_crane_old * d_crane_old + n_crane_2_new * d_crane_2_new + n_crane_1_new * d_crane_1_new + n_tanker * d_tanker) * 200)
    fuel_cost = fuel_l * d_price
    
    # Section Totals
    total_rig_move = (n_lowbed * p_lowbed) + (n_flat_move * p_flat_move) + (n_workshop * d_workshop * p_workshop) + (n_tanker * d_tanker * p_tanker)
    total_old_loc = (n_crane_old * d_crane_old * p_crane_old) + (n_rigger_old * d_rigger_old * p_rigger_old)
    total_new_loc = (n_crane_2_new * d_crane_2_new * p_crane_2_new) + (n_crane_1_new * d_crane_1_new * p_crane_1_new) + (n_fl_new * d_fl_new * p_fl_new) + (n_safety_new * d_safety_new * p_safety_new) + (n_tp_new * d_tp_new * p_tp_new)
    
    grand_total = fuel_cost + total_rig_move + total_old_loc + total_new_loc

    st.markdown(f"""
        <div class="neon-card">
            <h2 style="color:#00ffcc; margin:0;">GRAND TOTAL: {grand_total:,.2f} SAR</h2>
            <p style="color:white; margin:0;">Total Fuel: {fuel_l:,.2f} Litres</p>
        </div>
    """, unsafe_allow_html=True)

    # --- 6. Detailed Excel Export ---
    excel_data = {
        "Category": ["General", "General", "Rig Move", "Rig Move", "Rig Move", "Rig Move", "Old Loc", "Old Loc", "New Loc", "New Loc", "New Loc", "New Loc", "New Loc", "Fuel"],
        "Item": ["Rig Name", "Location", "Lowbed Move", "Flatbed Move", "Workshop Team", "Diesel Tanker", "Crane (Old Loc)", "Rigger (Old Loc)", "2 Cranes (New)", "One Crane (New)", "One Flatbed (New)", "Safety Man", "Truck Pusher", "Diesel Consumption"],
        "Qty/Days": [rig_name, location_name, n_lowbed, n_flat_move, f"{d_workshop} days", f"{d_tanker} days", f"{d_crane_old} days", f"{d_rigger_old} days", f"{d_crane_2_new} days", f"{d_crane_1_new} days", f"{d_fl_new} days", f"{d_safety_new} days", f"{d_tp_new} days", f"{fuel_l:,.2f} L"],
        "Cost (SAR)": ["-", "-", (n_lowbed*p_lowbed), (n_flat_move*p_flat_move), (n_workshop*d_workshop*p_workshop), (n_tanker*d_tanker*p_tanker), (n_crane_old*d_crane_old*p_crane_old), (n_rigger_old*d_rigger_old*p_rigger_old), (n_crane_2_new*d_crane_2_new*p_crane_2_new), (n_crane_1_new*d_crane_1_new*p_crane_1_new), (n_fl_new*d_fl_new*p_fl_new), (n_safety_new*d_safety_new*p_safety_new), (n_tp_new*d_tp_new*p_tp_new), fuel_cost]
    }
    
    df = pd.DataFrame(excel_data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KTS_Detailed_Report')
    
    st.download_button("📥 DOWNLOAD DETAILED EXCEL", buffer.getvalue(), f"KTS_Detailed_{rig_name}.xlsx", "application/vnd.ms-excel")

st.markdown("<br><h1 class='shiny-text' style='font-size:40px; border-top:2px solid #00ffcc; padding-top:20px;'>Ahmed Mugali</h1>", unsafe_allow_html=True)
