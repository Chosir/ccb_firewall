/**
 * Created by Administrator on 2016-09-27.
 */
console.log('模块开始加载');
openerp.ccb_firewall=function(instance){
    var _t=instance.web._t,
        _lt=instance.web._lt,
        QWeb=instance.web.qweb;
    instance.ccb_firewall={};

    instance.ccb_firewall.Widget=instance.web.Widget.extend({
        init:function(){
            var self=this;
            var timer=setInterval(function(){
                var action_manager=instance.client.action_manager;
                if(action_manager){
                    var inner_action=action_manager.inner_action;
                    if(inner_action){
                        var display_name=inner_action.display_name;
                        if(display_name){
                            clearInterval(timer);
                            self.addBtn(display_name)
                            watch(action_manager,"inner_action",function(pro,action,newVal,oldVal){
                                self.addBtn(newVal.display_name);
                            });
                        }
                    }
                }
            },100)
        },
        addBtn:function(display_name){
            var self=this;
            if(display_name=="需求单"){
                var timer=setInterval(function(){
                    var btnParent=$('.oe_list_buttons');
                    if(btnParent.length>0&&($('.oe_list_buttons button.need-search').length==0)){
                        clearInterval(timer);
                        var btn=$("<button class='need-search'>需求搜索</button>");
                        btnParent.append(btn);
                        btn.click(function(){
                            self.popDialog();
                        });
                    }
                },100)
            }
        },
        popDialog:function(){
            var $help = $(QWeb.render("needSearch", {

            }));
            new instance.web.Dialog(null,{
                size: 'medium',
                dialogClass: 'oe_act_window',
                title: _t("需求搜索")
            },$help).open();
        },
        start:function(){

        }
    });
    //弹出框
    instance.ccb_firewall.dialog=instance.web.Dialog.extend({
        init:function(_name){
            this.name=_name;
        },
        start:function(){

        }
    })

    instance.ccb_firewall.widget=new instance.ccb_firewall.Widget();
}