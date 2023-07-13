def sort_by_salary_from(vacancies):
    desc = True if input("> - по убыванию\n"
        "< - по возрастанию\n"
        ">>> ") == '>' else False
    return sorted(vacancies,reverse=desc)

def filter_by_salary_from(vacancies):
    minimal_salary = int(input("Введите минимальную зарплату\n"
        ">>> "))
    return sorted(vacancies, key=lambda x: (int(x.salary_from) >= minimal_salary if x.salary_from else 0))