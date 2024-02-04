from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Eatery_details, Items, Orders, Rating,Rating_eatery
from rest_framework import status
from .serializers import EaterySerializer,OrdersSerializer,ItemsSerializer,UserSerializer,RatingSerializer,Rating_EaterySerializer
from django.shortcuts import redirect
from django.urls import reverse
import requests
from django.contrib.auth import authenticate, login
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from urllib.parse import quote_plus, urlencode

#For Listing eateries
@login_required
@api_view (['GET'])
def eatery_list(request):
    
    eatery_objs =Eatery_details.objects.all()
    serializer =EaterySerializer(eatery_objs,many = 'True')
    response={'Page':'Eatery_list','Data':serializer.data}
    return Response(response)

#For adding eateries
@login_required
@api_view(['POST'])
def create_eatery(request):
    data = request.data
    serializer = EaterySerializer(data =data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#To delete or update    
@login_required
@api_view(['PUT','DELETE'])
def change_eatery(request,el):
    if request.method =='PUT':
        try:
            element = Eatery_details.objects.get(el)
        except:
            return Response(serializer.errors,status =status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer =EaterySerializer(element,data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        try:
            element = Eatery_details.objects.get(el)
        except:
            return Response(serializer.errors,status =status.HTTP_404_NOT_FOUND)
        element.delete(status =status.HTTP_204_NO_CONTENT)

#For Listing food_items
@login_required
@api_view (['GET'])
def food_list(request):
    
    food_objs =Items.objects.all()
    serializer =ItemsSerializer(food_objs,many = 'True')
    response={'Page':'Food_list','Data':serializer.data}
    return Response(response)

#For adding Food items
@login_required
@api_view(['POST'])
def create_item(request):
    data = request.data
    serializer = ItemsSerializer(data =data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#To delete or update
@login_required    
@api_view(['PUT','DELETE'])
def change_food(request,el):
    if request.method =='PUT':
        try:
            element = Items.objects.get(el)
        except:
            return Response(serializer.errors,status =status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer =ItemsSerializer(element,data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        try:
            element = ItemsSerializer.objects.get(el)
        except:
            return Response(serializer.errors,status =status.HTTP_404_NOT_FOUND)
        element.delete(status =status.HTTP_204_NO_CONTENT)
#For viewing orders
@login_required
@api_view (['GET'])
def order_list(request):
    
    orders_objs =Orders.objects.all()
    serializer =OrdersSerializer(orders_objs,many = 'True')
    response={'Page':'Order_list','Data':serializer.data}
    return Response(response)

#For adding orders
@login_required
@api_view(['POST'])
def create_order(request):
    data = request.data
    serializer = OrdersSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#To delete or update
@login_required    
@api_view(['PUT','DELETE'])
def change_order(request,el):
    if request.method =='PUT':
        try:
            element = Orders.objects.get(el)
        except:
            return Response(serializer.errors,status =status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer =OrdersSerializer(element,data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        try:
            element = Orders.objects.get(el)
        except:
            return Response(serializer.errors,status =status.HTTP_404_NOT_FOUND)
        element.delete(status =status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@login_required
def view_order(request,el):
    try:
        eatery = Orders.objects.get(el)
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrdersSerializer(eatery)
    return Response(serializer.data)

#For viewing rating
@login_required
@api_view (['GET'])
def rating_list(request):
    
    rating_objs =Rating.objects.all()
    serializer =RatingSerializer(rating_objs,many = 'True')
    response={'Page':'Eatery_list','Data':serializer.data}
    return Response(response)

#For adding rating
@login_required
@api_view(['POST'])
def create_rating(request):
    data = request.data
    serializer = RatingSerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

#For viewing rating_eatery
@login_required
@api_view (['GET'])
def eatery_rating_list(request):
    
    rating_objs =Rating_eatery.objects.all()
    serializer =Rating_EaterySerializer(rating_objs,many = 'True')
    response={'Page':'Eatery_list','Data':serializer.data}
    return Response(response)

#For adding rating_eatery
@login_required
@api_view(['POST'])
def create_eatery_rating(request):
    data = request.data
    serializer = Rating_EaterySerializer(data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@login_required
def homepage(request):
    return render(request,'homepage.html')
    
#For the users
@login_required
def user(request):
    return render(request, 'user.html')

#For the seller
@login_required
def seller(request):
    return render(request, 'seller.html')
#Order placement
@login_required
def order(request):
    return render(request, 'order.html')
#For the user food rating
@login_required 
def rating(request, code):
    return render(request, 'rating.html', {'Item_Code': code})
#For the user Eatery rating
@login_required
def rate_eatery(request, Eatery_code):
    return render(request, 'eatery_rating.html', {'Eatery_code': Eatery_code})


[{
	"resource": "/c:/Food_Delivery_App_By_CSA/FDA_By_CSA/views.py",
	"owner": "_generated_diagnostic_collection_name_#0",
	"code": {
		"value": "reportMissingImports",
		"target": {
			"$mid": 1,
			"path": "/microsoft/pyright/blob/main/docs/configuration.md",
			"scheme": "https",
			"authority": "github.com",
			"fragment": "reportMissingImports"
		}
	},
	"severity": 4,
	"message": "Import \"authlib.integrations.django_client\" could not be resolved",
	"source": "Pylance",
	"startLineNumber": 15,
	"startColumn": 6,
	"endLineNumber": 15,
	"endColumn": 40
}]
def my_login(request):
    auth0_domain = 'dev-8y5ohe28t15mieo2.us.auth0.com'
    client_id = 'Iqqbwjw3y1UWnv9AgaKiyB996AWw5K05'
    callback_url = 'https://127.0.0.1:9000/FDA_BY_CSA/homepage/'

    return redirect(f'https://{auth0_domain}/authorize?response_type=code&client_id={client_id}&redirect_uri={callback_url}')

def my_logout(request):
    auth0_domain = 'dev-8y5ohe28t15mieo2.us.auth0.com'
    client_id = 'Iqqbwjw3y1UWnv9AgaKiyB996AWw5K05'
    callback_url = 'https://127.0.0.1:9000/FDA_BY_CSA/homepage/'

    return redirect(f'https://{auth0_domain}/v2/logout?client_id={client_id}&returnTo={callback_url}')


def my_callback(request):
    auth0_domain ='dev-8y5ohe28t15mieo2.us.auth0.com'
    client_id ='Iqqbwjw3y1UWnv9AgaKiyB996AWw5K05'
    client_secret = '3ASw4mddGy8-ID3zyoIRaPX2mSQvoe5he7FuqAIOMquq4iynTthZTm-oyXS4C5zw'
    callback_url = 'https://127.0.0.1:9000/FDA_BY_CSA/homepage/'

    code = request.GET.get('code')
    url = f'https://{auth0_domain}/oauth/token'
    user_url = f'https://{auth0_domain}/userinfo'

    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': callback_url,
        'code': code,
        'grant_type': 'authorization_code'
    }
    response = requests.post(url, data=payload)
    data = response.json()
    access = data['access_token']

    userinfo_headers = {'Authorization': f'Bearer {access}'}
    userinfo_response = requests.get(user_url, headers=userinfo_headers)
    userinfo = userinfo_response.json()

    user = authenticate(request, auth0_user=userinfo)
    login(request, user)

    return redirect('https://127.0.0.1:9000/FDA_BY_CSA/homepage/')