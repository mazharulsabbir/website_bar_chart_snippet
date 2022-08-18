# -*- coding: utf-8 -*-
{
    'name': "Website Bar Chart Snippet",

    'summary': "Website Bar Chart Snippet",

    'description': """
        Website Bar Chart Snippet
    """,

    'author': "Md Mazharul Islam",
    'website': "https://www.mazharulsabbir.com",
    'category': 'Snippet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        # views
        'views/views_graph_config.xml',

        # templates/frontend
        'views/template_chart_config_dialog.xml',
        'views/template_bar_chart.xml',

        # dynamic snippet
        'views/bar_chart_snippet.xml',
    ],
    'assets': {
        'web.assets_qweb': [],
        'web.assets_backend': [],
        'web.assets_frontend': [
            'website_bar_chart_snippet/static/src/js/chart.min.js',
        ],
        'website.assets_editor': [
            'website_bar_chart_snippet/static/src/js/options.js',
            'website_bar_chart_snippet/static/src/js/bar_chart.js',
        ]
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
