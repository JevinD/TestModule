from odoo import fields, models


class Session(models.Model):
    _name = "academy.session"
    _description = "Academy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2one("res.partner", string="Instructor")
    course_id = fields.Many2one(
        "academy.course", ondelete="cascade", string="Course", required=True
    )
    attendee_ids = fields.Many2many("res.partner", string="Attendees")


class academyCourse(models.Model):
    _name = "academy.course"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Academy courses"

    name = fields.Char(string="Course")
    description = fields.Text()

    responsible_id = fields.Many2one(
        "res.users", ondelete="set null", string="Responsible", index=True
    )
    session_ids = fields.One2many("academy.session", "course_id", string="Sessions")
