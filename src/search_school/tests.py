from django.test import TestCase, Client
from django.shortcuts import reverse
from .views import getItems
from .views import getFilteredItems


class SearchSchoolTest(TestCase):
    def setUp(self):
        pass

    def testGetItems(self):
        name = 'ESCOLA ESTADUAL PEDRO LUDOVICO TEIXEIRA'
        state = 'TO'
        city = 'Maurilândia do Tocantins'
        item = getItems(name, state, city)
        self.assertEquals(item[0].get('nome'), name)

    def testGetFilteredItems(self):
        name = 'Nazare'
        state = 'DF'
        city = 'Brasília'
        schoolList = getFilteredItems(name, state, city)
        testList = [
            'INST EDUCACIONAL EVANGELICO NAZARENO',
            'CR MARIA DE NAZARE',
            'CR ESPIRITA MARIA DE NAZARE'
            ]
        self.assertEquals(schoolList, testList)

    def testRenderSchoolForm(self):
        client = Client()
        client.login(username="amanda", password="123")
        response = client.get(reverse('search_school:schoolForm'))
        self.assertEquals(response.status_code, 302)
