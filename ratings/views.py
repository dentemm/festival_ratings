from django.shortcuts import render
from django.views.generic import View, TemplateView

from braces.views import LoginRequiredMixin

# Create your views here.
class RatingView(LoginRequiredMixin, TemplateView):

	template_name = 'rating-template.html'

	#def post(self, request, *args, **kwargs):

		# get score from URL attributes
		#pass

class LoginView(TemplateView):

	pass