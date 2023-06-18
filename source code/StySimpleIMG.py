import cv2
import numpy as np
from tkinter import Tk, Button, Label, filedialog

def preprocess_image(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    
    # Преобразование изображения в черно-белое
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Применение фильтра Canny для обнаружения границ
    edges = cv2.Canny(gray, 50, 150)
    
    # Расширение границ для более точного обвода
    dilated_edges = cv2.dilate(edges, None, iterations=2)
    
    return dilated_edges

def save_processed_image(image_path, processed_image):
    # Сохранение обработанного изображения
    cv2.imwrite(image_path, processed_image)

def select_image():
    # Открытие диалогового окна выбора файла
    file_path = filedialog.askopenfilename(filetypes=[("Изображения", "*.jpg;*.jpeg;*.png")])
    
    # Если выбрано изображение, продолжаем обработку
    if file_path:
        # Предварительная обработка входного изображения
        processed_image = preprocess_image(file_path)
        
        # Генерация пути для сохранения обработанного изображения
        output_path = file_path.replace(".", "_processed.")
        
        # Сохранение обработанного изображения
        save_processed_image(output_path, processed_image)
        
        # Отображение сообщения об успешной обработке
        result_label.config(text="Изображение успешно обведено и сохранено.")

# Создание графического интерфейса с помощью Tkinter
root = Tk()
root.title("staytro simple image converter")
root.geometry("300x100")

# Кнопка выбора изображения
select_button = Button(root, text="Выбрать изображение", command=select_image)
select_button.pack(pady=10)

# Метка с результатом обработки
result_label = Label(root, text="")
result_label.pack()

# Запуск главного цикла Tkinter
root.mainloop()
