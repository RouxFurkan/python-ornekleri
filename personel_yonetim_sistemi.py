#Personel listeleme

#İçeride kayıtlı kullanıcılar

personel_ahmet = {
    "isim" : "Ahmet",
    "soyisim" : "Karalar",
    "brans" : "Full Stack Developer",
}

personel_mehmet = {
    "isim" : "Mehmet",
    "soyisim" : "Sudan",
    "brans" : "Backend developer",
}

personel_furkan = {
    "isim" : "Furkan",
    "soyisim" : "Yesilirmak",
    "brans" : "Frontend Developer",
}

personel_enes = {
    "isim" : "Enes",
    "soyisim" : "Isıl",
    "brans" : "Dev OPS",
}

personel_kerem = {
    "isim" : "Kerem",
    "soyisim" : "Anıl",
    "brans" : "Senior",
}


#Önceden tanımlanmış kullanıcı
kullanici_adi = "furkan"
sifre = "5223"

#Mevcutta bir hesabı oldup olmadığını öğrenme
while True:
    hesap_bilgisi = input("Mevcutta bir hesabınız var mı?\nVarsa, Evet, yoksa Hayır yazın. :")

    if hesap_bilgisi == "Evet" or hesap_bilgisi == "Hayır":
        break
    else:
        print("lütfen belirtilen formatta yazınız")
        continue



#Mevcutta kayıtlı bir hesabı yoksa yeni hesap oluşturma
while True:

    if hesap_bilgisi == "Hayır":
        yeni_kullanici_adi_giris = input("Yeni bir kullanıcı adı oluşturun: ")
        yeni_sifre_giris = input("Yeni bir şifre oluşturun: ")
        print(f"Hesabınız başarıyla oluşturuldu\n Kullanıcı adınız: {yeni_kullanici_adi_giris}\n Şifreniz: {yeni_sifre_giris}")
        break
    else:
        break



#Varsa ya da yeni oluşturulduysa login olma
while True:
    kullanici_adi_girin = input("Lütfen kullanıcı adınızı giriniz: ")
    sifre_girin = input("Lütfen şifrenizi giriniz: ")
    if kullanici_adi == kullanici_adi_girin and sifre == sifre_girin or yeni_kullanici_adi_giris == kullanici_adi_girin and yeni_sifre_giris == sifre_girin:
        print("giriş başarılı")
        break
    else:
        print("yanlış kullanıcı adı veya şifre\n")


#personel bilgilerini sorgulama
def personel_sorgulama():

    while True:
        personel_bilgi_alma = input("Hangi personelin bilgisini öğrenmek istiyorsunuz? : ")

        if personel_bilgi_alma in ["ahmet","mehmet","furkan","enes","kerem"]:
            if personel_bilgi_alma == "ahmet":
                print(personel_ahmet)
                break
            if personel_bilgi_alma == "mehmet":
                print(personel_mehmet)
                break
            if personel_bilgi_alma == "furkan":
                print(personel_furkan)
                break
            if personel_bilgi_alma == "enes":
                print(personel_enes)
                break
            if personel_bilgi_alma == "kerem":
                print(personel_kerem)
                break
        else:
            print("Lütfen gecerli bir isim giriniz")
            continue

    print("dogru isim girildi")

personel_sorgulama()
