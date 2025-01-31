from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('admin-panel/', AdminPanel.as_view(), name='admin_panel'),
    path('appointment/', AppointmentListView.as_view(), name='appoint_list'),
    path('appointments/', UserAppointmentListView.as_view(), name='user_appointments'),
    path('appointment/<int:pk>', ViewAppoint.as_view(), name='appoint_view'),
    path('appointment/add', AddAppoint.as_view(), name='appoint_add'),
    path('appointment/<int:pk>/update', UpdateAppoint.as_view(), name='appoint_update'),
    path('appointment/<int:pk>/delete', DeleteAppoint.as_view(), name='appoint_delete'),

    path('patient/add', AddPatient.as_view(), name='patient_add'),
    path('patient/<int:pk>/update', PatientUpdateView.as_view(), name='edit_patient'),
    path('patient/<int:pk>/delete', PatientDeleteView.as_view(), name='delete_patient'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/<int:pk>', PatientDetailView.as_view(), name='patient_view'),

    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('doctors/<int:pk>', DoctorDetailView.as_view(), name='doctor_view'),
    path('doctors/create', AddDoctor.as_view(), name='doctor_add'),
    path('doctors/<int:pk>/update', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete', DoctorDeleteView.as_view(), name='doctor_delete'),
    
]