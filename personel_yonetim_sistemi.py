#Personel listeleme

#İçeride kayıtlı kullanıcılar

personeller = {
    "ahmet": {"isim" : "ahmet"},



}

#Önceden tanımlanmış kullanıcı
kullanici_adi = "1"
sifre = "1"

#Mevcutta bir hesabı olup olmadığını öğrenme
while True:
    hesap_bilgisi = input("Mevcutta bir hesabınız var mı?\nVarsa, Evet yoksa Hayır yazın. :")

    if hesap_bilgisi == "Evet" or hesap_bilgisi == "Hayır":
        break
    else:
        print(f"lütfen belirtilen formatta yazınız\nyazdığınız hatalı format: {hesap_bilgisi}\n")
        continue

#Yeni hesap olusturma veya direkt login olma
while True:
    if hesap_bilgisi == "Evet":
        kullanici_adi_girin = input("Lütfen kullanıcı adınızı giriniz: ")
        sifre_girin = input("Lütfen şifrenizi giriniz: ")
        if kullanici_adi == kullanici_adi_girin and sifre == sifre_girin:
            print("giriş başarılı")
            break
        else:
            print("yanlış kullanıcı adı veya şifre\n")
            continue
    elif hesap_bilgisi == "Hayır":
            yeni_kullanici_girdi = False
            yeni_kullanici_adi_giris = input("Yeni bir kullanıcı adı oluşturun: ")
            yeni_sifre_giris = input("Yeni bir şifre oluşturun: ")
            print(f"Hesabınız başarıyla oluşturuldu\n Kullanıcı adınız: {yeni_kullanici_adi_giris}\n Şifreniz: {yeni_sifre_giris}\n")


            while not yeni_kullanici_girdi:
                kullanici_adi_girin = input("Lütfen kullanıcı adınızı giriniz: ")
                sifre_girin = input("Lütfen şifrenizi giriniz: ")
                if kullanici_adi_girin == yeni_kullanici_adi_giris and sifre_girin == yeni_sifre_giris:
                    yeni_kullanici_girdi = True
                    print("giriş başarılı")
                    break
                else:
                    print("yanlış kullanıcı adı veya şifre\n")
                    continue
            if yeni_kullanici_girdi:
                break

#personel bilgilerini sorgulama
def personel_sorgulama():


    while True:
        yapilmak_istenen_islem = input("Hangi işlemi yapmak istiyorsunuz? örneğin 'personel ekleme' veya 'personel bilgi alma' gibi:  ")
        if yapilmak_istenen_islem in ["personel ekleme", "personel bilgi alma"]:
            break
        else:
            print("lütfen belirtilen şekilde işlemi belirtiniz")
            continue

    while True:
        if yapilmak_istenen_islem in ["personel bilgi alma"]:
            personel_bilgi_alma = input("Hangi personelin bilgisini öğrenmek istiyorsunuz? (çıkmak için 'çık' yazınız) : ")
            if personel_bilgi_alma in personeller:
                print(personeller[personel_bilgi_alma])
                continue
            elif personel_bilgi_alma == "çık":
                quit()
            else:
                print("Lütfen gecerli bir isim giriniz\n")
                continue
        else:
            break



personel_sorgulama()
