# Deploying HackKit

## Option A: Streamlit Community Cloud (Free, Recommended)

### Prerequisites
- GitHub account
- Streamlit Cloud account (free at share.streamlit.io)

### Steps

1. **Push to GitHub:**
   ```bash
   cd HackKit
   git init
   git add .
   git commit -m "Initial commit: HackKit university hackathon toolkit"
   git remote add origin https://github.com/YOUR_USERNAME/HackKit.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Connect your GitHub repo
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Your app is live at:** `https://YOUR_APP_NAME.streamlit.app`

4. **Share the URL with judges** on event day. They open it on any device.

### Notes
- The database resets on each deployment (Streamlit Cloud is ephemeral)
- For persistent data, use the app during the event and download CSV before closing
- Each event gets a fresh start (this is a feature, not a bug)

---

## Option B: AWS Lightsail ($3.50/month)

### Steps

1. Create a Lightsail instance (Ubuntu, Nano plan)
2. SSH in and run:
   ```bash
   sudo apt update && sudo apt install python3-pip -y
   git clone https://github.com/YOUR_USERNAME/HackKit.git
   cd HackKit
   pip3 install -r requirements.txt
   streamlit run app.py --server.port 80 --server.headless true
   ```
3. Open port 80 in Lightsail networking tab
4. Access via the instance's public IP

---

## Option C: Run Locally (No Deploy)

```bash
pip install -r requirements.txt
streamlit run app.py
```

Share your screen or use a local network URL (shown in terminal output).

---

## Pre-Event Setup

Before the event, seed the database with your judges and categories:

```bash
# Edit seed_event.py with your judge names, then:
python seed_event.py
```

Or use the app UI to add judges, categories, and teams manually.

---

## Event Day Workflow

1. Open the app URL (or run locally)
2. Add team names as they register (Teams page)
3. Judges open the URL on their devices
4. Each judge selects their name and scores teams
5. After all presentations, go to Rankings
6. Download CSV for records
7. Announce winners!
