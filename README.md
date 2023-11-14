# DPO_PSTU_2023-2024

## Практические задания ДПО

Репозиторий Алексея Гребнева по курсу ДПО

### Задача на практику №1

**Цель практики:** Определить уровень знаний с которыми вы приходите на курс.

**Задание:** Требуется создать приложение, которое динамически (опционально, если хочется - можно статические) показывает курс валют с историческим промежутокм (на ваш выбор) на графике.

Инструменты для выполнения задания: Любые на ваш выбор.

**Вариант выполнения:**
Использовать python и matplotlib для графика, например: https://matplotlib.org/stable/gallery/mplot3d/errorbar3d.html#sphx-glr-gallery-mplot3d-errorbar3d-py
Получать данные для вашего графика из определённого источника:

2.1. На свой выбор;

2.2. Использовать XML сервис Центробанка: https://www.cbr.ru/development/dws/ (Сложность: комплексный сервис со сложной структурой справочников);

2.3. Использовать скрейпинг (Beautiful Soup, Requests, Scrapy) и достать данные вот отсюда: https://ru.investing.com/currencies/usd-rub-historical-data (Сложность: разобраться со структурой страницы);

2.4 Воспользоваться более простыми опциями вот отсюда: https://www.cbr-xml-daily.ru/;

**Репозиторий для сдачи практики:** https://github.com/lulzforme/iad-test-task1

Для сдачи нужно сделать Fork изначального репозитория и отправить Pull Request.

Именовать PR в формате: test-FIO-versionnumber
**Ссылка на документацию:** https://docs.github.com/ru/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
