from django.urls import path

from contract import views
app_name = 'contract'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_contract, name='create_contract'),
    path('contract/<int:contract_id>/', views.contract_detail, name='contract_detail'),
    path('contract/confirm/', views.confirm_contract, name='confirm_contract'),
    path('contracts/unconfirmed/', views.unconfirmed_contracts, name='unconfirmed_contracts'),
    path('contracts/admin-preview/<int:pk>/', views.admin_preview_contract, name='admin_preview_contract'),
    path('contracts/preview/<int:pk>/', views.admin_preview_contract, name='admin_preview_contract'),
    path('contracts/finalize/<int:pk>/', views.admin_finalize_contract, name='admin_finalize_contract'),
    path('contracts/confirmed/', views.confirmed_contracts, name='confirmed_contracts'),
    path('contracts/download/pdf/<int:pk>/', views.download_contract_pdf, name='download_contract_pdf'),
    path('contracts/download/word/<int:pk>/', views.download_contract_word, name='download_contract_word'),
    path('contracts/download/pdf/<int:pk>/', views.download_contract_pdf, name='download_contract_pdf'),
    path('contracts/download/word/<int:pk>/', views.download_contract_word, name='download_contract_word'),
    path('contracts/my/', views.my_contracts, name='my_contracts'),








]