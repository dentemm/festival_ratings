from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$', views.RatingView.as_view(), name='ratings'),

]