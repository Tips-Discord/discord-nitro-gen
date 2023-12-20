import requests
import json
import uuid
import time

def make_request():
    while True:
        headers = {
            'authority': 'api.discord.gx.games',
            'accept': '*/*',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'content-type': 'application/json',
            'origin': 'https://www.opera.com',
            'referer': 'https://www.opera.com/',
            'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0',
        }
        json_data = {
            'partnerUserId': str(uuid.uuid4()),
        }
        response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_data)
        print(response.text)
        with open('nitrox.txt', 'a') as file:
            file.write(f"{response.text}\n")
        if response == "":
            pass
        else:
            link = f"https://discord.com/billing/partner-promotions/1180231712274387115/{response.json().get('token')}"
            with open('nitro.txt', 'a') as file:
                file.write(f"{link}\n")

make_request()