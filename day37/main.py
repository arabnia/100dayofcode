import requests
from dotenv import load_dotenv
import os
import datetime
load_dotenv()
# endpoint
URL = "https://pixe.la"
headers = {
    "X-USER-TOKEN": os.getenv("TOKEN"),
}

## User section ##
# Create user
# params = {
#     "token": os.getenv("TOKEN"),
#     "username": os.getenv("USERNAME"),
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# user_endpoint = f"{URL}/v1/users"
# user_check = requests.post(url=user_endpoint, json=params)

## Graph section ##
# Create graph
# graph_endpoint = f"{URL}/v1/users/{os.getenv("USERNAME")}/graphs"
#
# graph_body = {"id":"sa01",
#               "name":"graph-name",
#               "unit":"Km",
#               "type":"float",
#               "color":"shibafu",
#               "timezone":"Asia/Tehran",
#               # "isSecret":"true",
#               "publishOptionalData":bool("true")
#               }
# create_graph_response = requests.post(url=graph_endpoint, json=graph_body, headers=headers)
# print(create_graph_response.text)
# list graphs
# get_graph_endpoin = f"{URL}/v1/users/{os.getenv('USERNAME')}/graphs"
# get_graph_response = requests.get(url=get_graph_endpoin, headers=headers)
# print(get_graph_response.text)

## pixel section ##
now = datetime.datetime.now().strftime("%Y%m%d")
addpixel_url = f"{URL}/v1/users/{os.getenv("USERNAME")}/graphs/sa01"
pixel_param = {"date": now,"quantity":"200","optionalData":"{\"key\":\"value\"}"}
add_pixel_resource = requests.post(url=addpixel_url, json=pixel_param, headers=headers)
print(add_pixel_resource.text)
