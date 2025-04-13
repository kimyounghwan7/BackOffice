import logging
from http import HTTPStatus
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import close_old_connections
from .service import get_report_list, register_report, get_report, modify_report, remove_report

logger = logging.getLogger(__name__)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def report_list(request:Request) -> Response:
	if request.method == "GET":
		try:
			#TODO auth check
			current_page = int(request.GET.get("currentPage", 1))
			search_str = request.GET.get("searchValue")
			result = get_report_list(current_page, search_str)
			return Response(result, status=HTTPStatus.OK)
		except Exception as e:
			logger.error(f"report_list get error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "POST":
		try:
			if register_report(request.data):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.BAD_REQUEST)
		except Exception as e:
			logger.error(f"report_list post error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def report_detail(request:Request, id:int) -> Response:
	if request.method == "GET":
		try:
			return Response(get_report(id), status=HTTPStatus.OK)
		except Exception as e:
			logger.error(f"report_detail get error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "PUT":
		try:
			if modify_report(request.data, id):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		except Exception as e:
			logger.error(f"report_detail put error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "DELETE":
		try:
			if remove_report(id):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		except Exception as e:
			logger.error(f"report_detail delete error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()