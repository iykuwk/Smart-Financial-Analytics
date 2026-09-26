import random
import numpy as np
import pandas as pd

from config import *

# =====================================================
# Reproducibility
# =====================================================

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# =====================================================
# Load Lookup Tables
# =====================================================

entities = pd.read_excel(DATA_FOLDER / "entities.xlsx")
departments = pd.read_excel(DATA_FOLDER / "departments.xlsx")
cost_centers = pd.read_excel(DATA_FOLDER / "cost_centers.xlsx")
gl_accounts = pd.read_excel(DATA_FOLDER / "gl_accounts.xlsx")

# =====================================================
# Calendar
# =====================================================

dates = pd.date_range(
    START_DATE,
    END_DATE,
    freq="D"
)

# =====================================================
# Currency Mapping
# =====================================================

currency_map = {
    "NHG Kenya Ltd": "KES",
    "NHG Uganda Ltd": "UGX",
    "NHG Tanzania Ltd": "TZS",
    "NHG South Africa Ltd": "ZAR",
    "NHG USA Inc": "USD"
}

# =====================================================
# Entity Size Multipliers
# =====================================================

entity_factor = {

    "NHG Kenya Ltd":1.00,

    "NHG Uganda Ltd":0.70,

    "NHG Tanzania Ltd":0.80,

    "NHG South Africa Ltd":1.40,

    "NHG USA Inc":1.65

}

# =====================================================
# Department Spend Multipliers
# =====================================================

department_factor = {

    "Finance":0.90,

    "HR":0.75,

    "Marketing":1.20,

    "IT":1.35,

    "Engineering":1.70,

    "Operations":1.60,

    "Procurement":1.10,

    "Legal":0.70,

    "Supply Chain":1.50,

    "Facilities":1.00

}

# =====================================================
# Department Variance Behaviour
# (Actual vs Budget)
# =====================================================

variance_profile = {

    "Finance":(0.98,1.03),

    "HR":(0.94,1.01),

    "Marketing":(0.90,1.15),

    "IT":(1.00,1.12),

    "Engineering":(0.92,1.18),

    "Operations":(0.95,1.10),

    "Procurement":(0.90,0.99),

    "Legal":(0.96,1.05),

    "Supply Chain":(0.94,1.10),

    "Facilities":(0.96,1.05)

}

# =====================================================
# Department → GL Account Rules
# =====================================================

department_gl = {

    "Finance":[
        "Salaries",
        "Consulting",
        "Insurance"
    ],

    "HR":[
        "Salaries",
        "Training",
        "Professional Services"
    ],

    "Marketing":[
        "Marketing",
        "Travel",
        "Consulting"
    ],

    "IT":[
        "Software",
        "Equipment",
        "Consulting"
    ],

    "Engineering":[
        "Equipment",
        "Maintenance",
        "Software"
    ],

    "Operations":[
        "Fuel",
        "Maintenance",
        "Utilities"
    ],

    "Procurement":[
        "Office Supplies",
        "Travel",
        "Consulting"
    ],

    "Legal":[
        "Professional Services",
        "Consulting",
        "Insurance"
    ],

    "Supply Chain":[
        "Fuel",
        "Maintenance",
        "Travel"
    ],

    "Facilities":[
        "Utilities",
        "Rent",
        "Maintenance"
    ]

}

# =====================================================
# Monthly Seasonality
# =====================================================

seasonality = {

    1:0.90,
    2:0.88,
    3:0.95,
    4:1.00,
    5:1.04,
    6:1.02,
    7:1.08,
    8:1.15,
    9:1.06,
    10:1.12,
    11:1.18,
    12:1.35

}

# =====================================================
# Empty Records List
# =====================================================

records = []

# =====================================================
# Generate Financial Transactions
# =====================================================

for i in range(NUM_TRANSACTIONS):

    # -----------------------------
    # Transaction ID
    # -----------------------------

    transaction_id = f"FIN-{2025 + (i // 2500)}-{i+1:06d}"

    # -----------------------------
    # Date
    # -----------------------------

    date = random.choice(dates)

    year = date.year
    month = date.month
    quarter = f"Q{((month-1)//3)+1}"

    # -----------------------------
    # Entity
    # -----------------------------

    entity = random.choice(
        entities["Entity"].tolist()
    )

    currency = currency_map[entity]

    # -----------------------------
    # Department
    # -----------------------------

    department = random.choice(
        departments["Department"].tolist()
    )

    # -----------------------------
    # Cost Center
    # -----------------------------

    dept_cc = cost_centers[
        cost_centers["Department"] == department
    ]

    cost_center = random.choice(
        dept_cc["Cost_Center"].tolist()
    )

    # -----------------------------
    # GL Account
    # -----------------------------

    gl_account = random.choice(
        department_gl[department]
    )

    # -----------------------------
    # Base Budget
    # -----------------------------

    base_budget = random.randint(
        300000,
        1200000
    )

    budget = (
        base_budget
        * entity_factor[entity]
        * department_factor[department]
        * seasonality[month]
    )

    # -----------------------------
    # Actual Spend
    # -----------------------------

    low, high = variance_profile[department]

    actual = budget * random.uniform(low, high)

    # -----------------------------
    # Forecast
    # -----------------------------

    forecast = actual * random.uniform(
        0.97,
        1.05
    )

    # -----------------------------
    # Variance
    # -----------------------------

    variance = actual - budget

    variance_pct = (
        variance / budget
    ) * 100

    # -----------------------------
    # Scenario
    # -----------------------------

    scenario = random.choices(

        ["Budget","Actual","Forecast"],

        weights=[40,40,20],

        k=1

    )[0]

       # =====================================================
    # Save Transaction
    # =====================================================

    records.append({

        "Transaction_ID": transaction_id,

        "Date": date,

        "Year": year,

        "Quarter": quarter,

        "Month Name": date.strftime("%B"),

        "Entity": entity,

        "Department": department,

        "Cost_Center": cost_center,

        "GL_Account": gl_account,

        "Budget": round(budget,2),

        "Actual": round(actual,2),

        "Forecast": round(forecast,2),

        "Variance": round(variance,2),

        "Variance_%": round(variance_pct,2),

        "Currency": currency,

        "Scenario": scenario

    })

# =====================================================
# Create DataFrame
# =====================================================

financial_df = pd.DataFrame(records)

# =====================================================
# Sort Dataset
# =====================================================

financial_df = (

    financial_df

    .sort_values(

        ["Date","Entity","Department"]

    )

    .reset_index(drop=True)

)

# =====================================================
# Export Dataset
# =====================================================

output_file = DATA_FOLDER / "financial_transactions.xlsx"

financial_df.to_excel(
    output_file,
    index=False
)

# =====================================================
# Validation Summary
# =====================================================

print("\n" + "=" * 70)
print(" SMART FINANCIAL PLANNING DATASET GENERATED ")
print("=" * 70)

print(f"Records             : {len(financial_df):,}")
print(f"Start Date          : {financial_df['Date'].min().date()}")
print(f"End Date            : {financial_df['Date'].max().date()}")

print(f"Entities            : {financial_df['Entity'].nunique()}")
print(f"Departments         : {financial_df['Department'].nunique()}")
print(f"Cost Centers        : {financial_df['Cost_Center'].nunique()}")
print(f"GL Accounts         : {financial_df['GL_Account'].nunique()}")

print("-" * 70)

print(f"Total Budget        : {financial_df['Budget'].sum():,.2f}")
print(f"Total Actual        : {financial_df['Actual'].sum():,.2f}")
print(f"Total Forecast      : {financial_df['Forecast'].sum():,.2f}")

print(f"Average Variance %  : {financial_df['Variance_%'].mean():.2f}%")

print("-" * 70)

print(f"Missing Values      : {financial_df.isnull().sum().sum()}")
print(f"Duplicate IDs       : {financial_df['Transaction_ID'].duplicated().sum()}")

print("=" * 70)

print("\nSample Records\n")
print(financial_df.head())

print("\nDataset successfully created!")

print(f"\nSaved to:\n{output_file}")