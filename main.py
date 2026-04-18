def eng_yaqin_juft_son(royxat):
    yangi_royxat = []
    for son in royxat:
        if son % 2 == 0:
            yangi_royxat.append(son)
        else:
            yangi_royxat.append(son + 1)
    return yangi_royxat

sonlar = [1, 2, 3, 4, 5, 6]
print(eng_yaqin_juft_son(sonlar))
