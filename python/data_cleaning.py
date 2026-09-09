import pandas
from pathlib import Path
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# ---------------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------------

"""Load the customer shopping behavior dataset into a pandas DataFrame."""

data_path = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "customer_shopping_behavior.csv"
)

raw_data = pandas.read_csv(data_path)


# ---------------------------------------------------------
# INITIAL DATA EXPLORATION
# ---------------------------------------------------------

"""Configure pandas to display all columns when printing the DataFrame."""

pandas.set_option("display.max_columns", None)


"""Preview the first five rows to understand the dataset structure."""

print(raw_data.head())


"""Display column names, data types, non-null counts, and memory usage."""

raw_data.info()


"""Generate descriptive statistics for numerical and categorical columns."""

print(raw_data.describe(include="all"))


"""Check the number of missing values in each column before cleaning."""

print(raw_data.isnull().sum())


# ---------------------------------------------------------
# HANDLE MISSING VALUES
# ---------------------------------------------------------

"""
Fill missing Review Rating values using the median rating
calculated within each product category.
"""

raw_data["Review Rating"] = (
    raw_data.groupby("Category")["Review Rating"]
    .transform(lambda x: x.fillna(x.median()))
)


"""Verify that missing Review Rating values were handled."""

print(raw_data.isnull().sum())


# ---------------------------------------------------------
# STANDARDIZE COLUMN NAMES
# ---------------------------------------------------------

"""
Standardize column names by converting them to lowercase
and replacing spaces with underscores.
"""

raw_data.columns = raw_data.columns.str.lower()
raw_data.columns = raw_data.columns.str.replace(" ", "_")


"""Display updated column names."""

print(raw_data.columns)


# ---------------------------------------------------------
# RENAME COLUMNS
# ---------------------------------------------------------

"""
Rename purchase_amount_(usd) to purchase_amount
for clarity and consistency.
"""

raw_data = raw_data.rename(
    columns={"purchase_amount_(usd)": "purchase_amount"}
)


"""Confirm the column was renamed."""

print(raw_data.columns)


# ---------------------------------------------------------
# FEATURE ENGINEERING: AGE GROUP
# ---------------------------------------------------------

"""
Create four age groups using quartile-based segmentation.

qcut divides customers into four groups containing
roughly equal numbers of customers based on age.
"""

labels = [
    "Young Adult",
    "Adult",
    "Middle Aged",
    "Senior"
]

raw_data["age_group"] = pandas.qcut(
    raw_data["age"],
    q=4,
    labels=labels
)


"""Preview age and corresponding age group."""

print(raw_data[["age", "age_group"]].head(10))


# ---------------------------------------------------------
# FEATURE ENGINEERING: PURCHASE FREQUENCY
# ---------------------------------------------------------

"""
Convert text-based purchase frequency values into
approximate numbers of days.
"""

frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every 3 Months": 90
}


raw_data["purchase_frequency_days"] = (
    raw_data["frequency_of_purchases"]
    .map(frequency_mapping)
)


"""Verify that frequency values were converted correctly."""

print(
    raw_data[
        [
            "frequency_of_purchases",
            "purchase_frequency_days"
        ]
    ].head(10)
)


# ---------------------------------------------------------
# REMOVE REDUNDANT COLUMN
# ---------------------------------------------------------

"""
Compare discount_applied and promo_code_used before
removing redundant data.
"""

print(
    raw_data[
        [
            "discount_applied",
            "promo_code_used"
        ]
    ].head(10)
)


"""
Remove promo_code_used because it contains duplicate
information already represented by discount_applied.
"""

raw_data = raw_data.drop(
    "promo_code_used",
    axis=1
)


"""Display final columns after cleaning."""

print(raw_data.columns)


# ---------------------------------------------------------
# SAVE CLEANED DATASET
# ---------------------------------------------------------

cleaned_data_path = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "customer_shopping_behavior_cleaned.csv"
)

raw_data.to_csv(
    cleaned_data_path,
    index=False
)

print("Cleaned dataset successfully saved!")


# ---------------------------------------------------------
# LOAD CLEANED DATA INTO SQL SERVER
# ---------------------------------------------------------

"""
Connect Python to SQL Server using SQLAlchemy and pyodbc.

Replace YOUR_SERVER_NAME with the appropriate SQL Server
instance when running the script locally.
"""

connection_string = (
    r"DRIVER={ODBC Driver 18 for SQL Server};"
    r"SERVER=YOUR_SERVER_NAME\SQLEXPRESS;"
    r"DATABASE=CustomerShoppingDB;"
    r"Trusted_Connection=yes;"
    r"TrustServerCertificate=yes;"
)


connection_url = (
    "mssql+pyodbc:///?odbc_connect="
    + quote_plus(connection_string)
)


engine = create_engine(connection_url)


raw_data.to_sql(
    "customer_shopping_behavior",
    con=engine,
    if_exists="replace",
    index=False
)


print("Data successfully sent to SQL Server!")
