from django.test import TestCase
from app.models import Clients

class ClientsModelTest(TestCase):
    def setUp(self):
        Clients.objects.create(name="Teste Post Api", cpf_cnpj="111.111.111-11")
    def test_post_content(self):
        client = Clients.objects.get(id=1)
        expected_name = f'{client.name}'
        expected_cpf_cnpj = f'{client.cpf_cnpj}'
        self.assertEqual(expected_name, "Teste Post Api")
        self.assertEqual(expected_cpf_cnpj, "111.111.111-11")
