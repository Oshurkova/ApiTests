import requests

#открываем файл
with open('credit_info.txt', 'r') as file:
    for line in file:

        loanAmount, loanPeriod, lastName, firstName, middleName, dob, \
        passportSeries, passportNumber, passportIssueDate, passportIssuedBy, \
        snils, education, registrationAddress, residentialAddress, phone \
        = line.strip().split(' ')

        form_data = {
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

        res = requests.post('http://127.0.0.1:5000/createcase', json=form_data)

        if res.ok:
            print(res.json())