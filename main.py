my_list = [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0]]

while True:
    print('1. Parkovkaga kirish: ')
    print('2. Parkovkaga chiqish: ')
    print('3. Parkovkani malumotini ko\'rish: ')
    print('4. end')
    
    tanlash = int(input('Tanlash: '))
    
    if tanlash == 1:
        qator = int(input('Nechanchi qator: '))-1
        joy = int(input('Nechanchi joy: '))-1
        moshina = (input('Nomi moshina: '))
        if my_list[qator][joy] == 0:
            my_list[qator][joy] = moshina
            print(f"{moshina} {qator+1} qatoru {joy+1} joyga qo'shildi")
        else: 
            print(f'Bu {qator+1} qatoru {joy+1} joyga {moshina} moshinasi mavjud')
            for i in range(len(my_list[qator])):
                if my_list[qator][i] == 0:
                    print(f'Bu {qator+1} qatoru {i+1} joy mavjud')
                    break
            else:  
                for i in range(len(my_list)):
                    for j in range(len(my_list[i])):
                        if my_list[i][j] == 0:
                            print(f'Bu {i+1} qatoru {j+1} joy mavjud')
                            break
                        if i == qator:
                            continue
            
    

    if tanlash == 2:
        uchirish = int(input('Moshin olib tashaysizmi? 1 - ha 2 - yoq: '))
        if uchirish == 1:
            qator = int(input('Nechanchi qator: '))-1
            joy = int(input('Nechanchi joy: '))-1
            my_list[qator][joy] = 0
            print(f"{moshina} moshinasi {qator+1} qatoru {joy+1} jyydan olib tashlandi")
        
                                                                                                                                                                                        
    if tanlash == 3:
        moshinani_kurish = int(input('Parkovkani malumotini ko\'rishni istaysizmi? 1 - ha 2 - yoq: '))
        if moshinani_kurish == 1:
            for i in my_list:
                for j in range(0, 5):
                    print(i[j], end=' ')
                print()


    if tanlash == 4:
        break




# my_list = [
#     [1, 23, 45, 67, 89, 90],
#     [-6, 56, 34, 12, 0],
#     [1, 3, 4, 8, 5, 6],
# ]

# for i in range(0, 3):
#     get_max = my_list[i][0]
#     for j in range(0, 5):
#         if my_list[i][j] > get_max:
#             get_max = my_list[i][j]
#     print(get_max)