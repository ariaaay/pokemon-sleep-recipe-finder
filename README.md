# pokemon-sleep-recipe-finder
Code to find recipes based on your current ingrendients, pot size and unknown recipes options.

Required packages:
numpy

```
pip install numpy
```

Modify the number of ingredients, pot limit, your name (if you use the sripts with your friends) and potential recipes in `find_recipe.py`. 
Then run:
```
python find_recipe.py
```
which outputs `recipe_to_try_[your_name].txt` that listed all possible dishes.

After you tried the dishes, add the ones your have tried to `tried_[dish].txt' (e.g. tried_salad.txt), so they will be excluded from next time.





