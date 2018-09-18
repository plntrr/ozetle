import math
metin = """
Öğrenciler ve veliler sınav sonuçlarının açıklanması ve Ağustos ayına girilmesiyle birlikte gözünü Milli Eğitim Bakanlığı (MEB) çalışma takvimine çevirdi. Peki bu sene okullar ne zaman açılacak.
Özellikle tatil planını şekillendirmek isteyen aileler yaz tatilinin bitiş tarihini merak ediyor. Bu konuya istinaden sosyal medya üzerinde çıkan "yaz tatili uzadı, okullar geç açılacak" haberleri gerçeği yansıtmıyor.
OKULLAR NE ZAMAN AÇILACAK?
2018 - 2019 MEB çalışma takvimine göre okulların ne zaman açılacağı kesinleşti;
Buna göre okulların açılma tarihi birinci dönem başlangıcı 17 Eylül 2018 Pazartesi günü olacak ve 18 Ocak 2019 cuma gününe kadar devam edecek.
15 günlük yarıyıl tatilinin ardından ikinci dönem 4 Şubat 2019 Pazartesi başlayacak ve önümüzdeki dönem okullar 14 Haziran 2019 cuma günü kapanacak.
MEB'DEN ÖNEMLİ AÇIKLAMA!
Okul öncesi, ilkokul birinci sınıf, ortaokul ve imam hatip ortaokullarının 5´inci sınıf öğrencileri, ortaöğretim kurumlarında eğitim ve öğretime başlayacak hazırlık sınıfı ve 9´uncu sınıf öğrencileri ile pansiyonda kalacak öğrencilerin, eğitim görecekleri okul hakkında bilgilendirilmesi, akademik ve mesleki gelişimlerinin desteklenmesi, öğrencilerin yeni girdikleri eğitim ortamına kısa sürede uyum sağlamalarına katkıda bulunulması amacıyla 10-14 Eylül 2018 tarihlerinde uyum eğitimi yapılacak.
"""
# Haber Kaynak : http://www.haber7.com/egitim/haber/2681236-2018-2019-okullar-ne-zaman-acilacak-bu-yil-tatil-uzayacak-mi


kelimelersay = {}
cumlelersay = {}
tekrar =[]
ozet =""

# kelimeleri " ", cümleleri . lardan böldüm
kelimeler = metin.split(" ")
cumleler = metin.split(".")


# kelimelerin toplamda kaç tane geçtiğini sayıyor. Her kelimeye tekrarına göre puan veriyor.
for kelime in kelimeler:
    if kelimelersay.get(kelime) is not None:
        kelimelersay[kelime] +=1
    else:
        kelimelersay[kelime] =1


# 2 den fazla geçen kelimeleri alıyor. Testlerde 2 en doğru sonucu verdi değişebilir.
for kelime in kelimelersay:
    if kelimelersay.get(kelime) > 2:
        tekrar.append(kelime)

# kelimelerin puanları ile cümleleri puanlandırıyor. Cümlelerin puanlarını elde ediyor.
for cumle in cumleler:
    for kelime in tekrar:
        if cumle.find(kelime) > -1:
            if cumlelersay.get(cumleler.index(cumle)) is not None:
                cumlelersay[cumleler.index(cumle)] += 1
            else:
                cumlelersay[cumleler.index(cumle)] = 1

print("-------------------------------")
# puanı belirli sayıdan fazla olan cümleleri yazıyor.
for a in cumlelersay:
    if cumlelersay[a] > 3: # Bu kısım yani Özetleme Düzeyi Metin Boyutu ve İçeriğine göre değiştirilecek.
        ozet += cumleler[int(a)]
print(ozet)
print("-------------------------------")
print("Metin Uzunluğu (Karakter): {}".format(len(metin)))
print("Özet Uzunluğu (Karakter): {}".format(len(ozet)))
