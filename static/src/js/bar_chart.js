odoo.define('website_display_modules.website_display_modules_frontend', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.dynamic_modules = publicWidget.Widget.extend({
        selector: '.s_website_bar_chart_section',
        disabledInEditableMode: false,
        start: function () {
            var self = this;
            if (this.editableMode) {
                const _html = '<div class="container text-center"><h2>Website Bar Chart</h2></div>';
                this.$target.empty().append(_html);
            }
            else {
                var attrs = this.$target.attr('data-model_info');
                // console.log(attrs);
                if (attrs != undefined) {
                    var realData = JSON.parse(attrs);
                    const labels = [
                        'January',
                        'February',
                        'March',
                        'April',
                        'May',
                        'June',
                    ];
                    const dataset1 = {
                        label: 'My First Dataset',
                        data: [65, 59, 80, 81, 56, 55, 40],
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 159, 64, 0.2)',
                            'rgba(255, 205, 86, 0.2)',
                            'rgba(75, 192, 192, 0.2)',
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(153, 102, 255, 0.2)',
                            'rgba(201, 203, 207, 0.2)'
                        ],
                        borderColor: [
                            'rgb(255, 99, 132)',
                            'rgb(255, 159, 64)',
                            'rgb(255, 205, 86)',
                            'rgb(75, 192, 192)',
                            'rgb(54, 162, 235)',
                            'rgb(153, 102, 255)',
                            'rgb(201, 203, 207)'
                        ],
                        borderWidth: 1
                    };

                    const data = {
                        labels: labels,
                        datasets: [dataset1, dataset1, dataset1]
                    };
                    const config = {
                        type: 'bar',
                        data: data,
                        options: {
                            scales: {
                                y: {
                                    beginAtZero: true
                                }
                            }
                        },
                    };

                    this._rpc({
                        route: '/api/website/snippet/model-info',
                        params: realData,
                    }).then((data) => {
                        console.log(data);
                        self.$target.empty().append(`<canvas id="websiteBarChartSnippetCanvasId" height="100px"></canvas>`)
                        const ctx = document.getElementById('websiteBarChartSnippetCanvasId').getContext('2d');
                        const myChart = new Chart(ctx, config);
                    })
                }
            }
        },
    });
});