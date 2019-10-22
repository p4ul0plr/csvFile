# -*- coding: utf-8 -*-
import csv
#from associate import *
#from unicodedata import normalize

class CsvFile:
    def __init__(self, path):
        self.objects = []
        self.path = path
        self.__object = {}
    
    def __getColumns(self):
        with open(self.path, newline='', encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in next(reader).items():
                self.__object[item[0]] = None
            
    def createCsvFile(self, columnNames):
        try:
            #O 'w' cria o arquivo e apaga os dados existentes. O 'a+' adiciona uma nova linha e não apaga o arquivo
            with open(self.path, 'w',  newline='', encoding='utf8') as csvfile:
                self.spamwriter = csv.writer(csvfile)
                self.spamwriter.writerow(columnNames)
        except:
            print("Erro ao criar arquivo: \'" + self.path + "\'")

    def readCsvFile(self):
        self.__getColumns()
        with open(self.path, newline='', encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for obj in self.__object:
                    self.__object[obj] = row[obj].strip(' ')
                self.objects.append(self.__object)
        
    def writeRowCsvFile(self, row):
        with open(self.path, 'a+',  newline='', encoding='utf8') as csvfile:
            self.spamwriter = csv.writer(csvfile)
            self.spamwriter.writerow(row)


csvFile = CsvFile('./teste.csv')
csvFile.readCsvFile()
print(csvFile.objects)
print(csvFile.objects[0]['Nome'])
""" csvFile = CsvFile('./Relatorios/associadosBoletoComEmail.csv')
csvFile.createCsvFile(['NOME', 'EMAIL'])
csvFile.writeRowCsvFile(['Paulo', 'bla@gmail.com'])
csvFile.writeRowCsvFile(['João', 'ola@hotmail.com'])

csvFile1 = CsvFile('./Relatorios/associadosBoletoComEmail.csv')
csvFile1.readCsvFile()
print(csvFile1.checkEmailByName('Paulo')) """

""" Ciar um novo CSV com a intersecção de associadosBoletoComEmail.csv com relatorio.csv e criar
Um novo CSV com o resultado """

""" csvFileRel = CsvFile('./Relatorios/relatorio.csv')
csvFileRel.readCsvFile()
csvFileRelFin = CsvFile('./Relatorios/relatoriofinanceiro.csv')
csvFileRelFin.readCsvFileNoEmail()
csvFileRes = CsvFile('./Relatorios/associadosBoletoComEmail.csv')
csvFileRes.createCsvFile(['NOME', 'EMAIL'])

for assRel in csvFileRel.associates:
    for assRelFin in csvFileRelFin.associates:
        if removeAaccent(assRelFin.name) == removeAaccent(assRel.name):
            csvFileRes.writeRowCsvFile([assRel.name, assRel.email]) """



