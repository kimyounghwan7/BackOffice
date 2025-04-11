import logging
from http import HTTPStatus
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db import close_old_connections
from django.middleware.csrf import get_token

logger = logging.getLogger(__name__)

@api_view(["GET"])
def set_csrf_token(request:Request) -> Response:
	try:
		response = Response({'detail': 'CSRF cookie set'},status=HTTPStatus.OK)
		response['X-CSRFToken'] = get_token(request)
		return response
	except Exception as e:
		logger.error(f"set_csrf_token] {e}")
		return Response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
	finally:
		close_old_connections()