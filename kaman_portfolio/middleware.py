class ForceEnglishDefaultMiddleware:
    """Default the site to English regardless of the visitor's browser language.

    LocaleMiddleware resolves language as: cookie -> Accept-Language header ->
    settings.LANGUAGE_CODE. We strip the Accept-Language header before it runs,
    so first visits always land on /en/; after the visitor picks a language from
    the menu, the language cookie persists their choice.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.META.pop('HTTP_ACCEPT_LANGUAGE', None)
        return self.get_response(request)
