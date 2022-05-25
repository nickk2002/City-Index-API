import json

from django.http import HttpResponse

# Create your views here.
from api.main import run_matrix, get_information_localitate, LocalitateNotFound


def get_all(request, matrix_code):
    data = run_matrix(matrix_code)

    return HttpResponse(json.dumps(data),content_type="application/json")


def get_location(request, matrix_code, localitate):
    try:
        data = get_information_localitate(matrix_code, localitate)
    except LocalitateNotFound:
        return HttpResponse("Nu am gasit localitatea " + localitate)
    return HttpResponse(json.dumps(data),content_type="application/json")
