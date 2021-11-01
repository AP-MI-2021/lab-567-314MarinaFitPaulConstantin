from Tests.testCRUD import testAdaugaObiect, testStergeObiect, testModificaObiect
from Tests.testDomain import testObiect


def runAllTests():
    testObiect()
    testAdaugaObiect()
    testStergeObiect()
    testModificaObiect()