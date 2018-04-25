from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('<res_file_name>/', views.detail, name="detail")
    path('<workload_id>/', views.workload, name='workload'),
    path('<workload_id>/<snapshot_id>/<vm_id>', views.detail, name='detail')
]
