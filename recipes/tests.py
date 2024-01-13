from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_corret(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_with_args_is_correct(self):
        category_url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(category_url, '/recipes/category/1/')

    def test_recipe_url_is_correct(self):
        recipe_url = reverse('recipes:detail', kwargs={'id': 1})
        self.assertEqual(recipe_url, '/recipes/1/')
