inggris = int (input("masukan nilai inggris: "))
matematika = int (input("masukan nilai matematika: "))
indonesia = int (input("masukan nilai indonesia: "))
ipa = int (input("masukan nilai ipa: "))
ips = int (input("masukan nilai ips: "))

if inggris + matematika + indonesia / 3 >=75:
    ket = "lulus"
elif inggris + matematika + indonesia + ipa +ips / 5 >=70:
    ket = "lulus"
elif inggris >90 and matematika >90:
    ket = "lulus"
else:
    ket ="tidak lulus"

print("anda dinyatakan", ket)