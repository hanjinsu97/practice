from django.shortcuts import render
from .models import *

# Create your views here.
def ideation(request):
    members = Member.objects.all()
    return render(request, 'ideation.html',{'members':members})
   