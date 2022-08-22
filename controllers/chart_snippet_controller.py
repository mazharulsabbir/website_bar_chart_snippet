# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from datetime import datetime, timedelta


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
        model_id = kw.get("model_id")
        date_range = kw.get("dateRange")
        day_frequency = kw.get("dayFrequency")

        if not model_id or not date_range or not day_frequency:
            return False

        data_diff = datetime.now() - timedelta(days=int(date_range))
        least_date = data_diff.strftime(r'%Y-%m-%d 23:59:59')

        graph_config = request.env['wbcs.graph_config'].sudo().search(
            [('id', '=', int(model_id))],
            limit=1
        )

        if not graph_config:
            return False

        print("Model Id: ", graph_config.model_id.model)

        domain = [
            '&',
            ('create_date', '>=', least_date),
            ('create_date', '<=', datetime.now())
        ]

        count_records = {}
        labels = []

        for field in graph_config.count_field_ids:
            groups = request.env[graph_config.model_id.model].read_group(
                domain, [field.name + ":count"], ['create_date:' + day_frequency]
            )
            print(groups)

            data = {d['create_date_count'] for d in groups}
            label = {d['create_date:' + day_frequency] for d in groups}
            # count_records[label] = data
            if label not in labels:
                labels.append(label)

        sum_records = []
        for field in graph_config.sum_field_ids:
            groups = request.env[graph_config.model_id.model].read_group(
                domain, [field.name + ':sum'], ['create_date:' + day_frequency]
            )
            print(groups)
            # data = [{
            #     field.name: d['create_date_count'],
            #     "create_date": d['create_date']
            # } for d in groups]
            data = {d['create_date_count'] for d in groups}
            sum_records.extend(data)

            label = {d['create_date:' + day_frequency] for d in groups}
            if label not in labels:
                labels.append(label)

        temp = request.env['ir.ui.view']._render_template(
            'website_bar_chart_snippet.website_bar_chart_view'
        )

        labels = sorted(labels)
        print(labels)
        return {'template': temp, 'dataset': [count_records, sum_records], 'labels': labels}
