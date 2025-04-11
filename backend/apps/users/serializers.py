import logging
from rest_framework import serializers
from .models.users import User

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
	isAuthenticated = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = '__all__'
		extra_kwargs = {"password": {"write_only": True}}

	def get_fields(self):
		fields = super().get_fields()
		if self.context.get('mode') == 'AUTH':
			allowed_fields = ['id', 'isAuthenticated', 'username']
			return {field: fields[field] for field in allowed_fields}
		return fields

	def get_isAuthenticated(self, obj):
		try:
			return obj.is_active
		except Exception:
			return None