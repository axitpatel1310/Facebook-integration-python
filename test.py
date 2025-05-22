import requests
app_id = '2169958220186033'
app_secret = 'b2c008caa0b3984d64d056eb3443a30f'
short_lived_token = 'EAAe1kMTkQbEBO6Nb8L8C1bDmygC3jnPjdEMsZBCDiJ8okhlkk8amyFDLgnZCR2cvzkFFfQwNFuTQCc4Fst3InhpZCJzmdXkz3PBPpZCV50gyszZBfKrbTZCyQdJjwB9LoTo86rhXZCJXVZCqWMFzxZBf3HYZBFsCVPld1ZAerOHD0ZAeyYklojtN8nBLbtfyCOlp3DUOyVjLjeOZAFwiOM8TBOCp0G9KIYwZDZD'
url = f"https://graph.facebook.com/v19.0/oauth/access_token"
params = {
    'grant_type': 'fb_exchange_token',
    'client_id': app_id,
    'client_secret': app_secret,
    'fb_exchange_token': short_lived_token
}
response = requests.get(url, params=params)
if response.status_code == 200:
    new_token = response.json()['access_token']
    print("New Access Token:", new_token)
else:
    print("Error:", response.status_code, response.text)
