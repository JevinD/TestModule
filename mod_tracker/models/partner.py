from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    module_customer_ids = fields.Many2many(
        "module.tracker.version", string="Customer", readonly=True
    )

    module_primary_ids = fields.One2many(
        "module.tracker.version",
        "prim_designer_id",
        string="Primary Designer",
        readonly=True,
    )
    module_primary_dev_ids = fields.One2many(
        "module.tracker.version",
        "prim_developer_id",
        string="Primary Developer",
        readonly=True,
    )
    module_contributor_ids = fields.Many2many(
        "module.tracker.version", string="Contributor", readonly=True
    )
