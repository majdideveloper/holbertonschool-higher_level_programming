fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    $('DIV#character').text(`${data.name}`);
  })
  .catch(error => {
    console.log('An error occurred:', error);
  });
