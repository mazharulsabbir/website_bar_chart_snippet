# -*- coding: utf-8 -*-
from email.policy import default
from odoo import models, fields, api


class BarChartConfigModel(models.Model):
    _name = 'wbcs.graph_config'
    _description = 'Create models to show the graph in bar chart'

    name = fields.Char(string="Title")
    active = fields.Boolean(string="Active", default=True)
    model_id = fields.Many2one(comodel_name='ir.model', string='Model Name')
    count_field_ids = fields.Many2many(
        comodel_name="ir.model.fields",
        relation="chart_count_field_rel",
        column1="chart_config_id",
        column2='field_id',
        string='Count Fields'
    )
    sum_field_ids = fields.Many2many(
        comodel_name="ir.model.fields",
        relation="chart_sum_field_rel",
        column1="chart_config_id",
        column2='field_id',
        string='Sum Fields'
    )

    @api.onchange('model_id')
    def onchange_model_id(self):
        self.sum_field_ids = False
        self.count_field_ids = False
        
        return {
            'domain': {
                'count_field_ids': [('model_id', '=', self.model_id.id)],
                'sum_field_ids': [('model_id', '=', self.model_id.id)],
            }
        }
