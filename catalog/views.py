from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse

# writing Django views using Serializer
# *****START*****
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from catalog.models import Advertisement, Accommodation_Review, Amenities, PropertyImage, Event
from catalog.models import User_Profile, User_Review
from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import AmentitiesSerializer, PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer, UserReviewSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth import authenticate, login

def login_user(request):
    user = authenticate(username=request.POST.get('username'),  password=request.POST.get('password'))
    if user:
       login(request, user)
       return HttpResponse("Logged In")
    return HttpResponse("Not Logged In")

def getAllTracks(request):
    if request.user.is_authenticated():
        return HttpResponse("Authenticated user")
    return HttpResponse("Non Authenticated user")

# Advertisement model
@api_view(['GET', 'POST'])
def advertisement_list(request):
    """
    List all Advertisements, or create a new Advertisement.
    """
    if request.method == 'GET':
        ad = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ad, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def advertisement_detail(request, pk):
    """
    Retrieve, update or delete an advertisement.
    """
    try:
        ad = Advertisement.objects.get(pk=pk)
    except ad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# ******END******

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")

def index(request):
    return HttpResponse("Home Page")
