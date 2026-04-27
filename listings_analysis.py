import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', None)


# load filtered sold dataset
listings = pd.read_csv("data/residential_listings.csv", low_memory=False)  


## DATASET UNDERSTANDING

# inspect structure
print("Number of rows and columns in listings dataset: ", listings.shape)   # print num rows and columns
print(listings.info())
print(listings.columns)                                                 # print column names
print(listings.head())                                                  # print first 5 rows 
print(listings.dtypes)                                                  # review column data types

# identify high missing values
print("\nIdentify high missing values\n")
print(listings.isnull().sum())                                              # print count of missing values per column

# Check property categories
print("\nCheck property categories (ensure all residential)\n")
print(listings['PropertyType'].unique())

# filter metadata
metadata_cols = [
    "ListingId", "ListingKey", "ListingKeyNumeric",
    "ListAgentFirstName", "ListAgentLastName", "ListAgentFullName",
    "ListAgentFirstName.1", "ListAgentLastName.1",
    "BuyerAgentFirstName", "BuyerAgentLastName", "BuyerAgentMlsId", "BuyerOfficeAOR",
    "CoBuyerAgentFirstName", "CoListAgentFirstName", "CoListAgentLastName",
    "ListOfficeName", "BuyerOfficeName", "BuyerOfficeName.1", "CoListOfficeName",
    "BuilderName",
    "BusinessType",
    "MlsStatus",
    "UnparsedAddress", "UnparsedAddress.1", "StreetNumberNumeric",
    "ElementarySchool", "MiddleOrJuniorSchool", "HighSchool",
    "ElementarySchoolDistrict", "MiddleOrJuniorSchoolDistrict", "HighSchoolDistrict",
    "BuyerAgencyCompensation", "BuyerAgencyCompensationType",
    "PropertyType.1", "DaysOnMarket.1", "LivingArea.1", "Longitude.1", "Latitude.1", "ListPrice.1"
]

market_data = listings.drop(columns=metadata_cols, errors="ignore")
metadata = listings[metadata_cols]

listingsFiltered = listings.drop(columns=metadata_cols, errors="ignore")    # create copy of listings dataset to filter missing values without affecting original dataset

## MISSING VALUE ANALYSIS
print("\nMissing Value Analysis\n")
missing_count = listingsFiltered.isnull().sum()             # calculate missing counts and percentages per column
missing_pct = listingsFiltered.isnull().mean() * 100        

missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing %": missing_pct
}).sort_values(by="Missing %", ascending=False)

print(missing_summary)


print("\nColumns with >85% missing values\n")
missing = missing_summary[missing_summary["Missing %"] > 85]     # flag columns with >85% missing values
print(missing)

listingsFiltered = listingsFiltered.drop(columns=missing.index)                    # drop columns with >85% missing values

# Validate completeness
print("\nDataset after filtering missing columns\n")
print(listingsFiltered.info())

# Save filtered dataset as CSV
listingsFiltered.to_csv("data/listings_filtered.csv", index=False)


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
#        np.log1p(listingsFiltered[col]).hist(bins=50)      # log scale histogram for price columns
#    else:
#        listingsFiltered[col].hist(bins=50)
#    plt.title(f"{col} Distribution")
#    plt.xlabel(col)
#    plt.ylabel("Frequency")
#    plt.show()


cols = ["ClosePrice", "LivingArea", "DaysOnMarket"]
summary = listingsFiltered[cols].describe(percentiles=[0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99])
print(summary)