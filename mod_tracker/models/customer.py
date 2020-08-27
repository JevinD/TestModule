from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    module_customer_ids = fields.One2many(
        "module.tracker", "customer_id", string="Customer", readonly=True
    )
