// 项目属组列表
$(function () {
  $.get("/projects/groups", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++){
      var id = result[i].id
      var name = result[i].name
      $("#project_group").append("<option value="+ name +">" + name + "</option>");
      $('#project_group').selectpicker('refresh');
      $('#project_group').selectpicker('render');
    }
  });
});

// 项目类型列表
$(function () {
  $.get("/projects/service", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++){
      var id = result[i].id
      var name = result[i].name
      $("#project_service").append("<option value="+ name +">" + name + "</option>");
      $('#project_service').selectpicker('refresh');
      $('#project_service').selectpicker('render');
    }
  });
});

// 项目环境列表
$(function () {
  $.get("/projects/environment", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++){
      var id = result[i].id
      var name = result[i].name
      $("#project_env").append("<option value="+ name +">" + name + "</option>");
      $('#project_env').selectpicker('refresh');
      $('#project_env').selectpicker('render');
    }
  });
});

// 部署主机列表
$(function () {
  $.get("/projects/hosts", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++){
      var id = result[i].id
      var hostname = result[i].hostname
      $("#host_address").append("<option value="+ hostname +">" + hostname + "</option>");
      $('#host_address').selectpicker('refresh');
      $('#host_address').selectpicker('render');
    }
  });
});


// 用户列表
$(function () {
  $.get("/projects/users", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++){
      var id = result[i].id
      var nickname = result[i].nickname
      $("#project_manager").append("<option value="+ nickname +">" + nickname + "</option>")
      $('#project_manager').selectpicker('refresh');
      $('#project_manager').selectpicker('render');
    }
  });
});

// 添加项目
$(function () {
  $('#add_projectForm').bootstrapValidator({
    message: 'This value is not valid',
    // 表示只对于禁用域不进行验证，其他的表单元素都要验证
    excluded: ':disabled',
    fields: {
      name: {
        validators: {
          notEmpty: {
            message: '项目名称不能为空，请输入项目名称.'
          },
          remote: {
            type: 'POST',
            url: '/projects/valid/',
            data: {name: $('#name').val()},
            delay :  1000,
            message: '项目名称已存在，请重新输入.'
          }
        }
      },
      project_service: {
        validators: {
          notEmpty: {
            message: '项目类型不能为空，请输入项目类型.'
          },
          callback: {
            message: '项目类型不能为空，请选择项目类型.',
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
      project_group: {
        validators: {
          notEmpty: {
            message: '项目属组不能为空，请输入项目属组.'
          },
          callback: {
            message: '项目属组不能为空，请选择项目属组.',
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
      project_env: {
        validators: {
          notEmpty: {
            message: '项目环境不能为空，请输入项目环境.'
          },
          callback: {
            message: '项目环境不能为空，请选择项目环境.',
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
      address: {
        validators: {
          notEmpty: {
            message: 'GIT地址不能为空，请输入GIT地址.'
          },
          remote: {
            type: 'POST',
            url: '/projects/valid/',
            data: {address: $('#address').val()},
            delay :  1000,
            message: '项目名称已存在，请重新输入.'
          },
        }
      },
      host_address: {
        validators: {
          notEmpty: {
            message: '部署主机不能为空，请输入部署主机.'
          },
          callback: {
            message: '部署主机不能为空，请选择部署主机.',
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
      path_address: {
        validators: {
          notEmpty: {
            message: '部署的路径地址不能为空，请输入部署的路径地址.'
          },
        }
      },
      port_address: {
        validators: {
          notEmpty: {
            message: '服务的端口地址不能为空，请输入服务的端口地址.'
          },
          regexp: {
            regexp: /^[0-9\.]+$/,
            message: '' +
            '服务端口仅支持数字类型，请输入正确的服务端口地址.'
          },
        }
      },
      project_manager: {
        validators: {
          notEmpty: {
            message: '项目负责人信息不能为空，请输入项目负责人信息.'
          },
          callback: {
            message: '项目负责人信息不能为空，请选择项目负责人信息.',
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
  $('.add_projectValid').click(function () {
    $('#add_projectForm').bootstrapValidator('validate');
    if($('#add_projectForm').data("bootstrapValidator").isValid()){
      var name = $('#name').val();
      var address = $('#address').val();
      var project_group = $('#project_group').val();
      var project_service = $('#project_service').val();
      var project_environment = $('#project_env').val();
      var host_address = $('#host_address').val();
      var path_address = $('#path_address').val();
      var port_address = $('#port_address').val();
      var project_manager = $('#project_manager').val();

      // 当设置为true后，会导致多层次的对象序列化为[object object](浅序列化)
      jQuery.ajaxSettings.traditional = true;

      $.post('/projects/add/', {
        name: name,
        address: address,
        project_service: project_service,
        project_group: project_group,
        project_environment: project_environment,
        host_address: host_address,
        path_address: path_address,
        port_address: port_address,
        project_manager: project_manager
      },
      function (result, status) {
        if (status == 'success') {
          var result = $.parseJSON(result);
          if (result.status == 'true') {
            bootbox.alert("<h4 class='text-center'>数据添加成功!</h4>", function(){ window.location.reload(); });
          }
        }
      });
    } else {
      return;
    }
  });
  $('.add_projectReset').click(function () {
    // bootstrap select多选,重置
    $("#host_address").selectpicker('refresh');
    $('#add_projectForm').data('bootstrapValidator').resetForm(true);
  });
});

// 删除项目信息
$(function () {
  $('.del_project').click(function () {
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
          $.post("/projects/delete/", {id: id}, function (result,status) {
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
