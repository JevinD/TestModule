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

    # check if module name and description set properly
    def test_mt_creation(self):
        self.assertEqual(self.mod_tracker.name, "name")
        self.assertEqual(self.mod_tracker.mod_description, "summary")

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

    # NOTE: Linked to demo data record will not work in practical use
    # links a project to the record and autofills the customer with onchange method
    def test_mt_onchange(self):
        self.mod_tracker.project_id = (
            self.env["project.project"].search([("name", "=", "Office Design")]).id
        )
        # trigger onchange method that fills in customer based off project selection
        self.mod_tracker._onchange_from_project()
        self.assertEqual(
            self.mod_tracker.customer_id,
            self.env["project.project"]
            .search([("name", "=", "Office Design")])
            .partner_id,
        )
