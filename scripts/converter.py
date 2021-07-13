# -*- coding: utf-8 -*-

import csv

csvFilePath  = 'data/DBNetz-Betriebsstellenverzeichnis-Stand2021-07.csv'

def converter(rlcode):
    with open(csvFilePath, newline='', encoding='utf-8-sig') as csvFile:
        csvFileAsJson = csv.DictReader(csvFile, delimiter=';')

        for operationsCenter in csvFileAsJson:
            if operationsCenter['RL100-Code'] == rlcode.upper():
                operationsCenter_short = {
                    'Name': operationsCenter['RL100-Langname'],
                    'Kurzname': operationsCenter['RL100-Kurzname'],
                    'Typ': operationsCenter['Typ Lang']
                }
                return operationsCenter_short