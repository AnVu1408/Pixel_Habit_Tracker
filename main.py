import requests 
from datetime import datetime
import pytz  # for timezone conversion 

pixela_url = "https://pixe.la/v1/users"

token = "ABC1234@56789"
username = "miavu"
graph_id = "graph1"

headers = {
    "X-USER-TOKEN": token
}

#create user account
user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
    

#create a graph definition 
graph_endpoint = f"{pixela_url}/{username}/graphs"

graph_config = {
    "id": graph_id,
    "name": "My Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

#post value to the graph
pixel_creation_endpoint = f"{pixela_url}/{username}/graphs/{graph_id}"

nz_timezone = pytz.timezone('Pacific/Auckland')
today_nz = datetime.now(nz_timezone)
today = today_nz.date()
print(today.strftime("%Y%m%d")) 

pixel_data = {
    "date": today.strftime("%Y%m%d"), 
    "quantity": input("How many minutes did you code today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

# pixel_update_data = {
#     "quantity": "180",
# }

#delete_endpoint = f"{pixela_url}/{username}/graphs/{graph_id}/{today.strftime('%Y%m%d')}"


