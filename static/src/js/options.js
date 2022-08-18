odoo.define('website_bar_chart_snippet.popular_course_options', function (require) {
    'use strict';

    const options = require('web_editor.snippets.options');
    const Dialog = require('web.Dialog');

    options.registry.s_bar_chart_js = options.Class.extend({
        _setConfig: function () {
            var self = this;
            this._rpc({
                route: '/api/website/snippet/chart-config',
                params: {}
            }).then(function (data) {
                self.dialog = new Dialog(self, {
                    title: 'Snippet Config',
                    buttons: [{
                        text: 'Save', classes: 'btn-primary', click: function (ev) {
                            self._submitData(ev)
                        }
                    },
                    { text: 'Discard', close: true }],
                    $content: data['config'],
                });
                self.dialog.opened().then(function () {
                    self.dialog.$el.find('#erp_model_field').change(function (ev) {
                        var current_val = $(ev.currentTarget).val();
                        self._get_field_data(current_val)
                    });
                });
                self.dialog.open();
            })
        },
        _get_field_data: function (val) {
            var self = this;
            console.log(val);

            // this._rpc({
            //     route: '/get/modules/fields',
            //     params: {'id':val}
            // }).then(function(data){
            // var options = "<option value=''>Select Field</option>"
            // var img_options = "<option value=''>Select Field</option>"
            // if(data){
            //     data['fields'].forEach(ele => {
            //         options = options + "<option value='"+ ele[0] +"' data_ttyle='"+ ele[2] +"'>"+ele[1]+"</option>"
            //     });
            //     data['images_field'].forEach(ele => {
            //         img_options = img_options + "<option value='"+ ele[0] +"' data_ttyle='"+ ele[2] +"'>"+ele[1]+"</option>"
            //     });
            //     self.dialog.$el.find(".model_fields").empty().append(options);
            //     self.dialog.$el.find(".img_model_fields").empty().append(img_options);
            // }
            // });
        },
        _submitData: function (ev) {
            var dateRange = this.dialog.$el.find("#date_range").val();
            var dayFrequency = this.dialog.$el.find("#day_frequency").val();
            var model_id = this.dialog.$el.find("#erp_model_field").val();

            if (model_id == undefined || model_id == "") {
                alert("Please select model!")
            } else {
                var json_data = {
                    'model_id': model_id,
                    'dateRange': dateRange,
                    'dayFrequency': dayFrequency
                }

                this.$target.attr("data-model_info", JSON.stringify(json_data))
                this.dialog.close();
            }
        },
        onBuilt: function () {
            this._setConfig()
        },
        cleanForSave: function () {
            this.$target.empty();
        }
    })
});