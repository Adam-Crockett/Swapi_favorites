(function($) {
  $(function() {
    $(".sidenav").sidenav();
  });
  document.addEventListener("DOMContentLoaded", function() {
    var elems = document.querySelectorAll(".sidenav");
    var instances = M.Sidenav.init(elems, options);
  }); // end of document ready
});

$(document).ready(function() {
  document.addEventListener("DOMContentLoaded", function() {
    var elems = document.querySelectorAll(".sidenav");
    var instances = M.Sidenav.init(elems, options);
  });
  $("select").formSelect();
});
jQuery; // end of jQuery name space
