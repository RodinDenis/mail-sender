#!//usr/bin/env python3

import argparse
import smtplib
import yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import os

def load_config():
    """Загрузка конфигурации из config.yml"""
    try:
        with open('config.yml', 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print("Ошибка: Файл config.yml не найден в директории запуска скрипта.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Ошибка парсинга config.yml: {e}")
        sys.exit(1)

def read_email_list(filename):
    """Чтение списка адресов из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            emails = [line.strip() for line in file if line.strip()]
        if not emails:
            print("Предупреждение: Файл со списком адресов пуст.")
        return emails
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        sys.exit(1)

def read_email_body(filename):
    """Чтение текста письма из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден.")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        sys.exit(1)

def send_email(smtp_server, from_addr, password, to_addr, subject, body):
    """Отправка одного письма"""
    try:
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        smtp_server.sendmail(from_addr, [to_addr], msg.as_string())
        print(f"Письмо отправлено на {to_addr}")
        return True
    except Exception as e:
        print(f"Ошибка отправки на {to_addr}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Рассылка писем через Gmail')
    parser.add_argument('email_list', help='Имя файла со списком почтовых адресов (каждый адрес с новой строки)')
    parser.add_argument('email_body', help='Имя файла с текстом письма')
    args = parser.parse_args()

    # Загрузка конфигурации
    config = load_config()

    required_config = ['email', 'password', 'smtp_server', 'smtp_port', 'subject']
    for key in required_config:
        if key not in config:
            print(f"Ошибка: В config.yml отсутствует обязательный параметр '{key}'")
            sys.exit(1)

    # Чтение данных
    email_list = read_email_list(args.email_list)
    email_body = read_email_body(args.email_body)

    if not email_list:
        print("Список адресов пуст, рассылка не будет выполнена.")
        return

    # Подключение к SMTP-серверу
    try:
        if config['smtp_port'] == 465:
            server = smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'])
        else:
            server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
            server.starttls()

        server.login(config['email'], config['password'])
        print("Успешное подключение к Gmail")
    except Exception as e:
        print(f"Ошибка подключения к SMTP-серверу: {e}")
        sys.exit(1)

    # Рассылка писем
    success_count = 0
    for email in email_list:
        if send_email(server, config['email'], config['password'], email, config['subject'], email_body):
            success_count += 1

    server.quit()
    print(f"\nРассылка завершена. Успешно отправлено: {success_count}/{len(email_list)} писем.")

if __name__ == "__main__":
    main()
