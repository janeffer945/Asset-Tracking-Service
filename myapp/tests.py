from django.test import TestCase
from myapp.models import Companies, Devices, Employees

class CompanyTestCase(TestCase):
    def setUp(self):
       Companies.objects.create(name="test limited", email="test@gmail.com")

    def test_create_company(self):
        "user should be able to create a company"
        company =Companies.objects.get(email="test@gmail.com")
        self.assertEqual(company.name,'test limited')

