from django.urls import path
from .views import report_list, report_detail

urlpatterns = [
	path('reports/', report_list, name='report-list'),
	path('reports/<int:id>', report_detail, name='report-detail'),
]