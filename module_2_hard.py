list_a = []
list_res = []
for d in range (0, 20):
    list_a.append(d + 1)
def password_(a):
    if a < 3 or a > 20:
        print("Извините, но вы ввели неверное число")
    else:
        for i in range (0, 20):
            for j in range(0, 20):
                if i == j:
                    continue
                if list_a[i] == a or list_a[j] == a:
                    break
                if a % (list_a[i] + list_a[j]) == 0:
                    no_dub = True
                    if len(list_res) > 0:
                        b = 0
                        while b < len(list_res):
                            if list_res[b] == list_a[i] and list_res[b + 1] == list_a[j]:
                                no_dub = False
                                break
                            if list_res[b + 1] == list_a[i] and list_res[b] == list_a[j]:
                                no_dub = False
                                break
                            b = b + 2
                    if no_dub:
                        list_res.append(list_a[i])
                        list_res.append(list_a[j])
        print (*list_res)
print ("Введите целое число от 3 до 20 включительно, чтобы получить пароль для выхода из ловушки:")
password_(int(input ()))