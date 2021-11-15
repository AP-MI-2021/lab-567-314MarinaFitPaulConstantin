from Domain.obiect import getLocatie, getDescriere, getId
from Logic.CRUD import adaugaObiect, getById
from Logic.funct import mutareObiecte
from Logic.funct import concatenare, PretMaximLocatie, OrdonareDupaPret, sumaPreturilor


def testMutareObiecte():
    lista=[]
    lista=adaugaObiect("1","Telefon", "Vorbesti cu alti oameni", 3000, "CCCC",lista)
    lista=adaugaObiect("2","Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "CCCC",lista)
    lista=adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "EEEE",lista)
    lista=mutareObiecte("CCCC", lista, "EEEE")

    assert getLocatie(getById("1", lista)) == "EEEE"
    assert getLocatie(getById("2", lista)) == "EEEE"
    assert getLocatie(getById("3", lista)) == "EEEE"

def testSchimbaDescrierea():
    lista = []
    lista=adaugaObiect("1","Telefon", "Vorbesti cu alti oameni", 3000, "CCCC",lista)
    lista=adaugaObiect("2","Masina", "Asigura deplasarea oamenilor pe strada", 30000, "CCCC",lista)
    lista=adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "EEEE",lista)
    lista=concatenare(" asa", lista, 2000)
    assert getDescriere(getById("1", lista))=="Vorbesti cu alti oameni asa"
    assert getDescriere(getById("2", lista))=="Asigura deplasarea oamenilor pe strada asa"
    assert getDescriere(getById("3", lista))=="Te ajuta sa te ghidezi"

def testPretMaximLocatie():
    lista = []
    ista = adaugaObiect("1", "Telefon", "Vorbesti cu alti oameni", 3000, "CCCC", lista)
    lista = adaugaObiect("2", "Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "CCCC", lista)
    lista = adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "EEEE", lista)
    lista = adaugaObiect("4", "Pix", "obiect de scris", 10, "CCCC", lista)
    lista = adaugaObiect("5", "Lanterna ", "Obiect de iluminat ", 300, "EEEE", lista)
    lista = adaugaObiect("6", "Bicicleta", "Deplasarea", 5000, "DDDD", lista)

    rezultat=PretMaximLocatie(lista)
    assert len(rezultat)==3
    assert rezultat["CCCC"]==30000
    assert rezultat["DDDD"]==5000
    assert rezultat["EEEE"]==300

def testOrdonareDupaPret():
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Vorbesti cu alti oameni", 3000, "CCCC", lista)
    lista = adaugaObiect("2", "Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "DDDD", lista)
    lista = adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "EEEE", lista)
    lista = adaugaObiect("4", "Pix", "obiect de scris", 10, "CCCC", lista)
    lista = adaugaObiect("5", "Lanterna ", "Obiect de iluminat ", 300, "EEEE", lista)
    lista = adaugaObiect("6", "Bicicleta", "Deplasarea", 5000, "DDDD", lista)
    rezultat=OrdonareDupaPret(lista)
    assert getId(rezultat[0])=="4"
    assert getId(rezultat[1])=="3"
    assert getId(rezultat[2])=="5"
    assert getId(rezultat[3])=="1"
    assert getId(rezultat[4])=="6"
    assert getId(rezultat[5])=="2"

def testsumaPreturilor():
    lista=[]
    lista = adaugaObiect("1", "Telefon", "Vorbesti cu alti oameni", 3000, "CCCC", lista)
    lista = adaugaObiect("2", "Masina", "Asigura desfasurarea oamenilor pe strada", 30000, "DDDD", lista)
    lista = adaugaObiect("3", "Harta", "Te ajuta sa te ghidezi", 200, "CCCC", lista)
    rezultat=sumaPreturilor(lista)
    assert len(rezultat)==2
    assert rezultat["CCCC"]==3200
    assert rezultat["DDDD"]==30000