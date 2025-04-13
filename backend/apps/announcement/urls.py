from django.urls import path
from .views import announcement_list, announcement_detail

urlpatterns = [
	path('announcements/', announcement_list, name='announcement-list'),
	path('announcements/<int:id>', announcement_detail, name='announcement-detail'),
]