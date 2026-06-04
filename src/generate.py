import csv

csv_path = ""


def load_action_label(csv_path: str) -> dict:
    actions = {}
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            actions[row] = {}
    return actions

