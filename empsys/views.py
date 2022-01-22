from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DeleteView, UpdateView, View, FormView
from .forms import EmployeeAdder, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        forms = Employee.objects.all()
        context['forms'] = forms
        return context


class AddEmployeeView(TemplateView):
    template_name = "addemployee.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = EmployeeAdder()
        context['form'] = form
        return context

    def post(self, request):
        form = EmployeeAdder(request.POST)
        if form.is_valid():
            ename = form.cleaned_data['ename']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            salary = form.cleaned_data['salary']
            empadd = Employee.objects.create(ename=ename, email=email, address=address, salary=salary)
            empadd.save()
            return redirect('empsys:home')


class EmployeeShowView(TemplateView):
    template_name = "viewemp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emp_id = self.kwargs["id"]
        emp_obj = Employee.objects.get(id=emp_id)
        context['emp_obj'] = emp_obj

        return context


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "deleteemp.html"
    success_url = reverse_lazy("empsys:home")


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = "editemp.html"
    fields = ['ename', 'email', 'address', 'salary']
    success_url = reverse_lazy('empsys:home')


class SearchView(TemplateView):
    template_name = "search.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get("keyword")
        results = Employee.objects.filter(Q(ename__icontains=kw) | Q(email__icontains=kw))
        context["results"] = results
        return context


class UserRegisterView(TemplateView):
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserCreationForm()
        context['form'] = form
        return context

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empsys:home')
        else:
            return redirect('empsys:register')


class UserLoginView(TemplateView):
    template_name = "login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = UserLoginForm()
        context['form'] = form
        return context

    def post(self, request):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('empsys:home')
        else:
            messages.error(self.request, 'Bad Test')
            return redirect('empsys:login')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("empsys:home")
