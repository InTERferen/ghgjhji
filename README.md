## 📦 tonRocket captcha solver
<img src="https://i.imgur.com/f6Jb6qA.jpg"></img>  

<div align="center">

  <a href="" alt="GitHub repo size"><img src="https://img.shields.io/github/repo-size/Conradk10/tonRocket-captcha-solver" /></a>
  <a href="" alt="GitHub issues"><img src="https://img.shields.io/github/issues-raw/Conradk10/tonRocket-captcha-solver" /></a>
  <a href="" alt="GitHub"><img src="https://img.shields.io/github/license/Conradk10/tonRocket-captcha-solver" /></a>
  <a href="" alt="GitHub"><img src="https://img.shields.io/github/forks/Conradk10/tonRocket-captcha-solver" /></a>
  <a href="" alt="GitHub"><img src="https://img.shields.io/github/stars/Conradk10/tonRocket-captcha-solver" /></a>

</div>

- Данный скрипт предназначен для автоматизации активации мульти-чеков из бота @tonRocketBot с множества аккаунтов Telegram. 
Скрипт использует библиотеку Telethon для взаимодействия с Telegram API.
## 💡 Обосенности
- Поддерживает неограниченное количество сессий
- Поддерживает ввода пароля от чека
- Автоматическое прохождение капчи с emoji
- Автоматическое прохождение капчи с подпиской на каналы/группы
## ⚙️ Принцип работы
- Работа скрипта начинается с загрузки списка сохраненных сессий для каждого аккаунта, затем создается клиент TelegramClient для каждой сессии и выполняется подключение к Telegram API. Затем происходит отправка сообщения боту и обработка ответа. В зависимости от содержимого сообщения, могут выполняться различные действия, например подписка на каналы, активация мульти-чека или нажатие на кнопку для прохождения капчи.
## 🛠 Установка
1. Клонируем репозиторий   
`git clone https://github.com/Conradk10/tonRocket-captcha-solver.git`   
2. Переходим в директорию  
`cd tonRocket-captcha-solver`  
3. Создаем виртуальное окружение   
`python3 -m venv env`   
4. Активируем виртуальное окружение   
`source env/bin/activate`   
5. Устанавливаем зависимости   
`python3 -m pip install -r requirements.txt`
## 🎚 Настройка `config.py`
- Получение `API_ID` и `API_HASH` из `config.py`   
1. Для начала нужно перейти по <a href="https://my.telegram.org/apps">этой</a> или <a href=https://my.telegram.org/auth>этой</a> ссылке   
2. Ввести номер телефона и нажать `API development tools`   
3. Создать приложение заполнив данные на свое усмотрение (если не создано ранее)  
4. Скопировать `App api_id` и `App api_hash` и заменить в файле `config.py` соответствующие переменные новыми значениями
- `TEMP_DIR` и `SESSIONS_DIR` отвечают за название директорий с временными файлами и файлами сессий (`*.session`)   
## ▶️ Запуск
Запуск скрипта осуществляем с активированным виртуальным окружением с помощью команды   
`python3 main.py [ссылка на чек (Пример: https://t.me/tonRocketBot?start=loremipsum)]`  
Либо с указанием ссылки в ходе выполнения скрипта  
`python3 main.py`  
Затем ввести пароль от чека (если имеется) или пропустить нажатием клавиши Enter
## 📝 Зависимости
`Python 3.8+`
```
tgchequeman==0.0.3
loguru==0.6.0
```
