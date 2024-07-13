"""
URL mappings for the user API.
"""
from django.urls import path

from user import views


# for the test_user_api to track
# CREATE_USER_URL = reverse('user:create')
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
]
