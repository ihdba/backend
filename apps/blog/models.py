from django.db import models

# Create your models here.



# ## Classes to use in Blog app

class Author(models.Model):

    fname = models.CharField(max_length=50, verbose_name="First name")
    lname = models.CharField(max_length=50, verbose_name="Last name")
    alias = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.fname + ' ' + self.lname

    class Meta:
        verbose_name_plural = "Authors"

    
class Article(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Articles"

## class User

class User(models.Model):

    username = models.CharField(max_length=100, verbose_name="User Name")
    user_email = models.EmailField(verbose_name="Email")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Users"

# Class Comment
# Users can leave a comment on the article 
# as well as they can grade the article with stars
# later will be added user foreign key to Comment class

class Comment(models.Model):

    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "Comments"




class Book(models.Model):

    BOOK_GENRE = [
        ("SF", "Science Fiction"),
        ("MY", "Mystery"),
        ("CR", "Crime"),
        ("NO", "Novel"),
        ("CS", "Computer Science"),
        ("NS", "Natural Sciences"),
    ]

    title = models.CharField(max_length=250)
    book_genre = models.CharField(max_length=2, choices = BOOK_GENRE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    published = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Books"
