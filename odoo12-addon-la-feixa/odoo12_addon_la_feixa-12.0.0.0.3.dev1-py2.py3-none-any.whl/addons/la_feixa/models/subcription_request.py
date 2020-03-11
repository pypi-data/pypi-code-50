from odoo import fields, models


class SubscriptionRequest(models.Model):
    _inherit = 'subscription.request'

    unit_composition = fields.Integer(
        string='Unit composition',
        help="How many people compose the consumption unit."
    )
