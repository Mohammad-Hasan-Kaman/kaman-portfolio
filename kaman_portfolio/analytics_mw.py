"""Analytics middleware — records page views & events server-side."""
from portfolio.analytics import record


class AnalyticsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.path
        # skip admin, static, media, favicon
        if (path.startswith('/admin') or path.startswith('/static/')
                or path.startswith('/media/') or path == '/favicon.ico'):
            return response
        if request.method != 'GET':
            return response
        if response.status_code != 200:
            return response
        return record(request, response)
