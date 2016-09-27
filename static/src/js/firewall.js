/**
 * Created by Administrator on 2016-09-27.
 */
console.log('模块开始加载');
openerp.ccb_firewall=function(instance){
    var _t=instance.web._t,
        _lt=instance.web._lt,
        QWeb=instance.web.qweb;
    instance.ccb_firewall={};

    instance.ccb_firewall.need=instance.web.Widget.extend({
        init:function(parent){
            this._super(parent);
            console.log('abc');
        },
        start:function(){
            console.log(1234);
        }
    });

    instance.web.client_actions.add('ccb_firewall.needs','instance.ccb_firewall.need');
}