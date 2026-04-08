
# 📧 Email Sender Script (Python)

![Python](https://img.shields.io/badge/Python-3.x-blue)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

> Простой и удобный CLI-скрипт для массовой отправки email через SMTP (например, Gmail)

---

## 📚 Содержание

- [🚀 Возможности](#-возможности)
- [📁 Структура проекта](#-структура-проекта)
- [⚙️ Установка](#️-установка)
- [🧩 Конфигурация](#-конфигурация)
- [📨 Формат файлов](#-формат-файлов)
- [▶️ Использование](#️-использование)
- [📊 Пример работы](#-пример-работы)
- [⚠️ Обработка ошибок](#️-обработка-ошибок)
- [🔒 Безопасность](#-безопасность)
- [💡 Roadmap](#-roadmap)

---

## 🚀 Возможности

- 📬 Массовая отправка писем
- 📄 Загрузка текста письма из файла
- ⚙️ Конфигурация через YAML
- 🔐 Поддержка SSL / TLS
- 📊 Отчёт об отправке
- ⚠️ Устойчивость к ошибкам

---

## 📁 Структура проекта

```bash
.
├── script.py
├── config.yml
├── emails.txt
└── body.txt
```

---

## ⚙️ Установка

```bash
git clone https://github.com/yourusername/email-sender.git
cd email-sender
pip install pyyaml
```

---

## 🧩 Конфигурация

Создайте файл `config.yml`:

```yaml
email: your_email@gmail.com
password: your_app_password
smtp_server: smtp.gmail.com
smtp_port: 465
subject: "Тема письма"
```

### 🔐 Gmail рекомендации

- Используйте **App Password**
- Включите 2FA
- Не используйте основной пароль

---

## 📨 Формат файлов

### 📄 emails.txt

```
user1@gmail.com
user2@gmail.com
user3@gmail.com
```

### 📝 body.txt

```
Здравствуйте!

Это тестовая рассылка.

С уважением,
Команда
```

---

## ▶️ Использование

```bash
python script.py emails.txt body.txt
```

---

## 📊 Пример работы

```bash
Успешное подключение к Gmail
Письмо отправлено на user1@gmail.com
Письмо отправлено на user2@gmail.com

Рассылка завершена. Успешно: 2/2
```

---

## ⚠️ Обработка ошибок

Скрипт обрабатывает:

- ❌ Отсутствие config.yml
- ❌ Ошибки YAML
- ❌ Проблемы SMTP
- ❌ Пустые файлы
- ❌ Ошибки отправки

---

## 🔒 Безопасность

- ❗ Не храните реальные пароли в репозитории
- ✅ Используйте `.env` или secrets
- 🔐 Применяйте App Password

---

## 💡 Roadmap

- [ ] HTML-письма
- [ ] Вложения
- [ ] Логирование
- [ ] Параллельная отправка
- [ ] Retry механизм

---

## 🤝 Contributing

Pull requests приветствуются 🚀  
Открывайте issue для предложений и багов.

---

## 📜 License

Apache License Version 2.0
