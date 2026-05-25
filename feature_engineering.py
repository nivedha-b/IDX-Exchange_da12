import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option("display.max_columns", None)

#-------------------------------------------------
# WEEK 6 - FEATURE ENGINEERING AND MARKET METRICS
#-------------------------------------------------

sold = pd.read_csv("data/sold_clean.csv", low_memory=False)
listings = pd.read_csv("data/listings_clean.csv", low_memory=False)

# METRIC CALCULATIONS

# make sure dates are in datetime format
date_fields = ["CloseDate", "PurchaseContractDate", "ContractStatusChangeDate", "ListingContractDate"]

for col in date_fields:
    sold[col] = pd.to_datetime(sold[col], errors='coerce')  # coerce handles invalid dates

# PriceRatio
sold["PriceRatio"] = sold["ClosePrice"] / sold["OriginalListPrice"]     # Measures negotiation strength

# PricePerSqFt
sold["PPSF"] = sold["ClosePrice"] / sold["LivingArea"]          # Normalizes price across sizes

# DaysonMarket
# Time-to-sell indicator --> uses raw field

# Year / Month / YrMo                                           Derived from CloseDate, enables time-series analysis
sold["Year"] = sold["CloseDate"].dt.year
sold["Month"] = sold["CloseDate"].dt.month
sold["YrMo"] = sold["CloseDate"].dt.to_period("M")

# Close to Original List Ratio
sold["CloseOriginalRatio"] = sold["ClosePrice"] / sold["OriginalListPrice"]     # Captures full price reduction history

# Listing to Contract Days
sold["ListingtoContractDays"] = sold["PurchaseContractDate"].dt.day - sold["ListingContractDate"].dt.day   # Measures time from listing to accepted offer

# Contract to Close Days
sold["ContracttoCloseDays"] = sold["CloseDate"].dt.day - sold["PurchaseContractDate"].dt.day  # Escrow and closing period duration


# SEGMENT ANALYSIS

# PropertyType and PropertySubType
print("\nGrouping by Property SubType...\n")
property_summary = sold.groupby("PropertySubType").agg({
    "PriceRatio": ["mean", "median", "min", "max"],
    "PPSF": ["mean", "median", "min", "max"],
    "CloseOriginalRatio": ["mean", "median", "min", "max"],
    "ListingtoContractDays": ["mean", "median", "min", "max"],
    "ContracttoCloseDays": ["mean", "median", "min", "max"]
})
print(property_summary.head)
property_summary.to_csv("out/property_summary.csv", index=False)

# CountyOrParish and MLSAreaMajor
print("\nGrouping by County/Parish...\n")
county_summary = sold.groupby("CountyOrParish").agg({
    "PriceRatio": ["mean", "median", "min", "max"],
    "PPSF": ["mean", "median", "min", "max"],
    "CloseOriginalRatio": ["mean", "median", "min", "max"],
    "ListingtoContractDays": ["mean", "median", "min", "max"],
    "ContracttoCloseDays": ["mean", "median", "min", "max"]
})
print(county_summary.head())
county_summary.to_csv("out/county_summary.csv", index=False)


print("\nGrouping by MLS Area...\n")
mls_area_summary = sold.groupby("MLSAreaMajor").agg({
    "PriceRatio": ["mean", "median", "min", "max"],
    "PPSF": ["mean", "median", "min", "max"],
    "CloseOriginalRatio": ["mean", "median", "min", "max"],
    "ListingtoContractDays": ["mean", "median", "min", "max"],
    "ContracttoCloseDays": ["mean", "median", "min", "max"]
})
print(mls_area_summary.head())
mls_area_summary.to_csv("out/mls_area_summary.csv", index=False)


# ListOfficeName and BuyerOfficeName (competitive intelligence)
print("\nGrouping by List Office...\n")
list_office_summary = sold.groupby("ListOfficeName").agg({
    "PriceRatio": ["mean", "median", "min", "max"],
    "PPSF": ["mean", "median", "min", "max"],
    "CloseOriginalRatio": ["mean", "median", "min", "max"],
    "ListingtoContractDays": ["mean", "median", "min", "max"],
    "ContracttoCloseDays": ["mean", "median", "min", "max"]
})
print(list_office_summary.head())
list_office_summary.to_csv("out/list_office_summary.csv", index=False)

print("\nGrouping by Buyer Office...\n")
buyer_office_summary = sold.groupby("BuyerOfficeName").agg({
    "PriceRatio": ["mean", "median", "min", "max"],
    "PPSF": ["mean", "median", "min", "max"],
    "CloseOriginalRatio": ["mean", "median", "min", "max"],
    "ListingtoContractDays": ["mean", "median", "min", "max"],
    "ContracttoCloseDays": ["mean", "median", "min", "max"]
})
print(buyer_office_summary.head())
buyer_office_summary.to_csv("out/buyer_office_summary.csv", index=False)



