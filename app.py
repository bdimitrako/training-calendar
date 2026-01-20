import streamlit as st
import pandas as pd
from datetime import datetime
import streamlit.components.v1 as components

st.set_page_config(page_title="Athens Prep: Basement Mode", layout="wide")

# 1. CSS for Background & Contrast
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: white; }
    .stMarkdown, p, h1, h2, h3 { color: white !important; }
    .basement-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Data Load
@st.cache_data
def load_data():
    df = pd.read_csv('training_plan.csv')
    df.columns = df.columns.str.strip()
    return df

df = load_data()
today_name = datetime.now().strftime("%a")
week_idx = st.sidebar.slider("Week", 1, 6, 1)
current_week = df[df['Week'] == week_idx].iloc[0]

# 3. BASEMENT MODE TRIGGER
st.sidebar.divider()
basement_mode = st.sidebar.toggle("Activate Basement Mode 📶")

if basement_mode:
    st.title("🏃 BASEMENT MODE: ACTIVE")
    st.warning("Signal lost? No problem. Screenshot this screen now.")
    
    st.markdown(f"""
    <div class="basement-card">
        <h2>Today: {current_week[today_name]}</h2>
        <hr>
        <h3>🏋️ Strength Protocol</h3>
        <ul>
            <li><b>Zercher Deadlift to Squat:</b> 3x12 (Hook bar in elbows from floor)</li>
            <li><b>Weighted Vest Lunges:</b> 3x10 per leg</li>
            <li><b>EZ Bar RDL:</b> 3x12</li>
            <li><b>Plank:</b> 3x60s (Use Vest)</li>
        </ul>
        <h3>🚴 Rouvy Focus</h3>
        <p>30-40m Z2 Pace (Conversational)</p>
    </div>
    """, unsafe_allow_html=True)

    # 4. JS Offline Timer (Runs in browser even without signal)
    st.subheader("⏱️ Basement Timer")
    components.html("""
        <div style="color: white; font-family: sans-serif; text-align: center; background: #262730; padding: 10px; border-radius: 10px;">
            <h1 id="timer">01:00</h1>
            <button onclick="startTimer(60)" style="padding: 10px;">Plank (1m)</button>
            <button onclick="startTimer(120)" style="padding: 10px;">Rest (2m)</button>
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
                    if (--timer < 0) { clearInterval(countdown); timerDisplay.textContent = "DONE!"; }
                }, 1000);
            }
        </script>
    """, height=150)
    st.stop() # Prevents heavy images/logic from loading below

# 5. Normal UI Logic (for when you have signal)
st.title(f"Week {week_idx}: {current_week['Phase']}")
# ... (rest of your existing UI code)