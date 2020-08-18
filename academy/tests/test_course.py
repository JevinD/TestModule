from odoo.tests.common import TransactionCase


class TestModelCourse(TransactionCase):
    def test_course_creation(self):
        responsible_id = self.env["res.partner"].search(
            [("name", "=", "Mitchell Admin")]
        )
        # couldnt access the value 3 to run test with responsible_id variable
        print("\n " + str(responsible_id) + " \n")
        record = self.env["academy.course"].create(
            {"name": "cs999", "description": "last class", "responsible_id": "3",}
        )
        self.assertEqual(record.name, "cs999")
