# HackKit

**A complete, pick-up-and-run toolkit for organizing GenAI hackathons at universities.**

Built from real experience running the #BeTheAgenticBuilder Hackathon at the University of Maryland (April 2026). Designed so anyone on the team can take this kit, customize it for their university, and execute a successful event.

---

## What's Inside

```
HackKit/
|-- playbook/               <-- Step-by-step guides (start here)
|   |-- 00_overview.md      <-- Read this first
|   |-- 01_planning.md      <-- 8-6 weeks out
|   |-- 02_recruitment.md   <-- 6-4 weeks out
|   |-- 03_content.md       <-- 4-2 weeks out
|   |-- 04_team_prep.md     <-- 2-1 weeks out
|   |-- 05_event_day.md     <-- Day-of run of show
|   |-- 06_judging.md       <-- How to use the scoring app
|   |-- 07_post_event.md    <-- Follow-up actions
|   |-- 08_lessons_learned.md
|
|-- templates/              <-- Editable templates (fill in [BRACKETS])
|   |-- email_invite_professor.md
|   |-- volunteer_briefing.md
|   |-- flyer_template.md
|   |-- linkedin_post_template.md
|   |-- agenda_template.md
|   |-- thank_you_students.md
|
|-- app.py                  <-- Scoring app (Streamlit)
|-- db.py                   <-- Database layer
|-- pages/                  <-- Scoring app pages
|-- KNOWLEDGE_BASE.md       <-- UMD 2026 reference data
|-- requirements.txt
```

---

## Quick Start (5 Minutes)

1. **Read the playbook overview:** `playbook/00_overview.md`
2. **Follow sections 01-08 in order** (each has checklists)
3. **Customize templates** for your university (replace `[BRACKETED]` fields)
4. **Set up the scoring app** for event day:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Who Is This For?

Any AWS employee (CSM, SA, AM, or volunteer) who wants to run a GenAI hackathon at a university. No prior event planning experience required. Just follow the playbook.

---

## The Event Formula

Students learn AWS Working Backwards methodology, then build a GenAI app using PartyRock (no code required), then pitch it to judges. Total time: 5 hours. Result: portfolio-ready deliverables for students, brand engagement for AWS.

---

## Created By

Kavita Chhabria, Sr. Customer Solutions Manager, AWS
Based on the UMD College Park event, April 24, 2026.
