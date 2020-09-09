from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blog.models import BlogModel
from blog.api.serializers import BlogModelSerializer

@api_view(['GET','POST'])
def api_blog_view(request):
    if request.method == 'GET':
        blog_list = BlogModel.objects.all()
        serializers = BlogModelSerializer(blog_list, many=True)
        return Response(data=serializers.data)

    elif request.method == 'POST':
        serializer = BlogModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def api_detail_blog_view(request, id):

    try:
        blog_post = BlogModel.objects.get(id=id)
    except BlogModel.DoesNotExist:
        return Response(
            {'message':'blog post is not found'},
            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogModelSerializer(blog_post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BlogModelSerializer(blog_post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update is successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        operation = blog_post.delete()
        data = {}
        if operation:
            data['success':'blog post deleted successfuly']
        else:
            data['success':'delete is failed']
        return Response(data=data)
