import json

Kny_data = {
    "title": "Kimetsu no Yaiba",
    "episodes": 63,
    "Author": "Koyoharu Gotoge",
    "Year": 2019,
    "Studio": "Ufotable"
}

with open('Kny_data', 'w', encoding='utf-8') as f:
    json.dump(Kny_data, f, ensure_ascii=False, indent=4)
with open('Kny_data', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)