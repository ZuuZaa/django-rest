from django.shortcuts import render
from blog.models import BlogModel
# Create your views here.

def blog_view(request):
    # try:
    #     blog_list = BlogModel.objects.all()
    # except BlogModel.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    blog_list = BlogModel.objects.all()
    context = {
        'blog_list': blog_list
    }
    return render(request, "blog_list.html", context)


def detail_blog_view(request, id):
    # try:
    #     blog_post = BlogModel.objects.get(id=id)
    # except BlogModel.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     return render(request, "blog_detail.html", {'blog_post':'blog_post'})
    # else:
    pass
