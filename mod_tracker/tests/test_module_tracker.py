from odoo.tests.common import TransactionCase


class TestMtCases(TransactionCase):
    def setUp(self, *args, **kwargs):
        """
            Creates and instance record for category and module tracker.
        """
        super(TestMtCases, self).setUp(*args, **kwargs)

        # create a category instance
        self.category = self.env["module.category"].create({"name": "category"})

        # create a module tracker instance
        self.mod_tracker = self.env["module.tracker"].create(
            {"name": "name", "mod_summary": "summary",}
        )

    # check if module name and summary set properly
    def test_mt_creation(self):
        self.assertEqual(self.mod_tracker.name, "name")
        self.assertEqual(self.mod_tracker.mod_summary, "summary")

    # unlink the record and check if it exists. it should not exists.
    def test_mt_delete(self):
        self.mod_tracker.unlink()
        self.assertFalse(self.mod_tracker.exists())

    # link category record with mod_tracker record
    # change name
    def test_mt_update(self):
        self.mod_tracker.prim_category_id = self.category.id
        self.mod_tracker.mod_name = "name change"
        self.assertEqual(self.mod_tracker.mod_name, "name change")
        self.assertEqual(self.mod_tracker.prim_category_id.name, "category")
