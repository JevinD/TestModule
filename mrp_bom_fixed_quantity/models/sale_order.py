# Copyright 2017 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class SaleORder(models.Model):
    _inherit = "sale.order"

    fixed_quantity = fields.Boolean(string="Q")
    character = fields.Char()
