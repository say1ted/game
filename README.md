# Текстовая РПГ
Версия 0.1a
Движок
- парсер файла локаций
- консольный интерфейс (быстрые клавиши, вывод данных по локации)
- обработчик команд
Ресурсы
- файл локаций

Пример файла локаций:
{
  "Локация 1": 
  { 
    "Описание": "Ты в дремучем лесу",
    "Направления": 
      {
        "Лес",
        "Дом"
      }
  }
  "Дом":
  {
  ...
  }
}

Интерфейс:
@@@@@@@@@@@@@@@@@
@   Локация 1   @
@@@@@@@@@@@@@@@@@
Описание
.
.
-----------------
Куда пойти:
-> Лес
<- Дом




