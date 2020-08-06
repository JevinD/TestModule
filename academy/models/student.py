from odoo import fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Table"

    name = fields.Char(string="Name", required=True)
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
