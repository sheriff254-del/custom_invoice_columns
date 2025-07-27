from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    previous_reading = fields.Float(string='Previous Reading', readonly=True)
    new_reading = fields.Float(string='New Reading')
    actual_usage = fields.Float(string='Actual Usage', compute='_compute_actual_usage', store=True)

    @api.depends('new_reading', 'previous_reading')
    def _compute_actual_usage(self):
        for line in self:
            line.actual_usage = line.new_reading - line.previous_reading

    @api.onchange('actual_usage')
    def _onchange_actual_usage(self):
        for line in self:
            line.quantity = line.actual_usage

    def _get_previous_reading(self):
        for line in self:
            if not line.move_id or not line.product_id:
                continue
            last_line = self.env['account.move.line'].search([
                ('partner_id', '=', line.move_id.partner_id.id),
                ('product_id', '=', line.product_id.id),
                ('move_id.move_type', '=', 'out_invoice'),
                ('id', '!=', line.id),
                ('new_reading', '!=', False)
            ], order='create_date desc', limit=1)
            line.previous_reading = last_line.new_reading if last_line else 0.0

    @api.model
    def create(self, vals):
        lines = super().create(vals)
        lines._get_previous_reading()
        return lines

    def write(self, vals):
        result = super().write(vals)
        self._get_previous_reading()
        return result
