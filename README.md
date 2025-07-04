Краткое описание кода
Этот скрипт — генератор паролей с поддержкой двух языков (русский/английский). 
Пользователь может выбрать:
Язык интерфейса (русский или английский).
Длину пароля.
Алфавит для букв (русские или английские символы).
Использование спецсимволов (да/нет).

Осовные компоненты
Словари символов:
rus: 33 русские буквы.
ang: 26 английских букв.
sim: 32 специальных символа (например, _, @, $).

Логика работы:
Шаг 1: Пользователь выбирает язык интерфейса.
Шаг 2: Указывает длину пароля (рекомендуется ≥8 символов).
Шаг 3: Выбирает алфавит (русский/английский).
Шаг 4: Разрешает или запрещает спецсимволы.

Генерация пароля:
Каждый символ пароля случайно выбирается из категорий: буквы (в верхнем/нижнем регистре), цифры (0-9), спецсимволы (если разрешены).
Каждые 3 символа добавляется дефис - (для удобочитаемости).
Результат выводится как строка (например, 5Тл-9@К-3р).


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Short description of the code
This script is a password generator with support for two languages (Russian/English). 
The user can choose:
Interface language (Russian or English).
The length of the password.
The alphabet for letters (Russian or English characters).
Using special characters (yes/no).

Main components
Character dictionaries:
rus: 33 Russian letters.
English: 26 English letters.
sim: 32 special characters (for example, _, @, $).

The logic of the work:
Step 1: The user selects the interface language.
Step 2: Specifies the password length (recommended ≥8 characters).
Step 3: Selects the alphabet (Russian/English).
Step 4: Allows or disables special characters.

Password generation:
Each character of the password is randomly selected from the categories: letters (uppercase/lowercase), numbers (0-9), special characters (if allowed).
Every 3 characters, a hyphen is added (for readability).
The result is output as a string (for example, 5Tl-9@K-3p).
