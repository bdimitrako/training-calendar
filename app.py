import streamlit as st
import pandas as pd
from datetime import datetime

# Setup
st.set_page_config(page_title="Athens Half Prep", layout="wide")

# Load and Strip Spaces
df = pd.read_csv('training_plan.csv')
df.columns = df.columns.str.strip()

# Sidebar
st.sidebar.title("🇬🇷 Athens Half 2026")
week_idx = st.sidebar.slider("Current Training Week", 1, 6, 1)
current_week = df[df['Week'] == week_idx].iloc[0]

# Main UI
st.title(f"Week {week_idx}: {current_week['Phase']} Phase")

# Create 7 Columns for the week
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
today_name = datetime.now().strftime("%a")

cols = st.columns(7)
for i, day in enumerate(days):
    with cols[i]:
        if day == today_name:
            st.success(f"**{day} (Today)**")
            st.write(current_week[day])
        else:
            st.write(f"**{day}**")
            st.caption(current_week[day])

st.divider()

# Specific Reminders (The "Tooltips")
col1, col2 = st.columns(2)

with col1:
    with st.expander("🏋️ Today's Strength Drill (Tuesdays)"):
        st.write("**Equipment:** EZ Bar (Στραβόμπαρα)")
        st.markdown("""
        - **Front Squats (Zercher):** 3x12 (Fast up, slow down)
        - **Weighted Vest Lunges:** 3x10 per leg
        - **EZ Bar RDL:** 3x12 (Keep back flat)
        - **Plank:** 3x60s (Use vest for resistance)
        """)

with col2:
    with st.expander("🔥 5-Min Bulletproof Warm-Up"):
        st.info("Do this before the Rouvy bike or running:")
        st.write("- Leg Swings (Front/Side): 15 each")
        st.write("- Dynamic Calf Stretch: 10 per side")
        st.write("- World's Greatest Stretch: 5 per side")
        st.write("- Air Squats: 15 reps")

# Pace Table
st.subheader("Target Reference")
st.table({
    "Activity": ["Easy Run", "Long Run", "Race Pace", "Intervals"],
    "BPM Range": ["130-145", "135-150", "150-160", "166-175"],
    "Target Pace": ["6:30-6:50", "6:15-6:30", "5:41", "5:15-5:30"]
})