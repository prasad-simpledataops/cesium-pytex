import json

import requests


def login(base_cesium_url: str, tex_id: str, password: str):
    print(f'Logging into {base_cesium_url} for texId {tex_id}')
    login_request = {'texId': tex_id, 'password': password}
    response = requests.request('POST',base_cesium_url + '/api/v1/executor/login', json=login_request)
    if response.status_code != 200:
        raise Exception(f'Got a invalid response from server: {response.status_code}')
    login_response_json = response.json()
    return login_response_json


if __name__ == '__main__':
    print("testing")
    login_response = login('https://dev-api.simpledata.app/cesium', '314ed063-cfe8-4ca9-a487-f84e6634c673', 'BOiM3BB4ko8QL8vMaucq')
    #login_response = login('http://localhost:8080', '771c8c44-cd84-4615-873c-9c215a3f4e1e', 'KQubTgwhA69KPh9CSSI9')
    print(login_response)