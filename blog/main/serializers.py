#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag