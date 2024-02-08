from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This response is from Class based view</h1>')

class TempalteCBV(TemplateView):
    template_name = 'testapp/results.html'

class TempalteCBV2(TemplateView):
    template_name = 'testapp/results2.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sairam'
        context['marks'] = 90
        context['subject'] = 'Python'
        return context
