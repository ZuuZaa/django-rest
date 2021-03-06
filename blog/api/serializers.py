from rest_framework import serializers
from blog.models import BlogModel

class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id','title', 'content']