with open("15.txt", 'r') as f:
    ingredients = f.readlines()

properties = {}

for ingredient in ingredients:
    ingredient = ingredient.split()
    name = ingredient[0][:-1]
    properties[name] = {}
    properties[name]["capacity"] = int(ingredient[2][:-1])
    properties[name]["durability"] = int(ingredient[4][:-1])
    properties[name]["flavor"] = int(ingredient[6][:-1])
    properties[name]["texture"] = int(ingredient[8][:-1])
    properties[name]["calories"] = int(ingredient[-1])

ingredients = list(properties.keys())

def recipes(ingredients, tsp):
    if len(ingredients) == 1:
        return [[tsp]]
    else:
        return [[i] + x for i in range(tsp + 1)
                for x in recipes(ingredients[1:], tsp - i)]

scores = set()
calorie_scores = set()

for recipe in recipes(ingredients, 100):
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for i, ingredient in enumerate(ingredients):
        capacity += recipe[i] * properties[ingredient]["capacity"]
        durability += recipe[i] * properties[ingredient]["durability"]
        flavor += recipe[i] * properties[ingredient]["flavor"]
        texture += recipe[i] * properties[ingredient]["texture"]
        calories += recipe[i] * properties[ingredient]["calories"]

    if any(p < 0 for p in (capacity, durability, flavor, texture)):
        score = 0
    else:
        score = capacity * durability * flavor * texture
    scores.add(score)

    if calories == 500:
        calorie_scores.add(score)

print(max(scores))
print(max(calorie_scores))
