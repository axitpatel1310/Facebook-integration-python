import requests
from datetime import datetime, timedelta, timezone

ACCESS_TOKEN = "EAAe1kMTkQbEBO5RZA8ilR9odPZBh0L4VoYVZAOmLCIZCNtyX4gK0pJfKX6DT8no9olM7Hb9PkIXIJW0f1J7Tb0hf3CXdOnLlhgfiuEHXvATloSdluRJsJpcqGoPlKxP5gCKkigy0lAYnzUvpopeKS4H5e29tuWjn1mco6mZAWyKynyRuBJPpoac1ZCYBdYxoIiVq5s1jKJ"
AD_ACCOUNT_ID = "1053657560033277"
CAMPAIGN_ID = "120222371064580243"

url = f"https://graph.facebook.com/v19.0/act_{AD_ACCOUNT_ID}/adsets"

start_time = (datetime.now(timezone.utc) + timedelta(minutes=10)).strftime('%Y-%m-%dT%H:%M:%S')

payload = {
    "name": "Test Ad Set",
    "campaign_id": CAMPAIGN_ID,
    "daily_budget": "8569",  # ₹85.69 or $1.00 (in cents)
    "start_time": start_time,
    "billing_event": "IMPRESSIONS",
    "optimization_goal": "REACH",
    "status": "PAUSED",
    "targeting": '{"geo_locations":{"countries":["IN"]}}',
    "bid_strategy": "LOWEST_COST_WITHOUT_CAP",  # Set bid strategy without a cap
    "access_token": ACCESS_TOKEN
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("✅ Ad Set created!")
    print(response.json())
else:
    print("❌ Error creating ad set")
    print(response.status_code, response.text)