def get_token():
    with open('.env') as f:
        return f.read().split('\n')[0]


def get_admin_id():
    with open('.env') as f:
        return f.read().split('\n')[1]


def get_type_of_device():
    with open('.env') as f:
        return f.read().split('\n')[2]


chat_id = "ID"
name = "ФИО"
structural_division = "Подразделение"
question_1 = "Понимание функциональных обязанностей"
question_2 = "Практическое исполнение функциональных обязанностей происходит"
question_3 = "Приходится ли исполнять функцию руководителя работ"
question_4 = "Практическое исполнение функциональных обязанностей руководителя работ происходит"
time = "Время начала прохождения анкеты"
