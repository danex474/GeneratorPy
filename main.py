import random

def generate_ip():
    #Здесь генерируем ip адресс рандомно выбирая 4 числа от 1 до 254 и соединяя их точкой и возвращаем это ip а функцию генерации
    return ".".join(map(str, (random.randint(1, 254) for _ in range(4))))


def generate_mask():
    #Создаем список из всех возможных масок в задании 13 (точнее какие я смог найти)
    masks = [
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.252",
        "255.255.255.0",
        "255.255.0.0",
        "255.0.0.0",
    ]
    #Вохвращаем рандомную маску из списка
    return random.choice(masks)


def calculate_13(ip, mask):
    #Разделяем на 4 части адресы ip и маски и заносим в список
    ip_parts = list(map(int, ip.split(".")))
    mask_parts = list(map(int, mask.split(".")))
    #Применяем поразрядную коньюнкцию к соответствующим частям и заносим в список
    network_parts = []
    for i in range(4):
        network_parts.append(ip_parts[i] & mask_parts[i])
    #Возвращаем адресс, соединенный из частей
    return ".".join(map(str, network_parts))


def task_13():
    #Генерируем ip и маску
    ip = generate_ip()
    mask = generate_mask()
    #С помощью calculate решаем задачу с помощью применения поразрядной конъюнкции к заданным ip и маске.
    network = calculate_13(ip, mask)

    condition_text = f" IP-адрес: {ip} Маска: {mask}"
    solution_text = f" Сетевой адрес: {network}"

    return condition_text, solution_text




def task_15():
    #Генерируем случайные отрезки P и Q
    P_start = random.randint(100, 140)
    P_end = P_start + random.randint(20, 50)
    Q_start = random.randint(150, 190)
    Q_end = Q_start + random.randint(20, 50)

    question = (
        f"\n (x ∈ P) → (((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P)) истинна при любом значении переменной x"
    )
    #Выводим сгенерированные значения
    return P_start, P_end, Q_start, Q_end, question

def calculate_15(P_start, P_end, Q_start, Q_end):
    #Решаем задачу по данной формуле
    for A_start in range(P_start, P_end + 1):
        for A_end in range(A_start, P_end + 1):
            A = (A_start, A_end)
            valid = True
            # Заранее ограничим область x 1000
            for x in range(1000):
                if P_start <= x <= P_end:
                    if Q_start <= x <= Q_end and not (A[0] <= x <= A[1]) and P_start <= x <= P_end:
                        valid = False
                        break
            if valid:
                return A
    return None




def main():
    print("Номер задачи (13 или 15)?")
    task = input()
    print("Сколько нужно сгенерировать?")
    amount = int(input())
    print("----------------------------------------------------------------------------------------------------------------------------------------------")

    for i in range(amount):
        if task == "13":
            condition, solution = task_13()
            print(f"\n {i+1} генерация из {amount}")
            print(f"\nЗадача 13 №")
            print(" В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети\n относится к адресу сети, а какая – к адресу узла в этой сети. Адрес сети получается в результате применения поразрядной\n конъюнкции к заданному IP-адресу узла и его маске. По заданным IP-адресу узла и маске определите адрес сети:")
            print(condition)
            print("\n Решение:")
            print(solution)
            print("----------------------------------------------------------------------------------------------------------------------------------------------")
        elif task == "15":
            P_start, P_end, Q_start, Q_end, question = task_15()
            print(f"\n {i + 1} генерация из {amount}")
            print(f"\nЗадача 13 №")
            print(f" На числовой прямой даны два отрезка: P = [{P_start}; {P_end}] и Q = [{Q_start}; {Q_end}]. Укажите наименьшую возможную\n длину такого отрезка A, что формула:")
            print(question)
            A = calculate_15(P_start, P_end, Q_start, Q_end)
            if A is not None:
                A_length = A[1] - A[0] + 1
                print(f"\n Решение: \n В отрезке [{A[0]}; {A[1]}] содержится {A_length + 1} целых числа. Длина этого отрезка {A_length}")
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
            else:
                print(f"\n Решение: \n Не удалось найти подходящий отрезок A.")
                print("----------------------------------------------------------------------------------------------------------------------------------------------")
        else:
            print("Нет такой задачи в списке")
            print("----------------------------------------------------------------------------------------------------------------------------------------------")


if __name__ == "__main__":
    main()
