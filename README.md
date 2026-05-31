# AMISES: Autonomous Micro-Income Agent Suite

This project is a high-fidelity execution suite showing how an autonomous language model agent can generate freelance revenue and digital asset sales using solely its native cognitive capabilities (writing, coding, design, and outreach).

The project is structured with a gorgeous, dark-themed, glassmorphic frontend dashboard along with automated Python scripts that perform live freelance gig scraping, solution compilation, and real-world email SMTP automation.

---

## 📂 Project Structure

```
amises-autonomous-micro-income-suite/
├── index.html                  # Premium glassmorphic Command Center (Dashboard)
├── index.css                   # Visual guidelines, color system, and HSL glow tokens
├── app.js                      # Application controller, live database feed, and SMTP console
├── README.md                   # This project guide
├── config.json                 # SMTP configurations and leads database
├── scripts/                    # Core execution backends
│   ├── asset_generator.py      # Generates ready-to-sell expert digital products
│   ├── real_gig_scraper.py     # Scrapes live remote programming RSS feeds and solves them
│   └── real_gig_hunter_sender.py # Value-first SMTP automation email sender
└── outputs/                    # Scraped jobs database and premium educational e-books
    ├── Prompt_Engineering_Playbook.md        # Specialized expert prompt playbook (PLR)
    ├── High_Conversion_Copywriting_Kit.txt   # Outreach templates and Gumroad landing copy
    └── jobs_database.json                    # Real-time remote jobs and solutions feed
```

---

## 📈 The Three Earning Funnels

1. **Path A: The Digital Asset Factory**
   - **Product**: `Prompt_Engineering_Playbook.md` (retail value $5.00) & `Glassmorphism_UI_Boilerplate.zip` (retail value $5.00).
   - **Mechanism**: Instant digital downloads on Payhip or Gumroad with 100% margins and PLR rights.

2. **Path B: The Micro-Gig Hunter (Immediate Value Delivery)**
   - **Product**: Pre-written, targeted code solutions tailored to active remote developer postings.
   - **Mechanism**: The scraper parses live boards, while the agent writes custom solutions and cover letters, storing them in a local JSON feed for rapid bidding or direct SMTP cold dispatch. A single contract yields **$15.00 – $25.00**.

3. **Path C: Exposing Local Dashboards**
   - Expose your workspace dashboard globally using public tunnels to pitch front-end capability live to potential clients.

---

## 🚀 Running Your Suite Locally

### Step 1: Parse Live Jobs
First, activate the autonomous crawlers to fetch the latest freelance programming jobs and solve them:
```bash
python scripts/real_gig_scraper.py
```
This updates `outputs/jobs_database.json` with fresh live listings and complete, formatted solutions.

### Step 2: Compile Premium Assets
Compile the latest developer e-books and the glassmorphism CSS components boilerplate package:
```bash
python scripts/asset_generator.py
```

### Step 3: Run the Visual Command Center
Launch a local web server to serve the frontend, allowing standard browser requests to fetch output data files seamlessly:
```bash
python -m http.server 8000
```
Navigate to `http://localhost:8000` to interact with your live Control Center!

---

## 📜 Resell and License
All materials compiled by the Asset Generator (e.g. Prompt Playbook, UI cards, email kits) are licensed under Private Label Rights (PLR). You have full permission to rebrand, sell, or package these products as your own and retain 100% of the revenue.
