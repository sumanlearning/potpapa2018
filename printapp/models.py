from django.db import models
import datetime
from datetime import date
from django.urls import reverse

# Create your models here.
class Kontrak(models.Model):
 	no_kontrak = models.CharField(max_length=20)
 	supplier = models.CharField(max_length=200)
 	deskripsi = models.CharField(max_length=500)
 	tgl_terbit = models.DateField(default=date.today)
 	tgl_due = models.DateField(default=date.today, verbose_name='tgl jatuh tempo')
 	nilai = models.DecimalField(max_digits=14, decimal_places=2)
 	nhari_har = models.IntegerField(default=0, verbose_name='masa pemeliharaan (hari)')

 	STATUS_CHOICES = (
 		('o','open'),
 		('p', 'partial'),
 		('c', 'closed'),
 		)
 	status = models.CharField(max_length=7,choices=STATUS_CHOICES, blank=True, default='o')

 	class Meta:
 		ordering = ['tgl_terbit']

 	def __str__(self):
 		return self.no_kontrak

 	def get_absolute_url(self):
 		return reverse('kontrak-detail', args=[str(self.id)])

class Termin(models.Model):
	kontrak = models.ForeignKey('Kontrak', on_delete=models.CASCADE)
	tgl_termin = models.DateField(default=date.today)
	nilai_termin = models.DecimalField(max_digits=14, decimal_places=2)
	nth_termin = models.IntegerField(default=1, verbose_name='termin ke-')

	@property
	def is_overdue(self):
		if self.tgl_termin and date.today() >= self.tgl_termin:
			return True
		return False

	@property
	def monitored(self):
		if self.tgl_termin and date.today() < self.tgl_termin and date.today()+ datetime.timedelta(weeks=2) > self.tgl_termin:
			return True
		return False


	def __str__(self):
		return self.kontrak.no_kontrak + ' ---> termin ke-' + str(self.nth_termin)

class Ppm(models.Model):
	kontrak = models.ForeignKey('Kontrak', on_delete=models.SET_NULL, null=True, unique=True)
	KETUA_CHOICES = (
		('MENG','Manager Enjenering'),
		('MOPH','Manager Operasi Pemeliharaan'),
		('MADM','Manajer Administrasi dan Keuangan'),
		)
	SEK_ANG_CHOICES = (
		('SPS POH', 'Supervisor Senior Perencanaan Operasi Pemeliharaan'),
		('SPS HPL', 'Supervisor Senior Pemeliharaan Sipil'),
		('SPS GHW', 'Supervisor Senior Geologi dan Hidrologi Waduk'),
		('SPS LLK', 'Supervisor Senior Lahan dan Lingkungan'),
		('SPS KKK', 'Supervisor Senior Kesehatan dan Keselamatan Kerja'),
		('SPS CBM', 'Supervisor Senior Condition Based Monitoring'),
		('SPS OTG', 'Supervisor Senior Outage'),
		('SPS REO', 'Supervisor Senior Reliability'),
		('SPS PUK', 'Supervisor Senior Perencanaan Unit dan Kinerja'),
		('SPS MUM', 'Supervisor Senior Umum'),
		('SPS KAS', 'Supervisor Senior Keamanan dan Humas'),
		('SPS SIS', 'Supervisor Senior Sistem Informasi'),
		('SPS HAR', 'Supervisor Senior Pemeliharaan'),
		('SPS OPN', 'Supervisor Senior Operasi'),
		('AMU RENOP', 'AMU Perencanaan Operasi'),

		)


	ketua = models.CharField(max_length=4, choices=KETUA_CHOICES,blank=True, default='MOPH')        #ForeignKey('Jabat',on_delete=models.SET_NULL, null=True)
	sekretaris = models.CharField(max_length=9, choices=SEK_ANG_CHOICES, blank=False, default='SPS POH')          #ForeignKey('Jabat', on_delete=models.SET_NULL, null=True)
	anggota = models.CharField(max_length=9, choices=SEK_ANG_CHOICES, blank=False, default='SPS HAR')	#ForeignKey('Jabat', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.sekretaris

class Jabat(models.Model):
	jabatan = models.CharField(max_length=7)
	nama = models.CharField(max_length=50)

	def __str__(self):
		return self.jabatan

	class Meta:
		ordering = ('jabatan',)

class Receiving(models.Model):
	termin = models.ForeignKey('Termin', on_delete=models.SET_NULL, null=True)
	no_bapp = models.CharField(max_length=27, help_text='Nomer Berita Acara Pemeriksaan Pekerjaan')
	tgl_bapp = models.DateField(default=date.today)
	no_bast = models.CharField(max_length=27, help_text='Nomer Berita Acara Serah Terima Pekerjaan')
	tgl_bast = models.DateField(default=tgl_bapp)
	tgl_periksa = models.DateField(default=date.today, help_text='Tanggal Pelaksanaan Pemeriksaan di Lapangan')
	bayar_now = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='pembayaran sekarang')
	bayar_prev = models.ForeignKey('HistoryBayar', on_delete=models.SET_NULL, null=True, verbose_name='pembayaran sebelumnya')
	nhari_telat = models.IntegerField(default=0, verbose_name='jumlah hari keterlambatan')

	def __str__(self):
		return self.no_bast

	def get_absolute_url(self):
		return reverse('receiving-detail', args=[str(self.id)])


class HistoryBayar(models.Model):
	no_bast = models.ForeignKey('Receiving', on_delete=models.CASCADE)
	bayar_sisa = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='kekurangan pembayaran')
	bayar_now = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='pembayaran sekarang')

	def __str__(self):
		return self.no_bast 


