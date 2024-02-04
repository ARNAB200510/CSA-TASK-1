from rest_framework import serializers
from .models import Eatery_details, Items, Orders, Rating,Rating_eatery
from django.contrib.auth.models import User

class EaterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Eatery_details
        fields = '__all__'
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'  
class Rating_EaterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating_eatery
        fields = '__all__'  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('BITS_ID')