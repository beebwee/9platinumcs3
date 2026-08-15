# File name: zodiacSectionLN.py

REQUIREMENTS:
a. Ask the user to enter a year of birth. The baseline year 1900.

user_input = input("Enter your birth year:\n")

birth_year = int(user_input)


b. Validate user input that it should not be earlier than 1900.

c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

if birth_year < 1900:

    print("Invalid birth year. It should not be earlier than 1900. Try again.”)
    exit()

-----------
ACTUAL CODE:

zodiac_animals = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)","Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

user_input = input("Enter your birth year:\n")

birth_year = int(user_input)

if birth_year < 1900:

    print("Invalid birth year. It should not be earlier than 1900. Try again.”)
    exit()

animal_index = (birth_year - 1900) % 12

zodiac_animal = zodiac_animals[animal_index]

print(f"Your Chinese Zodiac animal is: {zodiac_animal}")