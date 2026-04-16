# Skinomics: Quantitative Analysis of Digital Asset Liquidity

**Skinomics** is a project at the intersection of **Behavioral Economics**, **Financial Modeling**, and **Data Science**. By treating Counter-Strike 2 (CS2) skins as low-latency digital commodities, this project seeks to identify market inefficiencies, model transaction friction, and automate risk-adjusted decision-making.

---

## 📊 Core Economic Concepts

The current phase of the project focuses on **Transaction Friction Theory**. In decentralized digital marketplaces, the "Liquidation Value" of an asset is significantly impacted by platform-specific commission structures.

### **The Break-Even Model**
To account for sequential platform fees (Marketplace Commission + Withdrawal Fees), I utilize the following model to determine the minimum viable exit price:

$$Price_{Gross} = \frac{Asset\ Cost}{(1 - Fee_{Market}) \times (1 - Fee_{Withdraw})}$$

### **The Infrastructure Efficiency Gap**
Analysis of the current market landscape reveals a significant discrepancy between the **Steam Community Market** (15% friction) and **3rd Party Marketplaces** (e.g., CSFloat, ~4.8% combined friction). 

Current calculations identify a **~12% Efficiency Gap**, representing a substantial increase in "Buying Power" when optimizing for low-friction infrastructure.

---

## 🛠️ Roadmap: The 7-Day Sprint

### **Phase 1: Deterministic Modeling (Completed)**
* **Day 1: Manual Transaction Calculator**
    * Implemented `calc.py` to model the "Cash-to-Cash" cycle. 
    * Calculated sequential fee compounding and transaction-cost ratios.

### **Phase 2: Stochastic & Statistical Modeling (In Progress)**
* **Day 2: Expected Value ($E[X]$) Analysis**
    * Transitioning from fixed prices to probability-based outcomes.
    * Modeling "Bull" and "Bear" market scenarios to determine **Risk-Adjusted Net Return**.
* **Day 3: Descriptive Statistics**
    * Comparing Mean vs. Median pricing to identify market outliers in low-volume "Souvenir" categories.
* **Day 4: Volatility & Asset Risk**
    * Quantifying asset risk through price variance and historical range analysis.

### **Phase 3: Data Engineering & Deployment**
* **Day 5-6: SQL Warehouse Integration**
    * Moving from local variables to a persistent `SQLite` database for time-series analysis.
* **Day 7: Dashboard Deployment**
    * Visualizing market trends and trade signals via a **Streamlit** web interface.

---

## 📈 Methodology
* **Language**: Python 3.x
* **Libraries**: `sqlite3`, `math`, `requests`
* **Statistical Focus**: Discrete Probability Distributions, Transaction Cost Theory, and Market Liquidity.

---

## 📝 Progress Log
* **2026-04-16**: Successfully initialized `calc.py`. Optimized mathematical logic for sequential fee deductions and documented the 12% infrastructure efficiency gap.
