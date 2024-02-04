from django.urls import path
from .views import *
from .views import my_login, my_logout, my_callback
from django.contrib.auth import views as auth
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    #Homepage
    path('homepage/',homepage,name ='homepage'),
    #Seller
    path('homepage/seller/', seller, name='seller'),
    path('homepage/seller/ratings/',rating_list),
    path('homepage/seller/food/',create_item),
    path('homepage/seller/view_orders/',order_list),

    #User
    path('homepage/user/',user,name = 'user'),
    path('homepage/user/cart/', view_order, name='cart'),
    path('homepage/user/view_eateries/',eatery_list),
    path('homepage/user/view_food/',food_list),
    path('homepage/user/view_ratings/',rating_list),
    path('homepage/user/view_eatery_ratings/',eatery_rating_list),
    path('homepage/user/change_order',change_order,),
    path('homepage/user/place-order/', create_order, name='place_a_order'),
    path('homepage/user/rate_food/<int:food_code>/', create_rating, name='rate_food'),
    path('homepage/user/rate_eatery/<int:eatery_code>/', create_eatery_rating, name='rate_eatery'),
    path('login/', my_login, name='my_login'),
    path('logout/', my_logout, name='my_logout'),
    path('callback/', my_callback, name='my_callback'),
    path('accounts/login/', auth.LoginView.as_view() ),
    path('accounts/logout/', auth.LogoutView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
    
