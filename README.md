<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:0D1526,50:00FF41,100:39FF14&amp;height=210&amp;section=header&amp;text=Wealth-Wise&amp;fontSize=80&amp;fontColor=ffffff&amp;animation=fadeIn&amp;fontAlignY=35&amp;desc=Smart%20Personal%20Finance%20%C2%B7%20Expense%20Intelligence&amp;descAlignY=56&amp;descSize=18" width="100%" alt="Wealth-Wise banner" />

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3200&pause=900&color=00FF41&center=true&vCenter=true&multiline=true&repeat=true&width=760&height=120&lines=Income+%26+Expense+Tracking+%C2%B7+Financial+Goal+Engine;Bill+Management+%C2%B7+Multi-Currency+%C2%B7+Plotly+Insights;Dark+Mode+%C2%B7+Fully+Automated+%C2%B7+Cyberpunk+UI)](https://github.com/)

<br/>

<a href="https://figma.com/">
  <img src="https://img.shields.io/badge/%F0%9F%96%8A%EF%B8%8F_MOCKUP-FIGMA-00FF41?style=for-the-badge&labelColor=0a0f0d" alt="Mockup"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Backend-Django_5.1-00FF41?style=for-the-badge&logo=django&logoColor=white&labelColor=0a0f0d" alt="Django"/>
<img src="https://img.shields.io/badge/DB-MySQL_8.0-39FF14?style=for-the-badge&logo=mysql&logoColor=white&labelColor=0a0f0d" alt="DB"/>
<img src="https://img.shields.io/badge/Frontend-JS_+_HTML_+_CSS-00FF41?style=for-the-badge&logo=javascript&logoColor=black&labelColor=0a0f0d" alt="Frontend"/>
<img src="https://img.shields.io/badge/Charts-Plotly_6.0-39FF14?style=for-the-badge&logo=plotly&logoColor=white&labelColor=0a0f0d" alt="Charts"/>
<img src="https://img.shields.io/badge/Styling-Tailwind_CSS-00FF41?style=for-the-badge&logo=tailwindcss&logoColor=white&labelColor=0a0f0d" alt="Tailwind"/>

<br/><br/>

```text
💰 TRACK INCOME  →  📊 MANAGE EXPENSES  →  🎯 SET GOALS  →  📈 GROW WEALTH
```

</div>

---

> **Wealth-Wise** · Comprehensive Personal Finance & Expense Intelligence Platform  
> **Platform Status:** Operational  
> **Architecture:** Full Stack Django Monolith + MySQL  

Wealth-Wise empowers users to take full control of their financial lifecycle — from tracking income and expenses with multi-currency support, managing recurring bills with automated email reminders, setting and monitoring financial goals, to generating rich interactive reports powered by Plotly — all wrapped in a sleek cyberpunk dark-mode UI.

<div align="center">

| 💰 Income & Expenses | 🎯 Goal Engine | 📋 Bill Tracker | 📊 Financial Reports |
|:---:|:---:|:---:|:---:|
| Categorized tracking | Savings-linked targets | Due date management | Plotly bar/line/pie |
| Monthly breakdown | Progress percentage | Mark as paid | Monthly trend analysis |
| Multi-currency | Email notifications | Auto-reminders (CI/CD) | Expense categorization |

</div>

---

## Table of Contents

<details open>
<summary><b>Navigate</b></summary>

| # | Section | # | Section |
|---:|---|---:|---|
| 1 | [Overview](#1-overview) | 6 | [Architecture & Workflows](#6-architecture--workflows) |
| 2 | [Problem Statement](#2-problem-statement) | 7 | [Repository Structure](#7-repository-structure) |
| 3 | [Links & Credentials](#3-links--credentials) | 8 | [Authentication](#8-authentication) |
| 4 | [Features & Deliverables](#4-features--deliverables) | 9 | [Setup (Local)](#9-setup-local) |
| 5 | [Technology Stack](#5-technology-stack) | 10 | [Screenshots](#10-screenshots) |

</details>

---

## 1. Overview

**Wealth-Wise** is a full-stack, cyberpunk-themed personal finance management application designed to map the entire financial lifecycle of a user — from daily transactions to long-term wealth goals.

| Capability | What it does |
|---|---|
| Income & Expense Dashboard | Monthly transaction tracking with categorized emoji-tagged entries and savings calculations. |
| Multi-Currency Support | Users select their preferred currency at signup — all financial data is scoped accordingly. |
| Financial Goal Tracker | Set financial targets, link them to savings progress, receive email notifications on milestones. |
| Bill Management System | Add, track, and mark bills as paid with automatic email reminders via GitHub Actions CI/CD. |
| Interactive Financial Reports | Yearly reports with Plotly-powered bar charts, line graphs, and pie charts for expense breakdowns. |
| Asset Fit Engine | Rule-based engine evaluating Gold/REIT investment suitability based on financial stability scores. |
| Explainability Module | Human-readable explanations for financial decisions with risk assessments and recommendations. |

Stack shape: **JavaScript + HTML + CSS + Tailwind** frontend · **Django 5.1** backend · **MySQL 8.0** database · **Plotly 6.0** charts · Session Authentication · Dark Mode UI.

---

## 2. Problem Statement

### Smart Personal Finance Management for the Everyday User

**Problem Abstract**
Millions of individuals struggle with financial visibility — lacking clear insights into their income, expenses, savings patterns, and progress toward financial goals. Information is scattered across bank statements, manual spreadsheets, and mental notes. Most existing tools are either too complex or too simplistic.

Wealth-Wise addresses this by providing:
1. A centralized dashboard for income and expense tracking across 30+ predefined categories with emoji-tagged identification.
2. A goal engine that links financial targets to actual savings, providing real-time progress tracking with motivational email nudges.
3. A bill management system with automated daily reminders (GitHub Actions cron) to prevent missed payments.
4. Rich financial reports with interactive Plotly visualizations showing monthly trends, category breakdowns, and income vs. expense comparisons.
5. An asset fit engine with explainability layer for investment readiness assessment (Gold/REITs).

**Expected Outcomes**
- `→` Categorized income & expense tracking with monthly breakdowns across all 12 months
- `→` Savings rate calculation and progress visualization
- `→` Financial goal setting with milestone notifications via email
- `→` Bill tracking with paid/unpaid status and automated reminders
- `→` Interactive Plotly reports: bar charts, line graphs, and pie charts
- `→` Multi-currency support (50+ currencies seeded via management command)
- `→` Asset fitness evaluation with human-readable explainability

**Evaluation Criteria Mapping**
| Criteria | Implementation in Wealth-Wise |
|:---|:---|
| **Understanding of Problem** | Directly targets everyday users who lack financial visibility, providing a centralized cyberpunk-themed dashboard for complete financial lifecycle management. |
| **Proposed Approach** | Django 5.1 + MySQL monolith with Plotly-powered interactive reports, session-based auth, automated CI/CD bill reminders, and a rule-based asset fit engine. |
| **Market Fit & Relevance** | Addresses the gap between overly complex finance apps and basic spreadsheets, with a visually striking dark-mode UI, multi-currency support, and gamified goal tracking. |

---

## 3. Links & Credentials

| Resource | Link / note |
|---|---|
| Full stack + database | Local — Django `:8000` + MySQL |
| Local API | `http://127.0.0.1:8000` |
| Admin Panel | `http://127.0.0.1:8000/admin` |
| Email Service | `wealthwise200@gmail.com` (SMTP via Gmail) |

### Demo Access (Local)
Seed the database with currencies using `python manage.py currencies`, then sign up through the registration form.

| Page | URL Route | Description |
|---|---|---|
| Landing Page | `/` | Home / marketing page |
| Signup & Login | `/WW/signup/` | Dual-form auth (login + signup) |
| Dashboard | `/WW/i1.html/` | Income & expense management |
| Goals | `/WW/G.html/` | Financial goal tracker |
| Bills | `/WW/b1.html/` | Bill management |
| Reports | `/WW/report.html/` | Plotly-powered financial reports |

---

## 4. Features & Deliverables

### Core Features

| # | Feature | Status |
|---:|---|:---:|
| 01 | Email/Password Signup & Login (Session Auth) | ✅ |
| 02 | OTP-based Password Recovery (Email) | ✅ |
| 03 | Multi-Currency Selection (50+ currencies) | ✅ |
| 04 | Income Tracking (6 categories with emoji tags) | ✅ |
| 05 | Expense Tracking (30 categories with emoji tags) | ✅ |
| 06 | Monthly Financial Dashboard (savings, percentages) | ✅ |
| 07 | Financial Goal Engine (progress tracking) | ✅ |
| 08 | Bill Management System (add, pay, delete) | ✅ |
| 09 | Interactive Reports (Plotly bar/line/pie) | ✅ |
| 10 | Asset Fit Engine (Gold/REIT evaluation) | ✅ |
| 11 | Explainability Module (human-readable decisions) | ✅ |

### Bonus Features

| # | Feature | Status |
|---:|---|:---:|
| B1 | Cyberpunk Dark Mode UI (Green Neon theme) | ✅ |
| B2 | Automated Bill Reminders (GitHub Actions Cron) | ✅ |
| B3 | Welcome & Goal Achievement Email Notifications | ✅ |
| B4 | Motivational Progress Emails | ✅ |
| B5 | Currency Seeder Management Command | ✅ |
| B6 | FAQ, Privacy Policy, Terms, Security, Support Pages | ✅ |

---

## 5. Technology Stack

<div align="center">
<img src="https://skillicons.dev/icons?i=py,django,mysql,js,html,css,tailwind,github&theme=dark" alt="Stack icons"/>
</div>

<br/>

<div align="center">

<img src="https://img.shields.io/badge/Python-3.11-00FF41?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0f0d" alt="Python"/>
<img src="https://img.shields.io/badge/Django-5.1.4-39FF14?style=for-the-badge&logo=django&logoColor=white&labelColor=0a0f0d" alt="Django"/>
<img src="https://img.shields.io/badge/MySQL-8.0-00FF41?style=for-the-badge&logo=mysql&logoColor=white&labelColor=0a0f0d" alt="MySQL"/>
<img src="https://img.shields.io/badge/Plotly-6.0-39FF14?style=for-the-badge&logo=plotly&logoColor=white&labelColor=0a0f0d" alt="Plotly"/>
<img src="https://img.shields.io/badge/JavaScript-ES6-00FF41?style=for-the-badge&logo=javascript&logoColor=black&labelColor=0a0f0d" alt="JS"/>
<img src="https://img.shields.io/badge/Tailwind-CSS-39FF14?style=for-the-badge&logo=tailwindcss&logoColor=white&labelColor=0a0f0d" alt="Tailwind"/>

</div>

<br/>

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Django 5.1.4 (Python 3.11) | REST views, session auth, business logic |
| **Database** | MySQL 8.0 (utf8mb4) | Persistent storage for users, transactions, goals, bills |
| **Frontend** | JavaScript ES6 + HTML5 + CSS3 | Dynamic UI interactions and DOM manipulation |
| **Styling** | Tailwind CSS + Custom CSS | Cyberpunk dark theme with green neon accents |
| **Charts** | Plotly 6.0 | Interactive bar, line, and pie chart visualizations |
| **PDF** | xhtml2pdf + ReportLab | Financial report PDF generation |
| **Email** | Django SMTP (Gmail) | Transactional emails for signup, OTP, goals, reminders |
| **CI/CD** | GitHub Actions | Daily automated bill reminder cron job |
| **QR** | qrcode library | QR code generation |

---

## 6. Architecture & Workflows

### 6.1 Overall System Architecture
```mermaid
graph TD
    subgraph Client
        B[Browser]
    end
    
    subgraph Django Application
        R[URL Router]
        V[Views Layer]
        F[Forms & Validation]
        M[Models / ORM]
        FA[Financial Analysis]
        AFE[Asset Fit Engine]
        XAI[Explainability Module]
    end
    
    subgraph Data Layer
        DB[(MySQL 8.0)]
    end
    
    subgraph External
        SMTP[Gmail SMTP]
        GHA[GitHub Actions Cron]
    end
    
    B -->|HTTP Request| R
    R --> V
    V --> F
    V --> M
    M --> DB
    V --> FA
    FA --> AFE
    AFE --> XAI
    V -->|Email| SMTP
    GHA -->|Daily Trigger| V
    V -->|HTML + Plotly| B
```

### 6.2 Financial Data Pipeline
```mermaid
graph LR
    subgraph User Input
        I[Income Entry]
        E[Expense Entry]
    end
    
    subgraph Processing
        MC[Monthly Calculation]
        SR[Savings Rate]
        PP[Progress Percentage]
    end
    
    subgraph Output
        D[Dashboard View]
        R[Plotly Reports]
        G[Goal Progress]
    end
    
    I --> MC
    E --> MC
    MC --> SR
    MC --> PP
    SR --> D
    PP --> G
    MC --> R
```

### 6.3 Asset Fit Decision Engine
```mermaid
flowchart LR
    subgraph Financial Metrics
        FS[Financial Stability Score]
        EMI[EMI Ratio]
        SVR[Savings Rate]
    end
    
    subgraph Credit Engine
        MCS[Mock Credit Score]
        CB[Credit Band Lookup]
    end
    
    subgraph Decision Engine
        AFE[Asset Fit Evaluator]
        XAI[Explainability Generator]
    end
    
    FS --> MCS
    SVR --> MCS
    EMI --> MCS
    MCS --> CB
    CB --> AFE
    FS --> AFE
    AFE --> XAI
    XAI --> Result((Decision + Score))
```

### 6.4 Authentication & Session Flow
```mermaid
sequenceDiagram
    participant User
    participant Django
    participant MySQL
    participant Gmail

    User->>Django: POST /signup (name, email, password, currency)
    Django->>Django: Validate form + hash password
    Django->>MySQL: Save User record
    Django->>Gmail: Send welcome email
    Django-->>User: Redirect to login

    User->>Django: POST /login (email, password)
    Django->>MySQL: Fetch user by email
    Django->>Django: check_password()
    Django->>Django: Set session['user_id']
    Django-->>User: Redirect to dashboard
```

### 6.5 Automated Bill Reminder Pipeline
```mermaid
graph TD
    CRON[GitHub Actions Cron - 9AM UTC] -->|Trigger| SETUP[Setup Python + MySQL]
    SETUP --> MIGRATE[Run Django Migrations]
    MIGRATE --> REMINDER[Execute reminder.py]
    REMINDER --> QUERY[Query Unpaid Bills]
    QUERY --> EMAIL[Send Email via Gmail SMTP]
    EMAIL --> DONE((Reminders Sent))
```

### 6.6 Goal Tracking Lifecycle
```mermaid
graph LR
    CREATE[Create Goal] --> TRACK[Track Savings]
    TRACK --> CALC[Calculate Progress %]
    CALC -->|< 100%| MOTIVATE[Send Motivation Email]
    CALC -->|>= 100%| ACHIEVE[Mark All Goals Done]
    MOTIVATE --> TRACK
    ACHIEVE --> CLEAR[Clear Completed Goals]
```

---

## 7. Repository Structure

```text
WealthWise/
├── .github/
│   └── workflows/
│       └── reminder.yml          # GitHub Actions cron for daily bill reminders
├── p/                            # Django project root
│   ├── manage.py                 # Django CLI entry point
│   ├── requirements.txt          # Python dependencies (74 packages)
│   ├── db.sqlite3                # SQLite fallback (dev)
│   ├── p/                        # Django project config
│   │   ├── settings.py           # Django settings (MySQL, SMTP, Tailwind)
│   │   ├── urls.py               # Root URL configuration
│   │   ├── views.py              # Base views
│   │   ├── wsgi.py               # WSGI entry point
│   │   └── asgi.py               # ASGI entry point
│   ├── WW/                       # Main application module
│   │   ├── models.py             # User, Income, Expense, Bill, Goal, Currency
│   │   ├── views.py              # 20+ view functions (571 LOC)
│   │   ├── forms.py              # 8 Django forms with validation
│   │   ├── urls.py               # 18 URL routes
│   │   ├── admin.py              # Admin registration
│   │   ├── financial_analysis.py # Stability score, savings rate, EMI ratio
│   │   ├── asset_fit_engine.py   # Gold/REIT investment fitness evaluator
│   │   ├── explainability.py     # Human-readable financial decision explanations
│   │   ├── management/
│   │   │   └── commands/
│   │   │       ├── currencies.py # Seed 50+ world currencies
│   │   │       └── reminder.py   # Automated bill reminder emails
│   │   └── templates/WW/        # 15 HTML templates
│   │       ├── home.html         # Landing page
│   │       ├── signup.html       # Login + signup dual form
│   │       ├── i1.html           # Income & expense dashboard
│   │       ├── G.html            # Goal tracker
│   │       ├── b1.html           # Bill management
│   │       ├── report.html       # Plotly financial reports
│   │       ├── forgot-password.html
│   │       ├── verify-otp.html
│   │       ├── FAQ.html
│   │       ├── privacy.html
│   │       ├── security.html
│   │       ├── terms.html
│   │       ├── support.html
│   │       ├── fiscalpilot_choose_asset.html
│   │       └── fiscalpilot_decision_result.html
│   ├── static/                   # Static assets
│   │   ├── home.css / home.js    # Landing page styles & scripts
│   │   ├── i1.css                # Dashboard styles
│   │   ├── G.css                 # Goal tracker styles
│   │   ├── b1.css                # Bill management styles
│   │   ├── report.css            # Report styles
│   │   ├── signup.css            # Auth page styles
│   │   ├── forgot-password.css   # Password recovery styles
│   │   ├── FAQ.css / support.css # Info page styles
│   │   ├── styles.css            # Global stylesheet
│   │   ├── logoWw.jpg            # Wealth-Wise logo
│   │   └── *.svg                 # Social media icons
│   ├── templates/website/        # Base templates
│   └── theme/                    # Tailwind CSS theme app
│       ├── static/               # Compiled Tailwind output
│       └── static_src/           # Tailwind source config
└── README.md                     # This file
```

---

## 8. Authentication

Authentication is handled securely via **Django's Session framework** for traditional email/password logins. Passwords are hashed using Django's `make_password` / `check_password` utilities with PBKDF2 by default.

| Feature | Implementation |
|---|---|
| **Signup** | Email, name, password (regex-enforced), currency selection |
| **Login** | Email + password verification against hashed store |
| **Session** | `request.session['user_id']` for stateful access control |
| **Logout** | Session flush with cache-busting headers |
| **Password Recovery** | OTP via email (1-minute expiry) → new password reset |
| **Transactional Emails** | Welcome email on signup, OTP delivery, goal notifications |

Password requirements enforced via regex:
```text
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%?&]{8,}$
```

---

## 9. Setup (Local)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/WealthWise.git
   cd WealthWise
   ```

2. **Backend Setup:**
   ```bash
   cd p
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Database Setup (MySQL):**
   ```sql
   CREATE DATABASE wealthwise CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   Update `p/settings.py` with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'wealthwise',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

4. **Run Migrations & Seed Currencies:**
   ```bash
   python manage.py migrate
   python manage.py currencies
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```
   *Navigate to `http://127.0.0.1:8000` in your browser.*

---

## 10. Screenshots

<details>
<summary><b>🚀 Landing Page</b></summary>
<br/>
<i>Cyberpunk dark theme landing page with green neon accents</i>
</details>

<details>
<summary><b>🔐 Signup & Login</b></summary>
<br/>
<i>Dual-form authentication page with password strength validation</i>
</details>

<details>
<summary><b>📊 Income & Expense Dashboard</b></summary>
<br/>
<i>Monthly transaction tracker with savings percentage and category breakdowns</i>
</details>

<details>
<summary><b>🎯 Financial Goal Tracker</b></summary>
<br/>
<i>Goal setting with progress bars linked to actual savings</i>
</details>

<details>
<summary><b>📋 Bill Management</b></summary>
<br/>
<i>Bill tracker with paid/unpaid status and automated daily reminders</i>
</details>

<details>
<summary><b>📈 Financial Reports</b></summary>
<br/>
<i>Interactive Plotly charts — bar, line, and pie visualizations</i>
</details>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:0D1526,50:00FF41,100:39FF14&amp;height=120&amp;section=footer" width="100%" alt="Footer" />

<br/>

<i>Built with 💚 by the Wealth-Wise Team</i>

<br/><br/>

<img src="https://img.shields.io/badge/LICENSE-MIT-00FF41?style=flat-square&labelColor=0a0f0d" alt="License"/>
<img src="https://img.shields.io/badge/STATUS-ACTIVE-39FF14?style=flat-square&labelColor=0a0f0d" alt="Status"/>
<img src="https://img.shields.io/badge/PRs-WELCOME-00FF41?style=flat-square&labelColor=0a0f0d" alt="PRs"/>

</div>
