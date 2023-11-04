import random as r

print("Omad show o'yiniga xush kelibsiz!")

mijozlar = []

print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
n=1 # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-mahsulot xarid qilgan odam raqamini kiriting: "
    mijoz = input(savol)
    mijozlar.append(mijoz)
    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
    if javob =='ha':
        n+=1
        continue
    else:
        break

print(mijozlar)

print(f"Hurmatli {r.choice(mijozlar)} raqam egasi sizni keyingi ko'rsatuvga taklif qilamiz!")