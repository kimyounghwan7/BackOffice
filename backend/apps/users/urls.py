from django.urls import path
from .views import login_view, logout_view, user_list, user_detail

urlpatterns = [
	path('login', login_view, name='login-view'),
	path('logout', logout_view, name='logout-view'),
	path('users/', user_list, name='user-list'),
	path('users/<int:id>', user_detail, name='user-detail'),
]