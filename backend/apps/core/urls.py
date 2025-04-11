from django.urls import path
from .views import set_csrf_token

urlpatterns = [
	path('set-csrf', set_csrf_token)
]