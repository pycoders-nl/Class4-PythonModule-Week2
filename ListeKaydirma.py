
def rotate(listem, n):

     return listem[n:] + listem[:n]     #bu fonksiyonla rakamlar liste icinde kalarak, 2 yonlu kayiyor,
                                        # Burada benim girecegim bilgi hangi yonde ve kac basamak kayacagidir,
n= (input('Listeye ayrac, virgul kullanmadan giris yapiniz:'))
z= (input('listeyi kaydirmak icin bir rakam giriniz:'))
listem= list(n)              #girdigim rakam veya harfleri listeye cevirdim kaydirma yapabilmek icin

print ('liste:', listem)

y= int(z)  % len(listem)       #kaydirma yapacagim sayi listeden buyukse, mod (liste uyelerinin sayisi) yapiyorum
                              # yani 12 kaydirma yapmak istiyorsam listede 5 rakam varsa (12:5) kalan 2 kadar kaymis oluyor
print ('yeni liste:', rotate(listem, -y))    #odevde istenen yonde kaydirma yapabilmesi icin '-' deger verdim, + tersi yonde calistirdi
