
with open("21.txt") as f:
    foods = []
    for line in f.readlines():
        ingredients, allergens = line.strip()[:-1].split(" (contains ")
        ingredients = set(ingredients.split(" "))
        allergens = set(allergens.split(", "))
        foods.append((ingredients, allergens))

all_foods = {ingredient for ingredients, allergens in foods for ingredient in ingredients}
all_allergens = {allergen for ingredients, allergens in foods for allergen in allergens}

allergen_mapping = {}
for allergen in all_allergens:
    allergen_mapping[allergen] = cur = all_foods.copy()
    for ingredients, allergens in foods:
        if allergen in allergens:
            cur &= ingredients

impossible_foods = all_foods - set().union(*allergen_mapping.values())

print(sum(len(ingredients & impossible_foods) for ingredients, allergens in foods))

