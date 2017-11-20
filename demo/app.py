from tastemakers.client import TastemakersClient
api_key = "EF8EB27B572AE55A6B3814BED9AFC"
client = TastemakersClient(api_key)
print client.get_experiences()