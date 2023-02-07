from django.test import TestCase
from recipegenerator.models import Recipe

# Create your tests here.

class RecipeTestCase(TestCase):
    def setUp(self):
        self.recipe1 = Recipe()
        self.recipe2 = Recipe("fried egg", 1, ["egg", "salt", "pepper", "olive oil"])

    def test_constructor(self):
        self.assertEqual(self.recipe1.name, "")
        self.assertEqual(self.recipe2.name, "fried egg")
    
    def test_getName(self):
        self.assertEqual(self.recipe1.getName(), "")
        self.assertEqual(self.recipe2.getName(), "fried egg")