import csv
import xml.etree.ElementTree as ET

# Парсинг XML файла
tree = ET.parse('results.xml')
root = tree.getroot()

# Открытие CSV файла для записи
with open('results.csv', 'w', newline='') as csvfile:
    fieldnames = ['TestCase', 'ClassName', 'Result', 'Time', 'ErrorMessage']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for testsuite in root.findall('testsuite'):
        for testcase in testsuite.findall('testcase'):
            classname = testcase.get('classname')
            name = testcase.get('name')
            time = testcase.get('time')
            failure = testcase.find('failure')
            if failure is not None:
                result = 'Failed'
                error_message = failure.get('message')
            else:
                result = 'Passed'
                error_message = ''

            writer.writerow({
                'TestCase': name,
                'ClassName': classname,
                'Result': result,
                'Time': time,
                'ErrorMessage': error_message
            })

print("Results have been written to results.csv")
