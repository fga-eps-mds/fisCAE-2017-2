from django.test import TestCase
from .views import getItems
from .views import getFilteredItems


class SearchSchoolTest(TestCase):
    def setUp(self):
        pass

    def testGetItems(self):
        name = 'ESCOLA ESTADUAL PEDRO LUDOVICO TEIXEIRA'
        state = 'TO'
        item = getItems(name, state)
        self.assertEquals(item[0].get('nome'), name)

    def testGetFilteredItems(self):
        name = 'Nazare'
        state = 'DF'
        schoolList = getFilteredItems(name, state)
        testList = [
            'INST EDUCACIONAL EVANGELICO NAZARENO',
            'CR MARIA DE NAZARE',
            'CR ESPIRITA MARIA DE NAZARE'
            ]
        self.assertEquals(schoolList, testList)
