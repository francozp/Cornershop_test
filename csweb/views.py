from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import *
import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

class MenuView(FormView):
    form_class = MenuForm
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        data = super(MenuView, self).get_context_data(**kwargs)
        if self.request.POST:
            post_data = self.request.POST
            print(str(post_data))
            datos = MenuFormSet(self.request.POST)
            if datos.is_valid():
                maxforms = int(self.request.POST['form-TOTAL_FORMS'])
                #date = self.request.POST['date']
                #print(date)
                print(maxforms)
                """pedido = Pedido.objects.create(obra=Obra.objects.get(id=obra),
                                               usuario=self.request.user,
                                               fecha=timezone.now(),
                                               comentario=comentario)"""
                for i in range(maxforms):
                    maindish = str(self.request.POST['form-{0}-maindish'.format(i)])
                    salad = bool(self.request.POST.get('form-{0}-salad'.format(i),False))
                    dessert = bool(self.request.POST.get('form-{0}-dessert'.format(i),False))
                    print(maindish)
                    """ProductoEnPedido.objects.cre ate(idPedido=pedido,
                                                    idProducto=Producto.objects.get(id=prod),
                                                    cantidad=cant)"""
            else:
                print(datos)
                print(datos.errors)
            data['options'] = MenuFormSet()
        else:
            data['options'] = MenuFormSet()
        return data
    

    def form_valid(self, form):
        return super(MenuView, self).form_valid(form)