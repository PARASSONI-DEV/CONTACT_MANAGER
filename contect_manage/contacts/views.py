from django.shortcuts import render # type: ignore
from django.http import JsonResponse
from .models import User, contects
from django.views import generic

from .serializers import UserSerializer,MyTokenObtainPairSerializer,RegisterForm,ContactSerializer,ItemSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework import viewsets

# from rest_framework.decorators import api_view
# from rest_framework.response import Response


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=([AllowAny,])
    serializer_class=RegisterForm


@api_view(['GET','POST'])
def getRoutes(request):
    routes = [
        '/contacts/items/',
        '/contacts/token/',
        '/contacts/token/refresh/',
        '/contacts/register/',
    ]
    return Response(routes)



# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def dashboard(request):
#     if request.method=='GET':
#         response=f"hey {request.user},you are seeing a GET response"
#         return Response({'response':response},status=status.HTTP_200_ok)
#     elif request.method=="POST":
#         text=request.POST.get("text")
#         response=f"hey {request.user},your text is {text}"
#         return Response({'response':response},status=status.HTTP_200_ok)


#     return Response({},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)




class HomePage(generic.TemplateView):
    template_name ='homepage.js'





# views.py


# @api_view(['GET'])
# def search_contects(request):
#     query = request.GET.get('q', '')  # Get the search query
#     if query:
#         contects = contects.objects.filter(name__icontains=query)
#     else:
#         contects = contects.objects.all()
    
#     # Convert products to JSON-friendly data
#     contects_list = [{'id': p.id, 'name': p.name, 'number': p.number} for p in contects]
    
#     return Response({'contects': contects_list})

class ContactSearchView(generics.ListAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return contects.objects.filter(name__icontains=query)
        return contects.objects.all()
        

# @api_view(['GET', 'POST'])
class ItemViewSet(viewsets.ModelViewSet):
    queryset = contects.objects.all()
    serializer_class = ItemSerializer