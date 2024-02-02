\c recipe_app

INSERT INTO filter_types (NAME, VALUE)
VALUES
    ('Diet', 'diet'),
    ('Health', 'health'),
    ('Cuisine', 'cuisineType'),
    ('Meal', 'mealType'),
    ('Dish', 'dishType');
INSERT INTO
    filters (VALUE,NAME, f_type)
VALUES
    ('balanced', 'Balanced', 1),
    ('high-fiber', 'High-Fiber', 1),
    ('high-protein', 'High-Protein', 1),
    ('low-carb', 'Low-Carb', 1),
    ('low-fat', 'Low-Fat', 1),
    ('low-sodium', 'Low-Sodium', 1),
    ('alcohol-cocktail', 'Alcohol-Cocktail', 2),
    ('alcohol-free', 'Alcohol-Free', 2),
    ('celery-free', 'Celery-Free', 2),
    ('crustacean-free', 'Crustacean-Free', 2),
    ('dairy-free', 'Dairy-Free', 2),
    ('DASH', 'DASH', 2),
    ('egg-free', 'Egg-Free', 2),
    ('fish-free', 'Fish-Free', 2),
    ('fodmap-free', 'FODMAP-Free', 2),
    ('gluten-free', 'Gluten-Free', 2),
    ('immuno-supportive', 'Immuno-Supportive', 2),
    ('keto-friendly', 'Keto-Friendly', 2),
    ('kidney-friendly', 'Kidney-Friendly', 2),
    ('kosher', 'Kosher', 2),
    ('low-fat-abs', 'Low-Fat-ABS', 2),
    ('low-potassium', 'Low-Potassium', 2),
    ('low-sugar', 'Low-Sugar', 2),
    ('lupine-free', 'Lupine-Free', 2),
    ('Mediterranean', 'Mediterranean', 2),
    ('mollusk-free', 'Mollusk-Free', 2),
    ('mustard-free', 'Mustard-Free', 2),
    ('no-oil-added', 'No-Oil-Added', 2),
    ('paleo', 'Paleo', 2),
    ('peanut-free', 'Peanut-Free', 2),
    ('pescatarian', 'Pescatarian', 2),
    ('pork-free', 'Pork-Free', 2),
    ('red-meat-free', 'Red-Meat-Free', 2),
    ('sesame-free', 'Sesame-Free', 2),
    ('shellfish-free', 'Shellfish-Free', 2),
    ('sugar-conscious', 'Sugar-Conscious', 2),
    ('sulfite-free', 'Sulfite-Free', 2),
    ('tree-nut-free', 'Tree-Nut-Free', 2),
    ('vegan', 'Vegan', 2),
    ('wheat-free', 'Wheat-Free', 2),
    ('vegetarian', 'Vegetarian', 2),
    ('soy-free', 'Soy-Free', 2),
    ('American', 'American', 3),
    ('Asian', 'Asian', 3),
    ('British', 'British', 3),
    ('Caribbean', 'Caribbean', 3),
    ('Central Europe', 'Central Europe', 3),
    ('Chinese', 'Chinese', 3),
    ('Eastern Europe', 'Eastern Europe', 3),
    ('French', 'French', 3),
    ('Indian', 'Indian', 3),
    ('Italian', 'Italian', 3),
    ('Japanese', 'Japanese', 3),
    ('Kosher', 'Kosher', 3),
    ('Mediterranean', 'Mediterranean', 3),
    ('Mexican', 'Mexican', 3),
    ('Middle Eastern', 'Middle Eastern', 3),
    ('Nordic', 'Nordic', 3),
    ('South American', 'South American', 3),
    ('South East Asian', 'South East Asian', 3),
    ('Breakfast', 'Breakfast', 4),
    ('Dinner', 'Dinner', 4),
    ('Lunch', 'Lunch', 4),
    ('Snack', 'Snack', 4),
    ('Teatime', 'Teatime', 4),
    ('Biscuits and cookies', 'Biscuits and Cookies', 5),
    ('Bread', 'Bread', 5),
    ('Cereals', 'Cereals', 5),
    (
        'Condiments and sauces',
        'Condiments and Sauces',
        5),
    ('Desserts', 'Desserts', 5),
    ('Drinks', 'Drinks', 5),
    ('Main course', 'Main Course', 5),
    ('Pancake', 'Pancake', 5),
    ('Preps', 'Preps', 5),
    ('Preserve', 'Preserve', 5),
    ('Salad', 'Salad', 5),
    ('Sandwiches', 'Sandwiches', 5),
    ('Side dish', 'Side Dish', 5),
    ('Soup', 'Soup', 5),
    ('Starter', 'Starter', 5),
    ('Sweets', 'Sweets', 5);