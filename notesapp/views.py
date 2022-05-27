from asyncio import Task, tasks
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render

import notesapp
from .models import Note
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class UserLogin(LoginView):
    template_name = 'notesapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def success_url(self):
        return reverse_lazy('/')

class Notesview(LoginRequiredMixin,ListView):
    model =  Note
    context_object_name = 'notes'
    template_name ='notesapp/note_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(created_by = self.request.user)
        search_input = self.request.GET.get('tag_name') or ''
        if search_input:
            context['notes'] = context['notes'].filter(tags__icontains = search_input )
        return context
    
class Notesdetail(LoginRequiredMixin,DetailView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notesapp/note_detail.html'
    def form_valid(self, form):
        form.instance.created_by = self.request.user         #form.instance.get_object.context relate krna hai isse        
        form.save()
        return super(Notesdetail,self).form_valid(form)

class Notescreate(LoginRequiredMixin,CreateView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notesapp/note_form.html'
    fields = ['title','body','tags']
    success_url = reverse_lazy('Notesview')         

    def form_valid(self, form):
        form.instance.created_by = self.request.user         #form.instance.get_object.context relate krna hai isse        
        form.save()
        return super(Notescreate,self).form_valid(form)
        

class Notesupdate(LoginRequiredMixin,UpdateView):
    model = Note
    context_object_name= 'notes'
    template_name= 'notesapp/note_form.html'
    fields = ['title','body','tags']
    success_url=reverse_lazy("Notesview")

class Notesdelete(LoginRequiredMixin,DeleteView):
    model = Note
    context_object_name = 'notes'
    template_name = 'notesapp/note_confirm_delete.html'
    fields = ['title','body','tags']
    success_url=reverse_lazy("Notesview")

    

class RegisterUser(FormView):
     template_name = "notesapp/register.html"
     form_class = UserCreationForm
     redirect_authenticated_user = True
     success_url = reverse_lazy('Notesview')

     def form_valid(self, form):
         user = form.save()
         if user is not None:
             login(self.request,user)
         return super(RegisterUser,self).form_valid(form)

     def get(self,*args,**kwargs):
        if self.request.user.is_authenticated :
            return redirect('Notesview')
        return super(RegisterUser,self).get(*args,**kwargs)

