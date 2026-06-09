import base64
import random
from io import BytesIO
from odoo import api, fields, models
import barcode
from barcode.writer import ImageWriter
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    barcode_image = fields.Binary(
        string="Barcode Image",
        attachment=True,
    )

    def _get_barcode_type(self):
        return (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "tv_product_barcode_generate.barcode_type",
                default="code128",
            )
        )

    def _generate_barcode_number(self):
        self.ensure_one()

        barcode_type = self._get_barcode_type()

        for _ in range(100):

            if barcode_type in ['ean', 'ean13']:
                barcode = str(
                    random.randint(
                        100000000000,
                        999999999999
                    )
                )

            elif barcode_type == 'ean8':
                barcode = str(
                    random.randint(
                        1000000,
                        9999999
                    )
                )

            elif barcode_type == 'upca':
                barcode = str(
                    random.randint(
                        10000000000,
                        99999999999
                    )
                )

            elif barcode_type == 'isbn10':
                barcode = str(
                    random.randint(
                        100000000,
                        999999999
                    )
                )

            elif barcode_type == 'issn':
                barcode = str(
                    random.randint(
                        1000000,
                        9999999
                    )
                )

            elif barcode_type == 'pzn':
                barcode = str(
                    random.randint(
                        100000,
                        999999
                    )
                )

            else:  # code128, code39
                barcode = str(
                    random.randint(
                        100000000,
                        999999999999
                    )
                )

            existing = self.search_count([
                ('barcode', '=', barcode)
            ])

            if not existing:
                self.barcode = barcode
                return

        raise UserError(
            "Unable to generate a unique barcode. Please try again."
        )
            
    def _generate_barcode_image(self):
        self.ensure_one()

        if not self.barcode:
            return

        barcode_type = self._get_barcode_type()
        barcode_value = self.barcode

        # Manual barcode hoy to auto detect karo
        if barcode_value:

            if barcode_value.isdigit():

                if len(barcode_value) == 12:
                    barcode_type = 'ean13'

                elif len(barcode_value) == 7:
                    barcode_type = 'ean8'

                elif len(barcode_value) == 11:
                    barcode_type = 'upca'

                else:
                    barcode_type = 'code128'

            else:
                barcode_type = 'code128'

        try:
            barcode_class = barcode.get(
                barcode_type,
                barcode_value,
                writer=ImageWriter(),
            )

            buffer = BytesIO()
            barcode_class.write(buffer)

            self.barcode_image = base64.b64encode(
                buffer.getvalue()
            )

        except Exception as e:
            raise UserError(str(e))

    def action_generate_barcode(self):
        for rec in self:
            rec._generate_barcode_number()
            rec._generate_barcode_image()

    def action_generate_barcode_image(self):
        for rec in self:
            rec._generate_barcode_image()

    @api.model_create_multi
    def create(self, vals_list):
        products = super().create(vals_list)

        auto_generate = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "tv_product_barcode_generate.auto_generate",
                default="False",
            )
        )

        if auto_generate == "True":
            for product in products:
                product.action_generate_barcode()

        return products