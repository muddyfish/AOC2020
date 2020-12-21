
with open("21.txt") as f:
    foods = []
    for line in f.readlines():
        ingredients, allergens = line.strip()[:-1].split(" (contains ")
        ingredients = set(ingredients.split(" "))
        allergens = set(allergens.split(", "))
        foods.append((ingredients, allergens))

all_foods = {ingredient for ingredients, allergens in foods for ingredient in ingredients}
all_allergens = {allergen for ingredients, allergens in foods for allergen in allergens}


def update_allergens():
    for allergen in all_allergens:
        for ingredients, allergens in foods:
            if allergen in allergens:
                allergen_mapping[allergen] &= ingredients


allergen_mapping = {}
for allergen in all_allergens:
    allergen_mapping[allergen] = all_foods.copy()
update_allergens()

impossible_foods = all_foods - set().union(*allergen_mapping.values())

for ingredients, allergens in foods:
    ingredients -= impossible_foods

final_allergen_mapping = {}

while allergen_mapping:
    to_remove = {k for k, v in allergen_mapping.items() if len(v) == 1}
    for ingredients, allergens in foods:
        allergens -= to_remove
        for k in to_remove:
            final_allergen_mapping[next(iter(allergen_mapping[k]))] = k
            ingredients -= allergen_mapping[k]
    for k in to_remove:
        del allergen_mapping[k]
    update_allergens()

print(",".join(sorted(final_allergen_mapping, key=lambda k: final_allergen_mapping[k])))
