from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('kontraks/', views.KontrakListView.as_view(), name='kontrak-list'),
	path('kontrak/<int:pk>',views.KontrakPpm, name='kontrak-detail'),
	path('berita_acara/pilih_kontrak/<int:pk>', views.create_bapp, name='create-bapp'),
	path('berita_acara/pilih_kontrak/',views.KontrakNotClosed, name='pilih-kontrak'),
	path('berita_acara/', views.ReceivingListView.as_view(), name='receiving-list'),
	path('berita_acara/<int:pk>', views.receiving_detail_view, name='receiving-detail')

]