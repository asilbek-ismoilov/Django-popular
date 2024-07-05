from django.shortcuts import render
from .models import Contact,Blog,Category
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView


class BlogDetailView(HitCountDetailView):
    model = Blog        # your model goes here
    count_hit = True    # set to True if you want it to try and count the hit
    context_object_name = 'blog'
    template_name = 'publication.html'
    
    
# def blog_detail_view(request,id):
#     blog = Blog.objects.get(id=id)
#     context = {"blog":blog}
#     return render(request, 'publication.html',context)

def blog_view(request):
    blogs = Blog.objects.all()
    categories = Category.objects.all()
    context = {"blogs":blogs,"categories":categories}
    return render(request, 'blog.html',context)

def home_view(request): 
    # popular_blogs = Blog.objects.all().order_by('-hit_count__hits')
    popular_blogs = Blog.objects.all()
    sorted(popular_blogs,key=lambda x:x.hit_count.hits,reverse=True)
    context = {"popular_blogs":popular_blogs}
    return render(request,'home.html',context)


def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_contact = Contact(name=name,email=email,content=content)
            new_contact.save()
            messages.success(request, "Sizning xabaringiz yuborildi!!!") 
            return HttpResponseRedirect(reverse('home-page'))
        except:
            pass

    return render(request,'contact.html')