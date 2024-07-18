import os
from qaseio import QaseApi

# Получение API токена из переменной окружения
api_token = os.getenv("QASE_API_TOKEN")
api = QaseApi(api_token)

# Код вашего проекта в QASE
project_code = "HBT"

# Путь к файлу с результатами тестов
results_file = "results.xml"

# Отправка результатов тестов в QASE
api.results.create_from_file(project_code, results_file)
