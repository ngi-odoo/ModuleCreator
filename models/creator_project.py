from odoo import api, fields, models


class CreatorProject(models.Model):
    _name = 'creator.project'
    _description = 'Creator Project'
    _rec_name = 'name_version'

    name = fields.Char(string='Name',
                       required=True)
    version = fields.Char(string='Version',
                          required=True,
                          default='1.0')
    name_version = fields.Char(string='Name (version)',
                               compute='_compute_name_version')
    user_ids = fields.Many2many('res.users',
                                string='Users',
                                index=True,
                                tracking=True,
                                default=lambda self: self.env.user)
    manifest_category = fields.Char(string='Category',
                                    default='Technical')
    manifest_summary = fields.Text(string='Summary')
    manifest_description = fields.Text(string='Description')
    manifest_website = fields.Char(string='Website URL')

    model_ids = fields.One2many(string='Models',
                                comodel_name='creator.model',
                                inverse_name='project',
                                copy=True,
                                auto_join=True)

    @api.depends('name', 'version')
    def _compute_name_version(self):
        for record in self:
            record.name_version = "%s (%s)" % (record.name, record.version)
