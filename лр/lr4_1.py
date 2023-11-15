import json
def task() -> float:
    file_name = "input.json"
    with open(file_name, 'r') as file:
        data = json.load(file)
    summa = sum([item["score"] * item["weight"] for item in data])
    return summa
print(f"{task():.3f}")

