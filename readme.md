Sms Sender
==================================
Python3 support.<br>
SmsSender - Класс отправки SMS сообщений из python. Использует API сервиса http://sms.ru/.<br>
Написана на Python.<br>
Автор Sergey LittleBuster Denisov.<br>
Автор первоначального приложения Denis Saymon21 Khabarov.<br>
Email DenisovS21@gmail.com.<br>
Лицензия GNU GPLv3.<br>
Текущая версия: 0.3.<br>
Репозиторий: https://github.com/LittleBuster/smssend<br>

Функции:

````
send - Отправка сообщения, передавая параметры соединения

send_from_cfg - Отправка сообщения с загруженной из файла конфигурацией
````

Возвращаемые коды:

````
0	Сообщение отправлено успешно.
1 	Сервис вернул ошибку
2	HTTP ошибка
3	Ошибка при использовании утилиты
````


Конфигурации могут быть прочитаны из файла:
````
sms.cfg
````

Пример использования:

````
from smssend import SMSSender

sms = SMSSender()
sms.send_from_cfg("Привет мир", "sms.cfg")
````
