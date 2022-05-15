// $(function() {
//     $('[data-toggle="tooltip"]').tooltip()
//   })

$(document).ready(function(){
    $(".nav-pills a").click(function(){
       $(this).tab('show');
    });
  });