import random


def sayi_tahmin_oyunu():
    # 1 ile 100 arasında rastgele bir sayı seç
    hedef_sayi = random.randint(1, 100)
    tahmin_hakki = 7  # Kullanıcının tahmin etme hakkı
    print("Sayı Tahmin Oyununa Hoşgeldiniz!")
    print(f"1 ile 100 arasında bir sayı tahmin edin. {tahmin_hakki} hakkınız var.")

    while tahmin_hakki > 0:
        try:
            # Kullanıcıdan tahmin al
            tahmin = int(input("Tahmininiz: "))

            # Tahminin aralıkta olup olmadığını kontrol et
            if tahmin < 1 or tahmin > 100:
                print("Lütfen 1 ile 100 arasında bir sayı girin.")
                continue

            # Tahmini kontrol et
            if tahmin < hedef_sayi:
                print("Daha yüksek bir sayı tahmin edin.")
            elif tahmin > hedef_sayi:
                print("Daha düşük bir sayı tahmin edin.")
            else:
                print(f"Tebrikler! {hedef_sayi} sayısını doğru tahmin ettiniz.")
                break

            tahmin_hakki -= 1
            print(f"Kalana tahmin hakkınız: {tahmin_hakki}")

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    if tahmin_hakki == 0:
        print(f"Maalesef, tahmin hakkınız kalmadı. Doğru sayı {hedef_sayi} idi.")


# Oyunu başlat
sayi_tahmin_oyunu()
