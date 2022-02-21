from ast import Del
from re import template
from sys import flags
from typing import List
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Blog, Plan
from .jsongen import json_data
from django.contrib.auth.decorators import login_required
from .models import Workout, Log, Squat, Weight

import datetime
now = datetime.datetime.now()


# Create your views here.
"""class HomePage(View):
    def get(self, request):
        if not self.request.user_is_authenticated:
            return redirect('login')
        return render(request, 'base/home.html')"""

d1 = dict()
d2 = dict()
for i in json_data:
    name = i['name']
    if name not in d1:
        d1[name] = i['gifUrl']
        d2[name] = i['equipment']


def home(request):
    context = {"datetime":now.strftime("%Y-%m-%d %H:%M:%S")}
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('login')
        return super(RegisterPage, self).get(*args,**kwargs)

    return render(request, "base/home.html", context)

"""def blogs(request):
    context = {"blogs":Blog.objects.all()}
    return render(request, "base/blogs.html", context)"""


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args,**kwargs)


class BlogList(LoginRequiredMixin, ListView):
    login_url = "login/"
    model = Blog
    context_object_name = "blogs"
    template_name = "base/blogs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input"""
        return context

class BlogDetail(LoginRequiredMixin, DetailView):
    login_url = "login/"
    model = Blog
    context_object_name = "blog"
    template_name = "base/blog_detail.html"


class BlogCreate(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = "base/blog_form.html"
    fields = ['title','description']
    success_url = reverse_lazy('blogs')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)

class PlanList(LoginRequiredMixin, ListView):
    login_url = "login/"
    model = Plan
    context_object_name = "plans"
    template_name = "base/plan_list.html"

@login_required(login_url='login/')
def planlist(request):
    context = {'plans': Plan.objects.filter(user=request.user)}
    return render(request, "base/plan_list.html", context)

@login_required(login_url='login/')
def plandetail(request, id):
    plan = Plan.objects.get(pk=id)
    context = {'workouts': Workout.objects.filter(plan=plan), 'id':id}
    return render(request, "base/plan_detail.html", context)

class PlanCreate(LoginRequiredMixin, CreateView):
    model = Plan
    template_name = "base/plan_create.html"
    fields = ['title']
    success_url = reverse_lazy('plans')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@login_required(login_url='login/')
def sample(request):
    context = {
        'array':Log.objects.filter(user=request.user).values_list('num', flat=True),
        'array2':Squat.objects.filter(user=request.user).values_list('num', flat=True),
        'array3':Weight.objects.filter(user=request.user).values_list('num', flat=True)}
    return render(request, "base/sample.html", context)


"""class BlogUpdate(LoginRequiredMixin,UpdateView):
    login_url = "login/"
    model = Blog
    template_name = "base/blog_update.html"
    fields = ['title','description']
    success_url = reverse_lazy('blogs')"""

@login_required(login_url='login/')
def workout_search(request, id):
    print(id)
    l = []
    search = request.GET.get("muscles")
    if search is None or search=="":
        return render(request, "base/workout_search.html", {'id':id})
    search = search.lower()
    curr = 0
    for i in range(len(json_data)):
        if curr == 20:
            break
        data = json_data[i]
        body_part = data['bodyPart'].lower()
        if search in body_part or search in data['target'].lower() or search in data['name'].lower() or search in data['equipment'].lower():
            if data['name'] not in Workout.objects.filter(plan=Plan.objects.get(pk=id)).values_list('title', flat=True):
                l.append(data)
                curr += 1
    context = {"workouts":l, 'id':id}
    return render(request, "base/workout_search.html", context)



@login_required(login_url='login/')
def addworkout(request, name, id):
    plan = Plan.objects.get(pk=id)
    if(name not in list(Workout.objects.filter(plan=plan).values_list('title', flat=True))):
        w = Workout(title=name,plan=plan, gif=d1[name], equipment=d2[name])
        w.save()
    workouts = Workout.objects.filter(plan=plan)
    for i in workouts:
        pass
    context = {'workouts': Workout.objects.filter(plan=plan), 'id':id}

    return render(request, "base/plan_detail.html", context)

@login_required(login_url='login/')
def add_bench(request):
    num = request.GET.get("num")
    l = Log(user=request.user, num=num)
    l.save()
    print(l.user)
    context = {
        'array':Log.objects.filter(user=request.user).values_list('num', flat=True),
        'array2':Squat.objects.filter(user=request.user).values_list('num', flat=True),
        'array3':Weight.objects.filter(user=request.user).values_list('num', flat=True)}
    print(context['array'])
    return render(request, "base/sample.html", context)

@login_required(login_url='login/')
def add_squat(request):
    num = request.GET.get("num")
    l = Squat(user=request.user, num=num)
    l.save()
    print(l.user)
    context = {
        'array':Log.objects.filter(user=request.user).values_list('num', flat=True),
        'array2':Squat.objects.filter(user=request.user).values_list('num', flat=True),
        'array3':Weight.objects.filter(user=request.user).values_list('num', flat=True)}
    print(context['array2'])
    return render(request, "base/sample.html", context)

@login_required(login_url='login/')
def add_weight(request):
    num = request.GET.get("num")
    l = Weight(user=request.user, num=num)
    l.save()
    context = {
        'array':Log.objects.filter(user=request.user).values_list('num', flat=True),
        'array2':Squat.objects.filter(user=request.user).values_list('num', flat=True),
        'array3':Weight.objects.filter(user=request.user).values_list('num', flat=True)}
    print(context['array3'])
    return render(request, "base/sample.html", context)

@login_required(login_url='login')
def log(request):
    return render(request, "base/log.html")