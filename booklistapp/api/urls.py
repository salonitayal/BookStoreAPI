from django.urls import path, include
# from booklistapp.api.views import book_list, book_details
from booklistapp.api.views import BookListAV, BookDetailAV, PublishersListAV

urlpatterns = [
    path('list/', BookListAV.as_view(), name='book_list'),
    path('<int:pk>', BookDetailAV.as_view(), name='book_detail'),
    path('publisher_list/', PublishersListAV.as_view(), name='publisher')
]
