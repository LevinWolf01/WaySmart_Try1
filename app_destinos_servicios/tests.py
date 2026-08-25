from django.test import TestCase

from .models import Destino, Servicio


class DestinosServiciosTests(TestCase):
	def test_destino_se_guarda_y_aparece_en_lista(self):
		response = self.client.post('/waysmart/destino/', {
			'nombre_destinatario': 'Ana Pérez',
			'direccion': 'Carrera 10 # 20-30',
			'prioridad': 'Alta',
			'estado_entrega': 'Pendiente',
		})

		self.assertRedirects(response, '/waysmart/destino/lista/')
		self.assertTrue(Destino.objects.filter(nombre_destinatario='Ana Pérez').exists())
		self.assertContains(self.client.get('/waysmart/destino/lista/'), 'Ana Pérez')

	def test_servicio_se_guarda_y_aparece_en_lista(self):
		response = self.client.post('/waysmart/servicio/', {
			'empresa_id': 10,
			'codigo_servicio': 'SERV-001',
			'direccion_recogidas': 'Calle 5 # 6-7',
			'estado': 'Solicitado',
		})

		self.assertRedirects(response, '/waysmart/servicio/lista/')
		self.assertTrue(Servicio.objects.filter(codigo_servicio='SERV-001').exists())
		self.assertContains(self.client.get('/waysmart/servicio/lista/'), 'SERV-001')
