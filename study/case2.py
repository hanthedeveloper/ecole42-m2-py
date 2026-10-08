notlar = [("Ali", 85), ("Ayşe", 92), ("Can", 45), ("Ayşe", 78), ("Deniz", 60), ("Ali", 90)]

''' Bölüm 1: List metodları
Listeye yeni bir tuple ekle: ("Elif", 70) (append).
İki tuple'ı birden ekle (extend). append ile extend farkı nedir?
Listeden ("Can", 45) kaydını çıkar (remove). Listede olmayan bir kaydı çıkarmaya çalışınca hata gelir.
Notlara göre sırala. Hangisi listeyi yerinde değiştirir, hangisi yeni liste döndürür?
Kaç kayıt var (len), "Ali" kaç kez geçiyor (tuple'lar için count çalışmaz, nedenini düşün). '''

notlar.append(("Elif", 70))
print(notlar)
print()

newlist = [("Büşra", 90), ("Şilan", 100), ("Beyza", 101)]
notlar.extend(newlist)
print(notlar)
print()

for i in notlar:
    if i == ("Can", 45):
        try:
            notlar.remove(("Can", 45))
        except ValueError:
            print(f"Error: {i} is not in the list") 
print(notlar)
print()

notlar.append(("Can", 45))

print(sorted(notlar)) # alfabeye gore sıralar
print(sorted(notlar))