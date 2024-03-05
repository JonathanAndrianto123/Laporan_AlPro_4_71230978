def cek_angka(a, b, c) : 
    if (a != b != c) and (a + b == c or a + c == b or b + c == a) :
        return "True"
    else :
        return "False"

print(cek_angka(5, 3, 8))
print(cek_angka(6, 5, 9))

