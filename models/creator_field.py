from odoo import api, fields, models


FIELD_TYPES = [
    ('bool', 'Boolean'),
    ('int', 'Integer'),
    ('float', 'Float'),
    # Monetary is not supported for now because of currency_field
    #('monetary', 'Monetary'),
    ('char', 'Char'),
    ('text', 'Text'),
    ('html', 'Html'),
    ('date', 'Date'),
    ('datetime', 'Datetime'),
    ('binary', 'Binary'),
    ('image', 'Image'),
    ('selection', 'Selection'),
    ('m2o', 'Many2one'),
    ('o2m', 'One2many'),
    ('m2m', 'Many2many'),
]
MAX_LENGTH = 16


class CreatorField(models.Model):
    _name = 'creator.field'
    _description = 'Creator Field'

    name = fields.Char(string='Name',
                       required=True)
    model = fields.Many2one(string='Model',
                            comodel_name='creator.model',
                            required=True,
                            ondelete='cascade',
                            copy=False,
                            readonly=True)
    type = fields.Selection(string='Type',
                            selection=FIELD_TYPES,
                            required=True)
    required = fields.Boolean(string='Required')
    readonly = fields.Boolean(string='ReadOnly')
    default_boolean = fields.Boolean(string='Default Boolean')
    default_int = fields.Integer(string='Default Integer')
    default_float = fields.Float(string='Default Float')
    default_char = fields.Char(string='Default Char')
    default_text = fields.Text(string='Default Text')
    default_html = fields.Html(string='Default Html')
    default_date_current = fields.Boolean(string='Use current date')
    default_date = fields.Date(string='Default Date')
    default_datetime_current = fields.Boolean(string='Use current date')
    default_datetime = fields.Datetime(string='Default Datetime')
    default_value = fields.Char(string='Default Value', compute='_compute_default_value')

    @api.depends('type', 'default_boolean', 'default_int', 'default_float', 'default_char', 'default_text',
                 'default_html', 'default_date_current', 'default_date', 'default_datetime_current',
                 'default_datetime')
    def _compute_default_value(self):
        for record in self:
            if record.type == 'bool':
                record.default_value = 'True' if record.default_boolean else 'False'
            elif record.type == 'int':
                record.default_value = record.default_int if record.default_int else '0'
            elif record.type == 'float':
                record.default_value = record.default_float if record.default_float else '0.0'
            elif record.type == 'char':
                record.default_value = record.default_char[:MAX_LENGTH]
            elif record.type == 'text':
                record.default_value = record.default_text[:MAX_LENGTH]
            elif record.type == 'html':
                record.default_value = record.default_html[:MAX_LENGTH]
            elif record.type == 'date':
                record.default_value = '[now]' if record.default_date_current else record.default_date
            elif record.type == 'datetime':
                record.default_value = '[now]' if record.default_datetime_current else record.default_datetime
            else:
                record.default_value = '[object]'
