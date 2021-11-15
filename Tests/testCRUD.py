from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect


def testAdaugaObiect():
    lista=[]
    lista=adaugaObiect("1", "Scaun", "Stai pe el", 100, "AAAA",lista)
    assert len(lista) == 1
    assert getId(getById("1",lista))=="1"
    assert getNume(getById("1",lista))=="Scaun"
    assert getDescriere(getById("1",lista))=="Stai pe el"
    assert getPret(getById("1",lista))==100
    assert getLocatie(getById("1",lista))=="AAAA"

def testStergeObiect():
    lista = []
    lista = adaugaObiect("1", "Scaun", "Stai pe el", 100, "AAAA", lista)
    lista=adaugaObiect("2", "Dulap", "Loc de depozitat", 200, "BBBB", lista)

    lista=stergeObiect("1",lista)
    assert len(lista)==1
    assert getById("1",lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergeObiect("100", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False


def testModificaObiect():
    lista = []
    lista = adaugaObiect("1", "Scaun", "Stai pe el", 100, "AAAA", lista)
    lista = adaugaObiect("2", "Dulap", "Loc de depozitat", 200, "BBBB", lista)

    lista = modificaObiect("1", "Pix", "Obiect de scris",15,"AAAB", lista)

    obiectUpdatat = getById("1", lista)
    assert getId(obiectUpdatat) == "1"
    assert getNume(obiectUpdatat) == "Pix"
    assert getDescriere(obiectUpdatat) == "Obiect de scris"
    assert getPret(obiectUpdatat) == 15
    assert getLocatie(obiectUpdatat) == "AAAB"

    obiectNeupdatat = getById("2", lista)
    assert getId(obiectNeupdatat) == "2"
    assert getNume(obiectNeupdatat) == "Dulap"
    assert getDescriere(obiectNeupdatat) == "Loc de depozitat"
    assert getPret(obiectNeupdatat) ==200
    assert getLocatie(obiectNeupdatat) == "BBBB"

    lista = []
    lista = adaugaObiect("1", "Scaun", "Stai pe el", 100, "AAAA", lista)
    lista = adaugaObiect("2", "Dulap", "Loc de depozitat", 200, "BBBB", lista)
    obiectNeupdatat = getById("1", lista)
    assert getId(obiectNeupdatat) == "1"
    assert getNume(obiectNeupdatat) == "Scaun"
    assert getDescriere(obiectNeupdatat) == "Stai pe el"
    assert getPret(obiectNeupdatat) == 100
    assert getLocatie(obiectNeupdatat) =="AAAA"