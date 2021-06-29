**_VeloBot_** - Бот для парсинга сайтов для велопродажи по опередленной работе

**Цель**: Практика в асинхронном программировании на Python

**Инструменты**: 
- 
- Playwright - инструмент для взаимодействия с API браузера, для эмуляции действий пользователя
- Asyncio - библиотека для асинхроннного программирования на Python
- Docker - система контеризации

**Запуск приложения**:
- 
Необходимо указать 2 аргумента:
- BOT_TOKEN - Токен вашего бота в Telegram
- CHAT_ID - id чата с ботом

##### Команды для запуска контейнера:

- Создаем image: `docker build -t <name_for_your_image> . `
- Создаем container: `docker run -it -e BOT_TOKEN='<your_token>' -e CHAT_ID='<your_id>' --rm —-name=<name_for_container> <name_your_image>`