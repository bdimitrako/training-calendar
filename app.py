import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="Athens Half Prep", layout="wide", page_icon="🏃")

# 2. Data Loading (Cached for performance)
@st.cache_data
def load_data():
    # Make sure your training_plan.csv has headers: Week,Phase,Mon,Tue,Wed,Thu,Fri,Sat,Sun
    df = pd.read_csv('training_plan.csv')
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

# 3. Sidebar Navigation & State
st.sidebar.title("🇬🇷 Athens 21.1K")
week_idx = st.sidebar.slider("Current Training Week", 1, 6, 1)
current_week = df[df['Week'] == week_idx].iloc[0]
today_name = datetime.now().strftime("%a")

st.sidebar.divider()
basement_mode = st.sidebar.toggle("Activate Basement Mode 📶")

# 4. Background Image and Styling (Grayed-out effect)
bg_img_url = "https://images.unsplash.com/photo-1530143311094-34d807799e8f?q=80&w=2000"

st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url("{bg_img_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    h1, h2, h3, p, .stMarkdown, .stMetric, [data-testid="stHeader"] {{
        color: white !important;
    }}
    .basement-card {{
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #00ffcc;
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# 5. Logic Branch: Basement Mode vs. Normal UI
if basement_mode:
    st.title("🏃 BASEMENT MODE: ACTIVE")
    st.warning("Signal lost? No problem. Screenshot this screen now.")
    
    st.markdown(f"""
    <div class="basement-card">
        <h2>Today: {current_week[today_name]}</h2>
        <hr>
        <h3>🏋️ Strength Protocol</h3>
        <ul>
            <li><b>Zercher Start:</b> 3x12 (Hook bar in elbows from floor)</li>
            <li><b>Weighted Vest Lunges:</b> 3x10 per leg</li>
            <li><b>EZ Bar RDL:</b> 3x12</li>
            <li><b>Plank:</b> 3x60s (Weighted vest optional)</li>
        </ul>
        <h3>🚴 Rouvy Focus</h3>
        <p>30-40m Z2 Pace (Conversational effort)</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🦶 Ankle Alphabet Drill (Rest Period)"):
        st.write("While resting, 'write' the Greek alphabet in the air with your big toe.")
        st.caption("Strengthens stabilizers for the uneven Athens asphalt.")
        

    # Offline Timer Component
    st.subheader("⏱️ Offline Timer")
    components.html("""
        <div style="color: white; font-family: sans-serif; text-align: center; background: #262730; padding: 15px; border-radius: 10px; border: 1px solid #444;">
            <h1 id="timer" style="font-size: 40px; margin: 0;">01:00</h1>
            <div style="margin-top: 10px;">
                <button onclick="startTimer(60)" style="padding: 10px 20px; font-size: 16px;">Plank (1m)</button>
                <button onclick="startTimer(120)" style="padding: 10px 20px; font-size: 16px; margin-left: 10px;">Rest (2m)</button>
            </div>
        </div>
        <script>
            let timerDisplay = document.getElementById('timer');
            function startTimer(duration) {
                let timer = duration, minutes, seconds;
                let countdown = setInterval(function () {
                    minutes = parseInt(timer / 60, 10);
                    seconds = parseInt(timer % 60, 10);
                    minutes = minutes < 10 ? "0" + minutes : minutes;
                    seconds = seconds < 10 ? "0" + seconds : seconds;
                    timerDisplay.textContent = minutes + ":" + seconds;
                    if (--timer < 0) { 
                        clearInterval(countdown); 
                        timerDisplay.textContent = "DONE!"; 
                        alert("Timer Finished!");
                    }
                }, 1000);
            }
        </script>
    """, height=180)
    st.stop() 

else:
    # NORMAL UI (The Regular Dashboard)
    st.title(f"Week {week_idx}: {current_week['Phase']} Phase")
    
    # Weekly Grid
    st.subheader("Weekly Overview")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    cols = st.columns(7)
    
    for i, day in enumerate(days):
        with cols[i]:
            if day == today_name:
                st.success(f"**{day} (Today)**")
                st.markdown(f"**{current_week[day]}**")
            else:
                st.write(f"**{day}**")
                st.caption(current_week[day])

    st.divider()

    # Expanders for Cues
    col_a, col_b = st.columns(2)
    with col_a:
        with st.expander("🏋️ Strength Details"):
            st.write("**EZ Bar (Στραβόμπαρα) Cues:**")
            st.write("- Front Squats (Zercher): 'Fast up, slow down'")
            st.write("- Lunges: 3x10/leg")
            st.write("- RDL: 3x12 (Flat back)")
            
    with col_b:
        with st.expander("⏱️ Pace & HR Table"):
            st.table({
                "Target": ["Easy", "Long", "Race", "Intervals"],
                "BPM": ["130-145", "135-150", "150-160", "166-175"],
                "Pace": ["6:30-6:50", "6:15-6:30", "5:41", "5:15-5:30"]
            })
            

    # Warm-Up Reminder
    with st.expander("🔥 5-Min Bulletproof Warm-Up"):
        st.write("1. Leg Swings (Front/Side) - 15 per leg")
        st.write("2. Dynamic Calf Stretch - 10 per side")
        st.write("3. World's Greatest Stretch - 5 per side")
        st.write("4. Air Squats - 15 reps")