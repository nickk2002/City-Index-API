import json
import re
from pprint import pprint
from typing import List, Tuple

import requests

from apiINS.exceptions import CouldNotFindValue, CouldNotFindFieldLabel


def search_in_json(content: dict, query_list: List[Tuple[str, List[str]]]):
    post_data = []  # array of options selected
    ani = []
    found_labels = {}  # Alba Iulia -> Judete, Masculin -> Sexe

    dimensions_map = content['dimensionsMap']
    print("Data to filter for", query_list)
    index_query_list = 0
    # find the parent_id for judet
    for attribute in dimensions_map:
        field_label: str = attribute['label'].strip()
        options = attribute['options']
        if field_label == "Ani":
            post_data.append(options)
            for option in options:
                ani.append(option['label'])
        elif index_query_list < len(query_list) and field_label == query_list[index_query_list][0]:
            labels_to_search = list.copy(query_list[index_query_list][1])
            options_selected = []
            for option in options:
                option_label = option['label'].strip()  # remove the whitespace from the label
                if option_label in labels_to_search:
                    options_selected.append(option)
                    found_labels[option_label] = field_label  # certain value => main label
                    labels_to_search.remove(option_label)
            if labels_to_search:  # daca nu am gasit toate lucrurile scrise in lista
                raise CouldNotFindValue(field_label, labels_to_search)
            post_data.append(options_selected)
            index_query_list += 1
        else:  # iau total
            post_data.append([options[0]])
    if index_query_list < len(query_list):  # daca nu am gasit toate label-urile initiale
        raise CouldNotFindFieldLabel(query_list[index_query_list][0])
    return ani, found_labels, post_data


def get_information_localitate(cod_matrice: str, query_list: List[Tuple[str, List[str]]]):
    url = f"http://statistici.insse.ro:8077/tempo-ins/matrix/{cod_matrice}"
    content = json.loads(requests.get(url).content)

    try:
        ani, found_labels, post_data = search_in_json(content, query_list)
    except Exception as e:
        return {"error": e.__str__()}

    print("Param data", post_data)
    post_payload = {
        "arr": post_data,
        "language": "ro",
        "matrixName": content["matrixName"],
        "matrixDetails": content["details"]
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
    }
    response = requests.post(f"http://statistici.insse.ro:8077/tempo-ins/matrix/dataSet/{cod_matrice}",
                             data=json.dumps(post_payload), headers=headers)
    response_content = json.loads(response.content)

    indicator = post_data[-1][0]['label']

    pprint(f"Json response {response_content}")
    # trebuie sa iau cati indicatori iau de la final
    # produsul lungimii fiecarui parametru selectat (2 * 3 * 2)
    nr_selected_elements = 1
    for element in query_list:
        nr_selected_elements *= len(element[1])
    print(nr_selected_elements)

    json_output = []
    for arr_entry in response_content[len(response_content) - nr_selected_elements:]:
        output = {
            "matrixName": content["matrixName"],
            "matrixCode": cod_matrice,
            "indicator": indicator
        }
        other_fields = len(arr_entry) - len(ani)
        # pun label-urile selectate in output-ul json
        for label in arr_entry[:other_fields]:
            label = label.strip()
            if label in found_labels:
                output[found_labels[label]] = label

        ani_index = 0
        for number in arr_entry[other_fields:]:
            digits = re.findall(r"\d+", number)
            if digits:
                output[ani[ani_index]] = digits[0]
                ani_index += 1
        json_output.append(output)
    return json_output
