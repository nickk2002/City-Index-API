import csv
import json
from typing import List, Tuple

from django.http import HttpResponse

from apiINS.scraper import get_information_localitate


def parse_query_string(query_string: str) -> List[Tuple[str, List[str]]]:
    # 1=>ABC,BCA,CDA;2-BAC,sKASDj
    data = []
    for column in query_string.split(";"):
        split = column.split(":")
        if len(split) > 1:
            data.append((split[0], split[1].split(",")))
    return data


def get_location_json(request, matrix_code):
    if "query" in request.GET:
        query = request.GET['query']
        list_data = parse_query_string(query)
        print(list_data)
        data = get_information_localitate(matrix_code, list_data)

        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return HttpResponse("<h1> No query :( ")


def get_all_matrices(request):
    pass


