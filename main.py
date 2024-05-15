import requests
import time
import logging

# Статистика
stats = {
    'total_requests': 0,
    'successful_logins': 0,
    'failed_logins': 0,
    'successful_infos': 0,
    'failed_infos': 0,
    'successful_creations': 0,
    'failed_creations': 0
}

logging.basicConfig(filename='credit_info_analysis.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#открываем файл
with open('credit_info.txt', 'r') as file:
    for line in file:
        login, password, loanAmount, loanPeriod, lastName, firstName, middleName, dob, \
        passportSeries, passportNumber, passportIssueDate, passportIssuedBy, \
        snils, education, registrationAddress, residentialAddress, phone \
            = line.strip().split(' ')

        login_data = {
            'login': login,
            'password': password
        }

        info_data = {
            'login': login,
            'phone': phone
        }

        loan_data = {
            'credit_program': "program2",
            'loan_amount': loanAmount,
            'loan_period': loanPeriod,
            'last_name': lastName,
            'first_name': firstName,
            'middle_name': middleName,
            'dob': dob,
            'passport_series': passportSeries,
            'passport_number': passportNumber,
            'passport_issue_date': passportIssueDate,
            'passport_issued_by': passportIssuedBy,
            'snils': snils,
            'education': education,
            'registration_address': registrationAddress,
            'residential_address': residentialAddress,
            'phone': phone,
            'agreement': "on"
        }

        # Логин
        start_time = time.time()
        res = requests.post('http://127.0.0.1:5000/login', json=login_data)
        elapsed_time = time.time() - start_time
        stats['total_requests'] += 1
        if res.ok:
            stats['successful_logins'] += 1
            logging.info(f"Login successful for {login}: {res.json()} (Time: {elapsed_time:.2f}s)")
        else:
            stats['failed_logins'] += 1
            logging.error(f"Login failed for {login}: {res.status_code} {res.text} (Time: {elapsed_time:.2f}s)")

        # Получение информации
        start_time = time.time()
        res = requests.post('http://127.0.0.1:5000/getinfo', json=info_data)
        elapsed_time = time.time() - start_time
        stats['total_requests'] += 1
        if res.ok:
            stats['successful_infos'] += 1
            logging.info(f"Info retrieval successful for {login}: {res.json()} (Time: {elapsed_time:.2f}s)")
        else:
            stats['failed_infos'] += 1
            logging.error(f"Info retrieval failed for {login}: {res.status_code} {res.text} (Time: {elapsed_time:.2f}s)")

        # Создание кредитной заявки
        start_time = time.time()
        res = requests.post('http://127.0.0.1:5000/createcase', json=loan_data)
        elapsed_time = time.time() - start_time
        stats['total_requests'] += 1
        if res.ok:
            stats['successful_creations'] += 1
            logging.info(f"Case creation successful for {login}: {res.json()} (Time: {elapsed_time:.2f}s)")
        else:
            stats['failed_creations'] += 1
            logging.error(f"Case creation failed for {login}: {res.status_code} {res.text} (Time: {elapsed_time:.2f}s)")

# Вывод статистики
print("Общая статистика запросов:")
print(f"Общее количество запросов: {stats['total_requests']}")
print(f"Успешных логинов: {stats['successful_logins']}")
print(f"Неуспешных логинов: {stats['failed_logins']}")
print(f"Успешных запросов информации: {stats['successful_infos']}")
print(f"Неуспешных запросов информации: {stats['failed_infos']}")
print(f"Успешных запросов создания кредитной заявки: {stats['successful_creations']}")
print(f"Неуспешных запросов создания кредитной заявки: {stats['failed_creations']}")
