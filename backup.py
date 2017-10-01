''' Создание архива с файлами '''

import os
import time

source = [i for i in input('Укажите папки(-у) с файлами для создании архива zip: ').split(' ')] # указываем папки(-у) с файлами
target_dir = input('Укажите в какой папке будет храниться zip архив: ') # папка для хранения архива
catalog = target_dir + os.sep + input('Название папки для файла zip --> ')  # название для подпапки
name_of_zip = input('Введите название zip файла --> ')  # название архива

if len(name_of_zip) == 0:   # если название архива не было введено, задаем ныняшнее время
    target = catalog + os.sep + time.strftime('%H%M%S')
else:    
    target = catalog + os.sep + name_of_zip.replace(' ', '_') + '.zip' #

if not os.path.exists(catalog): # если подпапки не существует, создаем
    os.mkdir(catalog)
    print('Каталог успешно создан', catalog)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source)) # команда для архирования

if os.system(zip_command) == 0: # проверка на ошибки
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось!')