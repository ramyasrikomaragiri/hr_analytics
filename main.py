import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

INPUT_FILE = "data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
OUTPUT_FILE = "data/cleaned/hr_employee_cleaned.csv"

IMAGE_DIRS = [
    "images/eda",
    "images/employee",
    "images/attrition"
]

for directory in IMAGE_DIRS:
    os.makedirs(directory, exist_ok=True)

print("=" * 70)
print("HR EMPLOYEE ANALYTICS")
print("=" * 70)

# --------------------------------------------------
# 1. LOAD DATA
# --------------------------------------------------

print("\nLoading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# --------------------------------------------------
# 2. BASIC DATA CHECK
# --------------------------------------------------

print("\nChecking missing values...")

missing = df.isnull().sum()
missing = missing[missing > 0]

if len(missing) == 0:
    print("No missing values found.")
else:
    print(missing)

print(f"\nDuplicate rows: {df.duplicated().sum()}")

# --------------------------------------------------
# 3. DATA CLEANING
# --------------------------------------------------

print("\nCleaning data...")

df = df.drop_duplicates()

# Remove unnecessary constant columns
constant_columns = [
    "EmployeeCount",
    "StandardHours",
    "Over18"
]

existing_constant_columns = [
    column for column in constant_columns
    if column in df.columns
]

df = df.drop(columns=existing_constant_columns)

# Convert Yes/No columns to numeric indicators
binary_columns = [
    "Attrition",
    "OverTime",
    "BusinessTravel"
]

for column in binary_columns:
    if column in df.columns:
        if column == "BusinessTravel":
            df[column] = df[column].astype(str)
        else:
            df[column + "_Flag"] = df[column].map({
                "Yes": 1,
                "No": 0
            })

# --------------------------------------------------
# 4. CREATE BUSINESS METRICS
# --------------------------------------------------

print("\nCreating business metrics...")

df["MonthlyIncome"] = pd.to_numeric(
    df["MonthlyIncome"],
    errors="coerce"
)

df["AnnualIncome"] = df["MonthlyIncome"] * 12

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 25, 35, 45, 55, 100],
    labels=[
        "Under 25",
        "25-34",
        "35-44",
        "45-54",
        "55+"
    ],
    right=False
)

df["TenureGroup"] = pd.cut(
    df["YearsAtCompany"],
    bins=[-1, 2, 5, 10, 20, 100],
    labels=[
        "0-2 Years",
        "3-5 Years",
        "6-10 Years",
        "11-20 Years",
        "20+ Years"
    ]
)

# --------------------------------------------------
# 5. ATTRITION METRICS
# --------------------------------------------------

total_employees = len(df)

attrition_count = (
    df["Attrition"]
    .eq("Yes")
    .sum()
)

attrition_rate = (
    attrition_count / total_employees * 100
)

average_age = df["Age"].mean()

average_monthly_income = df["MonthlyIncome"].mean()

average_annual_income = df["AnnualIncome"].mean()

print("\n" + "=" * 70)
print("KEY HR METRICS")
print("=" * 70)

print(f"Total Employees       : {total_employees:,}")
print(f"Employees Left        : {attrition_count:,}")
print(f"Attrition Rate        : {attrition_rate:.2f}%")
print(f"Average Age           : {average_age:.1f}")
print(f"Avg Monthly Income    : ${average_monthly_income:,.2f}")
print(f"Avg Annual Income     : ${average_annual_income:,.2f}")

# --------------------------------------------------
# 6. DEPARTMENT ANALYSIS
# --------------------------------------------------

department_analysis = (
    df.groupby("Department")
    .agg(
        Employees=("EmployeeNumber", "count"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Average_Salary=("MonthlyIncome", "mean")
    )
    .reset_index()
)

department_analysis["Attrition_Rate"] = (
    department_analysis["Attrition_Count"]
    / department_analysis["Employees"]
    * 100
)

print("\nDepartment Analysis:")
print(department_analysis)

# --------------------------------------------------
# 7. JOB ROLE ANALYSIS
# --------------------------------------------------

job_role_analysis = (
    df.groupby("JobRole")
    .agg(
        Employees=("EmployeeNumber", "count"),
        Attrition_Count=("Attrition_Flag", "sum"),
        Average_Salary=("MonthlyIncome", "mean")
    )
    .reset_index()
)

job_role_analysis["Attrition_Rate"] = (
    job_role_analysis["Attrition_Count"]
    / job_role_analysis["Employees"]
    * 100
)

print("\nTop Job Roles by Attrition Rate:")
print(
    job_role_analysis
    .sort_values("Attrition_Rate", ascending=False)
    .head(10)
)

# --------------------------------------------------
# 8. OVERTIME ANALYSIS
# --------------------------------------------------

overtime_analysis = (
    df.groupby("OverTime")
    .agg(
        Employees=("EmployeeNumber", "count"),
        Attrition_Count=("Attrition_Flag", "sum")
    )
    .reset_index()
)

overtime_analysis["Attrition_Rate"] = (
    overtime_analysis["Attrition_Count"]
    / overtime_analysis["Employees"]
    * 100
)

print("\nOvertime Analysis:")
print(overtime_analysis)

# --------------------------------------------------
# 9. AGE GROUP ANALYSIS
# --------------------------------------------------

age_analysis = (
    df.groupby("AgeGroup", observed=False)
    .agg(
        Employees=("EmployeeNumber", "count"),
        Attrition_Count=("Attrition_Flag", "sum")
    )
    .reset_index()
)

age_analysis["Attrition_Rate"] = (
    age_analysis["Attrition_Count"]
    / age_analysis["Employees"]
    * 100
)

print("\nAge Group Analysis:")
print(age_analysis)

# --------------------------------------------------
# 10. SAVE CLEANED DATA
# --------------------------------------------------

os.makedirs("data/cleaned", exist_ok=True)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

print(f"\nCleaned dataset saved to: {OUTPUT_FILE}")

# --------------------------------------------------
# 11. VISUALIZATIONS
# --------------------------------------------------

sns.set_theme(style="whitegrid")

# Department Attrition

plt.figure(figsize=(10, 6))

sns.barplot(
    data=department_analysis.sort_values(
        "Attrition_Rate",
        ascending=False
    ),
    x="Attrition_Rate",
    y="Department"
)

plt.title("Attrition Rate by Department")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Department")
plt.tight_layout()

plt.savefig(
    "images/attrition/attrition_by_department.png",
    dpi=200
)

plt.close()

# Job Role Attrition

top_roles = (
    job_role_analysis
    .sort_values("Attrition_Rate", ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 7))

sns.barplot(
    data=top_roles,
    x="Attrition_Rate",
    y="JobRole"
)

plt.title("Top Job Roles by Attrition Rate")
plt.xlabel("Attrition Rate (%)")
plt.ylabel("Job Role")
plt.tight_layout()

plt.savefig(
    "images/attrition/attrition_by_job_role.png",
    dpi=200
)

plt.close()

# Salary Distribution

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="MonthlyIncome",
    bins=30,
    kde=True
)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Employees")
plt.tight_layout()

plt.savefig(
    "images/eda/salary_distribution.png",
    dpi=200
)

plt.close()

# Age Distribution

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Age",
    bins=20,
    kde=True
)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Employees")
plt.tight_layout()

plt.savefig(
    "images/eda/age_distribution.png",
    dpi=200
)

plt.close()

# Employees by Department

department_counts = (
    df["Department"]
    .value_counts()
    .reset_index()
)

department_counts.columns = [
    "Department",
    "Employees"
]

plt.figure(figsize=(10, 6))

sns.barplot(
    data=department_counts,
    x="Employees",
    y="Department"
)

plt.title("Employees by Department")
plt.xlabel("Employees")
plt.ylabel("Department")
plt.tight_layout()

plt.savefig(
    "images/employee/employees_by_department.png",
    dpi=200
)

plt.close()

# Overtime Attrition

plt.figure(figsize=(8, 6))

sns.barplot(
    data=overtime_analysis,
    x="OverTime",
    y="Attrition_Rate"
)

plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig(
    "images/attrition/attrition_by_overtime.png",
    dpi=200
)

plt.close()

# Age Group Attrition

plt.figure(figsize=(10, 6))

sns.barplot(
    data=age_analysis,
    x="AgeGroup",
    y="Attrition_Rate"
)

plt.title("Attrition Rate by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig(
    "images/attrition/attrition_by_age_group.png",
    dpi=200
)

plt.close()

# --------------------------------------------------
# 12. FINAL SUMMARY
# --------------------------------------------------

print("\n" + "=" * 70)
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nGenerated files:")

print("1. data/cleaned/hr_employee_cleaned.csv")
print("2. images/attrition/attrition_by_department.png")
print("3. images/attrition/attrition_by_job_role.png")
print("4. images/attrition/attrition_by_overtime.png")
print("5. images/attrition/attrition_by_age_group.png")
print("6. images/eda/salary_distribution.png")
print("7. images/eda/age_distribution.png")
print("8. images/employee/employees_by_department.png")

print("\nProject 2 Python analysis completed.")