import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_excel('dishes.xlsx')


all_ingredients = set()
dish_ingredients = []

for ingredients_str in df['Ingredients']:
    ingredients = [i.strip().lower() for i in ingredients_str.split(',')]
    dish_ingredients.append(ingredients)
    all_ingredients.update(ingredients)

ingredient_vocab = sorted(list(all_ingredients))

def encode_ingredients(ingredients, vocab):
    return [1 if item in ingredients else 0 for item in vocab]

dish_vectors = [encode_ingredients(ingredients, ingredient_vocab) for ingredients in dish_ingredients]


user_input = input("Enter your ingredients (comma-separated): ").lower()
user_ingredients = [i.strip() for i in user_input.split(',')]

user_vector = np.array(encode_ingredients(user_ingredients, ingredient_vocab)).reshape(1, -1)

similarities = cosine_similarity(user_vector, dish_vectors)[0]
ranked_indices = np.argsort(similarities)[::-1]


print("\nRecommended Dishes:")
for idx in ranked_indices:
    print(f"{df['Dish Name'][idx]} (similarity: {similarities[idx]:.2f})")
