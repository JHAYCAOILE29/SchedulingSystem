from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Appointment, Patient, Doctor
from django.urls import reverse_lazy
from .forms import PatientForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class Home(LoginRequiredMixin, TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        patient = Patient.objects.filter(name=self.request.user).first()
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['patient_exists'] = Patient.objects.filter(name=self.request.user).exists()
        else:
            return redirect('login')
        context['patient'] = patient
        return context

class AdminPanel(TemplateView):
    model = Appointment, Patient, Doctor
    template_name = "app/admin-panel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_patients'] = Patient.objects.count()
        context['total_doctors'] = Doctor.objects.count()
        context['total_appointments'] = Appointment.objects.count()
        context['appointments'] = Appointment.objects.all()
        return context

class AppointmentListView(ListView):
    model = Appointment
    template_name = 'app/list-appoint.html'  
    context_object_name = 'appointments'  
    ordering = ['appointment_time']

class AddAppoint(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'app/add-appoint.html'
    fields = ['doctor', 'appointment_time', 'reason']  
    success_url = reverse_lazy('home') 

    def form_valid(self, form):
        patient = get_object_or_404(Patient, name=self.request.user)
        form.instance.patient = patient
        form.instance.status = 'Pending'  
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        return context

class UserAppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'app/user-appoint-list.html'  
    context_object_name = 'appointments'  
    ordering = ['-appointment_time']  

    def get_queryset(self):
        return Appointment.objects.filter(patient__name=self.request.user)

class ViewAppoint(DetailView):
    model = Appointment
    context_object_name = 'appoint'
    template_name = 'app/view-appoint.html'

class UpdateAppoint(UpdateView):
    model = Appointment
    fields = ['patient','doctor','appointment_time','status','reason']
    template_name = 'app/update-appoint.html'
    success_url = reverse_lazy('appoint_list')

class DeleteAppoint(DeleteView):
    model = Appointment
    template_name = 'app/delete-appoint.html'
    success_url = reverse_lazy('appoint_list')

class AddPatient(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'app/add-patient.html'
    fields = ['date_of_birth', 'email', 'phone_number', 'address']
    success_url = reverse_lazy('home')  

    def dispatch(self, request, *args, **kwargs):
        if Patient.objects.filter(name=request.user).exists():
            return redirect('home') 
        return super().dispatch(request, *args, **kwargs)  
    def form_valid(self, form):
        form.instance.name = self.request.user 
        return super().form_valid(form)

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/update-patient.html'  
    success_url = reverse_lazy('home')  

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'app/update-patient.html'
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super().get_queryset()
            return queryset.filter(name=self.request.user)
        else:
            return Patient.objects.none()

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'app/delete-patient.html'  
    success_url = reverse_lazy('home') 
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(name=self.request.user)



class DoctorListView(ListView):
    model = Doctor
    template_name = 'app/list-doctor.html' 
    context_object_name = 'doctors'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'app/view-doctor.html'  
    context_object_name = 'doctor'

class AddDoctor(CreateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialization', 'email', 'phone_number']
    template_name = 'app/add-doctor.html'  
    success_url = reverse_lazy('list_doctor')

class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'specialization', 'email', 'phone_number'] 
    template_name = 'app/update-doctor.html' 
    success_url = reverse_lazy('list_doctor')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'app/delete-doctor.html' 
    success_url = reverse_lazy('list_doctor')

class PatientListView(ListView):
    model = Patient
    template_name = 'app/list-patient.html'  
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'app/view-patient.html'
    context_object_name = 'patient'
