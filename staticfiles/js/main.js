$(function() {
   $(document).on('click','#button-like',function(e){
      $('#button-dislike').removeClass('dislike-icon');
      $('#button-like').removeClass('like-icon');
   });
   $(document).on('click','#button-dislike',function(e){
      $('#button-like').removeClass('like-icon');
      $('#button-dislike').removeClass('dislike-icon');
   });

   const search = document.querySelector('.item-search');
   const btn = document.querySelector('.search-btn');
   const input = document.querySelector('.search-input');

   btn.addEventListener('click', () => {
      search.classList.toggle('active');
      input.focus();
   });
   
});
