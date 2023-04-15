from datetime import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = 'viniciusmotero'
TOKEN = 'thisissecret4950'
GRAPH_ID = "graph1"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_params = {
    'id': "graph1",
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#print(response.text)

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()

pixel_date = {
    'date': today.strftime('%Y%m%d'),
    'quantity': "9.74"
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_date, headers=headers)
#print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity': '4.5'
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint,headers=headers)
print(response.text)
