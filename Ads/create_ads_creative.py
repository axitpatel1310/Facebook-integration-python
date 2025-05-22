import requests
ACCESS_TOKEN = "EAAe1kMTkQbEBO5RZA8ilR9odPZBh0L4VoYVZAOmLCIZCNtyX4gK0pJfKX6DT8no9olM7Hb9PkIXIJW0f1J7Tb0hf3CXdOnLlhgfiuEHXvATloSdluRJsJpcqGoPlKxP5gCKkigy0lAYnzUvpopeKS4H5e29tuWjn1mco6mZAWyKynyRuBJPpoac1ZCYBdYxoIiVq5s1jKJ"
AD_ACCOUNT_ID = "1053657560033277"
# Image Upload URL

image_url = f"https://graph.facebook.com/v19.0/act_{AD_ACCOUNT_ID}/adimages"

# Image payload (replace with your image path)
image_file = {'file': open('images.png', 'rb')}

# Request to upload image
response = requests.post(image_url, data={
    'access_token': ACCESS_TOKEN
}, files=image_file)

# Inspecting the response
if response.status_code == 200:
    image_data = response.json()
    print("✅ Image uploaded successfully!")
    print("Response:", image_data)  # Add this line to inspect the full response
else:
    print("❌ Error uploading image")
    print(response.status_code, response.text)
