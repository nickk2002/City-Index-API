import json

from django.http import HttpResponse

# Create your views here.
from api.main import run_matrix


def home_view(request,matrix_code):
    data = run_matrix(matrix_code)

    return HttpResponse(json.dumps(data),content_type="application/json")


def nothing(request):
    return HttpResponse("<h1> Nothing here </h1>")