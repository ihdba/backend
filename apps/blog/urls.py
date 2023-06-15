from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name=""),
    # books
    path('library', views.library, name="library"),
    path('add_book/', views.bookCreate, name="add_book"),
    path('book_update/<int:id>', views.bookUpdate, name="book_update"),
    path('book_delete/<int:id>', views.bookDelete, name="book_delete"),
    path('book_detail/<int:id>', views.bookDetail, name="book_detail"),
    # authors
    path('authors', views.authors, name="authors"),
    path('add_author/', views.authorCreate, name="add_author"),
    path('author_update/<int:id>', views.authorUpdate, name="author_update"),
    path('author_delete/<int:id>', views.authorDelete, name="author_delete"),
     # users

    path('register', views.register, name="register"),
    # path('users', views.users, name="users"),
    # path('add_user/', views.userCreate, name="add_user"),
    # path('user_update/<int:id>', views.userUpdate, name="user_update"),
    # path('user_delete/<int:id>', views.userDelete, name="user_delete"),

     # Blog Comments
    path('comments', views.comments, name="comments"),
    path('add_comment/', views.commentCreate, name="add_comment"),
    path('comments_update/<int:id>', views.commentUpdate, name="comment_update"),
    path('comment_delete/<int:id>', views.commentDelete, name="comment_delete"),

]