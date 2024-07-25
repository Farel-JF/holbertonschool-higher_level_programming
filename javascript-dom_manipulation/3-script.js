document.getElementById('toggle_header').addEventListener('click', function() {
const header = document.querySelector('header');
  if (header.classList.contains('red')){
    header.classList.remove('red')
    header.classList.add('red')
  }else {
    header.classList.remove('red');
    header.classList.add('red');
  }
});
