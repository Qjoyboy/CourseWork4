import requests
from modules.modules import API, ParsingError

class HeadHunter(API):
    url = 'https://api.hh.ru/vacancies'
    headers = {
        "User-Agent": "MyAppVac/1.01"
    }

    def __init__(self, keyword: str):
        self.params = {
            "per_page": 100,
            "text": keyword,
            "page": None
        }
        self.vacancies = []

    def get_request(self):
        """ Метод запроса json-данных через API """
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError('Нет данных для получения, увы')
        return response.json()['items']

    def get_vacancies(self, page_count=1):
        self.vacancies = []
        for page in range(page_count):
            page_vacancies = []
            self.params["page"] = page
            print(f'{self.__class__.__name__[0:-3]}: Страница {page + 1}. ',end="")
            try:
                page_vacancies = self.get_request()
            except ParsingError as error:
                print(f'ошибка {error}')
            else:
                self.vacancies.extend(page_vacancies)
                print(f'Загружено вакансий - {len(page_vacancies)}')
            if len(page_vacancies) == 0:
                break




    def get_formatted_vacancies(self):
        formatted_vacancies= []
        for vacancy in self.vacancies:
            formatted_vacancy = {
                "employer": vacancy["employer"]["name"],
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
                "api": "HeadHunter",
            }
            salary = vacancy["salary"]
            if salary:
                formatted_vacancy["salary_from"] = salary["from"]
                formatted_vacancy["salary_to"] = salary["to"]
                formatted_vacancy["currency"] = salary["currency"]
            else:
                formatted_vacancy["salary_from"] = None
                formatted_vacancy["salary_to"] = None
                formatted_vacancy["currency"] = None
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies










