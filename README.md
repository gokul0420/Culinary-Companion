# 🍽️ Dish Recommendation System using Cosine Similarity

This project recommends dishes based on a list of user-input ingredients. It uses **Cosine Similarity** to find the most similar dish vectors from a dataset of 100 dishes.

---

## 📂 Files

- `dishes_100.xlsx`: Contains 100 dishes and their respective ingredients.
- `recommend.py`: Python script that takes user input and recommends dishes.

---

## 📊 Dataset Format (dishes_100.xlsx)

| Dish Name | Ingredients                     |
|-----------|----------------------------------|
| Dish 1    | tomato,onion,garlic,salt         |
| Dish 2    | pasta,tomato,cheese,olive oil    |
| ...       | ...                              |

Each row represents a dish with its comma-separated ingredients.

---

## 🔧 How It Works

1. **Loads the dataset** from `dishes_100.xlsx`.
2. **Builds an ingredient vocabulary** dynamically.
3. **Encodes ingredients** of each dish into binary vectors.
4. **Takes user input**, encodes it similarly.
5. **Calculates cosine similarity** between user vector and each dish vector.
6. **Ranks dishes** and returns the most similar ones.

---

## ▶️ How to Run

### Step 1: Install Dependencies

```bash
pip install pandas scikit-learn openpyxl
