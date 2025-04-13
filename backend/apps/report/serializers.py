import logging
from rest_framework import serializers
from .models.report import Report

logger = logging.getLogger(__name__)

class ReportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Report
		fields = '__all__'