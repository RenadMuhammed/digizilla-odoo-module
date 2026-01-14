odoo.define('digizilla.hide_create', function (require) {
    "use strict";
    var ListController = require('web.ListController');
    ListController.include({
        renderButtons: function ($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                this.$buttons.find('.o_list_button_add').hide(); // hide create
            }
        },
    });
});
