first_int = input('привет, начнём?')
int_cut = first_int
while int_cut != 'Выйти' and int_cut != '3':
    print('1) {Начать путишествие}')
    print('2) {Настройки}')
    int_cut = input('3) {Выйти}')
    print(' ')
    if int_cut == '1' or int_cut == 'Начать путишествие':
        print('загрузка')
        for i in range(1001):
            print(i)
            print(' ')
    if int_cut == '2' or int_cut == 'Настройки':
        print('пока, что недоступно')
        int_cut = input('1) {Назад}')
