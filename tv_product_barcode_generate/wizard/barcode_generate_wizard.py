from odoo import models, fields, api


class BarcodeGenerateWizard(models.TransientModel):
    _name = "barcode.generate.wizard"
    _description = "Generate Product Barcode"

    overwrite_existing = fields.Boolean(string="Overwrite Barcode If Exists")

    def action_generate(self):

        products = self.env[
            "product.template"
        ].browse(
            self.env.context.get("active_ids", [])
        )

        for product in products:

            if self.overwrite_existing:
                product.barcode = False
                product.action_generate_barcode()

            elif not product.barcode:
                product.action_generate_barcode()

        return {
            "type": "ir.actions.act_window_close"
        }