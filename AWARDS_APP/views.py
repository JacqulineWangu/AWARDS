# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm,VoteForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.

def home(request):
    all_projects = Project.fetch_all_images()
    return render(request,"AWARDS/index.html",{"all_images":all_projects})
