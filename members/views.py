from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))




def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def shop(request):
  template = loader.get_template('shop.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def men(request):
  template = loader.get_template('men.html')
  return HttpResponse(template.render())

def women(request):
  template = loader.get_template('women.html')
  return HttpResponse(template.render())










# def sonira(request):
#     return HttpResponse("Hello sonira (1)!")

