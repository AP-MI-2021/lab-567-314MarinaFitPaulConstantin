from Logic.CRUD import adaugaObiect
from Tests.testAll import runAllTests
from UI.Console import runMenu
from UI.comandline import command_line_console


def main():
    runAllTests()
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Vorbesti cu alti oameni", 3000, "AAAA", lista)
    lista = adaugaObiect("2", "Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "BBBB", lista)
    command_line_console(lista)
main()