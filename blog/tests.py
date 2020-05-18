from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
class BlogTests(TestCase):

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			)