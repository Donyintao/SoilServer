// 机房-机柜联动菜单
$(function () {
  // 初始化值
  $.get("/assets/idc_seleted/", function (result) {
    var result = $.parseJSON(result);
    var idc = $('#get_idc').val();
    for (var i = 0; i < result.length; i++){
      var id = result[i].id;
      var name = result[i].name;
      if (name == idc) {
        $("#idc").append("<option value=" + id + " selected=selected" + ">" + name + "</option>");
      } else {
        $("#idc").append("<option value="+ id +">" + name + "</option>")
      }
    }
  });
  // 机柜菜单
  $("#idc").click(function () {
    var idc = $(this).val();
    var cabinet = $('#get_cabinet').val();
    $("#cabinet option:gt(0)").remove();
    $.get("/assets/cabinet_seleted/", {id: idc}, function (result) {
      var result = $.parseJSON(result);
      for (var i = 0; i < result.length; i++){
        var id = result[i].id;
        var name = result[i].name;
        $("#cabinet option[index='0']").remove();
        if (name == cabinet) {
          $("#cabinet").append("<option value=" + id + " selected=selected" + ">" + name + "</option>");
        } else {
          $("#cabinet").append("<option value="+ id +">" + name + "</option>")
        }
      }
    });
  });
});

// 主机组菜单
$(function () {
  $.get("/assets/group_seleted", function (result) {
    var result = $.parseJSON(result);
    var group = $('#get_group').val();
    for (var i = 0; i < result.length; i++) {
      var id = result[i].id;
      var name = result[i].name;
      $("#group option[index='0']").remove();
      if (name == group) {
        $("#group").append("<option value=" + id + " selected=selected" + ">" + name + "</option>");
      } else {
        $("#group").append("<option value=" + id + ">" + name + "</option>")
      }
    }
  });
});

// 厂商菜单
$(function () {
  $.get("/assets/firm_seleted/", function (result) {
    var result = $.parseJSON(result);
    var name = $('#str_manufactory').val();
    for (var i = 0; i < result.length; i++) {
      var id = result[i].id;
      var manufactory = result[i].manufactory;
      $("#manufactory option[index='0']").remove();
      if (name == manufactory) {
        $("#manufactory").append("<option value=" + id + " selected=selected" + ">" + manufactory + "</option>");
      } else {
        $("#manufactory").append("<option value=" + id + ">" + manufactory + "</option>")
      }
    }
  });
});

// 项目负责人菜单
$(function () {
  $.get("/assets/users_seleted/", function (result) {
    var result = $.parseJSON(result);
    var name = $('#str_manager').val();
    for (var i = 0; i < result.length; i++) {
      var id = result[i].id;
      var nickname = result[i].nickname;
      $("#manager option[index='0']").remove();
      if (name == nickname) {
        $("#manager").append("<option value=" + id + " selected=selected" + ">" + nickname + "</option>");
      } else {
        $("#manager").append("<option value=" + id + ">" + nickname + "</option>")
      }
    }
  });
});

// 运维负责人菜单
$(function () {
  $.get("/assets/users_seleted/", function (result) {
    var result = $.parseJSON(result);
    var name = $('#str_admin').val();
    for (var i = 0; i < result.length; i++) {
      var id = result[i].id;
      var nickname = result[i].nickname;
      $("#admin option[index='0']").remove();
      if (name == nickname) {
        $("#admin").append("<option value=" + id + " selected=selected" + ">" + nickname + "</option>");
      } else {
        $("#admin").append("<option value=" + id + ">" + nickname + "</option>")
      }
    }
  });
});

// 添加主机信息
$(function () {
  $('#add_hostForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      hostname: {
        validators: {
          notEmpty: {
            message: '主机名称不能为空.'
          },
          remote: {
            type: 'POST',
            url: '/assets/hosts_valid/',
            data: {hostname: $('#hostname').val() },
            delay :  1000,
            message: '主机名称已存在.'
          }
        }
      },
      ip_address: {
        validators: {
          regexp: {
            regexp: /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/,
            message: '请输入正确的IPV4网段，例如: XX.XX.XX.XX.'
          },
          remote: {
            type: 'POST',
            url: '/assets/hosts_valid/',
            data: {ip: $('#ip').val() },
            delay :  1000,
            message: '公网地址已存在.'
          }
        }
      },
      nip_address: {
        validators: {
          notEmpty: {
            message: '内网地址不能为空.'
          },
          regexp: {
            regexp: /^192\.168\.\d{1,3}\.\d{1,3}$/,
            message: '请输入正确的IPV4网段，目前仅支持: 192.168.XX.XX网段.'
          },
          remote: {
            type: 'POST',
            url: '/assets/hosts_valid/',
            data: {nip: $('#nip').val() },
            delay :  1000,
            message: '内网地址已存在.'
          }
        }
      },
      group: {
        validators: {
          notEmpty: {
            message: '主机属组不能为空.'
          },
          callback: {
            message: '主机属组不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      idc: {
        validators: {
          notEmpty: {
            message: '机房地址不能为空.'
          },
          callback: {
            message: '机房地址不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      cabinet: {
        validators: {
          notEmpty: {
            message: '机柜地址不能为空.'
          },
          callback: {
            message: '机柜地址不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      manufactory: {
        validators: {
          notEmpty: {
            message: '服务厂商不能为空.'
          },
          callback: {
            message: '服务厂商不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      manager: {
        validators: {
          notEmpty: {
            message: '开发人员不能为空.'
          },
          callback: {
            message: '开发人员不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      admin: {
        validators: {
          notEmpty: {
            message: '运维人员不能为空.'
          },
          callback: {
            message: '运维人员不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
    }
  });
  $('.add_hostValid').click(function () {
    $('#add_hostForm').bootstrapValidator('validate');
    if ($('#add_hostForm').data("bootstrapValidator").isValid()){
      var sn = $('#sn').val();
      var server_model = $('#server_model').val();
      var hostname = $('#hostname').val();
      var ip_address = $('#ip_address').val();
      var nip_address = $('#nip_address').val();
      var system_type = $('#system_type').val();
      var system_distribution = $('#system_distribution').val();
      var system_release = $('#system_release').val();
      var kernel_release = $('#kernel_release').val();
      var group = $('#group').val();
      var idc = $('#idc').val();
      var cabinet = $('#cabinet').val();
      var manufactory = $('#manufactory').val();
      var manager = $('#manager').val();
      var admin = $('#admin').val();
      $.post('/assets/hosts_add/', {
        sn: sn,
        server_model: server_model,
        hostname: hostname,
        ip_address: ip_address,
        nip_address: nip_address,
        system_type: system_type,
        system_distribution: system_distribution,
        system_release: system_release,
        kernel_release: kernel_release,
        group: group,
        idc: idc,
        cabinet: cabinet,
        manufactory: manufactory,
        manager: manager,
        admin: admin,
        },
        function (result, status) {
          if (status == 'success') {
            var result = $.parseJSON(result);
            if (result.status == 'true') {
              bootbox.alert("<h4 class='text-center'>数据添加成功!</h4>", function(){ self.location='/assets/hosts_list/'; });
            }
          }
        });
    } else {
      return;
    }
  });
  $('.add_hostReset').click(function () {
    $('#add_hostForm').data('bootstrapValidator').resetForm(true);
  });
});

// 更新主机信息
$(function () {
  $('#up_hostForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      hostname: {
        validators: {
          notEmpty: {
            message: '主机名称不能为空.'
          },
          remote: {
            type: 'POST',
            url: '/assets/hosts_upvalid/',
            data: {hostname: $('#hostname').val(), str_hostname: $('#str_hostname').val() },
            delay :  1000,
            message: '主机名称已存在.'
          }
        }
      },
      ip_address: {
        validators: {
          regexp: {
            regexp: /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/,
            message: '请输入正确的IPV4网段，例如: XX.XX.XX.XX.'
          },
          remote: {
            type: 'POST',
            url: '/assets/hosts_upvalid/',
            data: {ip_address: $('#ip_address').val(), },
            delay :  1000,
            message: '公网地址已存在.'
          }
        }
      },
      nip_address: {
        validators: {
          notEmpty: {
            message: '内网地址不能为空.'
          },
          regexp: {
            regexp: /^192\.168\.\d{1,3}\.\d{1,3}$/,
            message: '请输入正确的IPV4网段，目前仅支持: 192.168.XX.XX网段.'
          },
          remote: {
            type: 'POST',
            url: '/assets/hosts_upvalid/',
            data: {nip_address: $('#nip_address').val(), str_nip_address: $('#str_nip_address').val()

            },
            delay :  1000,
            message: '内网地址已存在.'
          }
        }
      },
      group: {
        validators: {
          notEmpty: {
            message: '主机属组不能为空.'
          },
          callback: {
            message: '主机属组不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      idc: {
        validators: {
          notEmpty: {
            message: '机房地址不能为空.'
          },
          callback: {
            message: '机房地址不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      cabinet: {
        validators: {
          notEmpty: {
            message: '机柜地址不能为空.'
          },
          callback: {
            message: '机柜地址不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      manufactory: {
        validators: {
          notEmpty: {
            message: '服务厂商不能为空.'
          },
          callback: {
            message: '服务厂商不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      manager: {
        validators: {
          notEmpty: {
            message: '开发人员不能为空.'
          },
          callback: {
            message: '开发人员不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      admin: {
        validators: {
          notEmpty: {
            message: '运维人员不能为空.'
          },
          callback: {
            message: '运维人员不能为空.',
            callback: function(value, validator) {
              if (value == '0'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
    }
  });
  $('.up_hostValid').click(function () {
    $('#up_hostForm').bootstrapValidator('validate');
    if ($('#up_hostForm').data("bootstrapValidator").isValid()){
      var id = $(this).attr('CurlId');
      var sn = $('#sn').val();
      var server_model = $('#server_model').val();
      var hostname = $('#hostname').val();
      var ip_address = $('#ip_address').val();
      var nip_address = $('#nip_address').val();
      var system_type = $('#system_type').val();
      var system_distribution = $('#system_distribution').val();
      var system_release = $('#system_release').val();
      var kernel_release = $('#kernel_release').val();
      var group = $('#group').val();
      var idc = $('#idc').val();
      var cabinet = $('#cabinet').val();
      var manufactory = $('#manufactory').val();
      var manager = $('#manager').val();
      var admin = $('#admin').val();
      $.post('/assets/hosts_update/', {
        id: id,
        sn: sn,
        server_model: server_model,
        hostname: hostname,
        ip_address: ip_address,
        nip_address: nip_address,
        system_type: system_type,
        system_distribution: system_distribution,
        system_release: system_release,
        kernel_release: kernel_release,
        group: group,
        idc: idc,
        cabinet: cabinet,
        manufactory: manufactory,
        manager: manager,
        admin: admin,
        },
        function (result, status) {
          if (status == 'success') {
            var result = $.parseJSON(result);
            if (result.status == 'true') {
              bootbox.alert("<h4 class='text-center'>数据更新成功!</h4>", function(){ self.location='/assets/hosts_list/'; });
            }
          }
        });
    } else {
      return;
    }
  });
  $('.up_hostReset').click(function () {
    $('#up_hostForm').data('bootstrapValidator').resetForm(true);
  });
});

// 删除主机信息
$(function () {
  $('.del_hosts').click(function () {
    var id = $(this).attr('CurlId')
    bootbox.confirm({
      title: "提示内容:",
      message: "删除操作是不可恢复的，你确认要删除吗？",
      buttons: {
        confirm: {
          label: '<i class="fa fa-times"></i> 确认',
          className: 'btn-success'
        },
        cancel: {
            label: '<i class="fa fa-check"></i> 取消',
            className: 'btn-danger'
        }
      },
      callback: function (result) {
        if (result) {
          $.post("/assets/hosts_delete/", {id: id}, function (result,status) {
            if (status == 'success') {
              var result = $.parseJSON(result);
              if (result.status == 'true') {
                bootbox.alert("<h4 class='text-center'>数据已成功删除!</h4>", function(){ window.location.reload(); });
              } else {
                bootbox.alert("<h4 class='text-center'>数据删除失败，请稍后再试!</h4>", function(){ window.location.reload(); });
              }
            }
          });
        }
      }
    });
  });
});

