import streamlit as st
from datetime import datetime
import pandas as pd
import io

# --- 1. Page Configuration ---
st.set_page_config(page_title="KTS Specialized | Ahmed Mugali", layout="centered")

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
    label { color: #ffffff !important; font-size: 18px !important; font-weight: bold !important; }
    .stNumberInput input, .stTextInput input { background-color: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; font-size: 20px !important; }
    .section-header { background: rgba(0, 255, 204, 0.15); border-left: 5px solid #00ffcc; padding: 10px; margin-top: 25px; color: #fff; font-size: 22px; font-weight: bold; border-radius: 5px; }
    .neon-card { background: rgba(0,255,204,0.08); border: 2px solid #00ffcc; border-radius: 20px; padding: 20px; text-align: center; margin-bottom: 15px; }
    .stButton>button { width: 100%; height: 70px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 24px; border-radius: 15px; box-shadow: 0 0 20px #00ffcc; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 45px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>Ahmed Mugali Logistics Pro © 2026</p>", unsafe_allow_html=True)

# --- 4. General Info ---
st.markdown("<div class='section-header'>1. Project Details</div>", unsafe_allow_html=True)
rig_name = st.text_input("Rig Name / Number")
location_name = st.text_input("Location")
dist = st.number_input("Rig Move Distance (KM)", value=0)
d_price = st.number_input("Diesel Price", value=1.70)

# --- 5. New Location Section ---
st.markdown("<div class='section-header'>2. New Location Requirements</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.info("🏗️ Cranes & Flatbed")
    n_crane_2 = st.number_input("2 Cranes - Qty", value=2)
    d_crane_2 = st.number_input("2 Cranes - Days", value=0)
    p_crane_2 = st.number_input("2 Cranes - Day Rate", value=0)
    st.write("---")
    n_crane_1 = st.number_input("One Crane - Qty", value=1)
    d_crane_1 = st.number_input("One Crane - Days", value=0)
    p_crane_1 = st.number_input("One Crane - Day Rate", value=0)
    st.write("---")
    n_fl_new = st.number_input("One Flatbed - Qty", value=1)
    d_fl_new = st.number_input("One Flatbed - Days", value=0)
    p_fl_new = st.number_input("One Flatbed - Day Rate", value=0)

with col2:
    st.info("👮 Personnel Support")
    n_safety = st.number_input("Safety Man - Qty", value=1)
    d_safety = st.number_input("Safety Man - Days", value=0)
    p_safety = st.number_input("Safety Man - Day Rate", value=0)
    st.write("---")
    n_tp_new = st.number_input("Truck Pusher (TP) - Qty", value=1)
    d_tp_new = st.number_input("TP - Days", value=0)
    p_tp_new = st.number_input("TP - Day Rate", value=0)
    st.write("---")
    n_rigger_old = st.number_input("Rigger (Old Loc) - Qty", value=1)
    d_rigger_old = st.number_input("Rigger - Days", value=0)
    p_rigger_old = st.number_input("Rigger - Day Rate", value=0)

# --- 6. Rig Move & Workshop Section ---
st.markdown("<div class='section-header'>3. Rig Move & Workshop Team</div>", unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    st.info("🚚 Fleet & Logistics")
    n_lowbed = st.number_input("Lowbed Quantity", value=0)
    p_lowbed = st.number_input("Lowbed Rate (Trip/Day)", value=0)
    st.write("---")
    n_flatbed_move = st.number_input("Flatbed Move Qty", value=0)
    p_flatbed_move = st.number_input("Flatbed Move Rate", value=0)

with col4:
    st.info("🔧 Workshop & Fuel")
    n_workshop = st.number_input("Workshop Team Qty", value=1)
    d_workshop = st.number_input("Workshop Team Days", value=0)
    p_workshop = st.number_input("Workshop Team Day Rate", value=0)
    st.write("---")
    n_tanker = st.number_input("Diesel Tanker Qty", value=1)
    d_tanker = st.number_input("Diesel Tanker Days", value=0)
    p_tanker = st.number_input("Diesel Tanker Day Rate", value=0)

# --- 7. Calculations ---
if st.button("🚀 CALCULATE & GENERATE EXCEL"):
    # Fuel Calculation
    fuel_l = (n_lowbed * dist * 1.57) + (n_flatbed_move * dist * 1.39) + \
             ((n_crane_2 + n_crane_1 + n_tanker) * 200 * (d_crane_2 + d_crane_1 + d_tanker)/3)
    fuel_cost = fuel_l * d_price
    
    # Rental & Services Costs
    rent_total = (n_crane_2 * d_crane_2 * p_crane_2) + \
                 (n_crane_1 * d_crane_1 * p_crane_1) + \
                 (n_fl_new * d_fl_new * p_fl_new) + \
                 (n_safety * d_safety * p_safety) + \
                 (n_tp_new * d_tp_new * p_tp_new) + \
                 (n_rigger_old * d_rigger_old * p_rigger_old) + \
                 (n_lowbed * p_lowbed) + (n_flatbed_move * p_flatbed_move) + \
                 (n_workshop * d_workshop * p_workshop) + \
                 (n_tanker * d_tanker * p_tanker)
    
    grand_total = fuel_cost + rent_total

    st.markdown(f"""
        <div class="neon-card" style="background: #00ffcc; color: #000;">
            <p style="margin: 0; font-size: 20px; font-weight: bold;">TOTAL PROJECT BUDGET</p>
            <h1 style="font-size: 50px; margin: 0;">{grand_total:,.2f} SAR</h1>
        </div>
    """, unsafe_allow_html=True)

    # --- 8. Excel Report ---
    report_data = {
        "Description": ["Rig Name", "Location", "Distance (KM)", "2 Cranes Cost", "One Crane Cost", "One Flatbed Cost", "Safety Man Cost", "TP Cost", "Rigger Cost", "Lowbed Total", "Flatbed Move Total", "Workshop Team Cost", "Diesel Tanker Cost", "Fuel Cost", "Grand Total"],
        "Value (SAR)": [rig_name, location_name, dist, (n_crane_2*d_crane_2*p_crane_2), (n_crane_1*d_crane_1*p_crane_1), (n_fl_new*d_fl_new*p_fl_new), (n_safety*d_safety*p_safety), (n_tp_new*d_tp_new*p_tp_new), (n_rigger_old*d_rigger_old*p_rigger_old), (n_lowbed*p_lowbed), (n_flatbed_move*p_flatbed_move), (n_workshop*d_workshop*p_workshop), (n_tanker*d_tanker*p_tanker), f"{fuel_cost:,.2f}", f"{grand_total:,.2f}"]
    }
    df = pd.DataFrame(report_data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KTS_Summary')
    
    st.download_button("📥 DOWNLOAD EXCEL REPORT", buffer.getvalue(), f"KTS_{rig_name}.xlsx", "application/vnd.ms-excel")

st.markdown("<br><h1 class='shiny-text' style='font-size:40px; border-top:2px solid #00ffcc; padding-top:20px;'>Ahmed Mugali</h1>", unsafe_allow_html=True)
