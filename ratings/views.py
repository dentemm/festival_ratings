from django.shortcuts import render
from django.views.generic import View

from braces.views import LoginRequiredMixin

# Create your views here.
class RatingView(LoginRequiredMixin, View):

	def post(self, request, *args, **kwargs):

		# get score from URL attributes
		pass

