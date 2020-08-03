# -*- coding: utf-8 -*-

from odoo import models, fields, api


class academy(models.Model):
    _name = "academy.academy"
    _description = "academy.academy"

    day = fields.Selection(
        [
            ("monday", "Monday"),
            ("tuesday", "Tuesday"),
            ("wednesday", "Wednesday"),
            ("thursday", "Thursday"),
            ("friday", "Friday"),
        ],
        string="Day",
        required="True",
    )

    section = fields.Selection(
        [("github", "Github"), ("odoo programming", "Odoo Programming")],
        string="Topic",
        required="True",
    )
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(required="True")

    @api.depends("value")
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
