from django.test import TestCase
from recipegenerator.models import Recipe, Ingredient, Restriction

# Create your tests here.

class IngredientTestCase(TestCase):
    def setUp(self):
        Ingredient.objects.create(id='1', name='peanut', amount=1, protein=1, fat=1, carbs=1, calories=1)
        Ingredient.objects.create(id='2', name='almond', amount=2, protein=1, fat=1, carbs=1, calories=1)

    def test_constructor(self):
        one = Ingredient.objects.get(id="1")
        two = Ingredient.objects.get(id="2")
        self.assertEqual(one.name, 'peanut')
        self.assertEqual(two.name, 'almond')

    def test_str(self):
        one = Ingredient.objects.get(id="1")
        two = Ingredient.objects.get(id="2")
        self.assertEqual(str(one), 'peanut')
        self.assertEqual(str(two), 'almond')

    def test_get_calories_per_gram(self):
        one = Ingredient.objects.get(id="1")
        two = Ingredient.objects.get(id="2")
        self.assertEqual(one.get_calories_per_gram(), 1)
        self.assertEqual(two.get_calories_per_gram(), 0.5)
    
    def test_get_protein_per_gram(self):
        one = Ingredient.objects.get(id="1")
        two = Ingredient.objects.get(id="2")
        self.assertEqual(one.get_calories_per_gram(), 1)
        self.assertEqual(two.get_calories_per_gram(), 0.5)

    def test_get_fat_per_gram(self):
        one = Ingredient.objects.get(id="1")
        two = Ingredient.objects.get(id="2")
        self.assertEqual(one.get_calories_per_gram(), 1)
        self.assertEqual(two.get_calories_per_gram(), 0.5)

    def test_get_carbs_per_gram(self):
        one = Ingredient.objects.get(id="1")
        two = Ingredient.objects.get(id="2")
        self.assertEqual(one.get_calories_per_gram(), 1)
        self.assertEqual(two.get_calories_per_gram(), 0.5)

class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(name='test1', ingredients='["egg", "salt"]', proteinLevel='high', fatLevel='low')
        Recipe.objects.create(name='test2', ingredients='["egg", "salt", "pepper"]', proteinLevel='low', fatLevel='low')

    def test_constructor(self):
        one = Recipe.objects.get(name="test1")
        two = Recipe.objects.get(name="test2")
        self.assertEqual(one.proteinLevel, 'high')
        self.assertEqual(two.proteinLevel, 'low')

    def test_str(self):
        one = Recipe.objects.get(name="test1")
        two = Recipe.objects.get(name="test2")
        self.assertEqual(str(one), 'test1')
        self.assertEqual(str(two), 'test2')

    def test_get_ingredients(self):
        one = Recipe.objects.get(name="test1")
        two = Recipe.objects.get(name="test2")
        self.assertEqual(one.get_ingredients(), ["egg", "salt"])
        self.assertEqual(two.get_ingredients(), ["egg", "salt", "pepper"])

class RestrictionTestCase(TestCase):
    def setUp(self):
        Restriction.objects.create(id="1", ingredientId=1, userName="name1")
        Restriction.objects.create(id="2", ingredientId=1, userName="name2")

    def test_constructor(self):
        one = Restriction.objects.get(id="1")
        two = Restriction.objects.get(id="2")
        self.assertEqual(one.userName, 'name1')
        self.assertEqual(two.userName, 'name2')

    def test_str(self):
        one = Restriction.objects.get(id="1")
        two = Restriction.objects.get(id="2")
        self.assertEqual(str(one), '1')
        self.assertEqual(str(two), '2')