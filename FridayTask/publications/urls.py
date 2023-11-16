from django.urls import path
from . import views

urlpatterns = [
    path('', views.publ_home, name='publ_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PublDetailView.as_view(), name='publ-detail'),
    path('<int:pk>/update', views.PublUpdateView.as_view(), name='publ-update'),
    path('<int:pk>/delete', views.PublDeleteView.as_view(), name='publ-delete')
]