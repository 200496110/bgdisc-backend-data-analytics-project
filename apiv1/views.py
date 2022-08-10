from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from . import creds as cd

# Create your views here.
url_base = cd.url


@api_view(['POST', 'GET'])
def login(request):
    response = request.data

    # REQUESTS MODULE
    url = url_base + "dataset/user/login"
    header = {
        "Accept": "application/json",
        "Content-Length": "29",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    creds = {
        "username": cd.username,
        "password": cd.password
    }
    res = requests.post(url, data=creds, headers=header)
    print(res.text)

    return HttpResponse("The BGDISC Custom Backend App is working successfully. - LOGIN API")


# change the REQUEST method to just POST in the final version
@api_view(['POST', 'GET'])
def updateMetadata(request):
    response = request.data

    id = "cedcd327-4e5d-43f9-8eb1-c11850fa7c55"
    # "1/metastore/schemas/dataset/items/"
    # url_g = url_base + "1/metastore/schemas/dataset/items/" + id
    url_g = url_base + "3/action/package_show?id=" + id + "&page=0"
    header = {
        "Accept": "application/json"
    }
    res = requests.get(url_g, headers=header).json()
    print(res["result"][0])
    # res = requests.get(url_g, headers=header)
    # print(res.text)
    print("requested at:", url_g)
    # request data schema
    # data = { "fileid": "xxx" }
    # STEPS
    # Retrieve using GET on
    # /api/1/metastore/schemas/dataset/items/{identifier}
    # the file from the website
    # perform analysis on it
    # get the tags and update the metadata using PATCH on
    # /api/1/metastore/schemas/dataset/items/{identifier}
    # and the property name to be added  for changing tags
    # is "keyword": ["string", "string", ...]

    return HttpResponse("The BGDISC Custom Backend App is working successfully. - UPDATE METADATA API")


@api_view(['POST', 'GET'])
def getCookie(request):
    response = request.data

    return HttpResponse("The BGDISC Custom Backend App is working successfully. - GET COOKIE API")
