import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Athens Half Marathon Prep", layout="wide")

# 1. Load Data
df = pd.read_csv('training_plan.csv')

# 2. Sidebar Progress
st.sidebar.header("Progress Tracker")
current_week = st.sidebar.selectbox("Jump to Week", df['Week'].tolist())

# 3. Today's Workout Focus
st.header(f"Week {current_week}: {df.iloc[current_week-1]['Phase']} Phase")

# Create 7 columns for the week
cols = st.columns(7)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i, day in enumerate(days):
    with cols[i]:
        st.metric(label=day, value=df.iloc[current_week-1][day])

# 4. Technical Reminders (The Tooltips/Expanders)
st.divider()
st.subheader("Session Details & Cues")

with st.expander("Tuesday Strength Protocol"):
    st.write("**EZ Bar (Στραβόμπαρα) Focus:**")
    st.markdown("- Front Squats (Zercher): 3x12 (Fast up, slow down)")
    st.markdown("- Weighted Vest Lunges: 3x10/leg")
    st.markdown("- RDLs: 3x12 (Flat back)")
    st.info("Goal: Build explosive power for Athens hills.")

with st.expander("Warm-up & Injury Prevention (The 'Bulletproof' 5m)"):
    st.write("Do this before EVERY session:")
    st.help("Leg Swings, Calf Stretches, World's Greatest Stretch, Ankle Circles.")
    
with st.expander("Target Zones"):
    st.table({
        "Session": ["Easy", "Long Run", "Race Pace", "Intervals"],
        "BPM": ["130-145", "135-150", "150-160", "166-175"],
        "Pace": ["6:30-6:50", "6:15-6:30", "5:41", "5:15-5:30"]
    })