import requests
import json

url = "https://io.adafruit.com/api/v2/abhi16/feeds/temp/data"
x=100
payload={"value":x}
#payload = "{\"value\":100}"
headers = {
    'x-aio-key': "aio_UxTu16IykVBZ4HDEiCtLat1MluzL",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "aabcbdf6-6809-9351-dc95-110f18304b40"
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response.text)




#json code/output in postman

{
    "id": "0F26FEB46R1YEHBCQA4GRG05CD",
    "value": "180",
    "feed_id": 1853916,
    "feed_key": "temp",
    "created_at": "2022-07-03T08:04:30Z",
    "created_epoch": 1656835470,
    "expiration": "2022-08-02T08:04:30Z"
}
