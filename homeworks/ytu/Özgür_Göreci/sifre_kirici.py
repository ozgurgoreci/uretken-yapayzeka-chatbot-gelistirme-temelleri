#Özgür Göreci 20061077 Şifre Kırıcı Jupyter üzerinden .jpynb formatında yaptım (py çevirirken sorun çıktı.)

import string #harfleri kolayca almak için 

def sifre_coz(sifreli_metin): # Şifre Çözmek için fonksiyon tanımladım
    alfabe = string.ascii_lowercase
    kaydirilmis_alfabe = alfabe[-5:] + alfabe[:-5]  # Alfabeyi 5 geri kaydırma
    cozme_tablosu = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                   kaydirilmis_alfabe + kaydirilmis_alfabe.upper())
    
    cozulmus_metin = sifreli_metin.translate(cozme_tablosu)
    return sayilari_ters_cevir(cozulmus_metin)  # Sayıları ters çevir

def sifrele(duz_metin): #Şifrelemek için fonksiyon tanımladım
    alfabe = string.ascii_lowercase
    kaydirilmis_alfabe = alfabe[5:] + alfabe[:5]  # Alfabeyi 5 ileri kaydırma
    sifreleme_tablosu = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                                       kaydirilmis_alfabe + kaydirilmis_alfabe.upper())
    
    sifreli_metin = duz_metin.translate(sifreleme_tablosu)
    return sayilari_ters_cevir(sifreli_metin)  # Sayıları ters çevir

def sayilari_ters_cevir(metin): # sadece sayıları ters çevirmek için kullanılan fonksiyon yazdım
    return ' '.join(c[::-1] if c.isdigit() else c for c in metin.split())

# Şifreli mesajı çözüyoruz
sifreli_metin = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
cozulmus_metin = sifre_coz(sifreli_metin)
print("Çözülmüş Mesaj:", cozulmus_metin)


# Bonus- Kullanıcıdan giriş alıp şifreleme ve çözme
if __name__ == "__main__":
    while True:
        secim = input("Şifrelemek için 'E', çözmek için 'D', çıkmak için 'Q' girin: ").upper()
        if secim == 'E':
            metin = input("Şifrelenecek metni girin: ")
            print("Şifreli Metin:", sifrele(metin))
        elif secim == 'D':
            metin = input("Çözülecek metni girin: ")
            print("Çözülmüş Metin:", sifre_coz(metin))
        elif secim == 'Q':
            print("Görev tamamlandı.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")



