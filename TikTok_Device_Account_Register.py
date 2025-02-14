# TikTok API Client
#
# Step 1: Register your user
# Enter your username in the x_user_id field
# Call the function: register_user()
#
# Step 2: Top up your credit
# Send USDT (TRC20) to the following wallet address:
# Wallet Address: TKD3JPpYRw3XmxefJJb536ZmxZftkoCYHY
#
# Pricing:
# - 100,000 Requests: $1,400 USD
# - 50,000 Requests: $800 USD
# - 25,000 Requests: $600 USD
#
# Step 3: Confirm your transaction
# Provide your transaction ID via Telegram: https://t.me/reverse4free
#
# Step 4: Check your balance
# Call the function: balance()
#
# Step 5: Start making requests
# Once your balance is confirmed, you are ready to use the TikTok API.


import requests
import json
import random


host        = 'http://162.244.29.181:9137'
country     = 'de'
proxy       = 'username:password@host:ip'
x_user_id   = 'x_user_id'

number      = "+490000000000"

code        = 0

e_mail      = ""
password    = ""


def register_user():
    url = f"{host}/"

    payload = {}
    headers = {
        'X-User-ID': x_user_id
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def balance():
    url = f"{host}/balance"

    payload = {}
    headers = {
        'X-User-ID': x_user_id
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def register_device():
    url = f"{host}/register_device"

    payload = json.dumps({
      "country": country,
      "proxy": proxy
    })
    headers = {
      'X-User-ID': x_user_id,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(response)

    if int(response['code']) == 200:
        with open(f"{country}_devices.txt", 'a') as file:
            file.write(f"{json.dumps(response['data'])}\n")


def send_sms():
    url = f"{host}/send_sms"

    filename = f"{country}_devices.txt"
    with open(filename, "r") as file:
        random_line = random.choice(file.read().splitlines())

    device = json.loads(random_line)

    payload = json.dumps({
        "device": device,
        "number": number,
        "proxy": proxy,
        "country": country
    })
    headers = {
        'X-User-ID': x_user_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def verify_code():
    url = f"{host}/verify_code"

    filename = f"{country}_devices.txt"
    with open(filename, "r") as file:
        random_line = random.choice(file.read().splitlines())

    device = json.loads(random_line)

    payload = json.dumps({
        "device": device,
        "number": number,
        "proxy": proxy,
        "country": country,
        "code": code
    })
    headers = {
        'X-User-ID': x_user_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def register_account():
    url = f"{host}/register_account"

    filename = f"{country}_devices.txt"
    with open(filename, "r") as file:
        random_line = random.choice(file.read().splitlines())

    device = json.loads(random_line)

    payload = json.dumps({
        "device": device,
        "proxy": proxy,
        "e_mail": e_mail,
        "password": password
    })
    headers = {
        'X-User-ID': x_user_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    if int(response['code']) == 200:
        with open(f"{country}_accounts.txt", 'a') as file:
            file.write(f"{json.dumps(response['data'])}\n")


def update_token():
    url = f"{host}/update_token"

    filename = f"{country}_devices.txt"
    with open(filename, "r") as file:
        random_line = random.choice(file.read().splitlines())

    device = json.loads(random_line)

    payload = json.dumps({
        "device": device,
        "proxy": proxy
    })
    headers = {
        'X-User-ID': x_user_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(response)


def update_seed():
    url = f"{host}/update_seed"

    filename = f"{country}_devices.txt"
    with open(filename, "r") as file:
        random_line = random.choice(file.read().splitlines())

    device = json.loads(random_line)

    payload = json.dumps({
        "device": device,
        "proxy": proxy
    })
    headers = {
        'X-User-ID': x_user_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(response)


def update_report():
    url = f"{host}/update_report"

    filename = f"{country}_devices.txt"
    with open(filename, "r") as file:
        random_line = random.choice(file.read().splitlines())

    device = json.loads(random_line)

    payload = json.dumps({
        "device": device,
        "proxy": proxy,
    })
    headers = {
        'X-User-ID': x_user_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    print(response)


if __name__ == '__main__':
    #register_user()
    #balance()
    register_device()
    #send_sms()
    register_account()
