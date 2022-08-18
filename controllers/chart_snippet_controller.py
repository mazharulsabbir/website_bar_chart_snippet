# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteGraphSnippetController(http.Controller):
    @http.route('/api/website/snippet/chart-config', auth='public', type='json', website=True)
    def chart_config(self, **kw):
        # dialog content
        models = request.env['wbcs.graph_config'].search([])
        config = request.env['ir.ui.view']._render_template(
            'website_bar_chart_snippet.s_website_bar_chart_config', {'models': models})
        return {'config': config}

    @http.route('/api/website/snippet/model-info', auth='public', type='json', website=True)
    def model_info(self, **kw):
        graph_config = request.env['wbcs.graph_config'].sudo().search(
            [('id', '=', int(kw.get('model_id')))], limit=1)

        print("Model Id: ",graph_config.model_id)
        for field in graph_config.count_field_ids:
            print(field)

        for field in graph_config.sum_field_ids:
            print(field)

        # todo: return data here to load on bar chart
        data = {
            "name":"Mazharul Sabbir"
        }

        temp = request.env['ir.ui.view']._render_template(
            'website_bar_chart_snippet.website_bar_chart_view',
            data
        )
        return {'template': temp}

