document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(Objet => showObjet(Objet));

  function showObjet (Objet) {
    console.log(Objet);
    document.querySelector('#hello').textContent = Objet.hello;
  }
});
