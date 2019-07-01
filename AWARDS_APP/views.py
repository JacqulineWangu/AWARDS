# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm,VoteForm
from django.contrib.auth.decorators import login_required

# Create your views here.
