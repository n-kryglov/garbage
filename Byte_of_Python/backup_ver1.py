import os
import time

# 1. Каталоги и файлы для резерной копии собираем в список
source = ['C:\\Users\\Николай\\Documents', '"D:\\рэс подключение"']

# 2. Резервные копии будут храниться в этом каталоге
target_dir = 'D:\\BackUp'

# 3. Файлы помещаются в zip-архив
# 4. Именем для архива служит текущая дата и время
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.rar'

# 5. Используем команду "zip" для помещения файлов в архив
rar_command = "rar a {0} {1}".format(target, ' '.join(source))

# Запускаем создание резервной копии
if os.system(rar_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')