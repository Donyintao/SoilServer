$(function () {
  $('#duration_time').daterangepicker({
    "showDropdowns": false,
    "showHours" : true,
    "timePicker": true,
    "timePickerIncrement" : 1,
    "timePicker24Hour" : true,
    "autoApply": true,
    "minDate":"1970-01-01",
    "maxDate":"2099-01-01",
    "startDate": moment().startOf('minute'),
    "endDate": moment().startOf('minute').add(30, 'minute'),
    "locale": {
      //汉化
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
        alert(StartTime);
        EndTime = end.format('YYYY-MM-DD HH:mm:ss');
        alert(EndTime);
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
      var start_time = '';
      var end_time = '';
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