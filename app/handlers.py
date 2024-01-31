from django.http import HttpRequest
from django.shortcuts import render


def render_not_found_template(request: HttpRequest, *args, **kwargs):
    return render(request, "app/not_found.html")
