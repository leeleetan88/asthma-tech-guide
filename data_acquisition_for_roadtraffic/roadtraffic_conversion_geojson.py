import json

# Load the traffic flow JSON data
with open('roadtraffic_data.json', 'r') as f:
    data = json.load(f)

# Extract the 'Value' key, which contains the actual traffic data
entries = data["Value"]

# List to store GeoJSON features-
features = []

# Loop through each entry in 'Value' list
for entry in entries:
    try:
        # Extract coordinates for the LineString (start and end points of the road segment)
        coordinates = [
            [float(entry["StartLon"]), float(entry["StartLat"])],  # Start point
            [float(entry["EndLon"]), float(entry["EndLat"])]       # End point
        ]

        # Create a GeoJSON feature for the road segment
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coordinates
            },
            "properties": {
                "roadName": entry["RoadName"],
                "volume": entry["Volume"],
                "date": entry["Date"],
                "hourOfDate": entry["HourOfDate"],
                "roadCategory": entry["RoadCat"]
            }
        }

        # Add feature to the list
        features.append(feature)

    except KeyError as e:
        print(f"Skipping entry due to missing field: {e}")

# Create a GeoJSON structure
geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

# Save the GeoJSON data to a file
with open('roadtrafficdata.geojson', 'w') as f:
    json.dump(geojson_data, f)

print("GeoJSON file saved successfully.")
