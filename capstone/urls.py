"""
capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""

from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from catalog import views

'''
NOTE:
    - first refers to the part of the email before the @ sign
    - second refers to the part of the email after the @ sign
'''

urlpatterns = [

    # User Profile
    path('get/user/<slug:first>/<slug:second>/', views.user_profile_get),
    path('post/user/update/', views.user_profile_update),
    path('post/userLoggedIn/', views.is_loggedIn),

    #---------------- Poster Views ----------------#

    # Advertisement
    path('get/advertisement/<slug:first>/<slug:second>/', views.advertisement_get),
    path('post/advertisement/create/', views.advertisement_create), # in use
    path('post/advertisement/update/', views.advertisement_update),
    path('post/advertisement/delete/', views.advertisement_delete),

    # Advertisement Review
    path('get/review/<slug:first>/<slug:second>/<slug:ad_id>/', views.review_get), # in use
    path('post/review/create/', views.review_create),
    path('post/review/update/', views.review_update),
    path('post/review/delete/', views.review_delete),

    # Advertisement Event
    path('get/event/<slug:first>/<slug:second>/<slug:ad_id>/', views.event_get),
    path('post/event/create/', views.event_create), # in use
    path('post/event/update/', views.event_update),
    path('post/event/delete/', views.event_delete),

    # Advertisement Images
    path('get/image/<slug:first>/<slug:second>/<slug:ad_id>/', views.image_get),
    path('post/image/create/', views.image_create),
    path('post/image/update/', views.image_update),
    path('post/image/delete/', views.image_delete),

    #---------------- Accommodation Seeker Views ----------------#


    #---------------- General Views ----------------#

    path('get/advertisement/', views.get_all_ads), # in use
    path('get/advertisement/<slug:first>/<slug:second>/<int:ad_id>/', views.get_single_ad), # in use

    #---------------- Search module views ----------------#

    path('get/<checkIn>[0-9]{4}-[0-9]{2}-[0-9]{2}/    \
              <checkOut>[0-9]{4}-[0-9]{2}-[0-9]{2}/   \
              <location>/                             \
              <nGuests>/                              \
              <minPrice>[0-9].[0-9]/                  \
              <maxPrice>[0-9].[0-9]/                  \
              <distance>/', views.search),

    #---------------- URLs for testing ----------------#

    path('advertisement/<int:pk>/', views.advertisement_detail),
    path('user/<int:pk>/', views.user_detail),
    path('review/<int:pk>/', views.review_detail),
    path('event/<int:pk>/', views.event_detail),
    path('image/<int:pk>/', views.image_detail),

    path('api/public/', views.public),
    path('api/private/', views.private),

    path('admin/', admin.site.urls),
]
