import requests

AD_ACCOUNT_ID = "1303228834039841"
ADSET_ID = "120222371509140243"
image_hash = "7e4e9f070d6e2c29320da95644110ff6"
PAGE_ID = "122153613344557126"

ACCESS_TOKEN = "EAAe1kMTkQbEBO4ZBDK84A4f2DvAZAtHPDqX7FM6PXcKvsZAWZB6871Y3nEQ4Sdmp0QX4TNnu8dxZCehjl0L9gxkQSfiqep7D5k1whE5tqYYkoZAJrxKblTZAsVb3lu9TVZAPQox0FzyCYJpUgZBVAJwkDGDeqCdkucjt9vCIZAXQbgkDutbjAwZCga6MCpEQ2mIaXfd"

# Ad URL
ad_url = f"https://graph.facebook.com/v19.0/act_{AD_ACCOUNT_ID}/ads"

# Properly structured payload
payload = {
    "name": "Test Ad",
    "adset_id": ADSET_ID,
    "creative": {
        "object_story_spec": {
            "page_id": PAGE_ID,
            "link_data": {
                "image_hash": image_hash,
                "link": "https://your-website-url.com",
                "message": "This is a test ad message"
            }
        }
    },
    "status": "PAUSED",
    "access_token": ACCESS_TOKEN
}

# ✅ Use json instead of data
response = requests.post(ad_url, json=payload)

if response.status_code == 200:
    print("✅ Ad created!")
    print(response.json())
else:
    print("❌ Error creating ad")
    print(response.status_code, response.text)

