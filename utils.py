import requests

BASE_URL = 'https://service.nalog.ru/pau-proc.do'


def arbitr_check(inn: str) -> list:
    result = []
    sess = requests.Session()
    params = {
        'innAu': inn
    }
    r = sess.get(BASE_URL, params=params)
    result_list = r.json()['rows']
    for row in result_list:
        one_row = {'inn': row.get("СРО_ИНН", "ИНН не найден"),
                   "first_name": row.get("СРОНаим_Имя", "Имя не найдено"),
                   'middle_name': row.get("СРОНаим_Отчество", "Отчество не найдено"),
                   'last_name': row.get("СРОНаим_Фамилия", "Фамилия не найдена"),
                   "Company_name": row.get("НаимНП", "Наименование должника не найдено"),
                   "Decision": row.get("РешНарТип", "Решение не найдено"),
                   "region": row.get("Регион", "Регион не найден"),
                   "Decision_law": row.get("РешСУД", "Наименование суда не найдено"),
                   "Decision_number": row.get("РешНарНом", "Номер решения не найден"),
                   "Decision_data": row.get("РешНарДата", "Дата решения суда не найдено"),
                   "SRO_name_full": row.get("СРОНаим_НаимЮЛ", "Наименование организации СРО не найдено"),
                   },
        result.append(one_row)
    return result
