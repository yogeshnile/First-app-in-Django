from django.shortcuts import render
from .models import Post

# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allposts': allpost}
    return render(request, 'blog/bloghome.html', context)

def blogpost(request, slug):
    return render(request, 'blog/blogpost.html',{'slug':slug})