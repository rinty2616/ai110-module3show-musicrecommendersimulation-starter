from src.recommender import load_songs, recommend_songs


def main():
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.3
        },
        "Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95
        }
    }

    for name, user_prefs in profiles.items():
        print(f"\n=== {name} ===\n")

        recommendations = recommend_songs(
            user_prefs, songs, k=5
        )

        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()