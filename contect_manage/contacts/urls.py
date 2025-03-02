from django.urls import path,include
from . import views
from .views import ContactSearchView
from rest_framework_simplejwt.views import (TokenRefreshView)

# from rest_framework.routers import DefaultRouter
# from contacts.views import ItemViewSet
# router = DefaultRouter()
# router.register(r'items', ItemViewSet, basename='item')



urlpatterns=[
    path(" ",views.HomePage.as_view(), name='homepage'),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('items/',views.ItemViewSet,name='items'),
    path("token/",views.MyTokenObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("register/",views.RegisterView.as_view(), name="register"),
    path("test/",views.testEndPoint,name='test'),
    path('', views.getRoutes),
    path('search/', ContactSearchView.as_view(), name='contact-search'),



]