# AI Recommendation System

# Recommendation dataset
recommendations = {
    "action": ["John Wick", "Extraction", "Mission Impossible"],
    "comedy": ["3 Idiots", "Golmaal", "Hera Pheri"],
    "romance": ["The Notebook", "Titanic", "La La Land"],
    "horror": ["The Conjuring", "Insidious", "Annabelle"],
    "technology": ["Python Course", "AI Basics", "Machine Learning"],
    "sports": ["Football Highlights", "Cricket World Cup", "Sports Documentary"],
    "music": ["Arijit Singh Playlist", "Lo-fi Beats", "Classical Music"]
}

# Print recomendation
print("===== AI Recommendation System =====")
print("Available Interests:")

for item in recommendations:
    print("-", item)

user_input = input("\nEnter your interest: ").lower()

if user_input in recommendations:
    print("\nRecommended Items:")
    for i, item in enumerate(recommendations[user_input], start=1):
        print(f"{i}. {item}")
else:
    print("\nSorry! No recommendations found.")