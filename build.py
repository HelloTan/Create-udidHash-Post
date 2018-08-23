import random, json, requests

def generateUID():
    androidId = ""
    seed = "1234567890asdfghjklzxcvbnmqwertyuiop"
    for lol in range(30):
        androidId += random.choice(seed)
    return "3f" + androidId

# Tahap
header = {
    'Accept': "application/json",
    "Accept-Language": "id-ID",
    "X-LHM": 'POST',
    "X-LPV": '1',
    "X-Line-Application": "BIZANDROID\t1.7.2\tANDROID_OS\t7.1.2",
    "User-Agent": "Line/8.11.0"
}
payload = {"deviceInfo":{"deviceName":"Tanysz","model":"Redmi 4a","udidHash":""},"deviceUid": generateUID()}
res = requests.post('https://ga2s.line.naver.jp/plc/api/core/device/issueUdid', data=json.dumps(payload), headers=header)
udidHash = res.json()['udidHash']
dash = "Your udidHash : " + udidHash
print(dash)
