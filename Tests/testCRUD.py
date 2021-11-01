from Domain.obiect import getId, getNume, getDescriere, getPret, getLocatie
from Logic.CRUD import adaugaObiect, getById, stergeObiect, modificaObiect


def testAdaugaObiect():
    lista=[]
    lista=adaugaObiect("1", "Masa", "Utilizat pentru depozitarea obiectelor", 200, "In living",lista)
    assert len(lista) == 1
    assert getId(getById("1",lista))=="1"
    assert getNume(getById("1",lista))=="Masa"
    assert getDescriere(getById("1",lista))=="Utilizat pentru depozitarea obiectelor"
    assert getPret(getById("1",lista))==200
    assert getLocatie(getById("1",lista))=="In living"

def testStergeObiect():
    lista = []
    lista = adaugaObiect("1", "Masa", "Utilizat pentru depozitarea obiectelor", 200, "In living", lista)
    lista=adaugaObiect("2", "Scaun", "Utilizat pentru a sta pe el", 100, "Sub masa", lista)

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
    lista = adaugaObiect("1", "Masa", "Utilizat pentru depozitarea obiectelor", 200, "In living", lista)
    lista = adaugaObiect("2", "Scaun", "Utilizat pentru a sta pe el", 100, "Sub masa", lista)

    lista = modificaObiect("1", "Carte", "Obiect de citit",2,"In raft", lista)

    obiectUpdatat = getById("1", lista)
    assert getId(obiectUpdatat) == "1"
    assert getNume(obiectUpdatat) == "Carte"
    assert getDescriere(obiectUpdatat) == "Obiect de citit"
    assert getPret(obiectUpdatat) == 2
    assert getLocatie(obiectUpdatat) == "In raft"

    obiectNeupdatat = getById("2", lista)
    assert getId(obiectNeupdatat) == "2"
    assert getNume(obiectNeupdatat) == "Scaun"
    assert getDescriere(obiectNeupdatat) == "Utilizat pentru a sta pe el"
    assert getPret(obiectNeupdatat) ==100
    assert getLocatie(obiectNeupdatat) == "Sub masa"

    lista = []
    lista = adaugaObiect("1", "Masa", "Utilizat pentru depozitarea obiectelor", 200, "In living", lista)
    lista = adaugaObiect("2", "Scaun", "Utilizat pentru a sta pe el", 100, "Sub masa", lista)
    obiectNeupdatat = getById("1", lista)
    assert getId(obiectNeupdatat) == "1"
    assert getNume(obiectNeupdatat) == "Masa"
    assert getDescriere(obiectNeupdatat) == "Utilizat pentru depozitarea obiectelor"
    assert getPret(obiectNeupdatat) == 200
    assert getLocatie(obiectNeupdatat) =="In living"