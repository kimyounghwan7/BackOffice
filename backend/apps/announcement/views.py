import logging
from http import HTTPStatus
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import close_old_connections
from .service import get_announcement_list, register_announcement, get_announcemnet, modify_announcemnet, remove_announcemnet

logger = logging.getLogger(__name__)

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def announcement_list(request:Request) -> Response:
	if request.method == "GET":
		try:
			#TODO auth check
			current_page = int(request.GET.get("currentPage", 1))
			result = get_announcement_list(current_page)
			return Response(result, status=HTTPStatus.OK)
		except Exception as e:
			logger.error(f"announcement_list get error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "POST":
		try:
			if register_announcement():
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.BAD_REQUEST)
		except Exception as e:
			logger.error(f"announcement_list post error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def announcement_detail(request:Request, id:int) -> Response:
	if request.method == "GET":
		try:
			return Response(get_announcemnet(id), status=HTTPStatus.OK)
		except Exception as e:
			logger.error(f"announcement_detail get error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "PUT":
		try:
			if modify_announcemnet(request.data, id):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		except Exception as e:
			logger.error(f"announcement_detail put error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "DELETE":
		try:
			if remove_announcemnet(id):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		except Exception as e:
			logger.error(f"announcement_detail delete error] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()