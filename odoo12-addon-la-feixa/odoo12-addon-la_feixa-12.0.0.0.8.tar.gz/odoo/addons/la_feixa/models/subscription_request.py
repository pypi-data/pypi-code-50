from odoo import fields, models


class SubscriptionRequest(models.Model):
    _inherit = 'subscription.request'

    voluntary_contribution = fields.Monetary(
        string='Voluntary contribution',
        currency_field="company_currency_id",
        help="Voluntary contribution made by the cooperator while buying a share."
    )
    unit_composition = fields.Integer(
        string='Unit composition',
        help="How many people compose the consumption unit."
    )
