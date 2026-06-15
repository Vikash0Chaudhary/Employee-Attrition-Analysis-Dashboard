import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ==================================================
# PROJECT HEADER
# ==================================================

print("=" * 60)
print("EMPLOYEE ATTRITION ANALYSIS & PREDICTION SYSTEM")
print("=" * 60)

# ==================================================
# LOAD DATASET
# ==================================================

df = pd.read_csv("employee_attrition_500.csv")

print("\nDataset Loaded Successfully!")

# ==================================================
# DATASET INFORMATION
# ==================================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

# ==================================================
# MISSING VALUES
# ==================================================

print("\nMissing Values:")
print(df.isnull().sum())

# ==================================================
# ATTRITION DISTRIBUTION
# ==================================================

print("\nAttrition Count:")
print(df["Attrition"].value_counts())

# ==================================================
# PIE CHART
# ==================================================

plt.figure(figsize=(8,8))

df["Attrition"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Employee Attrition Distribution")
plt.ylabel("")

plt.savefig("attrition_pie_chart.png")

plt.show()

# ==================================================
# GENDER DISTRIBUTION
# ==================================================

plt.figure(figsize=(8,5))

sns.countplot(
    x="Gender",
    data=df
)

plt.title("Gender Distribution")

plt.savefig("gender_distribution.png")

plt.show()

# ==================================================
# GENDER VS ATTRITION
# ==================================================

plt.figure(figsize=(8,5))

sns.countplot(
    x="Gender",
    hue="Attrition",
    data=df
)

plt.title("Gender vs Attrition")

plt.savefig("gender_attrition.png")

plt.show()

# ==================================================
# DEPARTMENT ANALYSIS
# ==================================================

plt.figure(figsize=(10,5))

sns.countplot(
    x="Department",
    hue="Attrition",
    data=df
)

plt.title("Department Wise Attrition")

plt.savefig("department_attrition.png")

plt.show()

# ==================================================
# AGE DISTRIBUTION
# ==================================================

plt.figure(figsize=(10,5))

sns.histplot(
    df["Age"],
    bins=20,
    kde=True
)

plt.title("Age Distribution")

plt.savefig("age_distribution.png")

plt.show()

# ==================================================
# MONTHLY INCOME DISTRIBUTION
# ==================================================

plt.figure(figsize=(10,5))

sns.histplot(
    df["MonthlyIncome"],
    bins=20,
    kde=True
)

plt.title("Monthly Income Distribution")

plt.savefig("income_distribution.png")

plt.show()

# ==================================================
# YEARS AT COMPANY
# ==================================================

plt.figure(figsize=(10,5))

sns.histplot(
    df["YearsAtCompany"],
    bins=20,
    kde=True
)

plt.title("Years At Company")

plt.savefig("years_company_distribution.png")

plt.show()

# ==================================================
# OVERTIME VS ATTRITION
# ==================================================

plt.figure(figsize=(8,5))

sns.countplot(
    x="OverTime",
    hue="Attrition",
    data=df
)

plt.title("Overtime Impact on Attrition")

plt.savefig("overtime_attrition.png")

plt.show()

# ==================================================
# HR INSIGHTS
# ==================================================

total_employees = len(df)

employees_left = len(
    df[df["Attrition"] == "Yes"]
)

employees_stayed = len(
    df[df["Attrition"] == "No"]
)

attrition_rate = (
    employees_left / total_employees
) * 100

print("\n")
print("=" * 60)
print("HR INSIGHTS")
print("=" * 60)

print(f"Total Employees : {total_employees}")
print(f"Employees Left : {employees_left}")
print(f"Employees Stayed : {employees_stayed}")
print(f"Attrition Rate : {attrition_rate:.2f}%")


# ==================================================
# MACHINE LEARNING SECTION
# ==================================================

print("\n")
print("=" * 60)
print("EMPLOYEE ATTRITION PREDICTION MODEL")
print("=" * 60)

ml_df = df.copy()

# Convert ALL text columns into numbers

for col in ml_df.columns:
    if ml_df[col].dtype == "object":
        ml_df[col] = pd.factorize(ml_df[col])[0]

print("\nData Types After Encoding:\n")
print(ml_df.dtypes)

# Features and Target

X = ml_df.drop("Attrition", axis=1)
y = ml_df["Attrition"]

# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Train Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

# Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ==================================================
# FEATURE IMPORTANCE
# ==================================================

importance = pd.DataFrame(
    {
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }
)

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop Important Features")

print(
    importance.head(10)
)

plt.figure(figsize=(12,6))

sns.barplot(
    x="Importance",
    y="Feature",
    data=importance.head(10)
)

plt.title(
    "Top 10 Features Affecting Attrition"
)

plt.tight_layout()

plt.savefig("feature_importance.png")

plt.show()

# ==================================================
# CORRELATION HEATMAP
# ==================================================

plt.figure(figsize=(10,8))

sns.heatmap(
    ml_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title(
    "Correlation Heatmap"
)

plt.savefig("correlation_heatmap.png")

plt.show()

# ==================================================
# COMPLETED
# ==================================================

print("\n")
print("=" * 60)
print("PROJECT COMPLETED SUCCESSFULLY")
print("=" * 60)