from odoo import api, fields, models

class PerferTasca(models.Model):
     _name = 'perfer.tasca'
     _description = 'Tasca Per Fer'
     name = fields.Char('Descripcio', required=True)
     is_done = fields.Boolean('Fet?')
     active = fields.Boolean('Actiu?', default=True)
     date_deadline = fields.Date('Data límit')
     user_id = fields.Many2one(
          'res.users',
          string='Responsable',
          default=lambda self: self.env.user)
     team_ids = fields.Many2many('res.partner', string='Equip')

     @api.multi
     def esborrar_fet(self):
          for task in self:
               task.active = False
          return True

     @api.multi
     def write(self, values):
          if 'active' not in values:
               values['active'] = True
          super().write(values)