from odoo import api, fields, models


class CreatorModel(models.Model):
    _name = 'creator.model'
    _description = 'Creator Model'

    name = fields.Char(string='Id',
                       required=True)
    description = fields.Text(string='Description')
    project = fields.Many2one(string='Project',
                              comodel_name='creator.project',
                              required=True,
                              ondelete='cascade',
                              copy=False,
                              readonly=True)
    field_ids = fields.One2many(string='Fields',
                                comodel_name='creator.field',
                                inverse_name='model',
                                copy=True)
