from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import BlogModel
from blog.api.serializers import BlogModelSerializer

@api_view(['GET'])
def api_detail_blog_view(request, id):
    try:
        blog_post = BlogModel.get(id=id)
    except BlogModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        seializer = BlogModelSerializer(blog_post)
        return Response(seializer.data)