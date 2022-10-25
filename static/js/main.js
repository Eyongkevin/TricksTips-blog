$(function() {
   console.log("working.....");
   $(document).on('click','#button-like',function(e){
      $('#button-dislike').removeClass('dislike-icon');
      $('#button-like').removeClass('like-icon');
   });
   $(document).on('click','#button-dislike',function(e){
      $('#button-like').removeClass('like-icon');
      $('#button-dislike').removeClass('dislike-icon');
   });
});