import requests

ACCESS_TOKEN = "EAAe1kMTkQbEBO5RZA8ilR9odPZBh0L4VoYVZAOmLCIZCNtyX4gK0pJfKX6DT8no9olM7Hb9PkIXIJW0f1J7Tb0hf3CXdOnLlhgfiuEHXvATloSdluRJsJpcqGoPlKxP5gCKkigy0lAYnzUvpopeKS4H5e29tuWjn1mco6mZAWyKynyRuBJPpoac1ZCYBdYxoIiVq5s1jKJ"
AD_ACCOUNT_ID = "1053657560033277"

url = f"https://graph.facebook.com/v19.0/act_{AD_ACCOUNT_ID}/campaigns"
params = {
    "access_token": ACCESS_TOKEN,
    "fields": "id,name,status,effective_status"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    campaigns = response.json().get("data", [])
    for campaign in campaigns:
        print(f"ID: {campaign['id']} | Name: {campaign['name']} | Status: {campaign['status']}")
else:
    print("Error:", response.status_code, response.text)
print(response.json())
