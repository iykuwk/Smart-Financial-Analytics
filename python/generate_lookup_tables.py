import pandas as pd
from pathlib import Path

# Create data folder
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# ==========================
# Entities
# ==========================
entities = pd.DataFrame({
    "Entity": [
        "NHG Kenya Ltd",
        "NHG Uganda Ltd",
        "NHG Tanzania Ltd",
        "NHG South Africa Ltd",
        "NHG USA Inc"
    ]
})

# ==========================
# Departments
# ==========================
departments = pd.DataFrame({
    "Department": [
        "Finance",
        "HR",
        "Marketing",
        "IT",
        "Engineering",
        "Operations",
        "Procurement",
        "Legal",
        "Supply Chain",
        "Facilities"
    ]
})

# ==========================
# Cost Centers
# ==========================
cost_centers = pd.DataFrame({
    "Cost_Center": [
        "CC100",
        "CC101",
        "CC102",
        "CC103",
        "CC104",
        "CC105",
        "CC106",
        "CC107",
        "CC108",
        "CC109"
    ],
    "Department": [
        "Finance",
        "HR",
        "Marketing",
        "IT",
        "Engineering",
        "Operations",
        "Procurement",
        "Legal",
        "Supply Chain",
        "Facilities"
    ]
})

# ==========================
# GL Accounts
# ==========================
gl_accounts = pd.DataFrame({
    "GL_Account": [
        "Salaries",
        "Travel",
        "Utilities",
        "Rent",
        "Software",
        "Consulting",
        "Marketing",
        "Training",
        "Insurance",
        "Maintenance",
        "Office Supplies",
        "Equipment",
        "Fuel",
        "Security",
        "Professional Services"
    ]
})

# ==========================
# Export Lookup Tables
# ==========================
entities.to_excel(DATA_DIR / "entities.xlsx", index=False)
departments.to_excel(DATA_DIR / "departments.xlsx", index=False)
cost_centers.to_excel(DATA_DIR / "cost_centers.xlsx", index=False)
gl_accounts.to_excel(DATA_DIR / "gl_accounts.xlsx", index=False)

print("Lookup tables generated successfully.")