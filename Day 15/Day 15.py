with open('input.txt') as f:
    lines = f.read().splitlines()

# Part 1: Find most optimal cookie recipe by adding 100 teaspoons together
# Approach part 1 --> Only 4 ingredients present; brute force all possibilities of 100 teaspoons
# Approach part 2 --> As part 1 but also check on 500 calories

ingredients_data = dict()

for line in lines:
    line = line.replace(',', '')  # For easier reading the values after split
    # values = tuples of ints --> (capacity, durability, flavor, texture, calories)
    values = tuple(map(int, (line.split()[2], line.split()[4], line.split()[6], line.split()[8], line.split()[10])))
    ingredients_data[line.split(':')[0]] = values

ingredients = tuple(ingredients_data.keys())
maximum_score, maximum_score_with_500_calories = 0, 0
teaspoons = 100

for ingredient_1 in range(teaspoons + 1):
    for ingredient_2 in range(teaspoons + 1 - ingredient_1):
        for ingredient_3 in range(teaspoons + 1 - ingredient_1 - ingredient_2):
            for ingredient_4 in range(teaspoons + 1 - ingredient_1 - ingredient_2 - ingredient_3):
                if (ingredient_1 + ingredient_2 + ingredient_3 + ingredient_4) < 100:
                    continue
                # Exactl 100 spoons are used; calculate score
                teaspoons_per_ingeredient = {ingredients[0]: ingredient_1, ingredients[1]: ingredient_2,
                                             ingredients[2]: ingredient_3, ingredients[3]: ingredient_4}
                cap, dur, fla, tex, cal = 0, 0, 0, 0, 0
                for ingredient in ingredients:
                    cap += ingredients_data[ingredient][0] * teaspoons_per_ingeredient[ingredient]
                    dur += ingredients_data[ingredient][1] * teaspoons_per_ingeredient[ingredient]
                    fla += ingredients_data[ingredient][2] * teaspoons_per_ingeredient[ingredient]
                    tex += ingredients_data[ingredient][3] * teaspoons_per_ingeredient[ingredient]
                    cal += ingredients_data[ingredient][4] * teaspoons_per_ingeredient[ingredient]
                if cap <= 0 or dur <= 0 or fla <= 0 or tex <= 0:  # Required; -x * -y might result in higher score
                    current_score = 0
                else:
                    current_score = cap * dur * fla * tex
                if current_score > maximum_score:
                    maximum_score = current_score
                if cal == 500 and current_score > maximum_score_with_500_calories:
                    maximum_score_with_500_calories = current_score

print(f'The answer to part 1 is {maximum_score}')
print(f'The answer to part 2 is {maximum_score_with_500_calories}')
