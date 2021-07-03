from django.test import TestCase
from django.urls import resolve

# Create your tests here.

from solos.views import index

class SolosURLsTestCase(TestCase):
    def test_root_url_uses_index_view(self):
        root = resolve('/solos/')
        print('root dir',dir(root))
        print('root class: ', root.view_name)
        print('our root', dir(index.as_view()))
        self.assertEqual(root.view_name, index.as_view().__qualname__)
