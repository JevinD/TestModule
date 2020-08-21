from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    module_ids = fields.One2many(
        "module.tracker", "project_id", string="Project", readonly=True
    )
