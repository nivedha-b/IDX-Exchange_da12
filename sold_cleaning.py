import pandas as pd
pd.set_option('display.max_rows', None)

#-------------------------------------------
# WEEKS 4–5 – DATA CLEANING AND PREPARATION 
#-------------------------------------------


# load filtered sold dataset
sold = pd.read_csv("data/sold_with_mortgage_rates.csv", low_memory=False)
print(sold.columns)
print(len(sold.columns))

# Convert date fields to datetime format
date_fields = ["CloseDate", "PurchaseContractDate", "ContractStatusChangeDate", "ListingContractDate"]

for col in date_fields:
    sold[col] = pd.to_datetime(sold[col], errors='coerce')  # coerce handles invalid dates


# Remove unnecessary or redundant columns
columns_to_drop = [
    "LotSizeAcres", "LotSizeArea",  # redudant bc we have LotSizeSquareFeet, LotSizeDimensions also is null
    "AttachedGarageYN",             # not informative since we have GarageSpaces and ParkingTotal
    "Levels"                        # redundant bc we have Stories
]
sold = sold.drop(columns=columns_to_drop)


# Handle missing values
# check missing values and ensure they were filtered properly during dataset validation
missing_pct = sold.isnull().mean() * 100
print(missing_pct.sort_values(ascending=False))


# Ensure numeric fields are properly typed

print("\nEnsuring numeric fields are properly typed...\n")
numeric_fields = [                                          # some of these fields already defined in analysis script
    "ClosePrice", "ListPrice", "OriginalListPrice",     
    "LivingArea", "LotSizeSquareFeet",
    "BedroomsTotal", "BathroomsTotalInteger",
    "DaysOnMarket", "YearBuilt",
    "Latitude", "Longitude",
    "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms",
    "PostalCode",
    "AssociationFee", "AssociationFeeFrequency",
    "rate_30yr_fixed"
]

for col in numeric_fields:
    sold[col] = pd.to_numeric(sold[col], errors='coerce')  # coerce handles non-numeric values
    print(col, sold[col].dtype)                                  # check current data types

# Remove or flag invalid numeric values: ClosePrice <= 0, LivingArea <= 0, DaysOnMarket < 0, negative Bedrooms or Bathrooms

print("\nNull count in numeric fields before handling invalid values:\n")
print(sold[numeric_fields].isnull().sum())   # check how many nulls exist in numeric fields after coercion

sold[["ClosePrice", "LivingArea", "ListPrice", "LotSizeSquareFeet", "AssociationFee"]] = sold[["ClosePrice", "LivingArea", "ListPrice", "LotSizeSquareFeet", "AssociationFee"]].mask(       # these columns <= 0 become null / nan
    sold[["ClosePrice", "LivingArea", "ListPrice", "LotSizeSquareFeet", "AssociationFee"]] <= 0
)   

sold[["DaysOnMarket", "BedroomsTotal", "BathroomsTotalInteger", "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms", "PostalCode", "rate_30yr_fixed", "YearBuilt"]] = sold[      # these columns < 0 become null / nan
    ["DaysOnMarket", "BedroomsTotal", "BathroomsTotalInteger", "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms", "PostalCode", "rate_30yr_fixed", "YearBuilt"]].mask(
    sold[["DaysOnMarket", "BedroomsTotal", "BathroomsTotalInteger", "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms", "PostalCode", "rate_30yr_fixed", "YearBuilt"]] < 0
)

print("\nNull count in numeric fields after handling invalid values:\n")
print(sold[numeric_fields].isnull().sum())    # check how many nulls exist in numeric fields after handling invalid values


# Date Consistency Checks

print("\nChecking and flagging date inconsistencies...\n")
date_cols = ["CloseDate", "PurchaseContractDate", "ListingContractDate"]

# ListingContractDate should precede CloseDate, true if violated
sold["listing_after_close_flag"] = (
    sold["ListingContractDate"] > sold["CloseDate"]
)

# PurchaseContractDate should precede CloseDate, true if violated
sold["purchase_after_close_flag"] = (
    sold["PurchaseContractDate"] > sold["CloseDate"]
)

# ListingContractDate should precede PurchaseContractDate, true if violated
sold["negative_timeline_flag"] = (
    sold["ListingContractDate"] > sold["PurchaseContractDate"]
)

print("\nListing after close flags:", sold["listing_after_close_flag"].sum())    # check how many rows have listing after close
print("Purchase after close flags:", sold["purchase_after_close_flag"].sum())    # check how many rows have purchase after close
print("Negative timeline flags:", sold["negative_timeline_flag"].sum())    # check how many rows have negative timeline


# Geographic data checks

print("\nChecking and flagging geographic data inconsistencies...\n")
sold["missing_coords_flag"] = (                                     # flags true if longitude or latitude is null
    sold["Latitude"].isnull() | sold["Longitude"].isnull()  
)

sold["zero_coords_flag"] = (                                        # flags true if longitude or latitude is zero (invalid sentinel null values)
    (sold["Latitude"] == 0) | (sold["Longitude"] == 0)
)

sold["incorrect_longitude_flag"] = (                                # flags true if longitude is postive, since California is negative
    (sold["Longitude"] > 0)
)

sold["out_of_bounds_flag"] = (                                      # flags longitudes or latitudes that are not within California bounds
    (sold["Longitude"] < -125) | (sold["Longitude"] > -114) |
    (sold["Latitude"] < 32) | (sold["Latitude"] > 42)
)

print("\nCleaned data columns:\n")
print(sold.columns)    # check summary stats

# Save cleaned dataset as CSV
print("\nSaving cleaned dataset to CSV...\n")
sold.to_csv("data/sold_clean.csv", index=False)