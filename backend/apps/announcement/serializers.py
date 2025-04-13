import logging
from rest_framework import serializers
from .models.announcement import Announcement

logger = logging.getLogger(__name__)

class AnnouncementSerializer(serializers.ModelSerializer):
	class Meta:
		model = Announcement
		fields = '__all__'