/**
 * Created by Administrator on 2016-09-27.
 */
openerp.ccb_firewall=function(instance){
    var _t=instance.web._t,
        _lt=instance.web._lt,
        QWeb=instance.web.qweb;
    instance.ccb_firewall={};

    instance.ccb_firewall.Widget=instance.web.Widget.extend({
        init:function(){
        //暂时不需要
        },
        start:function(o){
            var displayName=o.client.action_manager.inner_action.display_name;
            this.addBtn(displayName);
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
            //用来存储表单插件的校验状态
            var o={source_ip:[],dst_ip:[]};
            var $help = $(QWeb.render("needSearch", {}));
            $help.find('input').blur(function(){
                var ip=$(this).val();
                var inputName=$(this).attr("name");
                o[inputName][1]=ip.toLowerCase();
                if(vliIpv4(ip)){
                    o[inputName][0]=true;
                    $(this).parents("div.form-group").removeClass("has-error").
                        children("span.help-block").html("")
                }else{
                    o[inputName][0]=false;
                    $(this).parents("div.form-group").addClass("has-error").
                        children("span.help-block").
                        html("您输入的"+(inputName=="source_ip"?"“源":"“目的")+"IP”格式存在问题，请重新输入！");
                }
            })
            $help.find('button.btn-block').click(function(e) {
                    e.preventDefault();
                    doRequest();
                }
            );
            //按回车键提交表单
            $help.find("form").keydown(function(e){
                if(e.keyCode==13){
                    $help.find('input').trigger("blur");
                    doRequest();
                }
            });
            //提交请求
            function doRequest(){
                var tem=$help.find("form").serialize();
                if(o.source_ip[0] && o.dst_ip[0]){
                    if((o.source_ip[1]=="any") && (o.dst_ip[1]=="any")){
                        $dialog.close();
                        setTimeout(function(){
                            //删除相关的已选择的选项标签
                            $("span.oe_facet_values>span.oe_facet_value").each(function (i,span) {
                                var html=$(span).html().trim();
                                if(html.indexOf("ID")===0){
                                    $(this).parent("span").siblings("span.oe_facet_remove").trigger("click");
                                }
                            });
                        },100)
                    }else{
                        instance.web.blockUI();
                        $.post("/ccb_firewall/needs/objects/", tem, doResponse,"json");
                    }
                }
            }
            //利用正则表达式校验ip地址
            function vliIpv4(ip){
                var reg=/^(2[5][0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})$/;
                ip=ip.toLowerCase();
                if(ip=="any"||reg.test(ip)){
                    return true;
                }else{
                    return false;
                }
            }
            //异步请求回调函数
            function doResponse(arr){
                //开始先删除相关的已选择的选项标签
                $("span.oe_facet_values>span.oe_facet_value").each(function (i,span) {
                    var html=$(span).html().trim();
                    if(html.indexOf("ID")===0){
                        $(this).parent("span").siblings("span.oe_facet_remove").trigger("click");
                    }
                });

                //开始根据id组成的数组去自动添加查询
                var length=arr.length;
                for(var i=1;i<length;i++){
                    $('.oe_add_condition').trigger("click");
                }
                for(var i=0;i<length;i++){
                    $("form li:eq("+i+") .searchview_extended_prop_field").val("id");
                    $("form li:eq("+i+") .searchview_extended_prop_field").trigger("change");
                    $("form li:eq("+i+") .searchview_extended_prop_op").val("=");
                    $("form li:eq("+i+") .searchview_extended_prop_value>input.field_integer").val(arr[i]);
                }
                instance.web.unblockUI();
                if(length>0){
                    $("form button.oe_apply:first").trigger("submit");
                    $dialog.close();
                }else{
                    window.alert("未查询到符合条件的需求！o(︶︿︶)o");
                }
            }
            var $dialog=new instance.web.Dialog(null,{
                size: 'medium',
                dialogClass: 'oe_act_window',
                title: _t("需求搜索")
            },$help).open();
        }
    });

    //当视图加载时调用自己指定代码
    instance.web.actionList.push(new instance.ccb_firewall.Widget());
}