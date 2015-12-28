from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Vote(models.Model):

	# Rating system makes use of contenttypes framework!
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	user = models.ForeignKey(User, blank=True, null=True, related_name='votes')
	score = models.IntegerField()

	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:

		unique_together = (
			('content_type', 'object_id', 'user')
		)

