$(function () {
  $('#duration_time').daterangepicker({
    "showDropdowns": false,
    "showHours" : true,
    "timePicker": true,
    "timePickerIncrement" : 1,
    "timePicker24Hour" : true,
    "minDate":"1970-01-01",
    "maxDate":"2099-01-01",
    "startDate": moment().startOf('minute'),
    "endDate": moment().startOf('minute').add(30, 'minute'),
    "locale": {
      // 时间格式
      "format": "YYYY-MM-DD HH:mm:ss",
      "separator": " - ",
      "applyLabel": "确认",
      "cancelLabel": "取消",
      "fromLabel": "从",
      "toLabel": "到",
      "customRangeLabel": "Custom",
      "daysOfWeek": [
          "日",
          "一",
          "二",
          "三",
          "四",
          "五",
          "六"
      ],
      "monthNames": [
          "01",
          "02",
          "03",
          "04",
          "05",
          "06",
          "07",
          "08",
          "09",
          "10",
          "11",
          "12"
      ],
      "firstDay": 0
    }
  }, function (start, end, label) {
        StartTime =  start.format('YYYY-MM-DD HH:mm:ss');
        EndTime = end.format('YYYY-MM-DD HH:mm:ss');
  });
});

// 故障级别列表
$(function () {
  $.get("/fault/level_seleted/", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++) {
      var id = result[i][0];
      var name = result[i][1];
      $("#level option[index='0']").remove();
      $("#level").append("<option value=" + id + ">" + name + "</option>")
    }
  });
});

// 故障类型列表
$(function () {
  $.get("/fault/types_seleted/", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++) {
      var id = result[i].id;
      var name = result[i].name;
      $("#types option[index='0']").remove();
      $("#types").append("<option value=" + id + ">" + name + "</option>")
    }
  });
});

// 影响项目列表
$(function () {
  $.get("/fault/project_seleted", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++) {
      var id = result[i][0];
      var name = result[i][1];
      $("#project option[index='0']").remove();
      $("#project").append("<option value=" + id + ">" + name + "</option>")
    }
  });
});

// 故障状态列表
$(function () {
  $.get("/fault/status_seleted", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++) {
      var id = result[i][0];
      var name = result[i][1];
      $("#status option[index='0']").remove();
      $("#status").append("<option value=" + id + ">" + name + "</option>")
    }
  });
});

// 主导改进列表
$(function () {
  $.get("/fault/improve_seleted", function (result) {
    var result = $.parseJSON(result);
    for (var i = 0; i < result.length; i++) {
      var id = result[i][0];
      var name = result[i][1];
      $("#improve option[index='0']").remove();
      $("#improve").append("<option value=" + id + ">" + name + "</option>")
    }
  });
});

// 删除故障类型信息
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
          $.post("/fault/type_delete/", {id: id}, function (result,status) {
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

// 添加故障类型信息
$(function () {
  $('#add_typeForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      name: {
        validators: {
          notEmpty: {
            message: '故障类型不能为空.'
          },
        remote: {
            type: 'POST',
            url: '/api/type_valid/',
            data: { name: $('#name').val() },
            delay :  1000,
            message: '故障类型已存在，请重新输入.'
          }
        }
      },
    }
  });
  $('.add_typeValid').click(function () {
    $('#add_typeForm').bootstrapValidator('validate');
    if($('#add_typeForm').data("bootstrapValidator").isValid()){
      var name = $('#name').val()
      $.post('/fault/type_add/', {name: name}, function (result, status) {
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
  $('.add_typeReset').click(function () {
    $('#add_typeForm').data('bootstrapValidator').resetForm(true);
  });
});

// 添加故障信息
$(function () {
  $('#add_faultForm').bootstrapValidator({
    message: 'This value is not valid',
    fields: {
      name: {
        validators: {
          notEmpty: {
            message: '故障简述不能为空.'
          },
        }
      },
      level: {
        validators: {
          notEmpty: {
            message: '故障级别不能为空.'
          },
          callback: {
            message: '故障级别不能为空.',
            callback: function(value, validator) {
              if (value == 'tag'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      types: {
        validators: {
          notEmpty: {
            message: '故障类型不能为空.'
          },
          callback: {
            message: '故障类型不能为空.',
            callback: function(value, validator) {
              if (value == 'tag'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      project: {
        validators: {
          notEmpty: {
            message: '影响项目不能为空.'
          },
          callback: {
            message: '影响项目不能为空.',
            callback: function(value, validator) {
              if (value == 'tag'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      status: {
        validators: {
          notEmpty: {
            message: '故障状态不能为空.'
          },
          callback: {
            message: '故障状态不能为空.',
            callback: function(value, validator) {
              if (value == 'tag'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      improve: {
        validators: {
          notEmpty: {
            message: '主导改进不能为空.'
          },
          callback: {
            message: '主导改进不能为空.',
            callback: function(value, validator) {
              if (value == 'tag'){
                return false;
              } else {
                return true;
              }
            }
          }
        }
      },
      duration_time: {
        validators: {
          notEmpty: {
            message: '故障时间不能为空.'
          },
        }
      },
    }
  });
  $('.add_faultValid').click(function () {
    $('#add_faultForm').bootstrapValidator('validate');
    if ($('#add_faultForm').data("bootstrapValidator").isValid()){
      var name = $('#name').val();
      var level = $('#level').val();
      var type = $('#types').val();
      var project = $('#project').val();
      var status = $('#status').val();
      var improve = $('#improve').val();
      var start_time = StartTime;
      var end_time = EndTime;
      var effect = $('#effect').val();
      var content = $('#content').val();
      var reasons = $('#reasons').val();
      var solution = $('#solution').val();
      var lesson = $('#lesson').val();
      $.post('/fault/fault_add/', {
        name: name,
        level: level,
        type: type,
        project: project,
        status: status,
        improve: improve,
        start_time: start_time,
        end_time: end_time,
        effect: effect,
        content: content,
        reasons: reasons,
        solution: solution,
        lesson:lesson,
        },
        function (result, status) {
          if (status == 'success') {
            var result = $.parseJSON(result);
            if (result.status == 'true') {
              bootbox.alert("<h4 class='text-center'>数据添加成功!</h4>", function(){ self.location='/fault/fault_list/'; });
            }
          }
        });
    } else {
      return;
    }
  });
  $('.add_faultReset').click(function () {
    $('#add_faultForm').data('bootstrapValidator').resetForm(true);
  });
});

// 删除故障简述信息
$(function () {
  $('.del_fault').click(function () {
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
          $.post("/fault/fault_delete/", {id: id}, function (result,status) {
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