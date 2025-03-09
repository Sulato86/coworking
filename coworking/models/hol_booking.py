from odoo import models, fields

class HolBooking(models.Model):
    _name = 'coworking.hol_booking'
    _description = 'Coworking Space Booking'

    coworking_hol_space_id = fields.Many2one('coworking.hol_space', string='Floor Plan', required=True)
    hol_member_id = fields.Many2one('coworking.hol_member', string='Membership', required=True)
    hol_booking_date = fields.Datetime(string='Booking Date', default=fields.Datetime.now, required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Canceled'),
    ], default='draft', string='Status')
