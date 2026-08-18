# HR Employee Analytics & Attrition Dashboard

## 📊 Project Overview

This project analyzes employee data to understand workforce characteristics, employee attrition, job roles, salary patterns, department-level trends, and other factors associated with employee turnover.

The project follows an end-to-end data analytics workflow using **Python, PostgreSQL, SQL, and Power BI**.

The objective is to transform raw HR data into meaningful business insights that can help HR teams understand employee attrition patterns and make data-driven workforce decisions.

---

## 🎯 Business Objectives

The main objectives of this project are to:

* Analyze overall employee attrition.
* Identify departments and job roles with higher attrition.
* Understand the relationship between salary and employee attrition.
* Analyze employee age and attrition patterns.
* Examine workforce distribution across departments.
* Analyze employee experience and other workforce characteristics.
* Identify factors that may be associated with employee turnover.
* Create an interactive Power BI dashboard for HR decision-making.
* Demonstrate an end-to-end data analytics workflow suitable for real-world business analysis.

---

## 📁 Dataset

The project uses the **IBM HR Analytics Employee Attrition & Performance** dataset.

### Dataset Information

* **Number of Employees:** 1,470
* **Number of Columns:** 35
* **File Format:** CSV
* **Domain:** Human Resources
* **Target Variable:** Attrition

The dataset contains information about employees, including:

* Age
* Gender
* Department
* Job Role
* Monthly Income
* Job Level
* Years at Company
* Years in Current Role
* Years Since Last Promotion
* Job Satisfaction
* Environment Satisfaction
* Work-Life Balance
* Overtime
* Business Travel
* Distance From Home
* Total Working Years
* Training Times Last Year
* Performance Rating
* Attrition
* And other employee-related attributes

---

## 🛠️ Tools & Technologies

| Tool         | Purpose                                                    |
| ------------ | ---------------------------------------------------------- |
| Python       | Data cleaning, preprocessing and exploratory data analysis |
| Pandas       | Data manipulation and transformation                       |
| NumPy        | Numerical analysis                                         |
| Matplotlib   | Data visualization                                         |
| PostgreSQL   | Database storage and analysis                              |
| SQL          | Business and HR analytics queries                          |
| Power BI     | Interactive dashboard and visualization                    |
| Git & GitHub | Version control and portfolio presentation                 |

---

## 🔄 Project Workflow

```text
Raw HR Dataset
      ↓
Data Cleaning with Python
      ↓
Exploratory Data Analysis
      ↓
Cleaned CSV Dataset
      ↓
PostgreSQL Database
      ↓
SQL Analysis
      ↓
Power BI Dashboard
      ↓
Business Insights
      ↓
Final Report
      ↓
GitHub Portfolio
```

---

## 🧹 Data Cleaning & Preparation

Python was used to prepare the raw HR dataset for analysis.

The data preparation process included:

* Loading the raw CSV dataset.
* Inspecting the dataset structure.
* Checking data types.
* Identifying missing values.
* Checking duplicate records.
* Reviewing categorical and numerical variables.
* Validating employee-level records.
* Preparing the dataset for database storage and analysis.
* Creating a cleaned dataset for downstream analytics.

The cleaned dataset was then used for PostgreSQL and Power BI analysis.

---

## 🔎 Exploratory Data Analysis

Exploratory Data Analysis was performed using Python to understand the workforce and identify important patterns.

The analysis focused on areas such as:

### Employee Demographics

* Employee age distribution.
* Gender distribution.
* Marital status.
* Education.
* Distance from home.

### Workforce Structure

* Employees by department.
* Employees by job role.
* Job level distribution.
* Business travel patterns.

### Compensation

* Monthly income.
* Salary patterns across job roles.
* Salary and attrition relationships.

### Employee Experience

* Total working years.
* Years at company.
* Years in current role.
* Years since last promotion.

### Employee Satisfaction

* Job satisfaction.
* Environment satisfaction.
* Work-life balance.
* Relationship between satisfaction and attrition.

### Attrition

* Overall attrition.
* Attrition by department.
* Attrition by job role.
* Attrition by age group.
* Attrition by salary range.
* Attrition by overtime.
* Attrition by experience.

---

## 🗄️ PostgreSQL Database

PostgreSQL was used to store and analyze the cleaned HR dataset.

The database layer demonstrates how an analyst can move beyond spreadsheet-based analysis and work with structured relational data.

The workflow includes:

1. Creating the HR analytics database.
2. Creating the employee table.
3. Loading the cleaned employee data.
4. Validating the imported records.
5. Running SQL queries for business analysis.

---

## 🧮 SQL Analysis

SQL queries were created to answer important HR business questions.

Examples include:

* What is the total number of employees?
* How many employees have left the company?
* What is the overall attrition rate?
* Which departments have the highest attrition?
* Which job roles have the highest attrition?
* What is the average salary by department?
* What is the average salary by job role?
* How does overtime relate to attrition?
* Which age groups have higher attrition?
* How does employee experience relate to attrition?
* Which job roles have higher employee counts?
* What is the average years at company by department?
* Which employee groups show higher turnover patterns?

These queries were used to generate business-focused insights and support the Power BI dashboard.

---

## 📊 Power BI Dashboard

An interactive Power BI dashboard was created to present the key findings in a clear and business-friendly format.

### Dashboard Areas

The dashboard focuses on:

* Total Employees
* Total Attrition
* Attrition Rate
* Average Employee Age
* Employee Distribution by Department
* Attrition by Department
* Attrition by Job Role
* Attrition by Salary
* Attrition by Age
* Attrition by Overtime
* Employee Distribution by Job Role
* Workforce and employee experience analysis

### Dashboard Features

The Power BI report includes:

* KPI cards
* Bar charts
* Donut/pie charts
* Column charts
* Interactive filters/slicers
* Department-level analysis
* Job-role analysis
* Attrition analysis

The dashboard is designed to allow HR stakeholders to quickly identify workforce trends and areas requiring attention.

---

## 💡 Key Business Questions

This project aims to answer questions such as:

### 1. How significant is employee attrition?

The overall attrition rate provides an initial measure of employee turnover and helps establish the scale of the workforce retention challenge.

### 2. Which departments experience higher attrition?

Comparing departments helps identify areas where employee retention may require additional attention.

### 3. Which job roles have higher attrition?

Job-role analysis helps identify positions that may experience greater employee turnover.

### 4. Does overtime appear to be associated with attrition?

Comparing employees who work overtime with those who do not can help identify potential workforce patterns.

### 5. Does salary appear to influence attrition?

Salary-band analysis provides insight into whether employees in lower or higher income groups show different attrition patterns.

### 6. Are younger or less experienced employees more likely to leave?

Age and experience analysis can help identify employee groups with potentially higher turnover.

### 7. Does employee satisfaction relate to attrition?

Satisfaction metrics can be compared with attrition to understand whether workplace experience is associated with employee retention.

---

## 📈 Business Insights

The analysis is designed to help HR stakeholders:

* Identify employee groups with higher turnover.
* Understand department-level attrition.
* Identify high-risk job roles.
* Examine compensation-related patterns.
* Understand workforce experience and tenure.
* Identify potential relationships between overtime and attrition.
* Monitor employee satisfaction patterns.
* Support data-driven employee retention strategies.

> **Note:** The analysis identifies patterns and associations in the dataset. These findings should not automatically be interpreted as causal relationships.

---

## 📂 Project Structure

```text
Project-2-HR-Employee-Analytics/
│
├── dashboard/
│   └── HR_Employee_Analytics.pbix
│
├── data/
│   ├── raw/
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   │
│   └── cleaned/
│       └── hr_employee_cleaned.csv
│
├── images/
│   ├── dashboard/
│   ├── eda/
│   ├── employee/
│   └── attrition/
│
├── reports/
│   └── HR_Employee_Analytics_Report.pdf
│
├── sql/
│   ├── database_setup.sql
│   ├── data_analysis.sql
│   └── business_questions.sql
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── employee_analysis.py
│   └── attrition_analysis.py
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🐍 Python Analysis

Python was used as the primary programming environment for data preparation and exploratory analysis.

The Python workflow includes:

```text
Load Dataset
    ↓
Inspect Data
    ↓
Clean Data
    ↓
Validate Data
    ↓
Perform EDA
    ↓
Generate Visualizations
    ↓
Export Cleaned Dataset
```

The analysis scripts are organized into reusable modules rather than keeping the entire analysis in one Python file.

---

## 🗃️ SQL Analysis

The SQL folder contains queries used to:

* Create database structures.
* Load and validate HR data.
* Calculate employee metrics.
* Calculate attrition metrics.
* Analyze departments.
* Analyze job roles.
* Analyze salary.
* Analyze employee experience.
* Answer HR business questions.

This demonstrates practical SQL skills including:

* `SELECT`
* `WHERE`
* `GROUP BY`
* `ORDER BY`
* Aggregate functions
* `CASE WHEN`
* Filtering
* Subqueries
* Business metric calculations

---

## 📊 Power BI Skills Demonstrated

This project demonstrates practical Power BI skills including:

* Data loading
* Data transformation
* Data modeling
* KPI creation
* DAX measures
* Interactive visualizations
* Slicers and filters
* Business-focused dashboard design
* HR analytics
* Data storytelling

---

## 📌 Key Metrics

The dashboard focuses on important HR metrics such as:

| Metric                   | Description                              |
| ------------------------ | ---------------------------------------- |
| Total Employees          | Total number of employees in the dataset |
| Attrition Count          | Number of employees who left             |
| Attrition Rate           | Percentage of employees who left         |
| Average Age              | Average age of employees                 |
| Average Monthly Income   | Average employee monthly income          |
| Average Years at Company | Average employee tenure                  |
| Department Headcount     | Number of employees by department        |
| Job Role Headcount       | Number of employees by job role          |

---

## 📷 Dashboard Preview

Dashboard screenshots are stored in:

```text
images/dashboard/
```

These images provide a quick preview of the Power BI report for visitors who cannot directly open the `.pbix` file through GitHub.

---

## 📄 Project Report

A detailed project report is available in:

```text
reports/
```

The report explains:

* Business problem
* Dataset
* Data preparation
* Exploratory analysis
* SQL analysis
* Power BI dashboard
* Key findings
* Business recommendations
* Conclusion

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Project-2-HR-Employee-Analytics
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Python Analysis

```bash
python main.py
```

### 6. PostgreSQL

Create the required PostgreSQL database and execute the SQL scripts inside:

```text
sql/
```

### 7. Power BI

Open the Power BI file located inside:

```text
dashboard/
```

Then refresh the data if required.

---

## 🔐 Database Configuration

Database credentials should not be committed to GitHub.

Sensitive configuration such as:

* Database username
* Database password
* Host
* Port
* Database name

should be stored using environment variables or a local configuration file excluded through `.gitignore`.

Example:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=hr_analytics
DB_USER=your_username
DB_PASSWORD=your_password
```

---

## 📚 Skills Demonstrated

### Data Analytics

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Statistical Analysis
* Business Analysis
* Data Visualization
* Insight Generation

### Python

* Pandas
* NumPy
* Matplotlib
* Modular Python Programming
* CSV Processing

### SQL

* PostgreSQL
* Aggregations
* Grouping
* Filtering
* Conditional Logic
* Business Queries
* Data Validation

### Power BI

* Dashboard Development
* DAX
* KPI Design
* Interactive Visualizations
* Data Storytelling
* HR Analytics

### Professional Skills

* Problem Solving
* Business Thinking
* Analytical Thinking
* Data Storytelling
* Documentation
* Git & GitHub

---

## 🎓 Portfolio Purpose

This project was developed as part of a data analytics portfolio to demonstrate practical experience in taking a business dataset from raw data through to actionable insights.

It demonstrates the ability to:

```text
Understand a Business Problem
        ↓
Work with Raw Data
        ↓
Clean & Validate Data
        ↓
Analyze Data Using Python
        ↓
Query Data Using SQL
        ↓
Build a Power BI Dashboard
        ↓
Communicate Business Insights
```

---

## 👩‍💻 Author

**Ramya Sri Komaragiri**

Aspiring Data Analyst

Skills:

**Python | SQL | PostgreSQL | Power BI | Excel | Data Analytics | Data Visualization**

---

## ⭐ Project Highlights

* End-to-end HR analytics project
* 1,470 employee records
* 35 employee-related attributes
* Python-based data preparation and EDA
* PostgreSQL database analysis
* SQL business analysis
* Interactive Power BI dashboard
* HR attrition analysis
* Business-focused insights
* GitHub-ready portfolio project

---

## 📌 Conclusion

The HR Employee Analytics & Attrition Dashboard provides an end-to-end view of employee workforce patterns and attrition.

By combining **Python, SQL, PostgreSQL, and Power BI**, the project demonstrates how raw HR data can be transformed into structured analysis, interactive visualizations, and meaningful business insights.

The project highlights the importance of using data to understand employee turnover patterns and support evidence-based HR decision-making.
