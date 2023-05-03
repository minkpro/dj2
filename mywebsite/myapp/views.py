from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff,Product, ContactUs

# Create your views here.
def Homepage(request):
    productlist = Product.objects.all()
    context = {'product': productlist}
    return render(request, 'myapp/home.html', context)

def About(request):
    return render(request, 'myapp/about.html')

def Products(request):
    
    return render(request, 'myapp/home.html')

def Contact(request):

    namelist = Staff.objects.all()
    context = {'name': namelist}

    if request.method == 'POST':
        data = request.POST.copy()
        # print(data)
        name = data.get('name')
        title = data.get('title')
        comment = data.get('comment')
        # email = data.get('email')
        newcontact = ContactUs()
        newcontact.name = name
        newcontact.title = title
        newcontact.comment = comment
        newcontact.save()
        # return HttpResponse('Thank you for your comment')

        context['alert'] = 'success'

    
    return render(request, 'myapp/contact.html', context)