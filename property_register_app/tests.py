from django.test import TestCase
from django.test import Client
from .models import Subdivision, Classroom

class ViewsTestCase(TestCase):
    def setUp(self):
        #Клиент для теста
        self.client = Client()
    def test_details1(self):
        #Проверка метода GET для страницы подразделений
        response = self.client.get('/subdivision/')
        #Проверка статуса (если 200 - ОК)
        self.assertEqual(response.status_code, 200)
    def test_details2(self):
        # Проверка метода GET для страницы аудиторий
        response = self.client.get('/classrooms_all/')
        # Проверка статуса (если 200 - ОК)
        self.assertEqual(response.status_code, 200)
    def test_details3(self):
        # Проверка метода GET для страницы подразделений по методу api
        response = self.client.get('/subdivisions/')
        # Проверка статуса (если 200 - ОК)
        self.assertEqual(response.status_code, 200)
# Тестирование моделей
# Тестирование модели подразделения
class SubdivisionModelTestCase(TestCase):
    # Создание временного объекта подразделения
    def setUp(self):
        self.subd = Subdivision.objects.create(subdivision_name="Test faculty", phone_number = "89881234567",
                                               subdivision_type="faculty")

    def testObject(self):
        # Проверка соответствия полей введенным значениям (если соответствует - ОК)
        self.assertEqual(self.subd.subdivision_name, "Test faculty")
        self.assertEqual(self.subd.subdivision_type, "faculty")
# Тестирование модели аудитории
class ClassroomModelTestCase(TestCase):
    # Создание временного объекта подразделения и аудитории
    def setUp(self):
        self.subd = Subdivision.objects.create(subdivision_name="Test faculty", phone_number="89881234567",
                                               subdivision_type="faculty")
        self.classr = Classroom.objects.create(number=100, area=100, appointment="lecture",
                                               subdivision=self.subd)

    def testObject(self):
        # Проверка связи по внешнему ключу
        self.assertEqual(self.classr.subdivision, self.subd)
        # Проверка соответствия полей введенным значениям (если соответствует - ОК)
        self.assertEqual(self.classr.number, 100)
        self.assertEqual(self.classr.area, 100)