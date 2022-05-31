from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import notes ,DBMS , Contact , Notice

# Create your views here.


def blogpost(request,id):
    note = DBMS.objects.filter(chapter_id = id)
    return render(request,'notes/blogpost.html',{"note":note , 'chapter_id':id})
# def DBMS(request):
#     dbms = DBMS.objects.filter()
def home(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']    
        mynotes = notes.objects.filter(subject__icontains = search_term)
    else:
       mynotes = notes.objects.all()

    return render(request,'notes/basic.html',{'mynotes':mynotes})


def contact(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        data = Contact(name = name , email = email , message = message)
        data.save()
        messages.success(request, 'contact submit successfully !!.')
    return render(request,'notes/contact.html')

def notice(request):
    notices = Notice.objects.all()
    # print(notices)
    return render(request,'notes/notice.html',{'notices':notices})