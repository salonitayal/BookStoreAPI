from django.urls import path, include
# from booklistapp.api.views import book_list, book_details
from booklistapp.api.views import BookListAV, BookDetailAV, PublisherListAV, ReviewCreate, ReviewList, ReviewDetail

urlpatterns = [
    path('list/', BookListAV.as_view(), name='book_list'),
    path('<int:pk>', BookDetailAV.as_view(), name='book_detail'),
    path('publisher_list/', PublisherListAV.as_view(), name='publisher'),

    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
