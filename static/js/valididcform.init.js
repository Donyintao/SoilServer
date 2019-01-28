// 删除机房信息
$(function () {
  $('.del_idc').click(function () {
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
          $.post("/assets/idc_delete/", {id: id}, function (result,status) {
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

// 添加机房信息
$(function () {
  $('#add_idcFrom').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      name: {
        validators: {
          notEmpty: {
            message: '机房名称不能为空.'
          },
          remote: {
            type: 'POST',
            url: '/assets/idc_valid/',
            data: {name: $('#name').val(), address: $('#address').val()},
            delay :  1000,
            message: '机房名称已经存在.'
          }
        }
      },
      address: {
        validators: {
          notEmpty: {
            message: '机房地址不能为空.'
          }
        }
      },
    }
  });
  $('.add_idcValid').click(function () {
    $('#add_idcFrom').bootstrapValidator('validate');
    if($('#add_idcFrom').data("bootstrapValidator").isValid()){
      var name = $('#name').val()
      var address = $('#address').val()
      $.post('/assets/idc_add/', {name: name, address: address}, function (result, status) {
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
  $('.add_idcReset').click(function () {
    $('#add_idcFrom').data('bootstrapValidator').resetForm(true);
  });
});

// 更新机房信息
$(function () {
  $('#up_idcForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      address: {
        validators: {
          notEmpty: {
            message: '机房地址不能为空.'
          }
        }
      },
    }
  });
  $('.up_idcValid').click(function () {
    $('#up_idcForm').bootstrapValidator('validate');
    if($('#up_idcForm').data("bootstrapValidator").isValid()){
      var id = $(this).attr('CurlId');
      var address = $('#address').val();
      $.post('/assets/idc_update/', {id: id, address: address}, function (result, status) {
        if (status == 'success') {
          var result = $.parseJSON(result);
          if (result.status == 'true') {
            bootbox.alert("<h4 class='text-center'>数据更新成功!</h4>", function(){ self.location='/assets/idc_list'; });
          }
        }
      });
    } else {
      return;
    }
  });
  $('.up_idcReset').click(function () {
    $('#up_idcFrom').data('bootstrapValidator').resetForm(true);
  });
});