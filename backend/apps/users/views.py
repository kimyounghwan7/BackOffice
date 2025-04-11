import logging
from http import HTTPStatus
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import close_old_connections
from django.contrib.auth import authenticate, login, logout
from .service import get_user_list, register_user, get_user, modify_user, remove_user

logger = logging.getLogger(__name__)

@api_view(["POST"])
def login_view(request:Request) -> Response:
	try:
		username = request.data.get("username")
		password = request.data.get("password")
  
		if username is None or password is None:
			return Response({"errors": "Please enter both username and password"}, status=HTTPStatus.BAD_REQUEST)
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return Response({"success":True}, status=HTTPStatus.OK)
		return Response({"errors": "Please enter both username and password"}, status=HTTPStatus.BAD_REQUEST)
	except Exception as e:
		logger.error(f"login_view] {e}")
		return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
	finally:
		close_old_connections()

@api_view(["GET"])
def logout_view(request:Request) -> Response:
	try:
		if not request.user.is_authenticated:
			return Response({"errors": "You\'re not logged in."}, status=HTTPStatus.BAD_REQUEST)
		logout(request)
		return Response({"success": "success logged out."}, status=HTTPStatus.OK)
	except Exception as e:
		logger.error(f"logout_view] {e}")
		return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
	finally:
		close_old_connections()

@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def user_list(request:Request) -> Response:
	if request.method == "GET":
		try:
			result = get_user_list()
			return Response(result, status=HTTPStatus.OK)
		except Exception as e:
			logger.error(f"users get] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "POST":
		try:
			if register_user(request.data):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.BAD_REQUEST)
		except Exception as e:
			logger.error(f"users post] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def user_detail(request:Request, id:int) -> Response:
	if request.method == "GET":
		try:
			return Response(get_user(request, id), status=HTTPStatus.OK)
		except Exception as e:
			logger.error(f"user_detail get] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "PUT":
		try:
			if modify_user(request.data, id):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.BAD_REQUEST)
		except Exception as e:
			logger.error(f"user_detail put] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()
	elif request.method == "DELETE":
		try:
			if remove_user(id):
				return Response(status=HTTPStatus.OK)
			return Response(status=HTTPStatus.BAD_REQUEST)
		except Exception as e:
			logger.error(f"user_detail delete] {e}")
			return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
		finally:
			close_old_connections()