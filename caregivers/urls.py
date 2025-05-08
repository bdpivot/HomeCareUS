from django.urls import path
from . import views

app_name = 'caregivers'

urlpatterns = [
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Caregiver URLs
    path('', views.CaregiverListView.as_view(), name='caregiver_list'),
    path('add/', views.CaregiverCreateView.as_view(), name='caregiver_add'),
    path('<int:pk>/', views.CaregiverDetailView.as_view(), name='caregiver_detail'),
    path('<int:pk>/edit/', views.CaregiverUpdateView.as_view(), name='caregiver_edit'),
    path('<int:pk>/delete/', views.CaregiverDeleteView.as_view(), name='caregiver_delete'),
    
    # Certification URLs
    path('caregiver/<int:caregiver_id>/certification/add/', views.CertificationCreateView.as_view(), name='certification_create'),
    path('certification/<int:pk>/edit/', views.CertificationUpdateView.as_view(), name='certification_update'),
    path('certification/<int:pk>/delete/', views.CertificationDeleteView.as_view(), name='certification_delete'),
    
    # Experience URLs
    path('caregiver/<int:caregiver_id>/experience/add/', views.ExperienceCreateView.as_view(), name='experience_create'),
    path('experience/<int:pk>/edit/', views.ExperienceUpdateView.as_view(), name='experience_update'),
    path('experience/<int:pk>/delete/', views.ExperienceDeleteView.as_view(), name='experience_delete'),
    path('experience/', views.experience_list, name='experience_list'),
    path('experience/add/', views.add_experience, name='add_experience'),
    path('experience/<int:pk>/edit/', views.edit_experience, name='edit_experience'),
    path('experience/upload-resume/', views.upload_resume, name='upload_resume'),
    
    # State License URLs
    path('caregiver/<int:caregiver_id>/state-license/add/', views.CaregiverStateLicenseCreateView.as_view(), name='caregiver_state_license_create'),
    path('state-license/<int:pk>/edit/', views.CaregiverStateLicenseUpdateView.as_view(), name='caregiver_state_license_update'),
    path('state-license/<int:pk>/delete/', views.CaregiverStateLicenseDeleteView.as_view(), name='caregiver_state_license_delete'),
    
    # Agency URLs
    path('agency/', views.AgencyListView.as_view(), name='agency_list'),
    path('agency/<int:pk>/', views.AgencyDetailView.as_view(), name='agency_detail'),
    path('agency/new/', views.AgencyCreateView.as_view(), name='agency_create'),
    path('agency/<int:pk>/edit/', views.AgencyUpdateView.as_view(), name='agency_update'),
    path('agency/<int:pk>/delete/', views.AgencyDeleteView.as_view(), name='agency_delete'),
    
    # Agency State License URLs
    path('agency/<int:agency_id>/state-license/add/', views.AgencyStateLicenseCreateView.as_view(), name='agency_state_license_create'),
    path('agency-state-license/<int:pk>/edit/', views.AgencyStateLicenseUpdateView.as_view(), name='agency_state_license_update'),
    path('agency-state-license/<int:pk>/delete/', views.AgencyStateLicenseDeleteView.as_view(), name='agency_state_license_delete'),
]