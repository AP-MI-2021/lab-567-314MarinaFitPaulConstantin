from Domain.obiect import creeazaObiect, getId, getNume, getLocatie, getPret, getDescriere



def testObiect():
    obiect = creeazaObiect("1", "Scaun", "Stai pe el", 100, "AAAA")

    assert getId(obiect) == "1"
    assert getNume(obiect) == "Scaun"
    assert getDescriere(obiect) == "Stai pe el"
    assert getPret(obiect) == 100
    assert getLocatie(obiect) == "AAAA"