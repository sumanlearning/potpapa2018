from django.shortcuts import render
from .models import Kontrak, Ppm, Termin, Receiving
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
	jumlah_kontrak = Kontrak.objects.all().count()
	termins = Termin.objects.all()


	return render(
		request,
		'index.html',
		context = {
			'jumlah_kontrak': jumlah_kontrak,
			'termins': termins,
			}
		)

class KontrakListView(ListView):
	model = Kontrak
	paginate_by = 10
	context_object_name = 'kontrak_list'
	print('KontrakListView is running')

# class KontrakDetailView(DetailView):
#     model = Kontrak
#     print('class KontrakDetailView is running')

class ReceivingListView(ListView):
	model = Receiving
	paginate_by = 10
	context_object_name = 'receiving_list'
	print('ReceivingListView is running.....')



from django.shortcuts import get_object_or_404
from .utils import terbilang
def KontrakPpm(request, pk):
	kontrak = Kontrak.objects.get(id=pk)
	terbilang_kontrak = terbilang(round(kontrak.nilai))
	ppm = get_object_or_404(Ppm,id=pk)
	termins = Termin.objects.all().filter(kontrak=pk)
	return render(request,'kontrakppm.html',
		context={
			'kontrak': kontrak,
			'ppm': ppm,
			'terbilang_kontrak': terbilang_kontrak,
			'termins': termins,
		})

def receiving_detail_view(request,pk):
	receiving = Receiving.objects.get(id=pk)
	terbilang_bayar_now = terbilang(round(receiving.bayar_now))
	terbilang_nilai_kontrak = terbilang(round(receiving.termin.kontrak.nilai))
	terbilang_nhari_telat = terbilang(receiving.nhari_telat)
	return render(request, 'receiving_detail.html',
		context={
			'receiving':receiving,
			'terbilang_bayar_now': terbilang_bayar_now,
			'terbilang_nilai_kontrak': terbilang_nilai_kontrak,
			'terbilang_nhari_telat': terbilang_nhari_telat,
		})

# class ReceivingDetailView(DetailView):
# 	model = Receiving
# 	bayar_now = model.bayar_now
# 	terbilang_bayar_now = terbilang(bayar_now)
# 	print("ini bayarnow", bayar_now)


def KontrakNotClosed(request):
	kontraks = Kontrak.objects.all().exclude(status='c')
	context = {'kontraks':kontraks}
	print(kontraks)
	return render(request, 'kontrak_not_closed.html',context)



from .forms import ReceivingForm
def create_bapp(request, pk):
	kontrak = Kontrak.objects.get(id=pk)
	if request.method == 'POST':
		form = ReceivingForm(request.POST)
		if form.is_valid():
			# obj = form.save(commit=False)
			termin = form.cleaned_data['termin']
			no_bapp = form.cleaned_data['no_bapp']
			tgl_bapp = form.cleaned_data['tgl_bapp']
			no_bast = form.cleaned_data['no_bast']
			tgl_bast = form.cleaned_data['tgl_bast']
			tgl_periksa = form.cleaned_data['tgl_periksa']
			bayar_now = form.cleaned_data['bayar_now']
			nhari_telat = form.cleaned_data['nhari_telat']
			obj = Receiving(
				termin = termin,
				no_bapp = no_bapp,
				tgl_bapp = tgl_bapp,
				no_bast = no_bast,
				tgl_bast = tgl_bast,
				tgl_periksa = tgl_periksa,
				bayar_now = bayar_now,
				nhari_telat = nhari_telat,
				)
			obj.save()
			print('saving ke db')
			return HttpResponseRedirect('/')
	else:
		termin_selected = Termin.objects.filter(kontrak= kontrak)
		print(termin_selected)
		form = ReceivingForm(
			initial={'kontrak':kontrak}
			)
		form.fields['termin'].queryset = termin_selected
	return render(request, 'create_bapp.html', context = {'form': form})






