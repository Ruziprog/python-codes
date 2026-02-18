import json

anime_data = {
    "title": "Frieren: Beyond Journey's End",
    "episodes": 12,
    "Author": "Kanehito Yamada",
    "Genres": "Adventure, Fantasy, Supernatural",
    "Year": 2023,
    "Studio": "Mad House",
    "Rating": 8.9,
    "Protagonist": "Frieren"
}

with open('anime_data.json', 'w', encoding='utf-8') as f:
    json.dump(anime_data, f, ensure_ascii=False, indent=4)
with open('anime_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)


second_anime = {
    "title": "Kimetsu no Yaiba",
    "episodes": 63,
    "Author": "Koyoharu Gotoge",
    "Year": 2019,
    "Studio": "Ufotable"
}

with open('second_anime', 'w', encoding='utf-8') as f:
    json.dump(second_anime, f, ensure_ascii=False, indent=4)
with open('second_anime', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)