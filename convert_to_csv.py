import xml.etree.ElementTree as ET
import csv

def convert_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['testcase', 'classname', 'name', 'time', 'status'])

        for testsuite in root.findall('testsuite'):
            for testcase in testsuite.findall('testcase'):
                classname = testcase.get('classname')
                name = testcase.get('name')
                time = testcase.get('time')
                status = 'passed'
                if testcase.find('failure') is not None:
                    status = 'failed'
                elif testcase.find('error') is not None:
                    status = 'error'
                csvwriter.writerow([classname, name, time, status])

convert_to_csv('results.xml', 'results.csv')
