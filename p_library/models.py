from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):  
  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

class Author(models.Model):
	full_name = models.TextField(blank=True, null=True)
	birth_year = models.SmallIntegerField()
	country = models.CharField(max_length=2)

	def __str__(self):
		return self.full_name

class Publisher(models.Model):
	name = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.name

class Friend(models.Model):
	friend_name = models.CharField(max_length=30)

	def __str__(self):
		return self.friend_name

class Book(models.Model):
	ISBN = models.CharField(max_length=13)
	title = models.TextField()
	description = models.TextField()
	year_release = models.SmallIntegerField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True, related_name='books')
	copy_count = models.SmallIntegerField(default=1)
	price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
	friend = models.ManyToManyField(Friend, blank=True, related_name='books')
	image = models.ImageField(upload_to='picture/%Y/%m/%d', blank=True)

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url

	def __str__(self):
		return self.title


