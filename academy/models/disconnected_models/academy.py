# -*- coding: utf-8 -*-
"""
This python model was created during the building of my first test module. Saving it for possible reference on building other modules
"""
from odoo import models, fields, api
import random


class academy(models.Model):
    _name = "academy.academy"
    _inherit = ["mail.thread", "mail.activity.mixin"]
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
    create_date = fields.Datetime(
        string="Creation Date",
        readonly=True,
        index=True,
        help="Date on which the task report is created.",
    )
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text(required="True")
    name = fields.Char(compute="_compute_name")

    def _compute_name(self):
        for record in self:
            record.name = "CS" + str(random.randint(1, 1e6))

    @api.depends("value")
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
