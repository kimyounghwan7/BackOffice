# business logic
import logging
from .models.users import User
from .serializers import UserSerializer
from django.db import close_old_connections
from django.shortcuts import get_object_or_404
from typing import Optional
from datetime import datetime

logger = logging.getLogger(__name__)

def get_user_list() -> Optional[dict]:
	try:
		users_query = User.objects.filter(delete_datetime__isnull = True)
		return UserSerializer(users_query, many=True).data
	except Exception as e:
		logger.error(f"get_user_list error] {e}")
		return None
	finally:
		close_old_connections()

def register_user(user_data:dict) -> Optional[bool]:
	try:
		serializer = UserSerializer(data=user_data)
		if serializer.is_valid():
			serializer.save()
			return True
		return False
	except Exception as e:
		logger.error(f"register_user error] {e}")
		return False
	finally:
		close_old_connections()

def get_user(user_id:int) -> Optional[dict]:
	try:
		user_query = get_object_or_404(User, id=user_id)
		return UserSerializer(user_query, many=False).data
	except Exception as e:
		logger.error(f"get_user error] {e}")
		return None
	finally:
		close_old_connections()

def modify_user(user_data:dict, user_id:int) -> Optional[bool]:
	try:
		user_query = get_object_or_404(User, id=user_id)
		serializer = UserSerializer(user_query, data=user_data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return True
		return False
	except Exception as e:
		logger.error(f"modify_user error] {e}")
		return False
	finally:
		close_old_connections()

def remove_user(user_id:int) -> Optional[bool]:
	try:
		user_query = get_object_or_404(User, id=user_id)
		user_query.delete_datetime = datetime.now()
		user_query.is_active = False
		user_query.save()
		return True
	except Exception as e:
		logger.error(f"remove_user error] {e}")
		return False
	finally:
		close_old_connections()