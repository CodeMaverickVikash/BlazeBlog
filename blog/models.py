from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog_categories(models.Model):
	category = models.CharField(max_length=50)
	desc = models.TextField()
	slug = models.SlugField(unique=True, null = True, blank = True)

	def __str__(self):
		return self.category

from .slug.cat_slugify import *
@receiver(pre_save, sender=Blog_categories)
def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)


class BlogPost(models.Model):
	# cat1 = models.ForeignKey(Blog_categories, on_delete=models.CASCADE)
	cat_slug = models.CharField(max_length=300, default="")
	blg_title = models.CharField(max_length=50)
	blg_desc = models.TextField()
	slug = models.SlugField(unique=True, null = True, blank = True)

from .slug.blog_slugify import *
@receiver(pre_save, sender=BlogPost)
def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

class Cantact(models.Model):
	full_name = models.CharField(max_length=255)
	email_address = models.EmailField()
	password = models.CharField(max_length=255)

# class Post_Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
#     like = models.IntegerField(null=True)

#     def __str__(self):
#         return self.post.title+"--"+str(self.like)