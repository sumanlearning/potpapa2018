from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from datetime import date

from .models import Kontrak, Receiving, Termin


class ReceivingForm(forms.Form):
	id = forms.IntegerField(required=False, widget=forms.HiddenInput())
	kontrak = forms.CharField(max_length=20)
	termin = forms.ModelChoiceField(queryset=Termin.objects.all())         

	no_bapp = forms.CharField(max_length=27)
	tgl_bapp = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
	# hari_bapp = models.CharField(max_length=10)
	no_bast = forms.CharField(max_length=27)
	tgl_bast = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
	tgl_periksa = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
	bayar_now = forms.DecimalField(label='pembayaran sekarang (Rp)')
	nhari_telat = forms.IntegerField(label='jumlah keterlambatan (hari)')
	

