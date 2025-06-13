import os
import uuid
import json 
import requests
from user_agent import generate_user_agent

def lookup(emailoruser):
    uid_val = str(uuid.uuid4())
    token = uuid.uuid4().hex * 2
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "i.instagram.com",
        "Connection": "Keep-Alive",
        "User-Agent": generate_user_agent(),
        "Cookie": f"mid={uuid.uuid4()}; csrftoken={token}",
        "Accept-Language": "en-US",
        "X-IG-Capabilities": "AQ==",
    }
    data = {
        "q": emailoruser,
        "device_id": f"android-{uid_val}",
        "guid": uid_val,
        "_csrftoken": token
    }
    response = requests.post("https://i.instagram.com/api/v1/users/lookup/", headers=headers, data=data).json()
    return response

result = lookup(input("Enter Username Or Email: "))
print(json.dumps(result, indent=4, ensure_ascii=False))
