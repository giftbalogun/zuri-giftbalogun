from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	text = models.TextField()
	author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE,related_name='blog_posts')
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now= True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.title
