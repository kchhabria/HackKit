import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import db

st.set_page_config(page_title="Schedule - HackKit", page_icon="calendar", layout="wide")
st.title("Schedule")

teams = db.get_teams()
if not teams:
    st.warning("Add teams first before setting up the schedule.")
    st.stop()

st.subheader("Set Presentation Slots")
for team in teams:
    col1, col2, col3 = st.columns([3, 2, 2])
    col1.write(f"**{team['name']}**")
    time_slot = col2.text_input("Time", key=f"time_{team['id']}", placeholder="e.g. 10:00 AM")
    room = col3.text_input("Room", key=f"room_{team['id']}", placeholder="e.g. Room A")
    if time_slot or room:
        db.upsert_schedule(team["id"], time_slot, room)

st.divider()
st.subheader("Current Schedule")
schedule = db.get_schedule()
if schedule:
    for slot in schedule:
        st.write(f"**{slot['time_slot']}** | {slot['team_name']} | {slot['room']}")
else:
    st.info("No schedule entries yet.")
