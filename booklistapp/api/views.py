from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

from booklistapp.models import Book, Publisher, Review
from booklistapp.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from booklistapp.api.serializers import BookSerializer, PublisherSerializer, ReviewSerializer

from booklistapp.api.throttling import ReviewCreateThrottle, ReviewListThrottle

# These are concrete view classes <review wali> 
# In them, we dont have to write CRUD functions, they are predefined
# Makes the work hassle free

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewCreateThrottle]
    

    def get_queryset(self):
        return Review.objects.all()
        
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(book=book, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this book!")
        
        if book.number_rating == 0:
            book.avg_rating = serializer.validated_data['rating']
        else:
            book.avg_rating = (book.avg_rating + serializer.validated_data['rating'])/2
        
        book.number_rating = book.number_rating+1

        serializer.save(book=book)

class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "review-data"
    #throttle_classes = [ReviewCreateThrottle, AnonRateThrottle]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(book=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AdminOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

class BookListAV(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:   
            return Response(serializer.errors)


class BookDetailAV(APIView):
    def get(self, request, pk):
        try:
            book  = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book  = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherListAV(APIView):
    def get(self, request):
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PublisherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:   
            return Response(serializer.errors)


class PublisherDetailAV(APIView):
    def get(self, request, pk):
        try:
            publisher  = Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            return Response({'Error': 'Publisher not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    def put(self, request, pk):
        publisher  = Publisher.objects.get(pk=pk)
        serializer = PublisherSerializer(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:   
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book_details(request, pk):
#     if request.method == 'GET':
#         try:
#             book  = Book.objects.get(pk=pk)
#         except Book.DoesNotExist:
#             return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         book  = Book.objects.get(pk=pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         book = Book.objects.get(pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

