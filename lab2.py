#1===========================================
password=input("Введите пароль:")
if len(password)<8:
    print("Слишком короткий пароль")
if len(password)>=8:
    print("Пароль принят")

#2===========================================
status=input("online or offline:")
if status=="online":
    print("Связь установлена")
else:
    print("Связь потеряна")

#3===========================================
n=int(input("Оцените угрозу по шкале от 1 до 100"))
if n<=30:
    print("Низкий уровень угрозы")
elif n>30 and n<71:
    print("Средний уровень угрозы")
elif n>70 and n<=100:
    print("Критический уровень угрозы")
else:
    print("Ошибка ввода")

#4===========================================
checksum_original=int(input())
checksum_current=int(input())
status="Файл не изменен" if checksum_current==checksum_original else "Файл поврежден"
print(status)

#5===========================================
event_code=input()
match event_code:
    case "ERR":
        print("Ошибка системы")
    case "WRN":
        print("Предупреждение")
    case "INF":
        print("Информационное сообщение")
    case _:
        print("Неизвестный код события")