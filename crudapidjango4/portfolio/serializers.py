from rest_framework import serializers
from .models import Category, Project, Page

class ProjectAPISerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'categories')
        
class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class ProjectSerializer(serializers.ModelSerializer):
    category = ProjectCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'start_date', 'category')

class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields =('_all_')
