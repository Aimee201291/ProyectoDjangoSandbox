from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.adopcion.models import Persona, Solicitud
from apps.adopcion.forms import PersonaForm, SolicitudForm

# Create your views here.

def index_adopcion(request):
    return HttpResponse("Soy la página principal de la app adopcion")


class SolicitudList(ListView):
    model = Solicitud
    template_name = 'adopcion/solicitud_list.html'


class SolicitudCreate(CreateView):
    model = Solicitud #indico de qué modelo voy a hacer esta vista
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm #indico cuál es el otro formulario que voy a usar
    success_url = reverse_lazy('adopcion:solicitud_listar')

	#Se pueden sobreescribir los métodos de nuestras vistas basadas en clases

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context


    def post(self, request, *args, **kwargs): #Estamos sobreescribiendo el método Post
        self.object = self.get_object
        form = self.form_class(request.POST) #Recogo del formulario la información que estoy ingresando
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False) #Variable que guarda el primer request, el que recogí en la línea 39. Se coloca commit=False para que no guarde hasta que yo guarde los valores del segundo formulario
            solicitud.persona = form2.save() #Indico que los valores del atributo persona, van a ser igual a los valores que ingresé en mi segundo formulario
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else: #Si no es válido, debemos devolver nuevamente el contexto (serían los formularios en blanco)
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


    #Recogemos los valores que se ingresaron en los formularios en las líneas 39 y 40
    #En las líneas evaluamos si son válidos en la línea 37
    #Guardamos el primer form y se lo asignamos a solicitud en la línea 42, luego creamos la relación en
    #y guardamos los avlores del segundo form la línea 43 
    #En la línea 44 guardamos el objeto

class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'adopcion/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('adopcion:solicitud_listar')


    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud) # Si no se coloca instance, crea un nuevo objeto en lugar de actualizar el que le estamos dando
        form2 = self.second_form_class(request.POST, instance=persona)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'adopcion/solicitud_delete.html'
    success_url = reverse_lazy('adopcion:solicitud_listar')
