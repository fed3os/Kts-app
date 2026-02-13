import streamlit as st
from datetime import datetime
import pandas as pd
import io

# --- 1. Page Configuration ---
st.set_page_config(page_title="KTS Pro System | Ahmed Mugali", layout="centered")

# --- 2. Royal Neon Styling (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@700&display=swap');
    html, body, [class*="css"] { font-family: 'Tajawal', sans-serif; background-color: #000; color: #00ffcc; }
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.92)), 
        url("data:image/svg+xml,%3Csvg width='150' height='150' viewBox='0 0 150 150' xmlns='http://www.w3.org/2000/svg'%3E%3Ctext x='50%25' y='50%25' font-size='30' fill='rgba(0,255,204,0.1)' font-family='Arial' font-weight='bold' text-anchor='middle' dominant-baseline='middle'%3EKTS%3C/text%3E%3C/svg%3E");
    }
    .shiny-text { animation: blinker 1.8s linear infinite alternate; color: #00ffcc; text-align: center; font-weight: bold; }
    @keyframes blinker { from { opacity: 1.0; text-shadow: 0 0 15px #00ffcc, 0 0 30px #00ffcc; } to { opacity: 0.6; } }
    label { color: #ffffff !important; font-size: 18px !important; font-weight: bold !important; text-shadow: 2px 2px 4px #000; }
    .stNumberInput input, .stTextInput input { background-color: #111 !important; color: #00ffcc !important; border: 1px solid #00ffcc !important; font-size: 20px !important; border-radius: 10px !important; }
    .section-header { background: rgba(0, 255, 204, 0.1); border-left: 5px solid #00ffcc; padding: 10px; margin-top: 30px; color: #fff; font-size: 22px; font-weight: bold; border-radius: 5px; }
    .neon-card { background: rgba(0,255,204,0.08); border: 2px solid #00ffcc; border-radius: 20px; padding: 20px; text-align: center; margin-bottom: 15px; box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
    .stButton>button { width: 100%; height: 75px; background: linear-gradient(45deg, #00ffcc, #007bff) !important; color: #000 !important; font-weight: bold; font-size: 24px; border-radius: 18px; box-shadow: 0 0 25px #00ffcc; border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Header ---
st.markdown(f"<div class='shiny-text'>{datetime.now().strftime('%I:%M:%S %p')}</div>", unsafe_allow_html=True)
st.markdown('<h1 class="shiny-text" style="font-size: 50px; margin-bottom:0;">KTS RIG MOVE</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white; font-size:18px;'>Logistics & Support Management © 2026</p>", unsafe_allow_html=True)

st.write("---")

# --- 4. General Information ---
st.markdown("<div class='section-header'>1. General Information</div>", unsafe_allow_html=True)
rig_name = st.text_input("Rig Name / Number", placeholder="Enter Rig Details")
location_name = st.text_input("Destination / Location", placeholder="Enter Location")
dist = st.number_input("Total Distance (KM)", value=0)
d_price = st.number_input("Diesel Price per Litre", value=1.70, format="%.2f")

# --- 5. New Location Section ---
st.markdown("<div class='section-header'>2. New Location Requirements</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.info("🏗️ Cranes (New Loc)")
    n_crane_new = st.number_input("Crane Quantity", value=0, key="n_cn")
    d_crane_new = st.number_input("Crane Days", value=0, key="d_cn")
    p_crane_new = st.number_input("Crane Day Rate", value=0, key="p_cn")
    
    st.write("---")
    st.info("🚛 Flatbed (New Loc)")
    n_fl_new = st.number_input("Flatbed Quantity", value=0, key="n_fn")
    d_fl_new = st.number_input("Flatbed Days", value=0, key="d_fn")
    p_fl_new = st.number_input("Flatbed Day Rate", value=0, key="p_fn")

with col2:
    st.info("👮 Safety Man")
    n_safety = st.number_input("Safety Man Qty", value=0, key="n_sm")
    d_safety = st.number_input("Safety Man Days", value=0, key="d_sm")
    p_safety = st.number_input("Safety Man Day Rate", value=0, key="p_sm")
    
    st.write("---")
    st.info("👨‍💼 Truck Pusher (TP)")
    n_tp = st.number_input("TP Quantity", value=0, key="n_tp")
    d_tp = st.number_input("TP Days", value=0, key="d_tp")
    p_tp = st.number_input("TP Day Rate", value=0, key="p_tp")

# --- 6. Old Location & Support Section ---
st.markdown("<div class='section-header'>3. Old Location & Support</div>", unsafe_allow_html=True)
col3, col4 = st.columns(2)

with col3:
    st.info("🔧 Rigger (Old Loc)")
    n_rigger_old = st.number_input("Rigger Quantity", value=0, key="n_ro")
    d_rigger_old = st.number_input("Rigger Days", value=0, key="d_ro")
    p_rigger_old = st.number_input("Rigger Day Rate", value=0, key="p_ro")
    
    st.write("---")
    st.info("⛽ Diesel Tanker")
    n_tanker = st.number_input("Tanker Quantity", value=0, key="n_dt")
    d_tanker = st.number_input("Tanker Days", value=0, key="d_dt")
    p_tanker = st.number_input("Tanker Day Rate", value=0, key="p_dt")

with col4:
    st.info("🚜 Support Equipment")
    n_loader = st.number_input("Loader Quantity", value=0, key="n_lo")
    d_loader = st.number_input("Loader Days", value=0, key="d_lo")
    p_loader = st.number_input("Loader Day Rate", value=0, key="p_lo")
    
    st.write("---")
    st.info("🚚 Lowbed Move")
    n_lowbed = st.number_input("Lowbed Quantity", value=0, key="n_lb")
    p_lowbed = st.number_input("Lowbed Trip/Day Rate", value=0, key="p_lb")

# --- 7. Calculation Logic ---
st.write("<br>", unsafe_allow_html=True)
if st.button("🚀 CALCULATE & EXPORT EXCEL"):
    # Fuel Consumption Calculations (Based on your standards)
    # Lowbed (1.57 L/km), Flatbed (1.39 L/km), Equipment (200L per day active)
    fuel_l = (n_lowbed * dist * 1.57) + (n_fl_new * dist * 1.39) + \
             ((n_crane_new * d_crane_new + n_loader * d_loader + n_tanker * d_tanker) * 200)
    fuel_cost = fuel_l * d_price
    
    # Rental & Services Costs
    rent_total = (n_crane_new * d_crane_new * p_crane_new) + \
                 (n_fl_new * d_fl_new * p_fl_new) + \
                 (n_safety * d_safety * p_safety) + \
                 (n_tp * d_tp * p_tp) + \
                 (n_rigger_old * d_rigger_old * p_rigger_old) + \
                 (n_tanker * d_tanker * p_tanker) + \
                 (n_loader * d_loader * p_loader) + \
                 (n_lowbed * p_lowbed)
    
    grand_total = fuel_cost + rent_total

    # Display Result
    st.markdown(f"""
        <div class="neon-card" style="background: #00ffcc; color: #000; box-shadow: 0 0 30px #00ffcc;">
            <p style="margin: 0; font-size: 20px; font-weight: bold;">TOTAL PROJECT BUDGET</p>
            <h1 style="font-size: 55px; margin: 0; font-weight: 900;">{grand_total:,.2f} SAR</h1>
        </div>
    """, unsafe_allow_html=True)

    # --- 8. Comprehensive Excel Export ---
    report_data = {
        "Category": ["General", "General", "General", "New Loc", "New Loc", "Personnel", "Personnel", "Old Loc", "Support", "Support", "Fleet", "Totals", "Totals"],
        "Item Description": ["Rig Name", "Location", "Distance KM", "Cranes", "Flatbeds", "Safety Man", "Truck Pusher", "Riggers", "Diesel Tanker", "Loader", "Lowbeds", "Fuel (Litre)", "Grand Total"],
        "Qty/Days": [rig_name, location_name, dist, f"{n_crane_new} units / {d_crane_new} days", f"{n_fl_new} units / {d_fl_new} days", f"{n_safety} units / {d_safety} days", f"{n_tp} units / {d_tp} days", f"{n_rigger_old} units / {d_rigger_old} days", f"{n_tanker} units / {d_tanker} days", f"{n_loader} units / {d_loader} days", n_lowbed, f"{fuel_l:,.2f} L", f"{grand_total:,.2f} SAR"],
        "Rate": ["-", "-", d_price, p_crane_new, p_fl_new, p_safety, p_tp, p_rigger_old, p_tanker, p_loader, p_lowbed, "-", "-"]
    }
    
    df = pd.DataFrame(report_data)
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='KTS_Project_Summary')
    
    st.download_button(
        label="📥 DOWNLOAD EXCEL REPORT",
        data=buffer.getvalue(),
        file_name=f"KTS_Report_{rig_name}_{datetime.now().strftime('%Y%m%d')}.xlsx",
        mime="application/vnd.ms-excel"
    )

# --- 9. Footer ---
st.write("<br><br>")
st.markdown(f"""
    <div style='text-align: center; border-top: 3px solid #00ffcc; padding-top: 30px;'>
        <h1 class="shiny-text" style='font-size: 45px;'>Ahmed Mugali</h1>
        <p style='color: #ffffff; font-size: 16px; letter-spacing: 2px;'>KTS LOGISTICS MASTER SYSTEM © 2026</p>
    </div>
""", unsafe_allow_html=True)
