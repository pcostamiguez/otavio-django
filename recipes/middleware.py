# middleware.py
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


class RequireLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Verifica se o usuário está autenticado e a solicitação é para um arquivo de mídia # noqa
        if not request.user.is_authenticated and request.path.startswith('/media/'): # noqa
            messages.error(request, "Você deve estar logado para acessar esta página.") # noqa
            return redirect(reverse('admin:login'))

        return response
