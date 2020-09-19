from django.shortcuts import render, redirect
from .models import Post, BlogComment
from django.contrib import messages

# Create your views here.
def bloghome(request):
    allpost = Post.objects.all()
    context = {'allposts': allpost}
    return render(request, 'blog/bloghome.html', context)

def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comment = BlogComment.objects.filter(post=post)
    context = {'post':post, 'comment':comment}
    return render(request, 'blog/blogpost.html',context)

def Postcomment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = request.user
        postSno = request.POST['postSno']
        post = Post.objects.get(sno=postSno)
        parent = request.POST['perentSno']

        if parent == "":
            Scomment = BlogComment(comment=comment, user=user, post=post)
            Scomment.save()
            messages.success(request, "Comment Added Successfully")
            return redirect(f"/blog/{post.slug}")
        else:
            parent = BlogComment.objects.get(sno=parent)
            Scomment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            Scomment.save()
            messages.success(request, "Replay Added Successfully")
            return redirect(f"/blog/{post.slug}")
        
    return redirect('home')