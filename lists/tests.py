from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        respones = home_page(request)
        self.assertTrue(respones.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', respones.content)
        self.assertTrue(respones.content.endswith(b'</html>'))
