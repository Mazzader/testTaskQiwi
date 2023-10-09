## Тестовое задание для QIWI
### Сборка и запуск:
```shell
docker-compose up --build -d 
docker-compose exec testapp bash
cd src
python manage.py migrate
```
Документацию ради одного метода писать не стал.

Метод лежит в:
```
POST: http://0.0.0.0:8000/api/game
```
Принцип работы:
Цепляемся за джанго сессии(храним в куках запроса и в б.д.) Пока сессия активна - игра продолжается.
Каждый новый запрос к API генерирует обновление поля.

Реализация алгоритма в виде класса лежит в пакете: ```src/gameOfLife/helpers.GameOfLife```


P.S. ENV файлы залил сознательно, чтобы для проверки работоспособности не пришлось придумыать логины пароли и ключи самостоятельно :)