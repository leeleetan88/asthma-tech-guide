import json
import re

# Load the GeoJSON file
with open('MasterPlan2019LandUselayer.geojson', 'r') as f:
    geojson_data = json.load(f)

# Function to filter only 'BUSINESS 1' or 'BUSINESS 2' in the 'Description' field
def filter_business_features(feature):
    description = feature['properties'].get('Description', '')

    # Look for exact matches for 'BUSINESS 1' or 'BUSINESS 2' or BUSINESS 1 - WHITE or BUSINESS 2 - WHITE using word boundaries
    match = re.search(r'\bBUSINESS 1\b|\bBUSINESS 2\b|\bBUSINESS 1 - WHITE\b|\bBUSINESS 2 - WHITE\b', description)

    # If a match is found, return True to include the feature, otherwise False
    return match is not None

# Filter the features where the 'Description' contains 'BUSINESS 1' or 'BUSINESS 2' or BUSINESS 1 - WHITE or BUSINESS 2 - WHITE
filtered_features = [feature for feature in geojson_data['features'] if filter_business_features(feature)]

# Create the filtered GeoJSON object
filtered_geojson = {
    "type": "FeatureCollection",
    "crs": geojson_data.get("crs", None),
    "features": filtered_features
}

# (Optional) Save the filtered GeoJSON to a new file
with open('filtered_data.geojson', 'w') as f:
    json.dump(filtered_geojson, f, indent=2)