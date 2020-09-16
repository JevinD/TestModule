"""
This python model was created during the building of my first test module. Saving it for possible reference on building other modules
"""

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Table"

    name = fields.Char(string="Names", required=True)
    age = fields.Integer(string="Age", default="18", required=True)
    guardian = fields.Selection(
        [("dad", "Dad"), ("mom", "Mom"),], string="Guardian", required=True
    )
    allergy = fields.Text(string="Allergies")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other"),],
        string="Gender",
        default="male",
        required=True,
    )
    image = fields.Binary("Image")

    @api.constrains("age")
    def _check_something(self):
        for record in self:
            if record.age <= 17:
                raise ValidationError(
                    "You are too young to register as a student \nYour age: %s \nRequirement age is 17"
                    % record.age
                )
        # all records passed the test, don't return anything
