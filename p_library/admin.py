from django.contrib import admin
from p_library.models import Book, Author, Publisher, Friend, UserProfile

@admin.register(UserProfile)  
class ProfileAdmin(admin.ModelAdmin):  
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author',)
	fields = ('image', 'friend', 'ISBN', 'title', 'description', 'year_release', 'author', 'price',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'description',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
	pass

# Register your models here.
