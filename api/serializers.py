# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import BlogModel

# Create a model serializer
class BlogsSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = BlogModel
		fields = ('title', 'description')
