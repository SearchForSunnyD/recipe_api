import requests
from db_models import Recipe, db


class Handler:
    def __init__(self):
        self.links = None
        self.recipe = None
        self.recipes = []
        self.ind_from = None
        self.ind_to = None
        self.count = None
        self.next = None
        self.app_id = "f3fa218a"
        self.app_key = "ad05961d4687f056aa92d3012ff082f7"
        self.type = "public"

    def set_vals(self, json):
        self.links = json["_links"]
        self.reset_recipes()
        self.update_recipes(json)
        self.ind_from = json["from"]
        self.ind_to = json["to"]
        self.count = json["count"]
        self.next = json["_links"]["next"]["href"]

    def reset_recipes(self):
        self.recipes = []

    def update_recipes(self, json):
        for r in json["hits"]:
            recipe_uri = r["recipe"]["uri"]

            existing_recipe = Recipe.query.filter_by(uri=recipe_uri).first()

            curr_recipe = Recipe_holder(r["recipe"])

            if existing_recipe:
                curr_recipe.id = existing_recipe.id
                self.recipes.append(curr_recipe)
            else:
                new_recipe = Recipe(uri=recipe_uri, name=r["recipe"]["label"])
                db.session.add(new_recipe)
                db.session.commit()

                curr_recipe.id = new_recipe.id
                self.recipes.append(curr_recipe)

    def api_query(self, args, q="Dinner"):
        url = "https://api.edamam.com/api/recipes/v2"
        params = {
            "q": q,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "type": self.type,
        }
        for args_dict in args:
            params.update(args_dict)

        response = requests.get(url, params)

        if response.status_code == 200 and len(response.json()["hits"]) != 0:
            self.set_vals(response.json())
            return True
        else:
            return False

    def api_uri_query(self, id):
        url = "https://api.edamam.com/api/recipes/v2/by-uri"

        r = Recipe.query.get_or_404(id)

        params = {
            "uri": r.uri,
            "app_id": self.app_id,
            "app_key": self.app_key,
            "type": self.type,
        }

        response = requests.get(url, params)

        if response.status_code == 200 and len(response.json()["hits"]) != 0:
            self.recipe = Recipe_holder(response.json()["hits"][0]["recipe"])
            return True
        else:
            return False

    @property
    def next_page(self):
        if self.next:
            response = requests.get(self.next)
            if response.status_code == 200:
                self.update_recipes(response.json())
                self.next = response.json()["_links"]["next"]["href"]
                return True
        return False


class Recipe_holder:
    def __init__(self, recipe_data):
        self.id = None
        self.uri = recipe_data["uri"] if "uri" in recipe_data else None
        self.label = recipe_data["label"] if "label" in recipe_data else None
        self.image = recipe_data["image"] if "image" in recipe_data else None
        self.source = recipe_data["source"] if "source" in recipe_data else None
        self.url = recipe_data["url"] if "url" in recipe_data else None
        self.yield_value = recipe_data["yield"] if "yield" in recipe_data else None
        self.dietLabels = (
            recipe_data["dietLabels"] if "dietLabels" in recipe_data else None
        )
        self.healthLabels = (
            recipe_data["healthLabels"] if "healthLabels" in recipe_data else None
        )
        self.cautions = recipe_data["cautions"] if "cautions" in recipe_data else None
        self.ingredientLines = (
            recipe_data["ingredientLines"] if "ingredientLines" in recipe_data else None
        )
        self.ingredients = (
            [Ingredient(ingredient) for ingredient in recipe_data["ingredients"]]
            if "ingredients" in recipe_data
            else None
        )
        self.calories = recipe_data["calories"] if "calories" in recipe_data else None
        self.totalCO2Emissions = (
            recipe_data["totalCO2Emissions"]
            if "totalCO2Emissions" in recipe_data
            else None
        )
        self.co2EmissionsClass = (
            recipe_data["co2EmissionsClass"]
            if "co2EmissionsClass" in recipe_data
            else None
        )
        self.totalWeight = (
            recipe_data["totalWeight"] if "totalWeight" in recipe_data else None
        )
        self.totalTime = (
            recipe_data["totalTime"] if "totalTime" in recipe_data else None
        )
        self.cuisineType = (
            recipe_data["cuisineType"] if "cuisineType" in recipe_data else None
        )
        self.mealType = recipe_data["mealType"] if "mealType" in recipe_data else None
        self.dishType = recipe_data["dishType"] if "dishType" in recipe_data else None
        self.totalNutrients = (
            recipe_data["totalNutrients"] if "totalNutrients" in recipe_data else None
        )
        self.totalDaily = (
            recipe_data["totalDaily"] if "totalDaily" in recipe_data else None
        )
        self.digest = recipe_data["digest"] if "digest" in recipe_data else None
        self.tags = recipe_data["tags"] if "tags" in recipe_data else None

    def __repr__(self):
        return self.label


class Ingredient:
    def __init__(self, ingredient_data):
        self.text = ingredient_data["text"] if "text" in ingredient_data else None
        self.quantity = (
            ingredient_data["quantity"] if "quantity" in ingredient_data else None
        )
        self.measure = (
            ingredient_data["measure"] if "measure" in ingredient_data else None
        )
        self.food = ingredient_data["food"] if "food" in ingredient_data else None
        self.weight = ingredient_data["weight"] if "weight" in ingredient_data else None
        self.foodCategory = (
            ingredient_data["foodCategory"]
            if "foodCategory" in ingredient_data
            else None
        )
        self.foodId = ingredient_data["foodId"] if "foodId" in ingredient_data else None
        self.image = ingredient_data["image"] if "image" in ingredient_data else None
