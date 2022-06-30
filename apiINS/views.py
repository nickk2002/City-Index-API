import csv
import json

from django.http import HttpResponse

from apiINS.scraper import run_matrix, get_information_localitate, LocalitateNotFound


def get_all(request, matrix_code):
    data = run_matrix(matrix_code)

    return HttpResponse(json.dumps(data), content_type="application/json")


def get_location_json(request, matrix_code, localitate):
    try:
        data = get_information_localitate(matrix_code, localitate)
    except LocalitateNotFound:
        return HttpResponse("Nu am gasit localitatea " + localitate)
    return HttpResponse(json.dumps(data), content_type="application/json")


def get_all_matrices(request):
    pass


def get_location_csv(request, matrix_code, localitate):
    try:
        json_data = get_information_localitate(matrix_code, localitate)
    except LocalitateNotFound:
        return HttpResponse("Nu am gasit localitatea " + localitate)
    response = HttpResponse(
        "Downloaded the file",
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="tabel.csv"'},
    )
    writer = csv.writer(response)
    first_row = ["Cnt", "matrixName", "martixCode", "localitate", "indicator"]
    nume_ani = []

    for key in json_data.keys():
        print(key)
        if key.startswith("Anul"):
            first_row.append(key)
            nume_ani.append(key)

    writer.writerow(first_row)
    second_row = [1, json_data['matrixName'], json_data["matrixCode"], json_data["localitate"], json_data["indicator"]]
    for ani in nume_ani:
        second_row.append(json_data[ani])
    writer.writerow(second_row)
    return response
