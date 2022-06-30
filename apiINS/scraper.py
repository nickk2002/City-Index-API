import csv
import json
import re

import requests


class LocalitateNotFound(Exception):
    pass


def search_in_json(content: dict, localitate: str):
    output_data = []
    dimensions_map = content['dimensionsMap']
    parent_id_judet = -1

    # find the parent_id for judet
    for attribute in dimensions_map:
        if parent_id_judet != -1:
            break
        options = attribute['options']
        for option in options:
            if option['label'] == localitate:
                parent_id_judet = option['parentId']
                print("ParentID", parent_id_judet)
                break
    if parent_id_judet == -1:
        raise LocalitateNotFound("Could not find localitate " + localitate)
    other_fields = 0
    ani = []
    for attribute in dimensions_map:
        label = attribute['label']
        options = attribute['options']
        found = None
        if label == "Ani":
            output_data.append(options)
            for option in options:
                ani.append(option['label'])
            continue
        else:
            other_fields += 1
        for option in options:
            if found:
                break
            if option['label'] == localitate:
                found = option
                print("Found", found)
            if option['nomItemId'] == parent_id_judet and not option['parentId']:
                found = option
                print("Found", found)
        if not found:
            output_data.append([attribute['options'][0]])
        else:
            output_data.append([found])
    return ani, output_data


def get_information_localitate(cod_matrice: str, localitate: str):
    url = f"http://statistici.insse.ro:8077/tempo-ins/matrix/{cod_matrice}"
    content = json.loads(requests.get(url).content)
    ani, param_data = search_in_json(content, localitate)
    post_data = {
        "arr": param_data,
        "language": "ro",
        "matrixName": content["matrixName"],
        "matrixDetails": content["details"]
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
    }
    response = requests.post(f"http://statistici.insse.ro:8077/tempo-ins/matrix/dataSet/{cod_matrice}",
                             data=json.dumps(post_data), headers=headers)
    response_content = json.loads(response.content)
    indicator = param_data[-1][0]['label']

    output = {
        "matrixName": content["matrixName"],
        "matrixCode": cod_matrice,
        "localitate": localitate,
        "indicator": indicator
    }

    index = 0
    last_entry = response_content[-1]
    other_fields = len(last_entry) - len(ani)
    for number in last_entry[other_fields:]:
        digits = re.findall("\d+", number)
        if digits:
            output[ani[index]] = digits[0]
            index += 1
    return output


def run_matrix(cod_matrice: str):
    json_data = []
    with open("apiINS/testData/localitati.txt") as f:
        for line in f.readlines():
            localitate = line.strip()
            print(localitate)
            data = get_information_localitate(cod_matrice, localitate)
            json_data.append(data)
    return json_data


def get_all_matrices():
    response = requests.get("http://statistici.insse.ro:8077/tempo-ins/matrix/matrices")
    data = response.json()
    with open('output/all_matrices.csv', mode='w', encoding="UTF-8", newline='') as f:
        rows = [[matrix_data['name'], matrix_data['code']] for matrix_data in data]
        print(len(rows))
        employee_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerows(rows)


if __name__ == '__main__':
    get_all_matrices()
