import json
import requests

URL = "https://developer.riotgames.com/"

headers = {
"accept": "application/json",
"Content-Type": "application/json"
}

params = {
"username": "Pichaperro17",
"password": "conxdemixta!!"
}

resp = requests.post(URL, headers = headers ,data=json.dumps(params))
tk = json.loads(resp.text)['token']

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('token: ' + str(tk))
print('Success')