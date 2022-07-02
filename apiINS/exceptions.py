from typing import List


class CouldNotFindValue(Exception):

    def __init__(self, label, labels_to_search: List[str]):
        self.label = label
        self.labels_to_search = labels_to_search

    def __str__(self):
        return f"For label {self.label} could not find {self.labels_to_search}"


class CouldNotFindFieldLabel(Exception):

    def __init__(self, label):
        self.label = label

    def __str__(self):
        return f"Could not find label {self.label}"