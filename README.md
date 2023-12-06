# Метод анализа иерархий Томаса Саати
### Исполнитель 
Смирнов Никита Артемович

### Описание программы: 
Программа, реализующая метод анализа иерархий Томаса Саати. Использовались такие библиотеки, как "tkinter", "numpy", "pandas" (для корректной работы numpy) и "threading".

- С помощью библиотеки "tkinter" был реализован простой интуитивный графический интерфейс. Если оставить поле ввода пустым, программа выдает предупреждение-ошибку в отдельном окне и продолжает свою работу. При введении данных неправильного типа программа не продолжает работу.

- С помощью библиотек "numpy" и "pandas" были реализованы вычисления коэффицентов матричным методом, находя собственный вектор матрицы и нормируя его.

- С помощью библиотеки "threading" был реализован поток, позволяющий приостановить выполнение цикла вычислений до заполнения поля ввода и нажатия кнопки "Ввод". Другими словами была реализована функция input в графическом интерфесе tkinter.

Программа предлагает ввести количество критериев, далее попарно сравнивая их и выясняя насколько один приоритетнее другого. После введения всех значений программа выдает результат измерений в виде коэффицентов 0.00

____

Программу желательно запускать в IDE JetBrains Community Edition 2023;

Программa создавалась в IDE JetBrains Community Edition 2023.2.1;

Также программу можно запустить не прибегая к помощи IDE, напрямую открыть файл.
____
### Скриншоты работы программы:
![image](https://github.com/timinius/lab6/assets/69468245/cc9055a2-e9eb-4c4a-b343-e95999e562db)
![image](https://github.com/timinius/lab6/assets/69468245/9c30b4e9-ed5e-474f-a506-a077ca7b9c65)
![image](https://github.com/timinius/lab6/assets/69468245/42a8dc80-9351-40f3-bf32-80f63155cb5d)
![image](https://github.com/timinius/lab6/assets/69468245/02cd9bb8-2034-4dd2-ad1a-bdc0764c9e3d)
![image](https://github.com/timinius/lab6/assets/69468245/721e962c-0c92-47ed-8f83-0a6d084b409f)


