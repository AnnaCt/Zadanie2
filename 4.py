all = 2800000 # Всего экспонатов
exp = 1/5 # Количество экспонатов за минуту
min_day = 60 * 8 # Количество минут за день просмотра
min_year = min_day * 365 # Количество минут просмотра за год
exp_day = min_day * exp # Количество экспонатов за 1 день просмотра
exp_year = min_year * exp # Количество экспонатов за год просмотра
print("Введите количество экспонатов, не больше 2800000")
expo= float(input())
print("Введите количество лет")
year= float(input())
in_day= expo//exp_day
in_year= year*exp_year
print("Просмотр", str(int(expo)) , "экспонатов займет", str(int(in_day)), "дней" , sep=" ")
print("За", str(int(year)), "лет будет просмотрено", str(int(in_year)), "экспонатов", sep=" ")
