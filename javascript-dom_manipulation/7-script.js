let character = document.querySelector('#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
    .then(response => response.json())
    .then(function(data) {
          const movies = data.results;
                movies.forEach((film)=> {
                  const filmTitle = film.title;
                  const listItem = document.createElement('li');
                  listItem.textContent = filmTitle;
                  listMovies.appendChild(listItem);
        })})
      .catch(error => console.error(error));
