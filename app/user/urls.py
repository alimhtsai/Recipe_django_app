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
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
]
