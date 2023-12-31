import requests

api_key = "YOUR_API_KEY"
target_ip = "TARGET_IP_ADDRESS"

url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={target_ip}"
response = requests.get(url)
data = response.json()

print("IP:", data["ip"])
print("Country:", data["country_name"])
print("Region:", data["state_prov"])
print("City:", data["city"])
print("Latitude:", data["latitude"])
print("Longitude:", data["longitude"])
