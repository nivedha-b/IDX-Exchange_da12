import pandas as pd

# aggregate listing datasets
listing42 = pd.read_csv("data/CRMLSListing202402.csv")  # 2024    
listing43 = pd.read_csv("data/CRMLSListing202403.csv")
listing44 = pd.read_csv("data/CRMLSListing202404.csv")
listing45 = pd.read_csv("data/CRMLSListing202405.csv")
listing46 = pd.read_csv("data/CRMLSListing202406.csv")
listing47 = pd.read_csv("data/CRMLSListing202407.csv")
listing48 = pd.read_csv("data/CRMLSListing202408.csv")
listing49 = pd.read_csv("data/CRMLSListing202409.csv")
listing410 = pd.read_csv("data/CRMLSListing202410.csv")
listing411 = pd.read_csv("data/CRMLSListing202411.csv")
listing412 = pd.read_csv("data/CRMLSListing202412.csv")
listing51 = pd.read_csv("data/CRMLSListing202501.csv")    # 2025
listing52 = pd.read_csv("data/CRMLSListing202502.csv")
listing53 = pd.read_csv("data/CRMLSListing202503.csv")
listing54 = pd.read_csv("data/CRMLSListing202504.csv")
listing55 = pd.read_csv("data/CRMLSListing202505.csv")
listing56 = pd.read_csv("data/CRMLSListing202506.csv")
listing57 = pd.read_csv("data/CRMLSListing202507.csv")
listing58 = pd.read_csv("data/CRMLSListing202508.csv")
listing59 = pd.read_csv("data/CRMLSListing202509.csv")
listing510 = pd.read_csv("data/CRMLSListing202510.csv")
listing511 = pd.read_csv("data/CRMLSListing202511.csv")
listing512 = pd.read_csv("data/CRMLSListing202512.csv")
listing61 = pd.read_csv("data/CRMLSListing202601.csv")    # 2026
listing62 = pd.read_csv("data/CRMLSListing202602.csv")
listing63 = pd.read_csv("data/CRMLSListing202603.csv")

# verify row counts for residential properties                 (uncomment if needed to verify)
#print("42: " + str(listing42["PropertyType"].value_counts()))   #17490 residential rows 02/24
#print("43: " + str(listing43["PropertyType"].value_counts()))   #20501 residential rows 03/24
#print("44: " + str(listing44["PropertyType"].value_counts()))   #24025 residential rows 04/24
#print("45: " + str(listing45["PropertyType"].value_counts()))   #25447 residential rows 05/24
#print("46: " + str(listing46["PropertyType"].value_counts()))   #23310 residential rows 06/24
#print("47: " + str(listing47["PropertyType"].value_counts()))   #23019 residential rows 07/24
#print("48: " + str(listing48["PropertyType"].value_counts()))   #22215 residential rows 08/24
#print("49: " + str(listing49["PropertyType"].value_counts()))   #22257 residential rows 09/24
#print("410: " + str(listing410["PropertyType"].value_counts())) #21921 residential rows 10/24
#print("411: " + str(listing411["PropertyType"].value_counts())) #15108 residential rows 11/24
#print("412: " + str(listing412["PropertyType"].value_counts())) #10694 residential rows 12/24
#print("51: " + str(listing51["PropertyType"].value_counts()))   #22690 residential rows 01/25
#print("52: " + str(listing52["PropertyType"].value_counts()))   #21930 residential rows 02/25
#print("53: " + str(listing53["PropertyType"].value_counts()))   #25104 residential rows 03/25
#print("54: " + str(listing54["PropertyType"].value_counts()))   #26695 residential rows 04/25
#print("55: " + str(listing55["PropertyType"].value_counts()))   #26438 residential rows 05/25
#print("56: " + str(listing56["PropertyType"].value_counts()))   #17056 residential rows 06/25
#print("57: " + str(listing57["PropertyType"].value_counts()))   #17194 residential rows 07/25
#print("58: " + str(listing58["PropertyType"].value_counts()))   #15658 residential rows 08/25
#print("59: " + str(listing59["PropertyType"].value_counts()))   #16859 residential rows 09/25
#print("510: " + str(listing510["PropertyType"].value_counts())) #17186 residential rows 10/25
#print("511: " + str(listing511["PropertyType"].value_counts())) #12194 residential rows 11/25
#print("512: " + str(listing512["PropertyType"].value_counts())) #10516 residential rows 12/25
#print("61: " + str(listing61["PropertyType"].value_counts()))   #22108 residential rows 01/26
#print("62: " + str(listing62["PropertyType"].value_counts()))   #19997 residential rows 02/26
#print("63: " + str(listing63["PropertyType"].value_counts()))   #25564 residential rows 03/26

listing = pd.concat([listing42, listing43, listing44, listing45, listing46, listing47, listing48, listing49, listing410, listing411, listing412,
                     listing51, listing52, listing53, listing54, listing55, listing56,  listing57, listing58, listing59, listing510, listing511, listing512,
                     listing61, listing62, listing63])

print(listing["PropertyType"].value_counts())           # 523176 Residential rows after concatenation
#print(listing.head())

# filter listing dataset to only include residential properties
listing = listing[listing["PropertyType"] == "Residential"]
print(listing["PropertyType"].value_counts())           # 523176 Residential rows after filtering
#listing.to_csv("data/residential_listings.csv", index=False)  # save filtered listings dataset to CSV