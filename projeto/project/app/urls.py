from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', views.ItemCreateView.as_view(), name='item-create'),  
    path('item/<int:pk>/edit/', views.ItemUpdateView.as_view(), name='item-edit'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item-delete'),
    path('polimorfismo/', views.PolimorthicView.as_view(), name='polimorfismo-list'),
    path('crud/', views.CrudView, name='CrudView'),
    path('crud/create/', views.CrudCreateView, name='CrudCreateView'),
    path('crud/read/', views.CrudReadView, name='CrudreadView'),
    path('crud/update/', views.CrudUpdateView, name='CrudUpdateView'),
    path('crud/delete/', views.CrudDeleteView, name='CrudDeleteView'),
    path('crud/complete/', views.CrudCompleteView, name='CrudCompleteView'),
    path('formulario/', views.FormularioView, name='formulario'),
    path('formulario/list/', views.FormListView, name='form-list'),
    path('formulario/<int:pk>/', views.FormDetailView, name='form-detail'),
    path('formulario/<int:pk>/edit/', views.FormUpdateView, name='form-edit'),
    path('formulario/<int:pk>/delete/', views.FormDeleteView, name='form-delete'),
    
]