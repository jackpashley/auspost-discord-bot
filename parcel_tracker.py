import requests
# %%
cookies = {
    'datadome': '60iTfhIOwmU0F2MWw5o47_JFJGFFQG8l1JD3zgzJpHBKBUIHRXZ0kwTbRQk14fPceK58hpkDyqNo--RSHB4ytztmAP5HcrimdZ7P10xlGrFep4864qHEijE-J6qX6DN5',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://auspost.com.au',
    'Referer': 'https://auspost.com.au/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'api-key': 'd11f9456-11c3-456d-9f6d-f7449cb9af8e',
}

def parcel_check(tracking_id):
    params = {
        'trackingIds': tracking_id,
    }
    response = requests.get(
        'https://digitalapi.auspost.com.au/shipmentsgatewayapi/watchlist/shipments',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    return response.json()[0]['shipment']["articles"][0]['details'][0]['events'][0]
