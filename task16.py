yosh = int(input("Yoshingizni kiriting: "))
chipta = 100000
if yosh <= 6:
    narx = chipta * 0.5
    print(f"Yakuniy narx: {narx} so'm 50% chegirma ")
elif yosh <= 17:
    narx = chipta * 0.8
    print(f"Yakuniy narx: {narx} so'm 20% chegirma ")
elif yosh <= 60:
    narx = chipta * 0.7
    print(f"Yakuniy narx: {narx} so'm 30% chegirma ")
else:
    print(f"Yakuniy narx: {chipta} so'm sizga hech qanaqa chegirma yo'q")