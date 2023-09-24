# Scripts to find recipes based on current ingrendients, pot size and unknown recipes options. Need to manually copy tried options to the "tried" list.

import numpy as np
import pickle
import json

#########
# MODIFY THE FOLLOWING. Change name to use it across multiple people.
name = "aria"
dish = "drinks"
pot_limit = 48
items_dict = {"apple": 9, "herb": 15, "sausage": 17, "honey": 3, "cacao": 4, "milk": 19, "soybean": 16, "oil": 17, "tomato": 13}
##########


if dish == "stew":
    recipe_to_find =[]
    recipe_to_find.append([25, 8])
    recipe_to_find.append([18, 15, 12, 10])
    recipe_to_find.append([14, 10, 8])
    recipe_to_find.append([14, 9])
    recipe_to_find.append([12, 11, 8, 4])
    recipe_to_find.append([10, 8, 4])
    recipe_to_find.append([15, 9, 9, 5])
    recipe_to_find.append([10, 6])
    recipe_to_find.append([12, 6, 4, 4])

if dish == "salad":
    recipe_to_find =[]
    recipe_to_find.append([10, 10, 15])
    recipe_to_find.append([17, 8, 8])
    recipe_to_find.append([10, 6])
    recipe_to_find.append([14, 9, 7, 6])
    recipe_to_find.append([10, 6])
    recipe_to_find.append([9, 6, 5, 3])
    recipe_to_find.append([14, 9])
    recipe_to_find.append([17, 10, 8])
    recipe_to_find.append([10, 5])
    recipe_to_find.append([15, 5, 3])
    recipe_to_find.append([15, 15, 12, 11])
    recipe_to_find.append([10, 6])

if dish == "drinks":
    recipe_to_find =[]
    recipe_to_find.append([9, 5])
    recipe_to_find.append([14, 12, 5, 4])
    recipe_to_find.append([9, 7])
    recipe_to_find.append([20, 15, 10, 10])
    recipe_to_find.append([11, 9, 7, 8])
    recipe_to_find.append([12, 4])
    recipe_to_find.append([15, 11, 9])
    recipe_to_find.append([8, 7])


def find_recipe(recipe_to_find, items_dict, pot_limit):
    all_trial_list = []
    for recipe in recipe_to_find:
        if np.sum(recipe) > pot_limit:
            continue

        n_ingr = len(recipe)
        item_list = []
        for ingr_num in recipe:
            valid_item = [k for k, v in items_dict.items() if v > ingr_num]
            if valid_item == []:
                continue
            item_list.append(valid_item)

        # print("possible recipe:" + str(recipe))
        # print(item_list)
        if item_list == []:
            continue
        if len(item_list) < len(recipe):
            continue
        

        trial_list = [{item: recipe[0]} for item in item_list[0]]
        for i in range(1,n_ingr):
            # print(i)
            for item in item_list[i]:
                # print(item)
                for d in trial_list:
                    if len(list(d.keys())) != i:
                        continue
                    if item in d.keys():
                        continue
                    else:
                        d_new = {**d, item: recipe[i]}
                        # print(d_new)
                        trial_list.append(d_new)
        # print("before pruning")
        # print(trial_list)
        for d in trial_list:
            if len(list(d.keys())) >= len(recipe):
                if d not in all_trial_list:
                    all_trial_list.append(d)
    return all_trial_list


trial_list = find_recipe(recipe_to_find, items_dict, pot_limit)

tried_dict = {}
try:
    with open("tried_%s.txt" % dish, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\'", "\"")
            try:
                d = json.loads(line)
            except json.decoder.JSONDecodeError:
                pass
            try:
                trial_list.remove(d)
            except ValueError:
                pass

            for t in trial_list:
                if set(t.keys()) == set(d.keys()):
                    strictly_smaller = [t[k] <= d[k] for k in t.keys()]
                    if sum(strictly_smaller) == len(list(t.keys())):
                        trial_list.remove(t)

except FileNotFoundError:
    f = open("tried_%s.txt" % dish, "w+")
    f.close()

to_remove = []
for i, r1 in enumerate(trial_list):
    for j, r2 in enumerate(trial_list):
        if i != j:
            if set(r1.keys()) == set(r2.keys()):
                strictly_smaller = [r1[k] <= r2[k] for k in r1.keys()]
                if sum(strictly_smaller) == len(list(r1.keys())):
                    to_remove.append(r1)
                    # print("*****")
                    # print(r1)
                    # print(r2)

for re in to_remove:
    try:
        trial_list.remove(re)
    except ValueError:
        # print(re)
        pass

print("Number of Recipe found: "+ str(len(trial_list)))
f = open("recipe_to_try_%s.txt" % name, "w")
for r in trial_list:
    f.write(str(r) + "\n")
f.close()





                

                
            
            









            
        