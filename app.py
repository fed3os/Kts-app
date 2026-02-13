import streamlit as st
from datetime import datetime
import pandas as pd
import io

# --- 1. Page Configuration ---
st.set_page_config(page_title="KTS Legend | Ahmed Mugali", layout="centered")

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
    
    label { color: #ffffff !important; font-size: 18px !important; font-weight: bold !important; }
    .stNumberInput input, .stTextInput input { background-color: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; font-size: 20px !important; }
    .neon-card { background: rgba(0,255,204,0.08); border: 2px solid #00ffcc; border-radius: 20px; padding: 25px; text-align: center; margin: 20px 0; }
    .stButton>button { width: 100%; height: 75px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 26px; border-radius: 15px; box-shadow: 0 0 25px #00ffcc; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 50px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Logistics & Support Management © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. Main Information ---
rig_name = st.text_input("Rig Name / Number", placeholder="e.g. Rig 100")
location_name = st.text_input("Location", placeholder="Destination")
dist = st.number_input("Rig Move Distance (KM)", value=0)
d_price = st.number_input("Diesel Price", value=1.70)

st.write("---")

# --- SECTION 1: RIG MOVE (Fleet & Workshop) ---
with st.expander("➕ SECTION 1: RIG MOVE (Fleet & Workshop)"):
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Transport Fleet")
        n_lowbed = st.number_input("Lowbed Quantity", value=0, key="lb_q")
        p_lowbed = st.number_input("Lowbed Rate", value=0, key="lb_p")
        st.write("---")
        n_flat_move = st.number_input("Flatbed Move Qty", value=0, key="fm_q")
        p_flat_move = st.number_input("Flatbed Move Rate", value=0, key="fm_p")
    with col2:
        st.write("### Workshop & Tanker")
        n_workshop = st.number_input("Workshop Team Qty", value=0, key="ws_q")
        d_workshop = st.number_input("Workshop Days", value=0, key="ws_d")
        p_workshop = st.number_input("Workshop Day Rate", value=0, key="ws_p")
        st.write("---")
        n_tanker = st.number_input("Diesel Tanker Qty", value=0, key="dt_q")
        d_tanker = st.number_input("Tanker Days", value=0, key="dt_d")
        p_tanker = st.number_input("Tanker Day Rate", value=0, key="dt_p")

# --- SECTION 2: OLD LOCATION (Loader Included) ---
with st.expander("➕ SECTION 2: OLD LOCATION"):
    col3, col4 = st.columns(2)
    with col3:
        st.write("### Lifting & Loader")
        n_crane_old = st.number_input("One Crane (Old) Qty", value=0, key="co_q")
        d_crane_old = st.number_input("Crane Days (Old)", value=0, key="co_d")
        p_crane_old = st.number_input("Crane Day Rate (Old)", value=0, key="co_p")
        st.write("---")
        n_loader_old = st.number_input("Loader (Old Loc) Qty", value=0, key="lo_q")
        d_loader_old = st.number_input("Loader Days (Old)", value=0, key="lo_d")
        p_loader_old = st.number_input("Loader Day Rate (Old)", value=0, key="lo_p")
    with col4:
        st.write("### Personnel")
        n_rigger_old = st.number_input("One Rigger (Old) Qty", value=0, key="ro_q")
        d_rigger_old = st.number_input("Rigger Days (Old)", value=0, key="ro_d")
        p_rigger_old = st.number_input("Rigger Day Rate (Old)", value=0, key="ro_p")

# --- SECTION 3: NEW LOCATION (Loader Included) ---
with st.expander("➕ SECTION 3: NEW LOCATION"):
    col5, col6 = st.columns(2)
    with col5:
        st.write("### Cranes & Loader")
        n_crane_2_new = st.number_input("2 Cranes (New) Qty", value=0, key="c2n_q")
        d_crane_2_new = st.number_input("2 Cranes Days (New)", value=0, key="c2n_d")
        p_crane_2_new = st.number_input("2 Cranes Day Rate (New)", value=0, key="c2n_p")
        st.write("---")
        n_crane_1_new = st.number_input("One Crane (New) Qty", value=0, key="c1n_q")
        d_crane_1_new = st.number_input("One Crane Days (New)", value=0, key="c1n_d")
        p_crane_1_new = st.number_input("One Crane Day Rate (New)", value=0, key="c1n_p")
        st.write("---")
        n_loader_new = st.number_input("Loader (New Loc) Qty", value=0, key="ln_q")
        d_loader_new = st.number_input("Loader Days (New)", value=0, key="ln_d")
        p_loader_new = st.number_input("Loader Day Rate (New)", value=0, key="ln_p")
    with col6:
        st.write("### Personnel & Logistics")
        n_fl_new = st.number_input("One Flatbed (New) Qty", value=0, key="fn_q") # For specific use cases if still needed
        d_fl_new = st.number_input("Flatbed Days (New)", value=0, key="fn_d")
        p_fl_new = st.number_input("Flatbed Rate (New)", value=0, key="fn_p")
        st.write("---")
        n_safety_new = st.number_input("One Safety Man Qty", value=0, key="sn_q")
        d_safety_new = st.number_input("Safety Man Days", value=0, key="sn_d")
        p_safety_new = st.number_input("Safety Man Day Rate", value=0, key="sn_p")
        st.write("---")
        n_tp_new = st.number_input("One Truck Pusher Qty", value=0, key="tn_q")
        d_tp_new = st.number_input("TP Days", value=0, key="tn_d")
        p_tp_new = st.number_input("TP Day Rate", value=0, key="tn_p")

# --- 5. Calculations ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE & GENERATE EXCEL"):
    # Fuel Calculation
    fuel_l = (n_lowbed * dist * 1.57) + (n_flat_move * dist * 1.39) + \
             ((n_crane_old * d_crane_old + n_crane_2_new * d_crane_2_new + n_crane_1_new * d_crane_1_new + \
               n_loader_old * d_loader_old + n_loader_new * d_loader_new + n_tanker * d_tanker) * 200)
    fuel_cost = fuel_l * d_price
    
    # Financials
    total_cost = fuel_cost + (n_lowbed*p_lowbed) + (n_flat_move*p_flat_move) + (n_workshop*d_workshop*p_workshop) + (n_tanker*d_tanker*p_tanker) + \
                 (n_crane_old*d_crane_old*p_crane_old) + (n_rigger_old*d_rigger_old*p_rigger_old) + (n_loader_old*d_loader_old*p_loader_old) + \
                 (n_crane_2_new*d_crane_2_new*p_crane_2_new) + (n_crane_1_new*d_crane_1_new*p_crane_1_new) + (n_loader_new*d_loader_new*p_loader_new) + \
                 (n_safety_new*d_safety_new*p_safety_new) + (n_tp_new*d_tp_new*p_tp_new) + (n_fl_new*d_fl_new*p_fl_new)

    st.markdown(f"""
        <div class="neon-card">
            <h2 style="color:#00ffcc; margin:0;">TOTAL BUDGET: {total_cost:,.2f} SAR</h2>
            <p style="color:white; margin:0;">Diesel Total: {fuel_l:,.2f} Litres</p>
        </div>
    """, unsafe_allow_html=True)

    # --- Excel Export ---
    excel_data = {
        "Category": ["Rig Move", "Rig Move", "Rig Move", "Rig Move", "Old Loc", "Old Loc", "Old Loc", "New Loc", "New Loc", "New Loc", "New Loc", "New Loc", "New Loc", "Fuel"],
        "Item": ["Lowbed", "Flatbed Move", "Workshop Team", "Diesel Tanker", "One Crane (Old)", "Rigger (Old)", "Loader (Old)", "2 Cranes (New)", "One Crane (New)", "Loader (New)", "Flatbed (New)", "Safety Man", "Truck Pusher", "Diesel"],
        "Total (SAR)": [(n_lowbed*p_lowbed), (n_flat_move*p_flat_move), (n_workshop*d_workshop*p_workshop), (n_tanker*d_tanker*p_tanker), (n_crane_old*d_crane_old*p_crane_old), (n_rigger_old*d_rigger_old*p_rigger_old), (n_loader_old*d_loader_old*p_loader_old), (n_crane_2_new*d_crane_2_new*p_crane_2_new), (n_crane_1_new*d_crane_1_new*p_crane_1_new), (n_loader_new*d_loader_new*p_loader_new), (n_fl_new*d_fl_new*p_fl_new), (n_safety_new*d_safety_new*p_safety_new), (n_tp_new*d_tp_new*p_tp_new), fuel_cost]
    }
    df = pd.DataFrame(excel_data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KTS_Summary_Report')
    st.download_button("📥 DOWNLOAD REPORT", buffer.getvalue(), f"KTS_{rig_name}.xlsx", "application/vnd.ms-excel")

st.markdown("<br><h1 class='shiny-text' style='font-size:45px; border-top:3px solid #00ffcc; padding-top:20px;'>Ahmed Mugali</h1>", unsafe_allow_html=True)
