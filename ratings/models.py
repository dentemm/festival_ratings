from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Score(models.Model):

	# Rating system makes use of contenttypes framework!
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	total_score = models.IntegerField(default=0)
	votes_count = models.PositiveIntegerField(default=0)
	average = models.FloatField(default=0)

	class Meta:

		unique_together = (
			('content_type', 'object_id')
		)

	def __unicode__(self):

		return 'Score voor %s' % (self.content_object, )

	def get_votes(self):
		'''
		Returns all related votes 
		'''

		return Vote.objects.filter(content_type=self.content_type, object_id=self.object_id)

	def recalculate(self, commit=True):

		# Score is updated by aggregating Vote data
		# total_score is sum of all Vote scores, and count is number of Vote objects (id is pk, so unique)
		current_score = self.get_votes().aggregate(total_score=models.Sum('score'), votes_count=models.Count('id'))

		self.total_score = current_score['total_score'] or 0
		self.votes_count = current_score['votes_count'] 

		if self.votes_count:
			self.average = self.total_score / self.votes_count

		else:
			self.average = 0

		if commit:
			self.save()


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

