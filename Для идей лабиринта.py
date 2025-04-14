import pygame,os,sys,subprocess,threading 
pygame.init()
def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None


def run_infinite_field():
    """Запуск бесконечного режима игры в отдельном процессе."""
    subprocess.run([sys.executable, file_path])


    """
    Проверка содержимого клетки поля по координатам (x,y).
    Возвращает текстовое описание объекта в клетке.
    """
def check_cell(x, y):
    cell_content = field[y][x]
    if cell_content == 1:
        return "Минотавр"
    elif cell_content == 0:
        return "Пустая клетка"
    elif cell_content == 2:
        return "Ключ"
    elif cell_content == 3:
        return "Выход"
    elif cell_content == 4:
        return "Начало Реки"
    elif cell_content == 5:
        return "Конец Реки"
    elif cell_content == 6:
        return "Река"
    elif cell_content == 7:
        return "Стена"
    elif cell_content == 8:
        return "Портал"
    elif cell_content == 9:
        return "Больница"
    elif cell_content == 10:
        return "Начало"
    return "Неизвестный объект"
def check_cell_vestrel(x,y):
    '''
    Проверяет взаимодейстрие пули с разными объектами
    '''
    cell_content = field[y][x]
    if cell_content == 1:
        field[y][x] = 0
        return 0
    elif cell_content == 0:
        return 0
    elif cell_content == 2:
        return 0
    elif cell_content == 3:
        return 0
    elif cell_content == 4:
        return 1
    elif cell_content == 5:
        return 1
    elif cell_content == 6:
        return 1
    elif cell_content == 7:
        return 0
    elif cell_content == 8:
        return 0
    elif cell_content == 9:
        return 0
    elif cell_content == 10:
        return 1
def vestrel(shoot,x,y):
    '''
    Совершает выстрел
    '''
    while shoot==1:
        smej=0
        for key_event in pygame.event.get():
            if key_event.type == pygame.KEYDOWN:
                if key_event.key == pygame.K_BACKSPACE: # Отмена выстрела
                    return
                # Выбор направления выстрела
                if key_event.key == pygame.K_UP: # Выстрел вверх
                    smej=1
                    while smej==1: # Пуля двигается в выбранном направлении, взаимодействуя с объектами
                        y=y-1
                        if y>=0:
                            smej=check_cell_vestrel(x,y)
                        else:
                            smej=0
                    shoot = 0
                elif key_event.key == pygame.K_DOWN: # Выстрел вниз
                    smej=1
                    while smej==1: # Пуля двигается в выбранном направлении, взаимодействуя с объектами
                        y=y+1
                        if y<=(field_height//SIZE):
                            smej=check_cell_vestrel(x,y)
                        else:
                            smej=0
                    shoot = 0
                elif key_event.key == pygame.K_LEFT: # Выстрел влево
                    smej=1
                    while smej==1: # Пуля двигается в выбранном направлении, взаимодействуя с объектами
                        x=x-1
                        if x>=0:
                            smej=check_cell_vestrel(x,y)
                        else:
                            smej=0
                    shoot= 0
                elif key_event.key == pygame.K_RIGHT: # Выстрел вправо
                    smej=1
                    
                    while smej==1: # Пуля двигается в выбранном направлении, взаимодействуя с объектами
                        x=x+1
                        if x<=(field_width//SIZE):
                            smej=check_cell_vestrel(x,y)
                        else:
                            smej=0
                    shoot = 0
    return


def getSizeByPressedKey(key):
    Size=0
    if key == pygame.K_5:
        Size= 500
    elif key == pygame.K_6:
        Size= 600
    elif key == pygame.K_7:
        Size= 700
    elif key == pygame.K_8:
        Size= 800
    elif key == pygame.K_9:
        Size= 900
    else:
        return False
    return Size

def river_flow(x, y):
    """
    Обработка течения реки. Определяет новую позицию при движении по реке.
    Возвращает новые координаты (x,y).
    """
    # Находим индекс текущей клетки реки
    for i in range(len(river_x)):
        if x == river_x[i] and y == river_y[i]:
            index = i
    
    # Меняем координаты в зависимости от направления течения
    if direction[index] == 1:  # Течение вверх
        y -= 1
    elif direction[index] == 2:  # Течение вниз
        y += 1
    elif direction[index] == 3:  # Течение влево
        x -= 1
    elif direction[index] == 4:  # Течение вправо
        x += 1
    
    return x, y


# ========== КОНСТАНТЫ ИГРЫ ==========
SIZE = 100  # Размер одной клетки поля в пикселях
BLACK = (0, 0, 0)  # Цвет черный (RGB)
WHITE = (255, 255, 255)  # Цвет белый (RGB)
DONE_BUTTON_TEXT = "ГОЙДА"  # Текст на кнопке подтверждения
RULES1 = "1-Минотавр 2-Ключ 3-Выход 4-Начало реки 5-Конец реки"  # Правила игры часть 1
RULES2 = "6-Река 7-Стена 8-Портал 9-Больница 0-Начало"  # Правила игры часть 2
SIZE_PROMPT = "Введите размеры поля от 5 до 9"  # Подсказка при выборе размера поля

# ========== ИНИЦИАЛИЗАЦИЯ ПЕРЕМЕННЫХ ==========
filename = "ads.py"  # Имя файла для бесконечного режима
file_path = find_file(filename, os.getcwd())  # Поиск пути к файлу

# Загрузка и подготовка изображений для объектов
images = {
    1: pygame.transform.scale(pygame.image.load('1.png'), (SIZE, SIZE)),
    2: pygame.transform.scale(pygame.image.load('2.png'), (SIZE, SIZE)),
    3: pygame.transform.scale(pygame.image.load('3.png'), (SIZE, SIZE)),
    4: pygame.transform.scale(pygame.image.load('4.png'), (SIZE, SIZE)),
    5: pygame.transform.scale(pygame.image.load('5.png'), (SIZE, SIZE)),
    6: pygame.transform.scale(pygame.image.load('6.png'), (SIZE, SIZE)),
    7: pygame.transform.scale(pygame.image.load('7.png'), (SIZE, SIZE)),
    8: pygame.transform.scale(pygame.image.load('8.png'), (SIZE, SIZE)),
    9: pygame.transform.scale(pygame.image.load('9.png'), (SIZE, SIZE)),
    10: pygame.transform.scale(pygame.image.load('10.png'), (SIZE, SIZE)),
}

# Переменные состояния игрока
player_status = "Вы стоите в начале"  # Текущий статус игрока
cell_description = "Пустую клетку"  # Описание текущей клетки
player_x = -1  # Позиция игрока по X (начальное значение -1 означает не установлено)
player_y = -1  # Позиция игрока по Y
hospital_x = 0  # X-координата больницы
hospital_y = 0  # Y-координата больницы
current_index = 0  # Текущий индекс для работы с массивами
hospital_count = 0  # Счетчик больниц на карте
keys_collected = 0  # Количество собранных ключей
keys_total = 0  # Общее количество ключей на карте
map_ready = False  # Флаг готовности карты
player_mode = False  # Флаг режима игры (False - редактор, True - игровой режим)

# Настройки отображения
display = pygame.display.set_mode((1800, 1000))  # Создание окна 1800x1000
current_object = None  # Текущий выбранный объект для размещения
last_color = 0  # Код последнего выбранного объекта
colors = []  # Список кодов объектов на поле
river_flow_active = 0  # Флаг активности течения реки
click_x = []  # Список X-координат размещенных объектов
click_y = []  # Список Y-координат размещенных объектов
portal_x = []  # Список X-координат порталов
portal_y = []  # Список Y-координат порталов
river_x = []  # Список X-координат рек
river_y = []  # Список Y-координат рек
direction = []  # Список направлений течения рек
current_direction = 0  # Текущее направление для новой реки

# Настройка шрифта для текста
font = pygame.font.Font(None, 36)

# Инициализация игрового поля
field = []  # Основное игровое поле
width_input = 0  # Ввод ширины поля
height_input = 0  # Ввод высоты поля
field_width = 500  # Ширина поля по умолчанию (5 клеток)
field_height = 500  # Высота поля по умолчанию (5 клеток)
width_set = 0  # Флаг установки ширины (0 - не установлена)

# ========== ЭТАП 1: ВЫБОР РАЗМЕРА ПОЛЯ ==========
selecting_size = True
while selecting_size:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Проверка нажатия на кнопку "ГОЙДА"
            if 700 < event.pos[0] < 1100 and 850 < event.pos[1] < 950:
                map_ready = True
                selecting_size = False
        elif event.type == pygame.KEYDOWN:
            # Обработка ввода цифр для выбора размера
            if width_set == 0:  # Если ширина еще не выбрана
                size = getSizeByPressedKey(event.key)
                if size!=False:
                    width_set = 1
                    field_width = size
                else:
                    width_set = 0
            else:  # Если ширина выбрана, выбираем высоту
                size = getSizeByPressedKey(event.key)
                if size!=False:
                    field_height=size
            # Обработка backspace для сброса выбора
            if event.key == pygame.K_BACKSPACE:
                width_set = 0

    # Отображение интерфейса выбора размера
    size_display = f"{field_width//100}x{field_height//100}" 
    display.fill(WHITE)  # Очистка экрана
    
    # Отображение текущего размера
    text = font.render(size_display, True, BLACK)
    text_rect = text.get_rect(center=(900, 700))
    display.blit(text, text_rect)
    
    # Отображение подсказки
    text = font.render(SIZE_PROMPT, True, BLACK)
    text_rect = text.get_rect(center=(900, 500))
    display.blit(text, text_rect)
    
    # Отображение кнопки
    text = font.render(DONE_BUTTON_TEXT, True, BLACK)
    text_rect = text.get_rect(center=(900, 900))
    display.blit(text, text_rect)
    
    pygame.display.flip()  # Обновление экрана

# Создание пустого поля выбранного размера
for i in range(field_width // SIZE):
    field.append([0] * (field_height // SIZE))

# ========== ЭТАП 2: РЕДАКТОР КАРТЫ ==========
while map_ready:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Проверка нажатия на кнопку завершения редактирования
            if 1100 < event.pos[0] < 1300 and 650 < event.pos[1] < 750:
                map_ready = False
                player_mode = True
            
            # Размещение объектов на поле
            if (event.pos[0] < field_width and event.pos[1] < field_height 
                    and last_color != 0):
                river_flow_active = 1
                click_x.append(event.pos[0])
                click_y.append(event.pos[1])
                colors.append(last_color)
                field[(event.pos[1] // 100)][(event.pos[0] // 100)] = last_color
                
                # Особые обработки для разных объектов:
                # 1. Начальная позиция игрока
                if last_color == 10 and player_x == -1 and player_y == -1:
                    player_x = event.pos[0] // 100
                    player_y = event.pos[1] // 100
                
                # 2. Больница (может быть только одна)
                elif last_color == 9 and hospital_count == 0:
                    hospital_x = event.pos[0] // 100
                    hospital_y = event.pos[1] // 100
                    hospital_count = 1
                
                # 3. Ключи (считаем количество)
                elif last_color == 2:
                    keys_total += 1
                
                # 4. Портал (добавляем координаты)
                elif last_color == 8:
                    portal_x.append(event.pos[0] // 100)
                    portal_y.append(event.pos[1] // 100)
                
                # 5. Река (начало или течение)
                elif last_color == 4 or last_color == 6:
                    river_x.append(event.pos[0] // 100)
                    river_y.append(event.pos[1] // 100)
                    current_direction = 1
                    
                    # Выбор направления течения реки
                    while current_direction == 1:
                        for key_event in pygame.event.get():
                            if key_event.type == pygame.KEYDOWN:
                                if key_event.key == pygame.K_UP:
                                    direction.append(1)  # Вверх
                                    current_direction = 0
                                elif key_event.key == pygame.K_DOWN:
                                    direction.append(2)  # Вниз
                                    current_direction = 0
                                elif key_event.key == pygame.K_LEFT:
                                    direction.append(3)  # Влево
                                    current_direction = 0
                                elif key_event.key == pygame.K_RIGHT:
                                    direction.append(4)  # Вправо
                                    current_direction = 0
        
        # Выбор объекта для размещения (по нажатию цифр)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                last_color = 1
                current_object = "Минотавр"
            elif event.key == pygame.K_2:
                last_color = 2
                current_object = "Ключ"
            elif event.key == pygame.K_3:
                last_color = 3
                current_object = "Выход"
            elif event.key == pygame.K_4:
                last_color = 4
                current_object = "Начало Реки"
            elif event.key == pygame.K_5:
                last_color = 5
                current_object = "Конец Реки"
            elif event.key == pygame.K_6:
                last_color = 6
                current_object = "Река"
            elif event.key == pygame.K_7:
                last_color = 7
                current_object = "Стена"
            elif event.key == pygame.K_8:
                last_color = 8
                current_object = "Портал"
            elif event.key == pygame.K_9:
                last_color = 9
                current_object = "Больница"
            elif event.key == pygame.K_0:
                last_color = 10
                current_object = "Начало"

    # Отрисовка редактора карты
    display.fill(WHITE)  # Очистка экрана
    
    # Отрисовка сетки поля
    for row in range(field_height // SIZE):
        for col in range(field_width // SIZE):
            pygame.draw.rect(display, BLACK, 
                           (col * SIZE, row * SIZE, SIZE, SIZE), 1)
    
    # Отрисовка размещенных объектов
    for i in range(len(click_x)):
        if last_color != 0 and river_flow_active != 0:
            display.blit(
                images[colors[i]],
                (click_x[i] // 100 * 100, click_y[i] // 100 * 100)
            )
    
    # Отрисовка интерфейса редактора
    if current_object is not None:
        text = font.render(current_object, True, BLACK)
        text_rect = text.get_rect(center=(1300, 500))
        display.blit(text, text_rect)
    
    text = font.render(RULES1, True, BLACK)
    text_rect = text.get_rect(center=(1300, 550))
    display.blit(text, text_rect)
    
    text = font.render(RULES2, True, BLACK)
    text_rect = text.get_rect(center=(1300, 600))
    display.blit(text, text_rect)
    
    text = font.render(DONE_BUTTON_TEXT, True, BLACK)
    text_rect = text.get_rect(center=(1300, 700))
    display.blit(text, text_rect)
    
    pygame.display.flip()  # Обновление экрана

# Создание копии поля для игрового режима
field_copy = []
for i in range(field_width // SIZE):
    field_copy.append([0] * (field_height // SIZE))

# ========== ЭТАП 3: ИГРОВОЙ РЕЖИМ ==========
while player_mode:
    display.fill(WHITE)  # Очистка экрана
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Запуск бесконечного режима по кнопке
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if 1100 < event.pos[0] < 1300 and 650 < event.pos[1] < 850:
                threading.Thread(target=run_infinite_field).start()
        
        # Обработка движения игрока
        if event.type == pygame.KEYDOWN:
            # Движение вверх
            if event.key == pygame.K_e:
                    player_status="Выберите направление выстрела с помощью стрелок или отмениете его с помощью backspace"
                    text = font.render(player_status, True, BLACK)
                    text_rect = text.get_rect(center=(1100, 500))
                    display.blit(text, text_rect)
                    pygame.display.flip()
                    vestrel(1,player_x,player_y)
                    player_status = (f"Вы стоите в "
                                f"{check_cell(player_x, player_y)}")
            if event.key == pygame.K_UP:
                player_y -= 1  # Изменяем координату Y
                
                # Проверка выхода за границы
                if player_y < 0:
                    cell_description = "Стена"
                else:
                    cell_description = check_cell(player_x, player_y)
                
                player_status = (f"Вы сдвинулись на клетку вверх и встретили "
                               f"{cell_description}")
                
                # Обработка столкновений с разными объектами
                if cell_description == "Стена":
                    player_y += 1  # Возвращаем на предыдущую позицию
                elif cell_description == "Минотавр":
                    # Телепортация в больницу
                    player_y = hospital_y
                    player_x = hospital_x
                elif cell_description == "Ключ":
                    # Сбор ключа
                    keys_collected += 1
                    field[player_y][player_x] = 0  # Убираем ключ с поля
                elif cell_description == "Выход" and keys_collected == keys_total:
                    # Условие победы
                    player_status = "Вы победили!"
                elif cell_description == "Портал":
                    # Телепортация через портал
                    for i in range(len(portal_x)):
                        if (player_x == portal_x[i] 
                                and player_y == portal_y[i]):
                            current_index = i
                            current_index += 1
                        if current_index == len(portal_x):
                            current_index = 0
                    player_x = portal_x[current_index]
                    player_y = portal_y[current_index]
                elif cell_description in ["Начало Реки", "Река"]:
                    # Движение по течению реки
                    player_x, player_y = river_flow(player_x, player_y)
            
            # Движение вниз (аналогично движению вверх)
            elif event.key == pygame.K_DOWN:
                player_y += 1
                if player_y == field_height // 100:
                    cell_description = "Стена"
                else:
                    cell_description = check_cell(player_x, player_y)
                
                player_status = (f"Вы сдвинулись на клетку вниз и встретили "
                               f"{cell_description}")
                
                if cell_description == "Стена":
                    player_y -= 1
                elif cell_description == "Минотавр":
                    player_y = hospital_y
                    player_x = hospital_x
                elif cell_description == "Ключ":
                    keys_collected += 1
                    field[player_y][player_x] = 0
                elif cell_description == "Выход" and keys_collected == keys_total:
                    player_status = "Вы победили!"
                elif cell_description == "Портал":
                    for i in range(len(portal_x)):
                        if (player_x == portal_x[i] 
                                and player_y == portal_y[i]):
                            current_index = i
                            current_index += 1
                        if current_index == len(portal_x):
                            current_index = 0
                    player_x = portal_x[current_index]
                    player_y = portal_y[current_index]
                elif cell_description in ["Начало Реки", "Река"]:
                    player_x, player_y = river_flow(player_x, player_y)
            
            # Движение влево (аналогично)
            elif event.key == pygame.K_LEFT:
                player_x -= 1
                if player_x < 0:
                    cell_description = "Стена"
                else:
                    cell_description = check_cell(player_x, player_y)
                
                player_status = (f"Вы сдвинулись на клетку влево и встретили "
                               f"{cell_description}")
                
                if cell_description == "Стена":
                    player_x += 1
                elif cell_description == "Минотавр":
                    player_y = hospital_y
                    player_x = hospital_x
                elif cell_description == "Ключ":
                    keys_collected += 1
                    field[player_y][player_x] = 0
                elif cell_description == "Выход" and keys_collected == keys_total:
                    player_status = "Вы победили!"
                elif cell_description == "Портал":
                    for i in range(len(portal_x)):
                        if (player_x == portal_x[i] 
                                and player_y == portal_y[i]):
                            current_index = i
                            current_index += 1
                        if current_index == len(portal_x):
                            current_index = 0
                    player_x = portal_x[current_index]
                    player_y = portal_y[current_index]
                elif cell_description in ["Начало Реки", "Река"]:
                    player_x, player_y = river_flow(player_x, player_y)
            
            # Движение вправо (аналогично)
            elif event.key == pygame.K_RIGHT:
                player_x += 1
                if player_x == field_width // 100:
                    cell_description = "Стена"
                else:
                    cell_description = check_cell(player_x, player_y)
                
                player_status = (f"Вы сдвинулись на клетку вправо и встретили "
                               f"{cell_description}")
                
                if cell_description == "Стена":
                    player_x -= 1
                elif cell_description == "Минотавр":
                    player_y = hospital_y
                    player_x = hospital_x
                elif cell_description == "Ключ":
                    keys_collected += 1
                    field[player_y][player_x] = 0
                elif cell_description == "Выход" and keys_collected == keys_total:
                    player_status = "Вы победили!"
                elif cell_description == "Портал":
                    for i in range(len(portal_x)):
                        if (player_x == portal_x[i] 
                                and player_y == portal_y[i]):
                            current_index = i
                            current_index += 1
                        if current_index == len(portal_x):
                            current_index = 0
                    player_x = portal_x[current_index]
                    player_y = portal_y[current_index]
                elif cell_description in ["Начало Реки", "Река"]:
                    player_x, player_y = river_flow(player_x, player_y)

    # Отрисовка игрового интерфейса
    text = font.render(player_status, True, BLACK)
    text_rect = text.get_rect(center=(1300, 500))
    display.blit(text, text_rect)
    
    # Отрисовка кнопки бесконечного режима
    pygame.draw.rect(display, BLACK, (1100, 650, 200, 200), 1)
    
    pygame.display.flip()  # Обновление экрана
