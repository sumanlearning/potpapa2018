def terbilang(x):
    satuan = [' ', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
    hasil = " "
    if x < 12 :
        hasil += satuan[x]
    elif x < 20 :
        hasil += terbilang(x-10) + " belas\n"
    elif x < 100:
        hasil += terbilang(int(x/10)) + " puluh\n" + terbilang(x%10)
    elif x < 200 :
        hasil += "seratus " + terbilang(x-100)
    elif x < 1000 :
        hasil += terbilang(int(x/100)) + " ratus\n" + terbilang(x%100)
    elif x < 2000 :
        hasil += "seribu " + terbilang(x-1000)
    elif x < 1000000 :
        hasil += terbilang(int(x/1000)) + " ribu\n" + terbilang(x%1000)
    elif x < 1000000000 :
        hasil += terbilang(int(x/1000000)) + " juta\n" + terbilang(x%1000000)
    elif x >= 1000000000 :
        hasil += terbilang(int(x/1000000000)) + " milyar\n" + terbilang(x%1000000000)

    return hasil

"""mulai dengan pdf... bismillah 23 februari 2018
"""
