// 删除域名信息
$(function () {
  $('.del_dns').click(function () {
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
          $.post("/dns/delete/", {id: id}, function (result,status) {
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

// 添加域名信息
$(function () {
  $('#add_dnsFrom').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      host: {
        validators: {
          notEmpty: {
            message: '主机记录不能为空.'
          }
        }
      },
      type: {
        validators: {
          notEmpty: {
            message: '记录类型不能为空.'
          }
        }
      },
      data: {
        validators: {
          notEmpty: {
            message: '解析地址不能为空.'
          }
        }
      },
    }
  });
  $('.add_dnsValid').click(function () {
    $('#add_dnsFrom').bootstrapValidator('validate');
    if($('#add_dnsFrom').data("bootstrapValidator").isValid()){
      var host = $('#host').val()
      var type = $('#type').val()
      var data = $('#data').val()
      $.post('/dns/add/', {host: host, type: type, data: data}, function (result, status) {
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
  $('.add_dnsReset').click(function () {
    $('#add_dnsFrom').data('bootstrapValidator').resetForm(true);
  });
});

// 更新域名信息
$(function () {
  $('#up_dnsForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      host: {
        validators: {
          notEmpty: {
            message: '主机记录不能为空.'
          }
        }
      },
      type: {
        validators: {
          notEmpty: {
            message: '记录类型不能为空.'
          }
        }
      },
      data: {
        validators: {
          notEmpty: {
            message: '解析地址不能为空.'
          }
        }
      },
    }
  });
  $('.up_dnsValid').click(function () {
    $('#up_dnsForm').bootstrapValidator('validate');
    if($('#up_dnsForm').data("bootstrapValidator").isValid()){
      var id = $(this).attr('CurlId');
      var host = $('#host').val()
      var type = $('#type').val()
      var data = $('#data').val()
      $.post('/dns/update/', {id: id, host: host, type: type, data: data},  function (result, status) {
        if (status == 'success') {
          var result = $.parseJSON(result);
          if (result.status == 'true') {
            bootbox.alert("<h4 class='text-center'>数据更新成功!</h4>", function(){ self.location='/dns/list/'; });
          }
        }
      });
    } else {
      return;
    }
  });
  $('.up_dnsReset').click(function () {
    $('#up_dnsFrom').data('bootstrapValidator').resetForm(true);
  });
});