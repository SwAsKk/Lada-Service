"""
project URL Configuration
"""

from collections import namedtuple
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views

# Renaming django admin title
admin.site.site_header = 'Панель администрации'
admin.site.site_title = 'Project'
admin.site.index_title = 'Модерация сайта'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Страничка index.html
    path('', views.index),
    
    # View pages
    path('branches/',    views.branches),
    path('clients/',     views.clients),
    path('consultants/', views.consultants),
	path('contracts/',   views.contracts),
    path('cars/',        views.cars),
    
    # Add pages
    path('branches/add/',   views.BranchAdd.as_view(),     name = 'add_branch_url'),
    path('clients/add/',    views.ClientAdd.as_view(),     name = 'add_client_url'),
	path('consultants/add', views.ConsultantAdd.as_view(), name = 'add_consultant_url'),
	path('contracts/add',   views.ContractAdd.as_view(),   name = 'add_contract_url'),
    path('cars/add/',       views.CarAdd.as_view(),        name = 'add_car_url'),
	
    # Detail pages
    path('branches/<int:id>/',    views.BranchDetails.as_view(),     name = 'branch_details_url'),
    path('clients/<int:id>/',     views.ClientDetails.as_view(),     name = 'client_details_url'),
	path('consultants/<int:id>/', views.ConsultantDetails.as_view(), name = 'consultant_details_url'),
    path('contracts/<int:id>/',   views.ContractDetails.as_view(),   name = 'contract_details_url'),
    path('cars/<int:id>/',        views.CarDetails.as_view(),        name = 'car_details_url'),
    
    # Edit pages
    path('branches/<int:id>/edit/',    views.BranchUpdate.as_view(),     name = 'branch_edit_url'),
    path('clients/<int:id>/edit/',     views.ClientUpdate.as_view(),     name = 'client_edit_url'),
    path('consultants/<int:id>/edit/', views.ConsultantUpdate.as_view(), name = 'consultant_edit_url'),
    path('contracts/<int:id>/edit/',   views.ContractUpdate.as_view(),  name = 'contract_edit_url'),
    path('cars/<int:id>/edit/',        views.CarUpdate.as_view(),        name = 'car_edit_url'),
    
    # Delete pages
    path('branches/<int:id>/delete/',    views.BranchDelete.as_view(),     name = 'branch_delete_url'),
    path('clients/<int:id>/delete',      views.ClientDelete.as_view(),     name = 'client_delete_url'),
    path('consultants/<int:id>/delete/', views.ConsultantDelete.as_view(), name = 'consultant_delete_url'),
    path('contracts/<int:id>/delete/',   views.ContractDelete.as_view(),   name = 'contract_delete_url'),
    path('cars/<int:id>/delete/',        views.CarDelete.as_view(),        name = 'car_delete_url'),
    
    
    path('contracts/<int:id>/print/', views.print_contract, name = 'print_contract_url'),
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
