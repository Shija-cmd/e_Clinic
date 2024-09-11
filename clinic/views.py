from django.shortcuts import render, redirect
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Patient
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
from io import BytesIO



class CustomLoginView(LoginView):
    template_name = 'clinic/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'clinic/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)         

class TaskList(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(jina_la_mtumiaji=self.request.user)
        context['count'] = context['tasks'].filter(jina_la_mtumiaji=True).count()
        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Patient
    context_object_name = 'tasks'
    template_name = 'clinic/task.html'
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('tasks')
     
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    
    
# functions for downloading files
# Downloads for excel files
def download_excel(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=Patient.xlsx'

    data_entries = Patient.objects.all().values('tarehe', 'jina_la_kwanza', 'jina_la_pili', 'simu', 'anwani', 'jinsia', 'umri', 'Namba_ya_mgonjwa', 'hospitali', 'MAAMBUKIZI')
    df = pd.DataFrame(data_entries)

    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Data')

    return response

# view to render the file
def download_page(request):
    return render(request, 'clinic/download.html')

# Lab forms 