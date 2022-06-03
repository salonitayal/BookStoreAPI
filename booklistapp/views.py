# from django.shortcuts import render
# from booklistapp.models import Book
# from django.http import JsonResponse

# # Create your views here.
# def book_list(request):
#     books = Book.objects.all()      # we got the data in form of query set
#     data = {
#         'books' : list(books.values()) # convert it inot iterable like list 
#     }
#     return JsonResponse(data) # then render it

# def book_details(request, pk):
#     book = Book.objects.get(pk=pk)
#     data = {
#         'name' : book.name,
#         'description' : book.description,
#         'active' : book.active
#     }
#     return JsonResponse(data) 

# not gnna utilise it