# Домашняя работа 

## Описание:

Домашняя работа (далее дз) - это проект в котором созданы и описаны простые функции банковского приложения,
такие как маскировка карт и счетов, сортировка банковских
операций по дате или вовсе фильтрация по завершенным или нет операциям

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/pav1eu/home_work.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Запустите одну из представленных строчек для проверки функционала
```
python src/masks.py
```
```
python src/widget.py
```
```
python src/processing.py
```
```
python src/generators.py
```

## Тестирование:
Для запуска тестирования кода введите команду:
```
poetry run pytest --cov
```
в командной строке (стаботает только после установки звисимостей)
## Документация:

Пока ничего нет.

## Лицензия:

Лицензирован мной