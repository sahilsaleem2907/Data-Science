import requests

headers = { "Authorization": "Bearer 242ddc63dead637ee31867f79676676a" }
r = requests.post(
  "https://api-staging.pledge.to/v1/donations",
  data={
    "email": "yjh@ok.gov",
    "first_name": "Yvonne",
    "last_name": "Hilda",
    "organization_id": "dd959794-d83f-4128-be24-651d2a398f12",
    "amount": "0.68",
    "phone_number": "(918) 555-0188",
    "metadata": "shopify_id 870203745"
    },
  headers=headers
  )