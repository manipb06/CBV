# from msilib.schema import Class
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ContactForm
import myapp


# Function Based View
def myview(request):
    return HttpResponse('<h1>This is Function Based View</h1>')


#Class Based View
class MyView(View):
    name = 'Mandy'
    def get(self,request):
        return HttpResponse(self.name)
        # return HttpResponse('<h1>This is Class Based View</h1>')

class MyChildView(MyView):
    def get(self, request):
        return HttpResponse(self.name)

def homefunc(request):
    return render(request,'home.html')

class HomeClassView(View):
    def get(self, request):
            return render(request,'home.html')
##############################################################################
def aboutfunc(request):
    context ={"msg":'Welcome to the Website this is Function Based View'}
    return render(request,'about.html', context)

class AboutClass(View):
    def get(self, request):
            context ={"msg":'Welcome to the Website this is Class Based View'}
            return render(request,'about.html',context)
###############################################################################
def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data['name'])
            return HttpResponse('Thank You! Form Submitted')
    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form':form})
################################################################################
class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html',{'form': form })

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data['name'])
            return HttpResponse('Thank You! Form Submitted')
###############################################################################
def newsfun(request,template_name):
    template_name = template_name
    context={'info':'Keep smiling, because life is a beautiful thing and there is so much to smile about.'}
    return render(request, template_name, context)
################################################################################

class NewsClassView(View):
    template_name= 'news.html' 
    def get(self, request):
        context= {'info':'Keep smiling, because life is a beautiful thing and there is so much to smile about.'}
        return render(request, self.template_name , context)