# 🍲 FOOD BRIDGE
### Smart Food Waste Management and Hunger Redistribution Platform
> *Closing the urban food waste and hunger paradox through predictive AI, temperature-controlled logistics, and hyperlocal redistribution.*

---

## 🌟 Executive Summary & Venture Vision

In modern metropolitan areas, luxury hotels, corporate dining halls, banquet caterers, and supermarkets routinely discard **30% to 40%** of prepared food due to forecasting uncertainty. Concurrently, millions of low-income families, daily-wage laborers, and shelter residents face daily food insecurity. Cooked food has a perishable safety margin of **3 to 6 hours**, making traditional charity logistics too slow and uncoordinated.

**FOOD BRIDGE** is an enterprise-grade technology platform that connects commercial food donors with verified local NGOs and volunteer logistics networks in real-time. By combining **geospatial proximity routing (Haversine)**, **Scikit-learn predictive surplus forecasting**, and **stringent food safety compliance**, Food Bridge redistributes safe surplus meals in under **90 minutes**, converting organic waste into verified social nutrition and quantifiable carbon offsets.

---

## 🏗️ System Architecture

```mermaid
graph TD
    subgraph Donors["Commercial Donors (Hotels, Restaurants, Supermarkets)"]
        D1[Post Surplus Batch] --> D2[Declare Prep Time & Expiry]
        D2 --> D3[Specify Storage Condition & Allergens]
    end

    subgraph Core["Food Bridge Platform Core (Python Flask + SQLAlchemy)"]
        D3 --> AI_Engine[AI Redistribution Intelligence Engine]
        AI_Engine --> Scoring[Multi-Attribute Scoring: Distance 35%, Feasibility 30%, Capacity 25%, Trust 10%]
        Scoring --> Notification_Svc[In-App Notification Dispatcher]
        DB[(Database: MySQL / SQLite Dual Engine)]
    end

    subgraph NGOs["Verified NGOs & Community Kitchens"]
        Notification_Svc --> N1[Receive Real-Time Food Alert]
        N1 --> N2[Request Servings]
        N2 --> N3[Food Safety & Quarantine Inspection]
    end

    subgraph Volunteers["Volunteer Logistics Fleet"]
        N2 --> V1[Claim Pickup Mission]
        V1 --> V2[Temperature Check & Packaging Verification]
        V2 --> V3[Leaflet Route Transit]
        V3 --> V4[OTP Handover & Delivery]
    end

    subgraph Admin["Central Admin & Safety Moderation"]
        A1[FSSAI & NGO Verification]
        A2[Food Safety Incident Audits]
        A3[Carbon Offset & ESG Metrics]
    end
```

---

## 💻 Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3, Bootstrap Icons |
| **Mapping & GIS** | Leaflet 1.9.4, OpenStreetMap API |
| **Visualizations** | Chart.js 4.4 (Surplus Forecasts, Category Doughnuts, Zone Indices) |
| **Backend** | Python 3.15, Flask 3.1, Flask-SQLAlchemy 3.1, Flask-Login 0.6 |
| **Database** | MySQL 8.0+ (Production Schema: `database/schema.sql`), SQLite3 (Zero-setup development fallback) |
| **AI / Machine Learning** | Scikit-learn (RandomForestRegressor for surplus volume prediction), NumPy, Pandas |
| **Security** | Werkzeug PBKDF2 Password Hashing, Session Security, Role-Based Access Control (RBAC) |
| **Testing** | Python `unittest`, automated model, lifecycle, and route test suite |

---

## 👥 Five Role-Based Dashboards & Capabilities

### 1. 🏨 Food Donors (Hotels, Restaurants, Supermarkets, Caterers)
- **Submit Food Donations:** Form collecting food name, category, quantity (kg), serves count, preparation time, safe consumption deadline, storage condition (Hot Holding >60°C, Chilled <4°C, Room Temp, Frozen), allergens, and pickup location.
- **AI Priority Score:** Computes real-time redistribution urgency (0 to 100).
- **Request Management:** Review incoming NGO requests; approve with automatic volunteer logistics dispatch or reject with operational reasons.
- **ESG Dashboard:** Track food saved (kg), meals served, and tax-deductible carbon offset savings ($1\text{ kg rescued} = 2.5\text{ kg CO}_2\text{e saved}$).

### 2. 🏢 Verified NGOs (Food Banks, Shelters, Community Kitchens)
- **Hyperlocal Surplus Feed:** Filter donations by distance radius, category, and safe consumption window.
- **AI-Matched Recommendations:** Tailored recommendations matching NGO daily capacity.
- **Request Submission:** Submit requests with recipient headcount and distribution readiness certification.
- **Food Safety Governance:** File rapid incident reports (temperature breach, spoilage, broken packaging) with automated batch quarantine.

### 3. 🛵 Logistics Volunteers
- **Mission Console:** Live pickup and delivery routing with donor and recipient contact details.
- **Delivery Lifecycle Stepper:** Update statuses: `Assigned` $\rightarrow$ `En Route` $\rightarrow$ `Picked Up` (with probe thermometer log) $\rightarrow$ `Delivered` (with OTP confirmation).
- **Availability Toggle:** Switch status between Online (available for missions) and Offline.

### 4. 🛡️ Platform Administrators
- **NGO Verification Queue:** Review NGO trust registration and Darpan IDs before approving donation privileges.
- **Food Safety Moderation:** Review quarantined batches, audit donor kitchens, and enforce account suspensions.
- **User Management:** Activate or deactivate accounts across all roles.
- **Platform Analytics:** Macro audit log of all system donations and zone supply-demand balance.

### 5. 🤝 Community Beneficiaries
- **Assistance Portal:** Submit assistance requests (Daily Hot Meals, Weekly Dry Ration Kits, Emergency Relief Food).
- **Nearby Food Banks:** Real-time directory of verified community food centers and serving schedules.

---

## 🔑 Demo Login Credentials

The database includes realistic demonstration data for all 5 roles. You can also use the **One-Click Demo Login** buttons on the Login page:

| Role | Email Address | Password | Organization / Name |
| :--- | :--- | :--- | :--- |
| **Platform Admin** | `admin@foodbridge.org` | `admin123` | Platform Operations Lead |
| **Food Donor** | `donor@royalorchid.com` | `donor123` | The Royal Orchid Grand Hotel |
| **Verified NGO** | `ngo@akshayacare.org` | `ngo123` | Akshaya Care Food Bank |
| **Logistics Volunteer** | `volunteer@foodbridge.org` | `volunteer123` | Rahul Kumar (Motorbike Fleet) |
| **Beneficiary** | `beneficiary@community.org` | `bene123` | Community Assistance Portal |

*Alternative demo accounts:*
- Secondary Donor (Bistro): `donor@greenbite.com` / `donor123`
- Secondary NGO (Shelter): `ngo@karuna.org` / `ngo123`
- Refrigerated Van Volunteer: `volunteer.david@foodbridge.org` / `volunteer123`

---

## 🧠 AI / ML Redistribution Intelligence Engine

### 1. Multi-Attribute Smart NGO Matching (`app/ai/matching.py`)
Computes an explainable composite match score ($0 - 100$) between a surplus batch and candidate NGOs:
$$\text{Score} = (W_{\text{dist}} \times S_{\text{dist}}) + (W_{\text{feas}} \times S_{\text{feas}}) + (W_{\text{cap}} \times S_{\text{cap}}) + (W_{\text{trust}} \times S_{\text{trust}})$$
- **Geographic Proximity (35%):** Haversine distance decay with a default 35 km radius.
- **Freshness Feasibility (30%):** Estimated travel time vs remaining safe consumption deadline.
- **Capacity Absorption (25%):** Ratio between batch servings and NGO daily meal throughput.
- **Trust & Verification (10%):** FSSAI license compliance and NGO verification history.

### 2. Machine Learning Surplus Forecasting (`app/ai/forecasting.py`)
- Powered by a **Scikit-learn Random Forest Regressor**.
- Trained on historical day-of-week, hour-of-day, business type, and category surplus distributions.
- Produces a **7-day predictive surplus forecast (kg and meals)** to help NGOs staff volunteer shifts ahead of weekend surplus surges.

### 3. Sustainability & Environmental Analytics (`app/ai/analytics.py`)
- **Carbon Dioxide Equivalent:** $1\text{ kg food waste prevented} = 2.5\text{ kg CO}_2\text{e averted}$.
- **Freshwater Conservation:** $1\text{ kg food} \approx 250\text{ liters embedded agricultural water}$.
- **Economic Value:** $1\text{ meal} \approx ₹120\text{ (\$1.45) nutritional preservation value}$.

---

## 🚀 Setup & Local Execution Guide

### 1. Prerequisites
- Python 3.10+ (Python 3.15 supported)
- MySQL 8.0+ *(optional; application runs out-of-the-box with SQLite)*
- `pip` package manager

### 2. Installation
Open your terminal in the project directory:
```bash
cd food_bridge
python -m pip install -r requirements.txt
```

### 3. Database Configuration
The application supports **both MySQL and SQLite seamlessly**.

#### Option A: Running with SQLite (Default / Instant Setup)
No configuration required! The application automatically creates and uses `instance/food_bridge.db`.

#### Option B: Running with MySQL (Production)
1. Ensure your MySQL server is running.
2. Create the database:
   ```sql
   CREATE DATABASE food_bridge CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. Import the production schema:
   ```bash
   mysql -u root -p food_bridge < database/schema.sql
   ```
4. Update `.env` with your MySQL connection string:
   ```env
   DATABASE_URL=mysql+pymysql://root:yourpassword@localhost:3306/food_bridge
   ```

### 4. Seed Demonstration Data
Populate the database with realistic hotels, NGOs, food donations, volunteer assignments, and safety audit records:
```bash
python database/seed.py
```

### 5. Run Automated Tests
Execute the unit and integration test suite:
```bash
python tests/test_food_bridge.py
```
*All 8 test suites (authentication, matching, lifecycle, safety quarantine, routes) will run and pass.*

### 6. Start the Web Server
Launch the Flask development server:
```bash
python run.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 📁 Project Directory Structure

```
food_bridge/
├── .env                  # Runtime environment configuration
├── .env.example          # Environment template with MySQL & SQLite settings
├── config.py             # 12-factor configuration (Dev, Test, Prod)
├── requirements.txt      # Python dependencies
├── run.py                # Server entry point
├── README.md             # Complete venture and technical documentation
│
├── app/
│   ├── __init__.py       # Application factory, LoginManager, context processors
│   ├── models.py         # SQLAlchemy models (User, Donor, NGO, Volunteer, etc.)
│   │
│   ├── ai/
│   │   ├── matching.py   # Multi-attribute scoring & Haversine proximity engine
│   │   ├── forecasting.py# Scikit-learn Random Forest 7-day surplus forecaster
│   │   └── analytics.py  # Environmental impact (CO2, water) & hotspot analytics
│   │
│   ├── routes/
│   │   ├── auth.py       # Authentication, registration & profile management
│   │   ├── main.py       # Home, About, Available Food, Map, Smart Match, Analytics
│   │   ├── donor.py      # Donor Dashboard, Add Donation, Request approval
│   │   ├── ngo.py        # NGO Dashboard, Food requests, Safety reporting
│   │   ├── volunteer.py  # Volunteer Dashboard, Mission claims, Status stepper
│   │   ├── beneficiary.py# Beneficiary assistance requests & nearby centers
│   │   └── admin.py      # Verification queue, Safety audits, User management
│   │
│   ├── services/
│   │   ├── donation_service.py     # Donation lifecycle business logic
│   │   └── notification_service.py # In-app notification dispatcher
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── foodbridge.css      # Custom styling, stepper, cards, color palette
│   │   └── js/
│   │       ├── main.js             # Notification mark-read & datetime helpers
│   │       └── map.js              # Leaflet OpenStreetMap interactive engine
│   │
│   └── templates/
│       ├── base.html               # Shared layout, navbar, notification dropdown, footer
│       ├── index.html              # Landing page with live impact counter & hero
│       ├── about.html              # Problem, solution & venture business model
│       ├── contact.html            # Contact & corporate partnerships inquiry
│       ├── login.html              # Sign-in with one-click demo credentials
│       ├── register.html           # Dynamic role-based registration form
│       ├── profile.html            # Profile editing & password change
│       ├── available_food.html     # Real-time surplus marketplace with filters
│       ├── food_details.html       # Batch specifications & request modal
│       ├── donation_tracking.html  # Live stepper tracking (Available -> Delivered)
│       ├── smart_match.html        # Interactive AI matching simulator & explainability
│       ├── map_view.html           # Full-page Leaflet geospatial map
│       ├── analytics.html          # Chart.js dashboards & impact calculator
│       ├── 404.html                # Not found error page
│       ├── 500.html                # Server error page
│       ├── donor/
│       │   ├── dashboard.html      # Donor KPIs, listings, request approval
│       │   └── add_donation.html   # Surplus food donation submission form
│       ├── ngo/
│       │   ├── dashboard.html      # NGO KPIs, AI recommendations, delivery feed
│       │   └── report_safety.html  # Unsafe food incident report & quarantine
│       ├── volunteer/
│       │   └── dashboard.html      # Volunteer mission hub & status stepper
│       ├── beneficiary/
│       │   └── dashboard.html      # Community assistance requests
│       └── admin/
│           └── dashboard.html      # Verification queue, safety audits, user governance
│
├── database/
│   ├── schema.sql        # Production MySQL 8.0+ DDL with foreign keys & indexes
│   └── seed.py           # Demonstration database seeder
│
└── tests/
    └── test_food_bridge.py # Automated test suite (8 tests, all passing)
```

---

## 💼 Startup Business Model & Monetization Strategy

1. **Free Tier for NGOs & Beneficiaries:** Access to food is guaranteed 100% free forever for charitable organizations and food-insecure families.
2. **Basic CSR Partner Tier (₹2,499 / month):** For restaurants and independent banquet halls wanting monthly ESG carbon offset certificates, priority volunteer pickup routing, and Section 80G tax benefit documentation.
3. **Enterprise Green Tier (₹9,999 / month):** For hotel chains, supermarket networks, and IT campus cafeterias requiring predictive waste analytics, dedicated cold-chain transport, and automated ERP/POS integration.
4. **Voluntary Carbon Credit Marketplace:** Converting verified organic waste diversion from landfills into certified carbon offsets sold to corporate sustainability funds.
5. **Municipal Smart City Contracts:** City-level organic waste compliance monitoring and landfill diversion tracking.

---

## 🛡️ Food Safety & Cold Chain Protocol
Food safety is prioritized through automated platform rules:
- **Automatic Expiry Enforcement:** Expired donations cannot be requested or dispatched.
- **Mandatory Safe Timestamps:** Donors must record preparation time and safe deadline.
- **Sensory & Temperature Logs:** Volunteers record probe temperatures upon pickup.
- **Immediate Batch Quarantine:** When an NGO flags a food safety concern, the donation is quarantined immediately, preventing distribution while notifying platform administrators.

---

*Food Bridge Technologies Inc. — Built for Real-World Urban Food Redistribution.*

