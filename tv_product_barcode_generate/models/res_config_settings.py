from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    auto_generate_barcode = fields.Boolean(
        string="Generate Product Barcode On Product Create?"
    )

    barcode_type = fields.Selection(
        [
            ("code128", "Code 128"),
            ("code39", "Code 39"),
            ("ean", "EAN"),
            ("ean13", "EAN-13"),
            ("ean8", "EAN-8"),
            ("isbn10", "ISBN10"),
            ("issn", "ISSN"),
            ("pzn", "PZN"),
            ("upca", "UPCA"),
        ],
        string="Barcode Type",
        default="code128",
    )

    def get_values(self):
        res = super().get_values()

        ICP = self.env["ir.config_parameter"].sudo()

        res.update(
            auto_generate_barcode=ICP.get_param(
                "tv_product_barcode_generate.auto_generate",
                default=False,
            ),
            barcode_type=ICP.get_param(
                "tv_product_barcode_generate.barcode_type",
                default="code128",
            ),
        )

        return res

    def set_values(self):
        super().set_values()

        ICP = self.env["ir.config_parameter"].sudo()

        ICP.set_param(
            "tv_product_barcode_generate.auto_generate",
            self.auto_generate_barcode,
        )

        ICP.set_param(
            "tv_product_barcode_generate.barcode_type",
            self.barcode_type,
        )