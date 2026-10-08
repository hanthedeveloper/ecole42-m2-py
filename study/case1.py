''' Görevler
Dict: Oyuncu adı → eşya set'i şeklinde bir dict kur. Ayrı bir dict'te oyuncu adı → konum tuple'ı tut.

Beklenen çıktı örneği (biçim serbest)
Ortak eşyalar: {'potion'}
Tüm eşyalar: {...}
Alice'e özel: {'shield'}
Bob'a özel: {'bow'}
Charlie'ye özel: {'helmet'}
Alice-Bob mesafesi: 5.0
Alice ve Charlie aynı konumda: True
Tuple değiştirilemez: ... '''

''' Set işlemleri:
Herkeste ortak olan eşyaları bul (intersection).
Haritadaki tüm farklı eşyaları bul (union).
Her oyuncu için sadece onda olan eşyaları bul (difference, diğerlerinin birleşimine karşı). '''

invdict: dict[str, set[str]] = {
    "alice": {"sword", "shield", "potion", "map"},
    "bob": {"potion", "map", "bow"},
    "charlie": {"potion", "helmet", "sword"}
}

posdict: dict[str, tuple[int, int]] = {
    "alice": (2, 3),
    "charlie": (2, 3),
    "bob": (5, 7)
}

print("ortak:", set.intersection(invdict["alice"], invdict["charlie"], invdict["bob"]))
print("tüm:", set.union(*(invdict.values())))

def get_diff(name: str, a_dict: dict[str, set[str]]) -> set[str]:
    newlist = []
    for k, v in a_dict.items():
        if k != name:
            newlist.append(v)
    try:
        newset = set.union(*newlist)
    except TypeError:
        print("bos dict.")
    else:
        return a_dict[name].difference(newset)
print("sadece alice:", get_diff("alice", invdict))
print("sadece bob:", get_diff("bob", invdict))
print("sadece charlie", get_diff("charlie", invdict))

''' Alice ile Bob arasındaki mesafeyi hesapla (Öklid, 2D).
Alice ve Charlie'nin konumunu karşılaştır. Aynı konumdalar mı? Tuple'lar == ile nasıl
karşılaştırılıyor?
Tuple + dict birlikte: Anahtarı konum, değeri o konumdaki oyuncuların listesi olan bir dict kur.
Alice ve Charlie aynı konumda olduğu için aynı anahtara düşecekler. Bunu kurarken bir sorunla
karşılaşmayacaksın, çünkü tuple hashable. Aynı şeyi liste anahtarıyla denersen ne olur?
Dene ve hatayı gör.
Exception: Alice'in konum tuple'ında x değerini değiştirmeyi dene. Çıkan hatayı try/except ile
yakala ve mesajı yazdır. Programın çökmemesi gerekiyor. '''