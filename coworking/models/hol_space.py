from odoo import models, fields

class HolSpace(models.Model):
    _name = 'coworking.hol_space'
    _description = 'Space Management Coworking'

    name = fields.Char(string='Space Name', required=True)
    capacity = fields.Integer(string='Capacity', required=True)
    available = fields.Boolean(string='Availability', default=True)
