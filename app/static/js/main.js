$(document).ready(function() {
  // $('.messages').addClass('animated fadeIn')
  //   .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend',
  //     function() { $(this).removeClass('fadeIn').addClass('fadeOutDown').css('animation-delay', '3s'); });
  $('.messages').addClass('animated fadeIn').css('animation-duration', '.3s');

  /* Reload form habit */
  reloadForm('body');

  /* Notification messages */
  $('.messages .message').click(function(event) {
    $(this).fadeOut('fast');
  });
});

var post = function(path, params) {
  var form = document.createElement("form");
  form.setAttribute("method", "post");
  form.setAttribute("action", path);
  for(var key in params) {
    if(params.hasOwnProperty(key)) {
      var hiddenField = document.createElement("input");
      hiddenField.setAttribute("type", "hidden");
      hiddenField.setAttribute("name", key);
      hiddenField.setAttribute("value", params[key]);
      form.appendChild(hiddenField);
     }
  }
  document.body.appendChild(form);
  form.submit();
};

var postConfirm = function(msg, path, params) {
  var r=confirm(msg);
  if (r==true) {
    post(path, params);
  }
};

var reloadForm = function(parent) {
  $('form', $(parent)).submit(function(event) {
    event.preventDefault();

    // disabled all input fields
    $(this).css('transition-duration', '0.3s');
    $(this).css('opacity', 0.5);
    $(':input', this).prop('readonly', true);
    $(':submit', this).html('<i class="fa fa-spinner fa-spin"></i> Loading ...');

    // delaying at least 2s make user feel it's on working...
    var form = this;
    setTimeout(function () {
      var fnSuccess = $(form).data('success');
      if (typeof fnSuccess != 'undefined') {
        $.ajax({
          type: $(form).prop('method'),
          url: $(form).prop('action'),
          data: $(form).serialize(),
          success: function(data) {
            // show a finish button if need
            $(form).css('opacity', 1);
            $(':submit', form).addClass('button-finish');
            $(':submit', form).html('<i class="fa fa-check"></i> Finish');
            // processing
            eval(fnSuccess + '(data)');
          }
        });
      } else {
        $(form).unbind('submit').submit();
      }
    }, 200);
  });
};
