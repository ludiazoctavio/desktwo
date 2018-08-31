from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView, CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView


urlpatterns_departments = ([

    path('', login_required(DepartmentListView.as_view()), name='list'),
    path('create', login_required(DepartmentCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(DepartmentUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(DepartmentDeleteView.as_view()), name='delete'),

], 'department')

urlpatterns_companies = ([

    path('', login_required(CompanyListView.as_view()), name='list'),
    path('create', login_required(CompanyCreateView.as_view()), name='create'),
    path('update/<str:pk>/', login_required(CompanyUpdateView.as_view()), name='update'),
    path('delete/<str:pk>/', login_required(CompanyDeleteView.as_view()), name='delete'),

], 'company')