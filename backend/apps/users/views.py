import logging
from http import HTTPStatus
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import close_old_connections
from django.contrib.auth import authenticate, login, logout

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