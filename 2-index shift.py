ilk_liste = list(input("Lutfen liste elemanlarinızı boşluk bırakmadan giriniz: "))

index_shift = int(input("Dizin kaydırma miktarini giriniz: "))
ilk_liste_boyu = len(ilk_liste)
if index_shift > 0:
    index_shift = index_shift % ilk_liste_boyu
listenin_kesim_noktasi = ilk_liste_boyu - index_shift

if index_shift > 0:
    listenin_sol_tarafi = list(ilk_liste[0:listenin_kesim_noktasi])
    listenin_sag_tarafi = list(ilk_liste[listenin_kesim_noktasi:ilk_liste_boyu])

    yeni_liste = listenin_sag_tarafi + listenin_sol_tarafi
    print(yeni_liste)

else:
    index_shift = abs(index_shift)
    index_shift = index_shift % ilk_liste_boyu
    listenin_sol_tarafi = list(ilk_liste[0:index_shift])
    listenin_sag_tarafi = list(ilk_liste[index_shift:ilk_liste_boyu])
    print(listenin_sag_tarafi + listenin_sol_tarafi)
