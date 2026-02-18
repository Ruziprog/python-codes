import json

all_anime = {
    "anime_list": [
        {
            "title": "Jujutsu Kaisen",
            "episodes": 53,
            "Author": "Gege Akutami",
            "Year": 2020,
            "Studio": "MAPPA",
            "Rating": 8.2,
        },
        {
            "title": "Hunter x Hunter",
            "episodes": 148,
            "Author": "Yoshihiro Togashi",
            "Year": 2011,
            "Studio": "MadHouse",
            "Rating": 9.0,
        }
    ]
}


with open("all_anime.json", 'w', encoding='utf-8') as f:
    json.dump(all_anime, f, ensure_ascii=False, indent=4)
with open("all_anime.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)

with open("all_anime.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
best = max(data["anime_list"], key=lambda x: x["Rating"])
longest = max(data["anime_list"], key=lambda x: x["episodes"])
avg_rating = sum(anime["Rating"] for anime in data["anime_list"]) / len(data["anime_list"])

stats = {
    "best_anime": best["title"],
    "best_rating": best["Rating"],
    "longest_anime": longest["title"],
    "average_rating": round(avg_rating, 2),
    "total_episodes": longest['episodes'],
    "total_anime": len(data["anime_list"])
}

with open("anime_stats.json", 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)

print(stats)


with open("all_anime.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

new_anime = {
    "title": "Oshi no Ko",
    "episodes": 12,
    "Author": "Aka Akasaka",
    "Year": 2023,
    "Studio": "Doga Kobo",
    "Rating": 8.5,
    "Genre": "Drama, Mystery, Supernatural",
    "Protagonist": "Ai Hoshino",
    "Antagonist": "Unknown",
    "Son of Protagonist": "Aqua Hoshino",
    "Daughter of Protagonist": "Ruby Hoshino"
}

data["anime_list"].append(new_anime)

with open("all_anime.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("New anime added successfully!")


with open("all_anime.json", 'r', encoding='utf-8') as f:
    final_data = json.load(f)

for i, anime in enumerate(final_data["anime_list"], start=1):
    print(f"{i}. {anime['title']} - Rating: {anime['Rating']}")