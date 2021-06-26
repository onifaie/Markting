from django.db.models import fields
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from . models import * 
from django.utils import timezone


class Test_list(ListView):
    model=Test
    template_name='Test_list'
    context_object_name='allTest'
    ordering='-Proname'
    paginate_by=4


    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['myname']=Test.objects.count()
        # context['fill']=Test.objects.filter(Proname__contains='m')
        context['product_Test']=product.objects.all()
        # context['product_count']=product.objects.filter(Test=2).count()
        # context['nametageory']=Test.objects.filter(id=2)
        return context

    def  get_queryset(self):
        queryset = super(Test_list, self).get_queryset()
        # queryset=Test.objects.all().order_by('-Brand')
        return queryset

    

class Detail_product(DetailView):
    model = product
    template_name='product/Detail_product.html'
    context_object_name='Detail_Product'

    def get_context_data(self, **kwargs):

        context=super().get_context_data(**kwargs)
        # post=product.objects.filter(pk=self.kwargs.get('pk'))


        return context
    




class product_form(CreateView):
    model=product
    fields='__all__'
    success_url ='/'
    
