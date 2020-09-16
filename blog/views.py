from django.shortcuts import render, HttpResponse

# Create your views here.
def bloghome(request):
    return render(request, 'blog/bloghome.html')

def blogpost(request, slug):
    return render(request, 'blog/blogpost.html')