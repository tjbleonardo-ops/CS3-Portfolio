while True:
    year = input("Enter your birth year: ")
    if year.isdigit():
        year = int(year)   
        if 1899 < year < 2027:
                break
    print("Please enter a valid year between 1900 and 2026.")
lista = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
zodiac_index = (year - 1900) % 12
zodiac_sign = lista[zodiac_index]
print(f"Your zodiac sign is {zodiac_sign}.")
