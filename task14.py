file = input("Faly nomini kengaytmasi bilan kiriting: ")

if file.endswith(".pdf"):
    print("Fayl turi: pdf")
elif file.endswith(".doc"):
    print("Fayl turi: doc")
elif file.endswith(".txt"):
    print("Fayl turi: txt")
else:
    print("Nomalun fayl turi")
    