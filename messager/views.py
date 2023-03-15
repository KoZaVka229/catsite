from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse(f'<h1>Боже какой же Азамат <a href=\"{reverse("my_profile")}\">бездарь</a></h1>')


@login_required
def chat(request, chat_id: int):
    return HttpResponse(f"Чат id{chat_id}")
