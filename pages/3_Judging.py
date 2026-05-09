import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import db

st.set_page_config(page_title="Judging - HackKit", page_icon="scales", layout="wide")
st.title("Judging")

with st.expander("Setup Judges and Categories"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Judges**")
        with st.form("add_judge"):
            judge_name = st.text_input("Judge Name")
            if st.form_submit_button("Add Judge") and judge_name:
                db.add_judge(judge_name)
                st.rerun()
        for j in db.get_judges():
            c1, c2 = st.columns([4, 1])
            c1.write(j["name"])
            if c2.button("X", key=f"dj_{j['id']}"):
                db.delete_judge(j["id"])
                st.rerun()
    with col2:
        st.markdown("**Categories**")
        with st.form("add_category"):
            cat_name = st.text_input("Category Name")
            cat_weight = st.number_input("Weight (%)", min_value=0, max_value=100, value=20)
            if st.form_submit_button("Add Category") and cat_name:
                db.add_category(cat_name, cat_weight / 100.0)
                st.rerun()
        for c in db.get_categories():
            c1, c2 = st.columns([4, 1])
            c1.write(f"{c['name']} ({int(c['weight']*100)}%)")
            if c2.button("X", key=f"dc_{c['id']}"):
                db.delete_category(c["id"])
                st.rerun()

st.divider()

judges = db.get_judges()
teams = db.get_teams()
categories = db.get_categories()

if not judges or not teams or not categories:
    st.info("Add judges, teams, and categories to start scoring.")
    st.stop()

st.subheader("Score Entry")
selected_judge = st.selectbox("Select Judge", judges, format_func=lambda j: j["name"])

if selected_judge:
    for team in teams:
        st.markdown(f"**{team['name']}**")
        cols = st.columns(len(categories))
        for i, cat in enumerate(categories):
            score = cols[i].number_input(
                cat["name"], min_value=0, max_value=10, value=0,
                key=f"score_{selected_judge['id']}_{team['id']}_{cat['id']}")
            if score > 0:
                db.upsert_score(selected_judge["id"], team["id"], cat["id"], score)

st.divider()
st.subheader("Rankings")

scores = db.get_scores()
if scores:
    results = {}
    for team in teams:
        weighted_total = 0
        for cat in categories:
            cat_scores = [s["value"] for s in scores if s["team_id"] == team["id"] and s["category_id"] == cat["id"]]
            if cat_scores:
                avg = sum(cat_scores) / len(cat_scores)
                weighted_total += avg * cat["weight"]
        results[team["name"]] = round(weighted_total, 2)

    df = pd.DataFrame(
        sorted(results.items(), key=lambda x: x[1], reverse=True),
        columns=["Team", "Weighted Score"])
    df.index = range(1, len(df) + 1)
    df.index.name = "Rank"
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv()
    st.download_button("Download Results CSV", csv, "hackkit_results.csv", "text/csv")
else:
    st.info("No scores entered yet.")
