# HR Employee Analytics – Project Report

## 1. Executive Summary

This project analyses employee workforce data to understand employee attrition and identify factors that may influence employee turnover.

The project uses Python for data preparation and exploratory analysis, SQL for business-focused analysis, and Power BI for interactive reporting.

The final dashboard provides HR-focused insights into employee attrition, departments, job roles, overtime, age groups and workforce distribution.

---

## 2. Business Problem

Employee attrition can create additional recruitment, training and operational costs for an organisation.

HR teams therefore need to understand where employee turnover is concentrated and which workforce characteristics are associated with higher attrition.

This project addresses the following questions:

- What is the overall employee attrition rate?
- Which departments experience higher attrition?
- Which job roles have higher attrition?
- Does overtime relate to employee attrition?
- Which age groups show higher attrition?
- How is the workforce distributed across departments?
- What HR actions could help improve employee retention?

---

## 3. Dataset

The project uses an employee attrition dataset containing demographic, professional and employment-related information.

Important variables include:

- Employee Number
- Age
- Gender
- Department
- Job Role
- Monthly Income
- OverTime
- Years at Company
- Attrition

The raw dataset is stored in:

`data/raw/`

The cleaned data is stored in:

`data/cleaned/`

---

## 4. Data Preparation

Python was used to prepare the dataset for analysis.

The preparation process included:

1. Loading the raw dataset
2. Inspecting the dataset structure
3. Checking missing values
4. Checking duplicate records
5. Validating data types
6. Reviewing categorical variables
7. Creating analytical variables
8. Creating age groups
9. Creating tenure groups
10. Exporting the cleaned dataset

The cleaned dataset was then used for SQL analysis and Power BI reporting.

---

## 5. Exploratory Data Analysis

Exploratory analysis was performed to understand workforce characteristics and attrition patterns.

The analysis focused on:

- Employee demographics
- Department distribution
- Job role distribution
- Monthly income
- Employee tenure
- Age groups
- Overtime
- Attrition

Visualisations were created to identify patterns and differences between employee groups.

---

## 6. SQL Analysis

SQL was used to perform business-oriented analysis.

The SQL analysis included:

- Basic employee statistics
- Department-level analysis
- Attrition analysis
- Customer-style segmentation techniques adapted for HR analysis
- Product-style analytical structures adapted to employee/job-role analysis
- Time and grouping analysis
- Window functions
- Common Table Expressions
- Views
- Interview-style analytical queries

The SQL scripts are available in the `sql/` directory.

---

## 7. Power BI Dashboard

The final Power BI dashboard provides an executive overview of employee attrition and workforce characteristics.

### Key Performance Indicators

| KPI | Value |
|---|---:|
| Total Employees | 1.47K |
| Employees Left | 237 |
| Attrition Rate | 16.12% |
| Average Monthly Income | 6.50K |

### Dashboard Visualisations

The dashboard contains:

- Attrition Rate by Department
- Attrition Rate by Job Role
- Attrition Rate by Overtime
- Employee Distribution by Department
- Attrition Rate by Age Group
- Interactive Department filter
- Interactive Gender filter
- Interactive Overtime filter

---

## 8. Key Findings

### Attrition

The organisation has an overall attrition rate of approximately 16.12%, indicating that employee retention is an important HR consideration.

### Department

Attrition differs between departments, allowing HR teams to identify departments that require closer investigation.

### Job Role

Employee turnover also varies across job roles. Roles with comparatively higher attrition may require targeted retention strategies.

### Overtime

Employees working overtime show a different attrition pattern compared with employees who do not work overtime. This suggests that workload and work-life balance should be considered when analysing retention.

### Age

Younger employee groups show comparatively higher attrition, suggesting that early-career employees may benefit from stronger career development and engagement programmes.

---

## 9. Business Recommendations

Based on the analysis, the following actions are recommended:

### 1. Monitor High-Attrition Departments

HR teams should regularly monitor departments with higher attrition and investigate the underlying causes.

### 2. Review Overtime

Workload and overtime patterns should be monitored to identify potential employee burnout and work-life balance issues.

### 3. Strengthen Career Development

Career progression, mentoring and learning opportunities can help improve retention, particularly among early-career employees.

### 4. Target High-Risk Job Roles

Retention strategies can be tailored to job roles that consistently show higher turnover.

### 5. Improve HR Monitoring

A recurring Power BI dashboard can help HR teams monitor attrition trends and workforce KPIs over time.

---

## 10. Limitations

The analysis is based on the variables available in the dataset.

The dataset does not provide detailed information about:

- Employee satisfaction surveys
- Manager quality
- Exit interview responses
- External labour market conditions
- Detailed reasons for leaving

Therefore, the findings should be treated as analytical indicators rather than direct evidence of causation.

---

## 11. Conclusion

This project demonstrates an end-to-end HR analytics workflow using Python, SQL and Power BI.

The analysis transforms raw employee data into actionable workforce insights and provides an interactive dashboard that can support HR decision-making.

The project demonstrates practical skills in data cleaning, exploratory analysis, SQL querying, KPI development, dashboard design and business storytelling.

---

## 12. Technologies Used

- Python
- Pandas
- Matplotlib
- SQL
- PostgreSQL
- Power BI
- Git
- GitHub