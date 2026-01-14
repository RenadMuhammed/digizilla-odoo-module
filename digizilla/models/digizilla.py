from odoo import models, fields, api
from datetime import date


class Digizilla(models.Model):
    _name = "digizilla.record"
    _description = "Digizilla Record"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    country_id = fields.Many2one('res.country', string="Country")
    birth_date = fields.Date(string="Birth Date")
    age = fields.Float(string="Age", compute="_compute_age")
    tags = fields.Many2many('res.partner.category', string="Tags")
    customer_id = fields.Many2one('res.partner', string="Customer", required=True)
    no_of_sales_orders = fields.Float(string="No. of Sales Orders", compute="_compute_sales_orders")
    notes = fields.Html(string="Notes")
    comments = fields.Char(string="Comments")

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = (today - rec.birth_date).days / 365
            else:
                rec.age = 0

    @api.depends('customer_id')
    def _compute_sales_orders(self):
        for rec in self:
            rec.no_of_sales_orders = len(self.env['sale.order'].search([('partner_id','=',rec.customer_id.id)]))
