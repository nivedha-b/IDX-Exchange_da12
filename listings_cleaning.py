import pandas as pd
pd.set_option('display.max_rows', None)

#-------------------------------------------
# WEEKS 4–5 – DATA CLEANING AND PREPARATION 
#-------------------------------------------


# load filtered sold dataset
listings = pd.read_csv("data/listings_with_mortgage_rates.csv", low_memory=False)
print(listings.columns)
print(len(listings.columns))

# Convert date fields to datetime format
date_fields = ["CloseDate", "PurchaseContractDate", "ContractStatusChangeDate", "ListingContractDate"]

for col in date_fields:
    listings[col] = pd.to_datetime(listings[col], errors='coerce')  # coerce handles invalid dates

print(listings.dtypes)
# Remove unnecessary or redundant columns
columns_to_drop = [
    "LotSizeAcres", "LotSizeArea",  # redudant bc we have LotSizeSquareFeet, LotSizeDimensions also is null
    "AttachedGarageYN",             # not informative since we have GarageSpaces and ParkingTotal
    "Levels",                        # redundant bc we have Stories
    "CloseDate.1", "PropertyType.1", "ListAgentFirstName.1", "DaysOnMarket.1", 
    "LivingArea.1", "Longitude.1", "Latitude.1", "ListPrice.1", "ListAgentLastName.1",
    "BuyerOfficeName.1", "UnparsedAddress.1"                   # we already have these
]
listings = listings.drop(columns=columns_to_drop)


# Handle missing values
# check missing values and ensure they were filtered properly during dataset validation
missing_pct = listings.isnull().mean() * 100
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
    listings[col] = pd.to_numeric(listings[col], errors='coerce')  # coerce handles non-numeric values
    print(col, listings[col].dtype)                                  # check current data types

# Remove or flag invalid numeric values: ClosePrice <= 0, LivingArea <= 0, DaysOnMarket < 0, negative Bedrooms or Bathrooms

print("\nNull count in numeric fields before handling invalid values:\n")
print(listings[numeric_fields].isnull().sum())   # check how many nulls exist in numeric fields after coercion

listings[["ClosePrice", "LivingArea", "ListPrice", "LotSizeSquareFeet", "AssociationFee"]] = listings[["ClosePrice", "LivingArea", "ListPrice", "LotSizeSquareFeet", "AssociationFee"]].mask(       # these columns <= 0 become null / nan
    listings[["ClosePrice", "LivingArea", "ListPrice", "LotSizeSquareFeet", "AssociationFee"]] <= 0
)   

listings[["DaysOnMarket", "BedroomsTotal", "BathroomsTotalInteger", "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms", "PostalCode", "rate_30yr_fixed", "YearBuilt"]] = listings[      # these columns < 0 become null / nan
    ["DaysOnMarket", "BedroomsTotal", "BathroomsTotalInteger", "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms", "PostalCode", "rate_30yr_fixed", "YearBuilt"]].mask(
    listings[["DaysOnMarket", "BedroomsTotal", "BathroomsTotalInteger", "ParkingTotal", "GarageSpaces", "Stories", "MainLevelBedrooms", "PostalCode", "rate_30yr_fixed", "YearBuilt"]] < 0
)

print("\nNull count in numeric fields after handling invalid values:\n")
print(listings[numeric_fields].isnull().sum())    # check how many nulls exist in numeric fields after handling invalid values


# Date Consistency Checks

print("\nChecking and flagging date inconsistencies...\n")
date_cols = ["CloseDate", "PurchaseContractDate", "ListingContractDate"]

# ListingContractDate should precede CloseDate, true if violated
listings["listing_after_close_flag"] = (
    listings["ListingContractDate"] > listings["CloseDate"]
)

# PurchaseContractDate should precede CloseDate, true if violated
listings["purchase_after_close_flag"] = (
    listings["PurchaseContractDate"] > listings["CloseDate"]
)

# ListingContractDate should precede PurchaseContractDate, true if violated
listings["negative_timeline_flag"] = (
    listings["ListingContractDate"] > listings["PurchaseContractDate"]
)

print("\nListing after close flags:", listings["listing_after_close_flag"].sum())    # check how many rows have listing after close
print("Purchase after close flags:", listings["purchase_after_close_flag"].sum())    # check how many rows have purchase after close
print("Negative timeline flags:", listings["negative_timeline_flag"].sum())    # check how many rows have negative timeline


# Geographic data checks

print("\nChecking and flagging geographic data inconsistencies...\n")
listings["missing_coords_flag"] = (                                     # flags true if longitude or latitude is null
    listings["Latitude"].isnull() | listings["Longitude"].isnull()  
)

listings["zero_coords_flag"] = (                                        # flags true if longitude or latitude is zero (invalid sentinel null values)
    (listings["Latitude"] == 0) | (listings["Longitude"] == 0)
)

listings["incorrect_longitude_flag"] = (                                # flags true if longitude is postive, since California is negative
    (listings["Longitude"] > 0)
)

listings["out_of_bounds_flag"] = (                                      # flags longitudes or latitudes that are not within California bounds
    (listings["Longitude"] < -125) | (listings["Longitude"] > -114) |
    (listings["Latitude"] < 32) | (listings["Latitude"] > 42)
)

print("\nCleaned data columns:\n")
print(listings.columns)    # check summary stats

# Save cleaned dataset as CSV
print("\nSaving cleaned dataset to CSV...\n")
listings.to_csv("data/listings_clean.csv", index=False)
