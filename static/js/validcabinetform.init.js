// 删除机柜信息
$(function () {
  $('.del_cabinet').click(function () {
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
          $.post("/assets/cabinet_delete/", {id: id}, function (result,status) {
            if (status == 'success') {
              var result = $.parseJSON(result);
              if (result.status == 'true') {
                bootbox.alert("<h4 class='text-center'>数据已成功删除!</h4>", function(){ window.location.reload(); });
              } else {
                bootbox.alert("<h4 class='text-center'>数据删除失败，已使用的机柜禁止删除!</h4>", function(){ window.location.reload(); });
              }
            }
          });
        }
      }
    });
  });
});

// 添加机柜
$(function () {
  $('#add_cabinetFrom').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      idc_name: {
        validators: {
          notEmpty: {
            message: '机房名称不能为空.'
          },
          callback: {
            message: '机房名称不能为空',
            callback: function(value, validator) {
              if (value == '请选择机房'){
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
            message: '机柜名称不能为空.'
          },
          remote: {
            type: 'POST',
            url: '/assets/cabinet_valid/',
            data: {cabinet: $('#cabinet').val()},
            delay :  1000,
            message: '机柜名称已经存在.'
          }
        }
      },
    }
  });
  $('.add_cabinetValid').click(function () {
    $('#add_cabinetFrom').bootstrapValidator('validate');
    if ($('#add_cabinetFrom').data("bootstrapValidator").isValid()){
      var name = $('#name').val()
      var cabinet = $('#cabinet').val()
      $.post('/assets/cabinet_add/', {name: name, cabinet: cabinet}, function (result, status) {
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
  $('.add_cabinetReset').click(function () {
    $('#add_cabinetFrom').data('bootstrapValidator').resetForm(true);
  });
});

// 更新机柜信息
$(function () {
  $('#up_cabinetFrom').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      cabinet: {
        validators: {
          notEmpty: {
            message: '机柜名称不能为空，请输入机柜名称.'
          },
          remote: {
            type: 'POST',
            url: '/assets/cabinet_valid/',
            data: {cabinet: $('#cabinet').val()},
            delay :  1000,
            message: '机柜名称已存在，请重新输入.'
          }
        }
      }
    }
  });
  $('.up_cabinetValid').click(function () {
    $('#up_cabinetFrom').bootstrapValidator('validate');
    if ($('#up_cabinetFrom').data("bootstrapValidator").isValid()) {
      var id = $(this).attr('CurlId')
      var cabinet = $('#cabinet').val()
      $.post('/assets/cabinet_update/', {id: id, cabinet: cabinet}, function (result, status) {
        var result = $.parseJSON(result);
        if (result.status == 'true') {
          bootbox.alert("<h4 class='text-center'>数据更新成功!</h4>", function(){ self.location='/assets/cabinet_list/'; });
        }
      });
    } else {
      return;
    }
  });
});