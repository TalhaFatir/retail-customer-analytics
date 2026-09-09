# Retail Customer Analytics: From Data to Business Insights

An end-to-end data analytics project using **Python, SQL Server, and Power BI** to transform raw customer shopping data into clear, business-focused insights.

The project analyzes **3,900 customer purchase records** to explore revenue, customer behavior, product performance, subscriptions, discounts, loyalty, shipping preferences, and age-based purchasing patterns.

---

##  Dashboard Preview

![Power BI Dashboard](images/Screenshot%202026-09-08%20223059.png)

> 🔗 **Live Interactive Power BI Dashboard:** Coming soon

---

##  Project Objectives

This project answers business questions such as:

- Which customer groups generate the most revenue?
- Which products receive the highest customer ratings?
- Do subscribers spend more than non-subscribers?
- Which products rely most heavily on discounts?
- Which products are purchased most within each category?
- Are repeat buyers more likely to subscribe?
- Which age groups contribute the most revenue?
- How does shipping method relate to purchase amount?

---

##  Tools & Technologies

### Python
- pandas
- SQLAlchemy
- pyodbc
- pathlib

### Database
- Microsoft SQL Server
- SQL Server Management Studio (SSMS)

### Visualization
- Microsoft Power BI

---

##  Project Workflow

```text
Raw CSV Dataset
       ↓
Python Data Exploration
       ↓
Data Cleaning
       ↓
Feature Engineering
       ↓
SQL Server
       ↓
SQL Business Analysis
       ↓
Power BI Dashboard
       ↓
Business Insights
```

---

##  Python Data Preparation

Python was used to:

- Load and inspect the raw CSV dataset
- Check data types, descriptive statistics, and missing values
- Fill missing `Review Rating` values using the median rating within each product category
- Standardize column names
- Rename `purchase_amount_(usd)` to `purchase_amount`
- Create four age groups using `pandas.qcut()`
- Convert purchase-frequency labels into approximate numbers of days
- Remove the redundant `promo_code_used` field
- Save a cleaned CSV file when the script is run locally
- Transfer the prepared DataFrame into SQL Server using SQLAlchemy and pyodbc

**Python code:**  
[`python/data_cleaning.py`](python/data_cleaning.py)

---

##  SQL Business Analysis

SQL Server was used to answer **10 business questions** covering:

1. Revenue by gender
2. High-spending customers who used discounts
3. Top 5 products by average review rating
4. Standard vs Express shipping purchase value
5. Subscribers vs non-subscribers
6. Products with the highest discount-use percentage
7. Customer segmentation into New, Returning, and Loyal
8. Top products within each category
9. Repeat buyers and subscription behavior
10. Revenue contribution by age group

The analysis uses `SUM()`, `AVG()`, `COUNT()`, `CASE`, `WHERE`, `GROUP BY`, subqueries, CTEs, and `ROW_NUMBER()`.

**SQL queries:**  
[`sql/customer_behavior_analysis.sql`](sql/customer_behavior_analysis.sql)

---

## Power BI Dashboard

The interactive dashboard includes:

- **3.9K** total customer purchase records
- **$59.76** average spend per purchase
- Approximately **$233K** total revenue
- Subscriber vs non-subscriber share
- Revenue and purchase volume by product category
- Revenue and purchase volume by age group
- Top 5 highest-rated products
- Interactive slicers for subscription status, gender, category, and shipping method

**Power BI file:**  
[`Customer Shopping Behavior & Revenue Insights Dashboard.pbix`](powerbi/Customer%20Shopping%20Behavior%20%26%20Revenue%20Insights%20Dashboard.pbix)

---

##  Key Insights

- Total revenue is **$233,081**
- Average purchase amount is **$59.76**
- **Clothing** generates the highest revenue and purchase volume
- About **27%** of customers are subscribers
- Subscriber and non-subscriber average spending is very similar
- **Young Adults** generate the highest revenue among the four engineered age groups
- A large proportion of repeat buyers are still not subscribers
- Hat, Sneakers, Coat, Sweater, and Pants have some of the highest discount-use rates

---

##  Business Recommendations

- Target frequent non-subscribers with clear subscription benefits
- Protect loyal customers with retention campaigns and personalized offers
- Review products that depend heavily on discounts
- Keep strong-performing categories such as Clothing well stocked
- Use highly rated products in merchandising and cross-selling
- Market to Young Adults while maintaining balanced targeting across age groups
- Test shipping-based offers carefully

---

##  Full Project Report

The full report explains the Python workflow, SQL analysis, Power BI dashboard, findings, and business recommendations in detail.

**Project report:**  
[`Project 1 Report.pdf`](report/Project%201%20Report.pdf)

---

## Repository Structure

```text
retail-customer-analytics/
│
├── data/
│   └── customer_shopping_behavior.csv
│
├── images/
│   └── Screenshot 2026-09-08 223059.png
│
├── powerbi/
│   └── Customer Shopping Behavior & Revenue Insights Dashboard.pbix
│
├── python/
│   └── data_cleaning.py
│
├── report/
│   └── Project 1 Report.pdf
│
├── sql/
│   └── customer_behavior_analysis.sql
│
└── README.md
```

---

##  Future Improvements

Future versions could include:

- Profit and cost analysis
- Time-series sales analysis
- Customer churn prediction
- Subscription conversion prediction
- Customer-level longitudinal analysis
- Machine learning models for purchase propensity

---

##  Author

**Talha Fatir**  
Data Analytics Portfolio Project
