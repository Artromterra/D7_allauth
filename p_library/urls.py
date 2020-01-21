from allauth.account.views import login, logout
from django.contrib import admin 
from p_library import views
from p_library.views import index
from django.urls import path  
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, FriendList, FriendFormEdit, books_friends_create, book_decrement, book_increment

app_name = 'p_library'  
urlpatterns = [ 
	path('', index, name='index'),
	path('login/', login, name='login'),  
	path('logout/', logout, name='logout'),
	path('book_list/', views.book_list, name='book_list'), 
	path('book_list/book_increment/', views.book_increment),
    path('book_list/book_decrement/', views.book_decrement),
	path('publisher_new/', views.publisher_new, name='publisher_new'),
	path('friend_list/', views.friend_list, name='friend_list'),
	path('author/create', AuthorEdit.as_view(), name='author_create'),  
	path('author_list/', AuthorList.as_view(), name='author_list'),
	path('author/create_many', author_create_many, name='author_create_many'),
	path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
	path('friend/create', FriendFormEdit.as_view(), name='friend_create'),
	path('friends', FriendList.as_view(), name='friend_form'),
	path('book_friend/create', books_friends_create, name='book_friend_create'),
	]