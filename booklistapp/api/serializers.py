from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from booklistapp.models import Book, Publisher, Review

# Why to use serializer?
# As when we were doing it in views then we had to
# change it in the iterable form and then send a JSONresponse()
# But serializer simplifies it. It directly does that.
# here after conversion to JSON we call it in api/views 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only = True)
    # read_only means while adding book or magazine then we cant add review at that time
    # we can add review through review serializer only

    len_name = serializers.SerializerMethodField()
    # to be used for Custom serializer field method
    # if we dont have model for this then also we can display it in
    # our JSON response
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ['id', 'title', 'description'] or simply use exclude
        # exclude = ['active']

    def get_len_name(self, object): # Custom serializer field method
        return len(object.title)

    def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and Description can't be same!")
        return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short!")
        return value

class PublisherSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Publisher
        fields = "__all__"




# def name_length(value):
#     if len(value) < 2:
#             raise serializers.ValidationError("Title is too short!")

# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description can't be same!")
#         return data

#     # # field level validation
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short!")
#     #     return value