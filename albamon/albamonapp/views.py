from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Comment
from django.utils import timezone

# Create your views here.
def home(request) :
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'home.html', context)

def detail(request, id):
    detail_data =get_object_or_404(Blog, pk=id)
    comments =Comment.objects.filter(blog_id =id)
    context = {
        'id' : id,
        'list' : detail_data.list,
        'information' : detail_data.information,
        'location' : detail_data.location,
        'pay' : detail_data.pay,
        'job' : detail_data.job,
        'applicant' : detail_data.applicant,
        'comments' : comments
    }
    return render(request, 'detail.html',context)

def create_page(request):
    return render(request,'create.html')

def create(request):
    new_data = Blog()
    new_data.list = request.POST['list']
    new_data.information = request.POST['information']
    new_data.location = request.POST['location']
    new_data.pay = request.POST['pay']
    new_data.job = request.POST['job']
    new_data.applicant = request.POST['applicant']
    new_data.save()
    return redirect('home')

def update_page(request,id):
    update_data =get_object_or_404(Blog, pk=id)
    context ={
        'id': id,
        'list': update_data.list,
        'information': update_data.information,
        'location': update_data.location,
        'pay': update_data.pay,
        'job': update_data.job,
        'applicant': update_data.applicant,
    }
    return render(request,'update.html', context)

def update(request, id):
    update_data = get_object_or_404(Blog, pk=id)
    update_data.list = request.POST['list']
    update_data.information = request.POST['information']
    update_data.location = request.POST['location']
    update_data.pay = request.POST['pay']
    update_data.job = request.POST['job']
    update_data.applicant = request.POST['applicant']
    update_data.save()
    return redirect('home')

def delete(request,id):
    delete_data = get_object_or_404(Blog, pk=id)
    delete_data.delete()
    return redirect('home')

def plus(request, id):
    data = get_object_or_404(Blog, pk=id)
    data.applicant += 1
    data.save()
    return redirect('detail', id)

def minus(request, id):
    data = get_object_or_404(Blog, pk=id)
    data.applicant -= 1
    data.save()
    return redirect('detail', id)


def create_comment(request, id):
    new_comment = Comment()
    blog_id = Blog.objects.get(pk=id)
    new_comment.blog_id = blog_id
    new_comment.user = request.POST['user']
    new_comment.content = request.POST['content']
    new_comment.pub_date = timezone.now()
    new_comment.save()

    return redirect('detail', id)

def delete_comment(request,id,comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()

    return redirect('detail',id)

