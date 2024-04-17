# In member_form/urls.py

from django.urls import path
from .views import member_form_view,member_details_view,add_family_member,members_list_view,edit_member_view

urlpatterns = [
  path('add_member/', member_form_view, name='member_form'),
    path('<member_id>/details/', member_details_view, name='member_view'),
    path('<member_id>/add-family-member/', add_family_member, name='add_family_member'),
    path('', members_list_view, name='home'),
    path('<member_id>/edit/', edit_member_view, name='edit_member'),
    path('members/', members_list_view, name='members_list'),
  
]


