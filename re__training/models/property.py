from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = "property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char(required=True)
    date_availability = fields.Date(default=fields.Date.today)
    expected_price = fields.Float(digits=(0, 0))
    selling_price = fields.Float(digits=(0, 0))
    diff_price = fields.Float(compute='_onchange_expected_price')
    bedrooms = fields.Integer(default='1')
    living_area = fields.Integer()
    facades = fields.Integer()
    owner_phone = fields.Char(related='owner_id.phone')
    owner_address = fields.Char(related='owner_id.address')
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], default='north')

    owner_id = fields.Many2one('owner')
    tags_ids = fields.Many2many('tags')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ], default='draft')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This name exists!')
    ]

    @api.constrains('bedrooms', 'selling_price')
    def _check_bedrooms_and_selling_price_greater_zero(self):
        for rec in self:
            if rec.bedrooms <= 0:
                raise ValidationError('Please add a valid number of rooms')
            elif rec.selling_price < 5000 or rec.selling_price > 1000000:
                raise ValidationError('Selling price should be set to a realistic price')

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            rec.state = 'sold'

    @api.onchange('expected_price', 'selling_price')
    def _onchange_expected_price(self):
        for rec in self:
            rec.diff_price = rec.expected_price - rec.selling_price

