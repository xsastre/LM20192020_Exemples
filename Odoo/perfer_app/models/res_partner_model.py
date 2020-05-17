from odoo import fields, models
class ResPartner(models.Model):
    _inherit = 'res.partner'
    perfer_ids= fields.Many2many(
        'perfer.tasca',
        string="Equips Per fer")