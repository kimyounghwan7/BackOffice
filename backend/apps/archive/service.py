# business logic
import logging
from typing import Optional
from django.db import close_old_connections
from django.shortcuts import get_object_or_404
from .models.archive import Archive
from .serializers import ArchiveSerializer
from django.db.models import Q
from datetime import datetime

logger = logging.getLogger(__name__)

PAGE_SIZE = 10

def get_archive_list(current_page:int, search_str:Optional[str]) -> Optional[dict]:
	try:
		condition = Q(delete_datetime__isnull = True)
		if search_str is not None:
			condition.add(Q(title__icontains = search_str) | Q(content__icontains = search_str), Q.AND)
		offset = (current_page - 1) * PAGE_SIZE
		total_count = Archive.objects.filter(condition).count()
		archives_query = Archive.objects.filter(condition).\
			order_by("-id")[offset : offset + PAGE_SIZE]
		return {
			"result": ArchiveSerializer(archives_query, many = True).data,
			"totalCount": total_count / PAGE_SIZE
		}
	except Exception as e:
		logger.error(f"get_archive_list error] {e}")
		return None
	finally:
		close_old_connections()

def register_archive(archive_data:dict) -> Optional[bool]:
	try:
		serializer = ArchiveSerializer(data = archive_data)
		if serializer.is_valid():
			serializer.save()
			return True
		return
	except Exception as e:
		logger.error(f"register_archive error] {e}")
		return False
	finally:
		close_old_connections()

def get_archive(archive_id:int) -> Optional[dict]:
	try:
		archive_query = get_object_or_404(Archive, id = archive_id)
		# TODO 첨부파일 serializer 연동.
		return ArchiveSerializer(archive_query, many = False).data
	except Exception as e:
		logger.error(f"get_archive error] {e}")
		return None
	finally:
		close_old_connections()

def modify_archive(archive_data:dict, archive_id:int) -> Optional[bool]:
	try:
		archive_query = get_object_or_404(Archive, id = archive_id)
		serializer = ArchiveSerializer(
			archive_query, 
			data=archive_data, 
			partial=True
		)
		if serializer.is_valid():
			serializer.save()
			return True
		return False
	except Exception as e:
		logger.error(f"modify_archive error] {e}")
		return False
	finally:
		close_old_connections()

def remove_archive(archive_id:int) -> Optional[bool]:
	try:
		archive_query = get_object_or_404(Archive, id = archive_id)
		archive_query.delete_datetime = datetime.now()
		archive_query.save()
		return True
	except Exception as e:
		logger.error(f"remove_archive error] {e}")
		return False
	finally:
		close_old_connections()