from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import TodoList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class Login(LoginView):
	fields="__all__"
	redirect_authenticated_user=True

	def get_success_url(self):
		return reverse_lazy('list')

class Register(FormView):
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	redirect_authenticated_user=True
	success_url= reverse_lazy('list')

	def form_valid(self,form):
		user=form.save()
		if user is not None:
			login(self.request,user)
		return super(Register,self).form_valid(form)
	def  get(self,*args, **kwargs):
		if self.request.user.is_authenticated:
			return redirect('list')
		return super(Register,self).get(*args, **kwargs)

class List(LoginRequiredMixin,ListView):
	model = TodoList
	context_object_name='tasks'
	def get_context_data(self, **kwargs):
		context=super().get_context_data(**kwargs)
		context['tasks']=context['tasks'].filter(user=self.request.user)
		context['count']= context['tasks'].filter(completed=False).count()
		return context

 
class Details(LoginRequiredMixin,DetailView):
	model = TodoList
	context_object_name='detail'
	#template_name = 'Todo/any.html'  - Can use any name in html, but have define in template_name

class Create(LoginRequiredMixin,CreateView):
	model=TodoList
	fields=["task","details","completed","Date"]
	success_url= reverse_lazy('list')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['Date'] = timezone.now()
		return context

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(Create,self).form_valid(form)

class Update(LoginRequiredMixin,UpdateView):
	model=TodoList
	fields=fields=["task","details","completed","Date"]
	success_url= reverse_lazy('list')


class Delete(LoginRequiredMixin,DeleteView):
	model=TodoList
	fields="__all__"
	template_name='Todo/delete.html'
	success_url= reverse_lazy('list')
