import streamlit as st
import pandas as pd
from datetime import datetime

# Setup
st.set_page_config(page_title="Athens Half Prep", layout="wide", page_icon="🏃")

# 1. Data Loading
@st.cache_data
def load_data():
    df = pd.read_csv('training_plan.csv')
    df.columns = df.columns.str.strip()
    return df

df = load_data()

# 2. Sidebar Navigation
st.sidebar.title("🇬🇷 Athens 21.1K")
week_idx = st.sidebar.slider("Current Training Week", 1, 6, 1)
current_week = df[df['Week'] == week_idx].iloc[0]

# 3. Dynamic Visuals based on Phase
phase = current_week['Phase']
images = {
    "Base": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?q=80&w=1000&auto=format&fit=crop",
    "Build": "https://images.unsplash.com/photo-1530143311094-34d807799e8f?q=80&w=1000&auto=format&fit=crop",
    "Peak": "https://images.unsplash.com/photo-1502224562085-639556652f33?q=80&w=1000&auto=format&fit=crop",
    "Taper": "https://images.unsplash.com/photo-1491553895911-0055eca6402d?q=80&w=1000&auto=format&fit=crop"
}

# 4. Main UI Header
st.title(f"Week {week_idx}: {phase} Phase")
st.image(images.get(phase, images["Base"]), use_container_width=True)

# 5. The Training Grid
st.subheader("Your Schedule")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
today_name = datetime.now().strftime("%a")

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

# 6. Functional Tooltips/Expanders
col1, col2 = st.columns(2)

with col1:
    with st.expander("🏋️ EZ Bar & Vest Protocol (Tuesdays)"):
        st.write("Focus on explosive power for the Athens hills.")
        st.info("Form Cue: 'Fast up, slow down' on squats.")
        st.markdown("- **Front Squats:** 3x12")
        st.markdown("- **Vest Lunges:** 3x10/leg")
        st.markdown("- **EZ Bar RDL:** 3x12")

with col2:
    with st.expander("🔥 5-Min Bulletproof Warm-Up"):
        st.write("Do this before Every session:")
        st.write("✅ Leg Swings (15 each) | ✅ Calf Stretches | ✅ World's Greatest Stretch")

# 7. Pace Table (Static Reference)
st.subheader("Pace & Heart Rate Targets")
st.table({
    "Session": ["Easy Run", "Long Run", "Race Pace", "Intervals"],
    "BPM": ["130-145", "135-150", "150-160", "166-175"],
    "Target Pace": ["6:30-6:50", "6:15-6:30", "5:41", "5:15-5:30"]
})