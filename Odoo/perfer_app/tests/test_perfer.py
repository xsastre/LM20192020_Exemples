from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestTodo(TransactionCase):

    def test_create(self):
        "Crea un simple PerFer"
        Perfer = self.env['perfer.tasca']
        tasca = Perfer.create({'name': 'Test Tasca'})
        self.assertEqual(tasca.is_done, False)

    def test_esborrar_fet(self):
        "Esborrar fet posa Perfer a no actiu"
        Perfer = self.env['perfer.tasca']
        tasca = Perfer.create({'name': 'Test Tasca'})
        tasca.esborrar_fet()
        self.assertFalse(tasca.active)

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result

    def test_record_rule(self):
        "Test de regla de registre per usuari"
        Perfer = self.env['perfer.tasca']
        tasca = Perfer.sudo().create({'name': 'Admin Tasca'})
        with self.assertRaises(AccessError):
            Perfer.browse([task.id]).name        