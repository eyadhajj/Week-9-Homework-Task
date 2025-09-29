import pandas as pd
import geopandas as gpd

# Load the shapefile (replace with your path)
gdf = gpd.read_file("ne_10m_geography_regions_points/ne_10m_geography_regions_points.shp")

# Export to GeoJSON
gdf.to_file("ne_10m_geography_regions_points.json", driver="GeoJSON")



file_path = "IHME-GBD_2021_DATA-6b23a41d-1.csv"
df = pd.read_csv(file_path)

# Get all rows where location_name == "Côte d'Ivoire"
ivory_rows = df[df["location_name"] == "Côte d'Ivoire"]

# Duplicate those rows with alternate names
alt_rows = ivory_rows.copy()
alt_rows["location_name"] = "Côte d’Ivoire"   # curly apostrophe

alt_rows2 = ivory_rows.copy()
alt_rows2["location_name"] = "Ivory Coast"   # English alias



# ----------------------------
# Laos aliases
# ----------------------------
# Select all Laos rows in the CSV
laos_rows = df[df["location_name"] == "Lao People's Democratic Republic"]

# Duplicate them with the alias 'Laos'
laos_alias = laos_rows.copy()
laos_alias["location_name"] = "Laos"

# Append them to the dataframe
df_updated = pd.concat([df, alt_rows, alt_rows2], ignore_index=True)

# Save to a new CSV
output_path = "IHME-GBD_2021_DATA-6b23a41d-1.csv"
df_updated.to_csv(output_path, index=False)
output_path
