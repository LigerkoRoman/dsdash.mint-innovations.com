from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', dashboard1, name="dashboard1"),
    path('dash/', dash, name="dash"),
    path('dashboardgr/', dashboardgr, name="dashboardgr"),
    path('dashboardgrimages/', dashboardgrimages, name="dashboardgrimages"),
    path('test/', test, name ="test"),
    path('table/', table, name="table"),

    path('ajax/', add_ajax, name="add_ajax"),
    path('ajaxtwo/', add_ajaxtwo, name="add_ajaxtwo"),
    path('ajaxthree/', add_ajaxthree, name="add_ajaxthree"),
    path('ajaxfour/', add_ajaxfour, name="add_ajaxfour"),
    path('ajaxfive/', add_ajaxfive, name="add_ajaxfive"),
    path('ajaxsix/', add_ajaxsix, name="add_ajaxsix"),

    path('display_data/', display_data, name="display_data"),

    path('fridge/', fridge, name="fridge"),
    path('redshelf/', redshelf, name="redshelf"),
    path('panorama/', panorama, name="panorama"),
    path('glassfridge/', glassfridge, name="glassfridge"),
    path('philipmorris/', philipmorris, name="philipmorris"),

    path('glassfridgeimages/', glassfridgeimages, name="glassfridgeimages"),

]
