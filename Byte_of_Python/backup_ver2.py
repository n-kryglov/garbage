import os
import time

# 1. Каталоги и файлы для резерной копии собираем в список
source = ['C:\\Users\\Николай\\Documents', '"D:\\рэс подключение"']

# 2. Резервные копии будут храниться в этом каталоге
target_dir = 'D:\\BackUp'

# 3. Файлы помещаются в zip-архив
# 4. Именем для архива служит текущая дата и время
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.rar'
else:
    target = today + os.sep + now + '_' + comment + '.rar'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)
# Имя zip-файла
target = today + os.sep + now + '_' + comment + '.rar'


# 5. Используем команду "zip" для помещения файлов в архив
rar_command = "rar a {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(rar_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')