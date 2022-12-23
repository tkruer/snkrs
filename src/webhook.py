import requests
import log

def send_webhook(webhook: str, event: str, store: str, sku: str, size: str, mode: str, email: str):
    data = {
      "content": "",
      "embeds": [
        {
          "color": 7995224,
          "fields": [
            {
              "name": "Event",
              "value": f"`{event}`"
            },
            {
              "name": "Store",
              "value": f"`{store}`"
            },
            {
              "name": "SKU",
              "value": f"`{sku}`"
            },
            {
              "name": "Size",
              "value": f"`{size}`"
            },
            {
              "name": "Email",
              "value": f"||{email}||"
            },
            {
              "name": "Mode",
              "value": f"`{mode}`"
            }
          ],
          "author": {
            "name": "SNKRS Bot Success"
          }
        }
      ],
      "attachments": []
    }
    response = requests.post(url=webhook, json=data)
    if response.status_code == 204:
        print(f"Webhook sent to {webhook}")
    else:
        print(f"Webhook failed to send to {webhook}")