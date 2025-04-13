from django.urls import path
from .views import archive_list, archive_detail

urlpatterns = [
	path('archives/', archive_list, name='archive-list'),
	path('archives/<int:id>', archive_detail, name='archive-detail'),
]