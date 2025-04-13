# business logic
import logging
from typing import Optional
from django.db import close_old_connections
from django.shortcuts import get_object_or_404
from .models.announcement import Announcement
from .serializers import AnnouncementSerializer
from django.db.models import Q
from datetime import datetime

logger = logging.getLogger(__name__)

PAGE_SIZE = 10

def get_announcement_list(current_page:int, search_str:Optional[str]) -> Optional[dict]:
	try:
		condition = Q(delete_datetime__isnull = True)
		if search_str is not None:
			condition.add(Q(title__icontains = search_str) | Q(content__icontains = search_str), Q.AND)
		offset = (current_page - 1) * PAGE_SIZE
		total_count = Announcement.objects.filter(condition).count()
		announcemnets_query = Announcement.objects.filter(condition).\
			order_by("-id")[offset : offset + PAGE_SIZE]
		return {
			"result": AnnouncementSerializer(announcemnets_query, many = True).data,
			"totalCount": total_count / PAGE_SIZE
		}
	except Exception as e:
		logger.error(f"get_announcement_list error] {e}")
		return None
	finally:
		close_old_connections()

def register_announcement(announcement_data:dict) -> Optional[bool]:
	try:
		serializer = AnnouncementSerializer(data = announcement_data)
		if serializer.is_valid():
			serializer.save()
			return True
		return False
	except Exception as e:
		logger.error(f"register_announcement error] {e}")
		return False
	finally:
		close_old_connections()

def get_announcement(announcement_id:int) -> Optional[dict]:
	try:
		announcement_query = get_object_or_404(Announcement, id = announcement_id)
		# TODO 첨부파일 serializer 연동.
		return AnnouncementSerializer(announcement_query, many = False).data
	except Exception as e:
		logger.error(f"get_announcement error] {e}")
		return None
	finally:
		close_old_connections()

def modify_announcement(announcement_data:dict, announcement_id:int) -> Optional[bool]:
	try:
		announcement_query = get_object_or_404(Announcement, id = announcement_id)
		serializer = AnnouncementSerializer(
			announcement_query, 
			data=announcement_data, 
			partial=True
		)
		if serializer.is_valid():
			serializer.save()
			return True
		return False
	except Exception as e:
		logger.error(f"modify_announcement error] {e}")
		return False
	finally:
		close_old_connections()

def remove_announcement(announcement_id:int) -> Optional[bool]:
	try:
		announcement_query = get_object_or_404(Announcement, id = announcement_id)
		announcement_query.delete_datetime = datetime.now()
		announcement_query.save()
		return True
		return
	except Exception as e:
		logger.error(f"remove_announcement error] {e}")
		return False
	finally:
		close_old_connections()