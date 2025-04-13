# business logic
import logging
from typing import Optional
from django.db import close_old_connections
from django.shortcuts import get_object_or_404
from .models.report import Report
from .serializers import ReportSerializer
from django.db.models import Q
from datetime import datetime

logger = logging.getLogger(__name__)

PAGE_SIZE = 10

def get_report_list(current_page:int, search_str:Optional[str]) -> Optional[dict]:
	try:
		condition = Q(delete_datetime__isnull = True)
		if search_str is not None:
			condition.add(Q(title__icontains = search_str) | Q(content__icontains = search_str), Q.AND)
		offset = (current_page - 1) * PAGE_SIZE
		total_count = Report.objects.filter(condition).count()
		reports_query = Report.objects.filter(condition).\
			order_by("-id")[offset : offset + PAGE_SIZE]
		return {
			"result": ReportSerializer(reports_query, many = True).data,
			"totalCount": total_count / PAGE_SIZE
		}
	except Exception as e:
		logger.error(f"get_report_list error] {e}")
		return None
	finally:
		close_old_connections()

def register_report(report_data:dict) -> Optional[bool]:
	try:
		serializer = ReportSerializer(data = report_data)
		if serializer.is_valid():
			serializer.save()
			return True
		return
	except Exception as e:
		logger.error(f"register_report error] {e}")
		return False
	finally:
		close_old_connections()

def get_report(report_id:int) -> Optional[dict]:
	try:
		report_query = get_object_or_404(Report, id = report_id)
		# TODO 첨부파일 serializer 연동.
		return ReportSerializer(report_query, many = False).data
	except Exception as e:
		logger.error(f"get_report error] {e}")
		return None
	finally:
		close_old_connections()

def modify_report(report_data:dict, report_id:int) -> Optional[bool]:
	try:
		report_query = get_object_or_404(Report, id = report_id)
		serializer = ReportSerializer(
			report_query, 
			data=report_data, 
			partial=True
		)
		if serializer.is_valid():
			serializer.save()
			return True
		return False
	except Exception as e:
		logger.error(f"modify_report error] {e}")
		return False
	finally:
		close_old_connections()

def remove_report(report_id:int) -> Optional[bool]:
	try:
		report_query = get_object_or_404(Report, id = report_id)
		report_query.delete_datetime = datetime.now()
		report_query.save()
		return True
	except Exception as e:
		logger.error(f"remove_report error] {e}")
		return False
	finally:
		close_old_connections()