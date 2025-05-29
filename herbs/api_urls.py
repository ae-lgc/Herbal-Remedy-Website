from django.urls import path
from . import api_views  # make sure naa pud kay api_views.py

urlpatterns = [
    path('herbs/', api_views.HerbListAPI.as_view(), name='herb_list_api'),
]
