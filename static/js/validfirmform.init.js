// 删除厂商信息
$(function () {
  $('.del_firm').click(function () {
    var id = $(this).attr('CurlId');
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
          $.post("/assets/firm_delete/", {id: id}, function (result,status) {
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

// 添加厂商信息
$(function () {
  $('#add_firmForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      manufactory: {
        validators: {
          notEmpty: {
            message: '厂商名称不能为空.'
          },
        }
      },
    }
  });
  $('.add_firmValid').click(function () {
    $('#add_firmForm').bootstrapValidator('validate');
    if ($('#add_firmForm').data("bootstrapValidator").isValid()){
      var manufactory = $('#manufactory').val();
      var support_num = $('#support_num').val();
      $.post('/assets/firm_add/', {manufactory: manufactory, support_num: support_num}, function (result, status) {
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
  $('.add_firmReset').click(function () {
    $('#add_firmForm').data('bootstrapValidator').resetForm(true);
  });
});

// 更新厂商信息
$(function () {
  $('#up_firmForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      manufactory: {
        validators: {
          notEmpty: {
            message: '厂商名称不能为空.'
          },
        }
      },
    }
  });
  $('.up_firmValid').click(function () {
    $('#up_firmForm').bootstrapValidator('validate');
    if ($('#up_firmForm').data("bootstrapValidator").isValid()){
      var id = $(this).attr('CurlId');
      var manufactory = $('#manufactory').val();
      var support_num = $('#support_num').val();
      $.post('/assets/firm_update/', {id: id, manufactory: manufactory, support_num: support_num}, function (result, status) {
        if (status == 'success') {
          var result = $.parseJSON(result);
          if (result.status == 'true') {
            bootbox.alert("<h4 class='text-center'>数据更新成功!</h4>", function(){ self.location='/assets/firm_list/'; });
          }
        }
      });
    } else {
      return;
    }
  });
  $('.up_firmReset').click(function () {
    $('#up_firmForm').data('bootstrapValidator').resetForm(true);
  });
});