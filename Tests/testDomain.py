from Domain.obiect import creeazaObiect, getId, getNume, getLocatie, getPret, getDescriere



def testObiect():
    obiect = creeazaObiect("1", "Masa", "Utilizat pentru depozitarea obiectelor", 200, "In living")

    assert getId(obiect) == "1"
    assert getNume(obiect) == "Masa"
    assert getDescriere(obiect) == "Utilizat pentru depozitarea obiectelor"
    assert getPret(obiect) == 200
    assert getLocatie(obiect) == "In living"