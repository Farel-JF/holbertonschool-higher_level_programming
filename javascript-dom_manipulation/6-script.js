let character = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
    .then(response => response.json())
    .then(function(data) {
          const characterName = data.name;
          characterName = document.textContent = char;
        })
      .catch(error => console.error(error));

