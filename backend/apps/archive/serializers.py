import logging
from rest_framework import serializers
from .models.archive import Archive

logger = logging.getLogger(__name__)

class ArchiveSerializer(serializers.ModelSerializer):
	class Meta:
		model = Archive
		fields = '__all__'