from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
# Create your views here.
class CompanyListView(ListView):
    model = Company
    #default template filename: company_list.html
    #default context object name: company_list

class CompanyDetailView(DetailView):
    model = Company
    #default template filename: company_detail.html
    #default context object name: company or object

class CompanyCreateView(CreateView):
    model = Company
    #fields = ['name','location','ceo']
    fields = '__all__'
    #default template filename: company_form.html

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ['location','ceo']
    #default template filename: company_form.html

from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')
