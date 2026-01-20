import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Athens Half Prep", layout="wide")

# Load and clean
df = pd.read_csv('training_plan.csv')
df.columns = df.columns.str.strip()

# Sidebar: Quick Navigation
st.sidebar.title("🏃 Athens 21.1K")
week_idx = st.sidebar.slider("Select Training Week", 1, 6, 1)
current_week = df[df['Week'] == week_idx].iloc[0]

# UI Header
st.title(f"Week {week_idx}: {current_week['Phase']}")

# Days Display
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
today_name = datetime.now().strftime("%a") # e.g., 'Tue'

cols = st.columns(7)
for i, day in enumerate(days):
    with cols[i]:
        # Highlight today
        if day == today_name:
            st.success(f"**{day} (Today)**")
            st.info(current_week[day])
        else:
            st.write(f"**{day}**")
            st.caption(current_week[day])

# Tooltip Reminders section
st.divider()
col1, col2 = st.columns(2)

with col1:
    with st.expander("💡 Tuesdays: EZ Bar & Vest Cues"):
        st.write("- **Squats:** Fast up, slow down (Explosive power).")
        st.write("- **Lunges:** Focus on stability, use the vest for weeks 2-4.")
        st.write("- **Post-Strength:** 30-40m Rouvy (Conversational Z2).")

with col2:
    with st.expander("📈 Pace & HR Targets"):
        st.write("- **Easy/Long:** 130-150 bpm | 6:15-6:50 min/km")
        st.write("- **Race Pace:** 150-160 bpm | **5:41 min/km**")
        st.write("- **Intervals:** 166-175 bpm")