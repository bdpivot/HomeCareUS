from django.urls import path
from . import views

urlpatterns = [
    path('', views.CaregiverListView.as_view(), name='caregiver_list'),
    path('<int:pk>/', views.CaregiverDetailView.as_view(), name='caregiver_detail'),
    path('add/', views.CaregiverCreateView.as_view(), name='caregiver_add'),
    path('<int:pk>/edit/', views.CaregiverUpdateView.as_view(), name='caregiver_edit'),
    path('<int:pk>/delete/', views.CaregiverDeleteView.as_view(), name='caregiver_delete'),
    path('<int:caregiver_id>/certification/add/', views.CertificationCreateView.as_view(), name='certification_add'),
    path('<int:caregiver_id>/experience/add/', views.ExperienceCreateView.as_view(), name='experience_add'),
    path('<int:caregiver_id>/state-license/add/', views.CaregiverStateLicenseCreateView.as_view(), name='state_license_add'),
]