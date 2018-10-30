;
var user_login_ops = {
    init: function(){
        this.eventBind()
    },
    eventBind: function(){
        $(".login_wrap .do-login").click(function(){
            var login_name = $(".login_wrap input[name=login_name]").val()
            var login_pwd = $(".login_wrap input[name=login_pwd]").val()

            if (login_name == undefined || length(login_name) < 1){
                common_ops.alert('请输入正确的用户名或密码')
                return
            }
            if (login_pwd == undefined || length(login_pwd) < 1){
                common_ops.alert('请输入正确的用户名或密码')
                return
            }  
            $.ajax({
                url: '/usr/login',
            });
        });
    }
};
$(document).ready(function(){
    user_login_ops.init()
});