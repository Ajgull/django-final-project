from django.http import HttpRequest, HttpResponse


def Rec(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello world!')
