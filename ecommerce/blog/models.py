from django.db import models
from django.forms import ModelForm

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	author = models.EmailField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()
	image = models.ImageField(upload_to="userimages/")

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=20)
	tweet = models.CharField(max_length=140)
	blog = models.ForeignKey('Blog')

	def __unicode__(self):
		return self.name

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ('name')
