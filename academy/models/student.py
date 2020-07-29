from odoo import fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student Table"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    guardian = fields.Char(string="Guardian")
    note = fields.Text(string="Notes")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other"),],
        string="Gender",
        default="male",
    )
    image = fields.Binary(string="Image")
