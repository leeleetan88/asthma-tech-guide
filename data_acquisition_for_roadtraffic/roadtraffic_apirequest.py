import requests
import json

# API endpoint
url = "https://datamall2.mytransport.sg/ltaodataservice/TrafficFlow"

# Your API key from LTA DataMall
headers = {
    'AccountKey': '',  # Replace with your actual API key
    'accept': 'application/json'
}

# Send the request
response = requests.get(url, headers=headers)

# Check the status code and content of the response
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Try to parse the JSON if the response is OK
if response.status_code == 200:
    try:
        traffic_data = response.json()
        # Save the traffic data link to a file
        with open('traffic_data_link.json', 'w') as outfile:
            json.dump(traffic_data, outfile)
        print("Data fetched and saved successfully.")
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    print("Failed to fetch data. Check API key or URL.")




