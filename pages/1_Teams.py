import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import db

st.set_page_config(page_title="Teams - HackKit", page_icon="people", layout="wide")
st.title("Teams")

with st.expander("Add New Team", expanded=False):
    with st.form("add_team"):
        name = st.text_input("Team Name")
        members = st.text_input("Members (comma-separated)")
        project_title = st.text_input("Project Title")
        submitted = st.form_submit_button("Add Team")
        if submitted and name:
            db.add_team(name, members, project_title)
            st.success(f"Added team: {name}")
            st.rerun()

teams = db.get_teams()
if teams:
    st.subheader(f"Registered Teams ({len(teams)})")
    for team in teams:
        col1, col2, col3, col4 = st.columns([2, 3, 3, 1])
        col1.write(f"**{team['name']}**")
        col2.write(team["members"] or "-")
        col3.write(team["project_title"] or "-")
        if col4.button("X", key=f"del_{team['id']}"):
            db.delete_team(team["id"])
            st.rerun()
else:
    st.info("No teams registered yet. Add one above!")
