import requests

ACCESS_TOKEN = "EAAe1kMTkQbEBO5RZA8ilR9odPZBh0L4VoYVZAOmLCIZCNtyX4gK0pJfKX6DT8no9olM7Hb9PkIXIJW0f1J7Tb0hf3CXdOnLlhgfiuEHXvATloSdluRJsJpcqGoPlKxP5gCKkigy0lAYnzUvpopeKS4H5e29tuWjn1mco6mZAWyKynyRuBJPpoac1ZCYBdYxoIiVq5s1jKJ"
AD_ACCOUNT_ID = "1053657560033277"

url = f"https://graph.facebook.com/v19.0/act_{AD_ACCOUNT_ID}/campaigns"

payload = {
    "name": "Test Campaign",
    "objective": "OUTCOME_LEADS",
    "status": "PAUSED",
    "special_ad_categories": "[]",
    "access_token": ACCESS_TOKEN
}

response = requests.post(url, data=payload)

if response.status_code == 200:
    print("Campaign created!")
    print(response.json())
else:
    print("Error creating campaign")
    print(response.status_code, response.text)
