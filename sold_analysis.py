import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', None)


# load filtered sold dataset
sold = pd.read_csv("data/residential_sold.csv", low_memory=False)  


## DATASET UNDERSTANDING

# inspect structure
print("Number of rows and columns in sold dataset: ", sold.shape)   # print num rows and columns
print(sold.info())
print(sold.columns)                                                 # print column names
print(sold.head())                                                  # print first 5 rows 
print(sold.dtypes)                                                  # review column data types

# identify high missing values
print("\nIdentify high missing values\n")
print(sold.isnull().sum())                                              # print count of missing values per column

# Check property categories
print("\nCheck property categories (ensure all residential)\n")
print(sold['PropertyType'].unique())

# filter metadata
metadata_cols = [
    "ListingId", "ListingKey", "ListingKeyNumeric",
    "ListAgentFirstName", "ListAgentLastName", "ListAgentFullName",
    "ListAgentEmail", "ListAgentAOR",
    "BuyerAgentFirstName", "BuyerAgentLastName", "BuyerAgentMlsId", "BuyerAgentAOR",
    "CoBuyerAgentFirstName", "CoListAgentFirstName", "CoListAgentLastName",
    "ListOfficeName", "BuyerOfficeName", "CoListOfficeName", "BuyerOfficeAOR",
    "BuilderName",
    "OriginatingSystemName", "OriginatingSystemSubName",
    "BusinessType",
    "UnparsedAddress", "StreetNumberNumeric",
    "ContractStatusChangeDate", "PurchaseContractDate",
    "ElementarySchool", "MiddleOrJuniorSchool", "HighSchool",
    "ElementarySchoolDistrict", "MiddleOrJuniorSchoolDistrict", "HighSchoolDistrict",
    "BuyerAgencyCompensation", "BuyerAgencyCompensationType",
    "latfilled", "lonfilled"
]

market_data = sold.drop(columns=metadata_cols, errors="ignore")
metadata = sold[metadata_cols]

soldFiltered = sold.drop(columns=metadata_cols, errors="ignore")    # create copy of sold dataset to filter missing values without affecting original dataset

## MISSING VALUE ANALYSIS
print("\nMissing Value Analysis\n")
missing_count = soldFiltered.isnull().sum()             # calculate missing counts and percentages per column
missing_pct = soldFiltered.isnull().mean() * 100        

missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing %": missing_pct
}).sort_values(by="Missing %", ascending=False)

print(missing_summary)


print("\nColumns with >90% missing values\n")
missing = missing_summary[missing_summary["Missing %"] > 90]     # flag columns with >90% missing values
print(missing)

market_data = market_data.drop(columns=missing.index)                    # drop columns with >90% missing values

# Validate completeness
print("\nDataset after filtering missing columns\n")
print(market_data.info())

# Save filtered dataset as CSV
soldFiltered.to_csv("data/sold_filtered.csv", index=False)


## NUMERIC DISTRIBUTION REVIEW
numeric_fields = [
    "ClosePrice", "ListPrice", "OriginalListPrice",
    "LivingArea", "LotSizeAcres",
    "BedroomsTotal", "BathroomsTotalInteger",
    "DaysOnMarket", "YearBuilt"
]

#for col in numeric_fields:
#    plt.figure()
#    if(col == "ClosePrice" or col == "ListPrice" or col == "OriginalListPrice"):
#        np.log1p(soldFiltered[col]).hist(bins=50)      # log scale histogram for price columns
#    else:
#        soldFiltered[col].hist(bins=50)
#    plt.title(f"{col} Distribution")
#    plt.xlabel(col)
#    plt.ylabel("Frequency")
#    plt.show()


cols = ["ClosePrice", "LivingArea", "DaysOnMarket"]
summary = soldFiltered[cols].describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
print(summary)


