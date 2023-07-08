from odoo import api, fields, models
from odoo.exceptions import UserError


class InheritSaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    up_sale_state = fields.Boolean(string="Up-Sale Unlock state",
                                   help="Tells if up sale is allowed or not : "
                                        "If True it's unlocked if False it's locked", readonly=True)
    quantity_read_only_state = fields.Boolean(string="Quantity Unlock state", readonly=True)

    @api.onchange('qty_delivered')
    def line_amount_log(self):
        for doc in self:
            if not doc.up_sale_state:
                if doc.qty_delivered > doc.product_uom_qty:
                    raise UserError('Upsale is not allowed, please check quantity entered.')


def update_status(self, field_name, bol):
    active_ids = self._context.get('active_ids', []) or []
    for record in self.env['sale.order'].browse(active_ids):
        setattr(record, field_name, bol)
        for recs in self.env['sale.order.line'].browse(record.order_line.ids):
            setattr(recs, field_name, bol)


class InheritSaleOrder(models.Model):
    _inherit = "sale.order"

    up_sale_state = fields.Boolean(string="Up-Sale Unlock state",
                                   help="Tells if up sale is allowed or not : "
                                        "If True it's unlocked if False it's locked", readonly=True)
    quantity_read_only_state = fields.Boolean(string="Quantity Unlock state", readonly=True)

    def _unlock_up_sale(self):
        update_status(self, "up_sale_state", True)

    def _lock_up_sale(self):
        update_status(self, "up_sale_state", False)

    def _lock_quantity_action(self):
        update_status(self, "quantity_read_only_state", False)

    def _unlock_quantity_action(self):
        update_status(self, "quantity_read_only_state", True)
