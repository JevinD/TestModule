from odoo import fields, models


class academyMajor(models.Model):
    _name = "academy.major"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "major and type"

    major = fields.Char(required=True, string="Major")
    degreeType = fields.Selection(
        [("b/s", "B/S"), ("a/a", "A/A")], required=(True), string="Degree Type",
    )


class academyCourse(models.Model):
    _name = "academy.course"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "course "

    course = fields.Char(required=True, string="Course")
