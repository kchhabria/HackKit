# 06 - Judging Guide

## Using the HackKit Scoring App

### Setup (Before Presentations Start)

```bash
cd HackKit
pip install -r requirements.txt
streamlit run app.py
```

1. Go to **Judging** page in sidebar
2. Add judges by name
3. Add categories with weights:
   - Business Impact / Industry Alignment: 40%
   - Technical Excellence: 40%
   - Innovation: 20%
4. Go to **Teams** page and add all team names

### During Presentations

1. Each judge selects their name from the dropdown
2. For each team, score 1-10 in each category
3. Scores auto-save

### After All Presentations

1. Scroll to "Rankings" section
2. App calculates weighted averages across all judges
3. Download CSV for records
4. Announce top 3

## Scoring Guidelines

### Business Impact / Industry Alignment (40%)

| Score | Meaning |
|-------|---------|
| 9-10 | Exceptional PR/FAQ, clear real-world problem, compelling pitch |
| 7-8 | Strong PR/FAQ, good problem definition, solid presentation |
| 5-6 | Adequate PR/FAQ, problem identified but could be sharper |
| 3-4 | Weak PR/FAQ, vague problem, disorganized presentation |
| 1-2 | No clear problem or solution, poor delivery |

### Technical Excellence (40%)

| Score | Meaning |
|-------|---------|
| 9-10 | Advanced PartyRock features, sophisticated AI integration, flawless demo |
| 7-8 | Good PartyRock usage, solid implementation, working demo |
| 5-6 | Basic PartyRock app, functions correctly, simple demo |
| 3-4 | Minimal features, partially working |
| 1-2 | Barely functional or no working demo |

### Innovation (20%)

| Score | Meaning |
|-------|---------|
| 9-10 | Truly original idea, creative approach nobody else thought of |
| 7-8 | Original with creative elements, clear differentiation |
| 5-6 | Some creativity but follows common patterns |
| 3-4 | Generic approach, nothing distinctive |
| 1-2 | Copy of existing solution, no originality |

## Tips for Judges

- Score independently (do not discuss with other judges during presentations)
- Use the full range (do not cluster everything at 7-8)
- Ask at least one question per team
- Be encouraging regardless of score (these are students!)
