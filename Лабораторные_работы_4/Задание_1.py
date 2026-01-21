# TODO решите задачу
import json


def task() -> float:
    with open ('input.json') as f:
        data = json.load(f)
    total = 0.0
    for i in data:
        total += i["score"] * i["weight"]
    return round(total, 3)

print(task())