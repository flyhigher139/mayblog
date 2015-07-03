#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from . import models

class AuthorDisplayField(serializers.RelatedField):
    def to_representation(self, value):
        return value.account.display_name

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag

class PostSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True)
    # category = CategorySerializer()

    # author = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='username'
    #  )

    tags = serializers.SlugRelatedField(
        allow_null = True,
        slug_field = 'name',
        queryset = models.Tag.objects.all(),
        many = True
     )

    category = serializers.SlugRelatedField(
        allow_null = True,
        slug_field = 'name',
        queryset = models.Category.objects.all()
     )

    author = AuthorDisplayField(read_only=True)

    class Meta:
        model = models.Post 
        fields = ('id', 'title', 'abstract', 'raw', 'pub_time', 'update_time', 'author', 'category', 'tags')

        extra_kwargs = {'raw': {'write_only': True}}
