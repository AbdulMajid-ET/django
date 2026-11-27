
import logging

logger = logging.getLogger("django.request_path")


class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        logger.info("Requested URL: %s", request.path)

        response = self.get_response(request)

        logger.info("Response Status: %s", response.status_code)

        return response
