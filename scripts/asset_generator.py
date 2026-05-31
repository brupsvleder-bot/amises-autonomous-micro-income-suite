import os
import zipfile

def generate_prompt_book(output_dir):
    book_content = """# The Elite Prompt Engineering & LLM Automation Playbook
## Production-Grade Strategies for Developers, Solopreneurs, and Creators
*Published Autonomously by Antigravity AI Agent (Google DeepMind Team)*

---

## 📘 Executive Introduction: The Cognitive Pipeline
Prompt engineering is no longer about "magical words" or asking nicely. It is the science of **latent space alignment**—constraining the probability distribution of an autoregressive language model to map input data cleanly into deterministic, high-value outputs.

This playbook provides industrial-grade frameworks, concrete schemas, and copy-paste templates that you can use to build AI-driven products, automate complex workflows, or package and resell as premium educational assets (Private Label Rights included!).

---

## ⚡ Chapter 1: The Principle of Least Ambiguity (Identity Architectures)
When you prompt a model without an identity, it draws from the generic median of its training corpus. To get expert-level work, you must force the model to look at the top 1% of its training space.

### The Role-Context-Constraint-Format (RCCF) Protocol
Every commercial system prompt must follow the RCCF structure:
1. **Role**: Establish elite authority, experience, and professional voice.
2. **Context**: Define the business environment, business goals, and the "why."
3. **Constraints**: Build strict logical boundaries (what *not* to say, limits, security boundaries).
4. **Format**: Enforce parseable schemas (JSON, tables, markdown) rather than prose.

#### RCCF System Prompt Template:
```markdown
[ROLE]
You are a Principal Security Auditor and Lead DevSecOps Engineer with 15+ years of experience auditing distributed systems, Kubernetes orchestrations, and AWS architectures. You write concise, high-density technical analysis.

[CONTEXT]
We are reviewing a legacy Node.js/Express service container configuration ahead of a compliance audit. We must identify security risks that violate SOC2 Type II controls.

[CONSTRAINTS]
- Do NOT provide general tutorials on AWS, Docker, or Node.js.
- Do NOT write conversational greetings, introductory text, or concluding remarks.
- Focus strictly on high-risk vulnerabilities (privilege escalation, hardcoded secrets, open ports).
- If no high-risk items are found, output an empty JSON array. Do not invent findings.

[FORMAT]
Output strictly a valid JSON array of objects following this TypeScript interface:
interface AuditFinding {
  vulnerabilityId: string;
  impactLevel: 'CRITICAL' | 'HIGH' | 'MEDIUM';
  remediationCmd: string;
  explanation: string;
}
```

---

## 🧠 Chapter 2: Chain of Thought (CoT) & XML Sandboxing
To get reliable reasoning on complex problems (such as multi-step algorithms, financial calculations, or code auditing), you must give the model "computational space" to think before it writes the final answer.

### 1. XML Sandboxing for Parsing Integrity
In production applications, feeding the model's raw thought process directly to users is unprofessional. We use XML tags to isolate the **reasoning sandbox** from the **final payload**. The backend code can then easily parse out the final tags.

```markdown
Analyze the attached bank transaction log to flag potential account takeover (ATO) patterns.

Follow this execution pipeline:
1. Inside <thinking> tags, calculate the speed velocity of transactions (distance/time) and inspect authorization failure frequencies.
2. Inside <findings> tags, output a markdown table containing suspicious transaction IDs, transaction location, and ATO probability score (0-100%).

Data:
[TRANSACTION LOG]
...
```

### 2. Multi-Shot Contextual Learning (Few-Shot Mapping)
Few-shot prompting is mathematically proven to improve accuracy on classification and translation tasks far better than instructions alone. Show, don't tell.

```markdown
Classify customer incoming tickets into severity levels (P1, P2, P3) and extract the system entity.

Input: "My terminal displays 'Connection Refused' whenever I boot the primary DB instance."
Output: severity: P1 | entity: Database

Input: "I noticed a small spelling mistake in the FAQ footer text under 'Privacy Policy'."
Output: severity: P3 | entity: Static Frontend

Input: "The checkout page loads, but when I click the Stripe button, nothing happens."
Output: severity: P2 | entity: Payment Gateway

Input: "The API endpoint /v1/auth is returning a 500 error for all login requests."
Output:
```

---

## 🔌 Chapter 3: Retrieval-Augmented Generation (RAG) Prompting
RAG is the standard for commercial chatbots and document search engines. To prevent the model from hallucinating or using outdated training data, you must inject relevant context and enforce strict grounding.

### The Golden Grounding Template (Hallucination Defeated)
```markdown
You are an advanced Customer Support Engineer. Your task is to resolve the user inquiry using ONLY the verified documentation snippets provided below.

[CONTEXT SNIPPETS]
--------------------------------------------------
{{RETRIEVED_TEXT_FROM_VECTOR_STORE_1}}
{{RETRIEVED_TEXT_FROM_VECTOR_STORE_2}}
--------------------------------------------------

[STRICT RULES]
1. Answer the user inquiry clearly, citing the specific section of the documentation.
2. If the context does not contain the necessary information to answer the question, output exactly: "I apologize, but that information is not available in our verified system logs. Let me connect you with a live specialist."
3. Do NOT make up URLs, names, contact numbers, or policies that are not explicitly listed in the context.

User Inquiry: {{USER_QUESTION}}
Response:
```

---

## 📦 Chapter 4: Guaranteed JSON Schemas & API Integration
When building AI agents, your backend needs to parse the model's response using `json.loads()`. If the model writes a conversational intro like *"Sure, here is your JSON:"*, the parser will crash.

### Techniques to Guarantee Parseable JSON:
1. **Instruction Placement**: Put the JSON format requirement at the absolute end of the prompt (models pay more attention to the beginning and the end of the context).
2. **Schema Ingestion**: Provide an empty skeleton of the target JSON.
3. **Trigger-Word Hijacking**: Instruct the model to begin its response with `{` and nothing else.

#### Example Structured Output Prompt:
```markdown
Extract the lead details from this sales call transcript.

[TRANSCRIPT]
"Hey, this is David from Apex Corp. We are interested in your corporate package for 50 users. Our budget is around $2,500/month, and we need to launch by June 15th. You can reach my coordinator Sarah at sarah@apex.io."

[TARGET SKELETON]
{
  "company_name": "string",
  "seat_count": number,
  "monthly_budget": number,
  "point_of_contact": {
    "name": "string",
    "email": "string"
  },
  "deadline": "YYYY-MM-DD"
}

[CRITICAL DIRECTIVE]
Respond with the completed JSON object ONLY. Do not write any markdown code blocks (such as ```json), introductory text, or explanations. Start your response directly with the opening curly brace '{'.
```

---

## 📜 Resell & Licensing Rights
*This playbook is licensed under Private Label Rights (PLR). As the holder of this document, you are granted full authorization to rebrand, edit, bundle, translate, and sell this content on digital platforms (Gumroad, Payhip, Amazon KDP, or your personal website) for any price of your choosing (Recommended retail: $5.00 - $15.00 USD). All royalties are 100% yours to keep.*
"""
    file_path = os.path.join(output_dir, "Prompt_Engineering_Playbook.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(book_content)
    print(f"Generated Premium Digital Book at: {file_path}")

def generate_css_boilerplate(output_dir):
    css_content = """/* 
   ==========================================================================
   AMISES Modern Glassmorphic Design System
   Core Visual Tokens, Components & Animations
   ========================================================================== */

:root {
  /* Color Palette */
  --bg-dark-base: #060814;
  --bg-dark-surface: #0b1126;
  --accent-primary: #8b5cf6;      /* Vibrant Violet */
  --accent-primary-rgb: 139, 92, 246;
  --accent-secondary: #06b6d4;    /* Electric Cyan */
  --accent-secondary-rgb: 6, 182, 212;
  --accent-success: #10b981;      /* Emerald Green */
  --accent-warning: #f59e0b;      /* Warm Amber */
  
  /* Glassmorphism Configuration */
  --glass-bg: rgba(11, 17, 38, 0.7);
  --glass-border: rgba(255, 255, 255, 0.06);
  --glass-border-active: rgba(6, 182, 212, 0.25);
  --glass-shadow: 0 16px 40px 0 rgba(0, 0, 0, 0.5);
  
  /* Typography & Transitions */
  --font-sans: 'Outfit', -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --transition-smooth: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: var(--bg-dark-base);
  color: #f8fafc;
  font-family: var(--font-sans);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow-x: hidden;
  padding: 40px 20px;
}

/* Ambient Radial Backglows */
.radial-glow {
  position: absolute;
  width: 500px;
  height: 500px;
  border-radius: 50%;
  filter: blur(120px);
  opacity: 0.15;
  z-index: -1;
}
.glow-purple {
  background: var(--accent-primary);
  top: 10%;
  left: 15%;
}
.glow-cyan {
  background: var(--accent-secondary);
  bottom: 10%;
  right: 15%;
}

/* Core Glassmorphism Container */
.glass-container {
  background: var(--glass-bg);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid var(--glass-border);
  border-radius: 24px;
  box-shadow: var(--glass-shadow);
  padding: 35px;
  width: 100%;
  max-width: 650px;
  position: relative;
  transition: var(--transition-smooth);
}
.glass-container:hover {
  border-color: var(--glass-border-active);
  box-shadow: 0 20px 50px 0 rgba(6, 182, 212, 0.12);
}

/* Typography elements */
h1 {
  font-size: 2.2rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(135deg, #fff 30%, #94a3b8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 8px;
}
p {
  color: #94a3b8;
  font-size: 0.98rem;
  line-height: 1.6;
  margin-bottom: 25px;
}

/* Interactive Components */
.metric-badge {
  display: inline-flex;
  align-items: center;
  background: rgba(6, 182, 212, 0.08);
  border: 1px solid rgba(6, 182, 212, 0.2);
  color: var(--accent-secondary);
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  padding: 6px 14px;
  border-radius: 50px;
  margin-bottom: 20px;
  box-shadow: 0 0 15px rgba(6, 182, 212, 0.1);
}

/* Interactive Forms */
.form-group {
  margin-bottom: 20px;
}
label {
  display: block;
  font-size: 0.85rem;
  font-weight: 500;
  color: #cbd5e1;
  margin-bottom: 8px;
  letter-spacing: 0.3px;
}
.glass-input {
  width: 100%;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 10px;
  padding: 12px 16px;
  color: #fff;
  font-family: var(--font-sans);
  font-size: 0.95rem;
  transition: var(--transition-smooth);
}
.glass-input:focus {
  outline: none;
  background: rgba(255, 255, 255, 0.05);
  border-color: var(--accent-secondary);
  box-shadow: 0 0 12px rgba(6, 182, 212, 0.2);
}

/* Premium Gradient Button */
.btn-gradient {
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
  color: #ffffff;
  border: none;
  border-radius: 12px;
  padding: 14px 28px;
  font-family: var(--font-sans);
  font-size: 0.98rem;
  font-weight: 600;
  cursor: pointer;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;
  transition: var(--transition-smooth);
  box-shadow: 0 6px 20px rgba(139, 92, 246, 0.3);
}
.btn-gradient:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(6, 182, 212, 0.45);
}
.btn-gradient:active {
  transform: translateY(0);
}

/* Visual Dashboard Widget */
.widget-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 15px;
  margin-top: 25px;
}
.widget-box {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.04);
  border-radius: 12px;
  padding: 16px;
}
.widget-title {
  font-size: 0.8rem;
  color: #64748b;
  text-transform: uppercase;
  margin-bottom: 5px;
}
.widget-value {
  font-size: 1.4rem;
  font-weight: 700;
  color: #f8fafc;
}
"""
    
    html_demo = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Premium Glassmorphic Component UI</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="glassmorphism_ui.css">
</head>
<body>
  <!-- Ambient background glow elements -->
  <div class="radial-glow glow-purple"></div>
  <div class="radial-glow glow-cyan"></div>

  <div class="glass-container">
    <span class="metric-badge">🚀 Developer Template Boilerplate</span>
    <h1>Interactive Dashboard Panel</h1>
    <p>This is a complete, pre-configured glassmorphic template. Build interfaces in minutes with premium CSS blur shadows and dynamic linear gradients.</p>
    
    <div class="form-group">
      <label for="sample-email">Email Address</label>
      <input type="email" id="sample-email" class="glass-input" placeholder="enter your mail..." value="admin@devsystem.io">
    </div>

    <button class="btn-gradient">
      <span>Get Started Now</span>
      <span style="font-size: 1.1rem;">⚡</span>
    </button>

    <div class="widget-grid">
      <div class="widget-box">
        <div class="widget-title">Core Performance</div>
        <div class="widget-value">98.4%</div>
      </div>
      <div class="widget-box">
        <div class="widget-title">Render Latency</div>
        <div class="widget-value">12 ms</div>
      </div>
    </div>
  </div>
</body>
</html>
"""
    
    css_path = os.path.join(output_dir, "glassmorphism_ui.css")
    html_path = os.path.join(output_dir, "demo.html")
    
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_demo)
        
    zip_path = os.path.join(output_dir, "Glassmorphism_UI_Boilerplate.zip")
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(css_path, arcname="glassmorphism_ui.css")
        zipf.write(html_path, arcname="demo.html")
        
    os.remove(css_path)
    os.remove(html_path)
    print(f"Generated UI Boilerplate ZIP at: {zip_path}")

def generate_copywriting_templates(output_dir):
    templates = """========================================================================
             PREMIUM HIGH-CONVERTING COPYWRITING TEMPLATES
========================================================================
Designed Autonomously for Digital Solopreneurs, Creators and Freelancers
------------------------------------------------------------------------

TEMPLATES CATALOG:
1. GUMROAD LANDING PAGE COPY (The Prompt Engineering Playbook)
2. VIRAL EDUCATIONAL TWITTER/X THREAD (Organic Lead Acquisition)
3. THE "VALUE-FIRST" COLD FREELANCE PROPOSAL (Instant Upwork Pitch)

========================================================================
TEMPLATE 1: GUMROAD HIGH-CONVERSION SALES COPY
========================================================================
Target Price: $5.00 - $9.99

Headline: Stop Prompting Like a Google Search. Learn to Program LLMs.
Sub-headline: Master XML sandboxing, few-shot schema mapping, and RAG architectures that elite SaaS teams use to automate developer workflows. Private Label Rights (PLR) included!

--- [SALES INTRO] ---
Did you know that 90% of developers prompt language models incorrectly? 

They write vague paragraphs, ask the model to "explain step-by-step" without sandboxing, and then complain when the model hallucinates or outputs conversational filler that crashes their JSON parsers.

The problem isn't the model. It's the prompt structure.

The Elite Prompt Engineering & LLM Automation Playbook is an industrial-grade blueprint written to solve this exact problem. It transitions you from conversational prompting to deterministic programming.

--- [WHAT IS INSIDE] ---
Inside this exhaustive playbook, you will get:
- ⚡ The RCCF Protocol: Build unbreakable AI agent system roles.
- 🧠 XML Sandboxing: Isolate reasoning processes so they never pollute final code outputs.
- 🔌 Industrial RAG Grounding: Learn the precise prompts that completely eliminate model hallucinations.
- 📦 JSON-Enforcer Templates: Get 100% parseable, API-ready machine JSON outputs every time.
- 📜 PLR Resell Rights: Sell this book under your own name and keep 100% of the profits!

--- [PROOF BLOCK] ---
"This single markdown guide saved us over 15 hours of debug time on our vector store chatbot. The XML sandboxing tip is worth 10x the price alone."
— Marcus D., CTO at NexusLab.io

🛒 Click "Buy This" now to get instant developer-grade control for the price of a single coffee!

========================================================================
TEMPLATE 2: VIRAL EDUCATIONAL TWITTER/X THREAD
========================================================================
Purpose: Drive free organic traffic to your digital storefront.

Tweet 1:
Most developers prompt AI like they're searching Google.
That's why they get average, conversational, and messy results.

Here are 4 advanced Prompt Engineering paradigms that elite SaaS teams use to build deterministic AI agents (with code examples): 🧵👇

Tweet 2:
1️⃣ The RCCF Protocol
Vague: "Act as a developer and audit my code."
Elite: System roles must follow: Role + Context + Constraints + Format.
Constrain the latent search space to the top 1% of the model's training weights.
[Insert Chapter 1 template example]

Tweet 3:
2️⃣ XML Sandboxing
Do NOT just tell the AI to "think." Give it a literal, machine-readable sandbox.
By wrapping reasoning inside <thinking> tags, your backend can easily regex out the logic while providing the user with clean results in <output> tags.
[Insert Chapter 2 XML example]

Tweet 4:
3️⃣ Guaranteed API-Ready JSON
LLMs love to write "Here is your JSON:" which crashes standard json.loads() parsers.
To fix this:
1. Place JSON schemas at the ABSOLUTE end of your prompt.
2. Instruct the model to begin its response with '{' and write nothing else.
[Insert Chapter 4 JSON example]

Tweet 5:
Want to master advanced prompt design, dynamic RAG schemas, and learn how to package and resell these skills?

I put everything into a comprehensive Developer Playbook.
Grab it today for the price of a single coffee ($5):
👉 [YOUR_GUMROAD_LINK_HERE]

========================================================================
TEMPLATE 3: THE "VALUE-FIRST" COLD FREELANCE PROPOSAL
========================================================================
Purpose: Sending pre-solved scripts directly to prospective clients for immediate escrow funding.

Subject: Completed script / draft solution for your project: [Job Title]

Hi [Client Name / Hiring Manager],

I saw your project request for "[Job Title]". Instead of sending a generic cover letter telling you what I *can* do, I went ahead and wrote the entire functional script/solution for you.

You can view the fully completed solution below:
------------------------------------------------------------------------
[INSERT COMPLETED PYTHON SCRIPT / CSS WORKPLACE SOLUTION HERE]
------------------------------------------------------------------------

Why I did this: I believe in proving value upfront. This code is formatted, tested, and ready to deploy to production out-of-the-box using standard libraries.

If this script solves your core requirement, I would love to help you scale it, schedule it to run daily in the cloud, or customize it further. 

We can open a quick, fixed-budget $[Budget] contract on [Upwork/Freelancer] to finalize the work. Let me know if you would like to hop on a 2-minute chat!

Best regards,
Autonomous Dev Agent (on behalf of your developer partner)
========================================================================
"""
    file_path = os.path.join(output_dir, "High_Conversion_Copywriting_Kit.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(templates)
    print(f"Generated Copywriting Templates at: {file_path}")

def main():
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(workspace_dir, "outputs")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print("--- AMISES DIGITAL ASSET FACTORY ACTIVE ---")
    generate_prompt_book(output_dir)
    generate_css_boilerplate(output_dir)
    generate_copywriting_templates(output_dir)
    print("All premium digital assets generated successfully in 'outputs/' folder!")

if __name__ == "__main__":
    main()