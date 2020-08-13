from odoo.tests.common.BaseCase import TransactionCase


class TestModelCourse(common.TransactionCase):
    def test_course_creation(self):
        record = self.env["academy.course"].create(
            {"name": "cs999", "description": "last class", "responsible_id": "beverly"}
        )
        self.assertEqual(record.name, "cs999")
