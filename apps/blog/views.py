from django.shortcuts import render, redirect

from .models import Book, Author,  Comment #User
from .forms import BookForm, AuthorForm, CommentForm, CreateUserForm, LoginForm #, UserForm,




def  home(request):
    context = {
        'title': "Project X",
    }
    return render(request, 'blog/home.html', context = context)





# create views for Creating and Login 
# register user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            #return redirect('')
    
    context = {
        'form': form,
    }

    return render(request, 'blog/users/register.html', context=context)




def library(request):

    books = Book.objects.all()


    context = {
        'title': "Library",
        'books': books
    }

    return render(request, 'blog/books/books.html', context = context)



def bookCreate(request):  
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('library')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'blog/books/add_book.html',{'form':form})  

def bookUpdate(request, id):  
    book = Book.objects.get(id=id)
    form = BookForm(initial={'title': book.title, 'genre': book.book_genre, 'author': book.author, 'published': book.published})
    if request.method == "POST":  
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('library')  
            except Exception as e: 
                pass    
    return render(request,'blog/books/book_update.html',{'form':form})  

def bookDelete(request, id):
    book = Book.objects.get(id=id)
    try:
        book.delete()
    except:
        pass
    return redirect('library')


def bookDetail(request, id):
    
    book = Book.objects.get(id=id)

    context = {
        'book': book,
        'title': "Book Details",
    }

    return render(request, 'blog/books/book_detail.html', context = context)

# Author List, update / delete

def authors(request):

    authors = Author.objects.all()

    context = {
        'title': ' List of Authors',
        'authors': authors,
    }
    return render(request, 'blog/authors/authors.html', context = context)


def authorCreate(request):  
    if request.method == "POST":  
        form = AuthorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('authors')  
            except:  
                pass  
    else:  
        form = AuthorForm()  
    return render(request,'blog/authors/add_author.html',{'form':form})  


def authorUpdate(request, id):  
    author = Author.objects.get(id=id)
    form = AuthorForm(initial={'fname': author.fname, 'lname': author.lname})
    if request.method == "POST":  
        form = AuthorForm(request.POST, instance=author)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('authors')  
            except Exception as e: 
                pass    
    return render(request,'blog/authors/author_update.html',{'form':form})  

def authorDelete(request, id):
    author = Author.objects.get(id=id)
    try:
        author.delete()
    except:
        pass
    return redirect('authors')


## Users and Comments are under Blog Section

# # User List, update / delete

# def users(request):

#     users = User.objects.all()

#     context = {
#         'title': ' List of Users',
#         'users': users,
#     }
#     return render(request, 'blog/users/users.html', context = context)


# def userCreate(request):  
#     if request.method == "POST":  
#         form = UserForm(request.POST)  
#         if form.is_valid():  
#             try:  
#                 form.save() 
#                 model = form.instance
#                 return redirect('users')  
#             except:  
#                 pass  
#     else:  
#         form = UserForm()  
#     return render(request,'blog/users/add_user.html',{'form':form})  


# def userUpdate(request, id):  
#     user = User.objects.get(id=id)
#     form = UserForm(initial={'username': user.username, 'email': user.user_email})
#     if request.method == "POST":  
#         form = UserForm(request.POST, instance=user)  
#         if form.is_valid():  
#             try:  
#                 form.save() 
#                 model = form.instance
#                 return redirect('users')  
#             except Exception as e: 
#                 pass    
#     return render(request,'blog/users/user_update.html',{'form':form})  

# def userDelete(request, id):
#     user = User.objects.get(id=id)
#     try:
#         user.delete()
#     except:
#         pass
#     return redirect('users')



## Comments


def comments(request):

    comments = Comment.objects.all()

    context = {
        'title': ' List of Users',
        'comments': comments,
    }
    return render(request, 'blog/comments/comments.html', context = context)


def commentCreate(request):  
    if request.method == "POST":  
        form = CommentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('comments')  
            except:  
                pass  
    else:  
        form = CommentForm()  
    context = {
        'form': form,
        'title': "Add new Comment",
        'user': "Ioannis"
    }
    return render(request,'blog/comments/add_comment.html',context)  

# reply to comment
def relpyComment(request, id):
    pass


# update comment
def commentUpdate(request, id):  
    comment = Comment.objects.get(id=id)
    form = UserForm(initial={'comment': comment.comment, 'user': comment.user})
    if request.method == "POST":  
        form = CommentForm(request.POST, instance=comment)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('comments')  
            except Exception as e: 
                pass    
    return render(request,'blog/comments/comment_update.html',{'form':form})  



def commentDelete(request, id):
    comment = Comment.objects.get(id=id)
    try:
        comment.delete()
    except:
        pass
    return redirect('comments')


