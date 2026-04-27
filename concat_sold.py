import pandas as pd

# aggregate sold datasets
sold41 = pd.read_csv("data/CRMLSSold202401.csv")    # 2024
sold42 = pd.read_csv("data/CRMLSSold202402.csv")
sold43 = pd.read_csv("data/CRMLSSold202403.csv")
sold44 = pd.read_csv("data/CRMLSSold202404.csv",
                    dtype={
                        "WaterfrontYN": "string",
                        "ElementarySchool": "string",
                        "BuilderName": "string",
                        "CoBuyerAgentFirstName": "string",
                        "PostalCode": "string"
                    }
                )
sold45 = pd.read_csv("data/CRMLSSold202405.csv")
sold46 = pd.read_csv("data/CRMLSSold202406.csv")
sold47 = pd.read_csv("data/CRMLSSold202407.csv")
sold48 = pd.read_csv("data/CRMLSSold202408.csv")
sold49 = pd.read_csv("data/CRMLSSold202409.csv")
sold410 = pd.read_csv("data/CRMLSSold202410.csv")
sold411 = pd.read_csv("data/CRMLSSold202411.csv")
sold412 = pd.read_csv("data/CRMLSSold202412.csv")
sold51 = pd.read_csv("data/CRMLSSold202501.csv")    # 2025
sold52 = pd.read_csv("data/CRMLSSold202502.csv")
sold53 = pd.read_csv("data/CRMLSSold202503.csv")
sold54 = pd.read_csv("data/CRMLSSold202504.csv")
sold55 = pd.read_csv("data/CRMLSSold202505.csv")
sold56 = pd.read_csv("data/CRMLSSold202506.csv",
                     dtype={
                        "WaterfrontYN": "string",
                        "ElementarySchool": "string",
                        "BuilderName": "string",
                        "CoBuyerAgentFirstName": "string",
                        "PostalCode": "string"
                    }
                )
sold57 = pd.read_csv("data/CRMLSSold202507.csv")
sold58 = pd.read_csv("data/CRMLSSold202508.csv")
sold59 = pd.read_csv("data/CRMLSSold202509.csv")
sold510 = pd.read_csv("data/CRMLSSold202510.csv")
sold511 = pd.read_csv("data/CRMLSSold202511.csv")
sold512 = pd.read_csv("data/CRMLSSold202512.csv")
sold61 = pd.read_csv("data/CRMLSSold202601.csv",    # 2026
                     dtype={
                        "WaterfrontYN": "string",
                        "ElementarySchool": "string",
                        "BuilderName": "string",
                        "CoBuyerAgentFirstName": "string",
                        "PostalCode": "string"
                    }
                )    
sold62 = pd.read_csv("data/CRMLSSold202602.csv")
sold63 = pd.read_csv("data/CRMLSSold202603.csv")

# verify row counts for residential properties              (uncomment if needed to verify)
#print("41: " + str(sold41["PropertyType"].value_counts()))  # 11203 residential rows 01/24
#print("42: " + str(sold42["PropertyType"].value_counts()))  # 13063 residential rows 02/24
#print("43: " + str(sold43["PropertyType"].value_counts()))  # 20501 residential rows 03/24
#print("44: " + str(sold44["PropertyType"].value_counts()))  # 24025 residential rows 04/24
#print("45: " + str(sold45["PropertyType"].value_counts()))  # 25447 residential rows 05/24  
#print("46: " + str(sold46["PropertyType"].value_counts()))  # 23310 residential rows 06/24
#print("47: " + str(sold47["PropertyType"].value_counts()))  # 23019 residential rows 07/24
#print("48: " + str(sold48["PropertyType"].value_counts()))  # 22215 residential rows 08/24
#print("49: " + str(sold49["PropertyType"].value_counts()))  # 22257 residential rows 09/24
#print("410: " + str(sold410["PropertyType"].value_counts())) # 21921 residential rows 10/24
#print("411: " + str(sold411["PropertyType"].value_counts())) # 15108 residential rows 11/24
#print("412: " + str(sold412["PropertyType"].value_counts())) # 10694 residential rows 12/24 
#print("51: " + str(sold51["PropertyType"].value_counts()))  # 22690 residential rows 01/25
#print("52: " + str(sold52["PropertyType"].value_counts()))  # 21930 residential rows 02/25
#print("53: " + str(sold53["PropertyType"].value_counts()))  # 25104 residential rows 03/25
#print("54: " + str(sold54["PropertyType"].value_counts()))  # 26695 residential rows 04/25
#print("55: " + str(sold55["PropertyType"].value_counts()))  # 26438 residential rows 05/25
#print("56: " + str(sold56["PropertyType"].value_counts()))  # 17056 residential rows 06/25
#print("57: " + str(sold57["PropertyType"].value_counts()))  # 17194 residential rows 07/25
#print("58: " + str(sold58["PropertyType"].value_counts()))  # 15658 residential rows 08/25
#print("59: " + str(sold59["PropertyType"].value_counts()))  # 16859 residential rows 09/25
#print("510: " + str(sold510["PropertyType"].value_counts())) # 17186 residential rows 10/25
#print("511: " + str(sold511["PropertyType"].value_counts())) # 12194 residential rows 11/25
#print("512: " + str(sold512["PropertyType"].value_counts())) # 10516 residential rows 12/25
#print("61: " + str(sold61["PropertyType"].value_counts()))  # 22108 residential rows 01/26
#print("62: " + str(sold62["PropertyType"].value_counts()))  # 19997 residential rows 02/26 
#print("63: " + str(sold63["PropertyType"].value_counts()))  # 25564 residential rows 03/26 



sold = pd.concat([sold41, sold42, sold43, sold44, sold45, sold46, sold47, sold48, sold49, sold410, sold411, sold412,
                  sold51, sold52, sold53, sold54, sold55, sold56, sold57, sold58, sold59, sold510, sold511, sold512,
                  sold61, sold62, sold63])

print(sold["PropertyType"].value_counts())          # 398011 Residential rows after concatenation

# filter sold dataset to only include residential properties
sold = sold[sold["PropertyType"] == "Residential"]
print(sold["PropertyType"].value_counts())          # 398011 Residential rows after filtering
#sold.to_csv("data/residential_sold.csv", index=False) # save filtered sold dataset to CSV