import pandas as pd

file_path = "IHME-GBD_2021_DATA-6b23a41d-1.csv"
df = pd.read_csv(file_path)

# Get all rows where location_name == "Côte d'Ivoire"
ivory_rows = df[df["location_name"] == "Côte d'Ivoire"]

# Duplicate those rows with alternate names
alt_rows = ivory_rows.copy()
alt_rows["location_name"] = "Côte d’Ivoire"   # curly apostrophe

alt_rows2 = ivory_rows.copy()
alt_rows2["location_name"] = "Ivory Coast"   # English alias

# Append them to the dataframe
df_updated = pd.concat([df, alt_rows, alt_rows2], ignore_index=True)

# Save to a new CSV
output_path = "IHME-GBD_2021_DATA-6b23a41d-1.csv"
df_updated.to_csv(output_path, index=False)
output_path
