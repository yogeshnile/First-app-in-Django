from django.shortcuts import render, HttpResponse

# Create your views here.
def bloghome(request):
    return HttpResponse("hello from bloghome")

def blogpost(request, slug):
    return HttpResponse(f"this is blogpost{slug}")