document.getElementById('add_item').addEventListener('click', function() {

  const newitem = document.createElement('li');

  newitem.textContent = 'item';

  const list = document.querySelector('.my_list');

  list.appendChild(newitem);

  });
