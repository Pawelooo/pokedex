from django.http import JsonResponse


def error_400(request, exception):
    message = ('Nie znaleziono')
    respone = JsonResponse(data={'message': message, 'status_code':404})
    return respone

def error_500(request):
    message = ('Wystąpił błąd, nasza wina')
    response = JsonResponse(data={'message': message, 'status_code':500})
    return response