fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
   let items = data.results;
    for (let item of items){
        $('UL#list_movies').append(`<li>${item.title}</li>`);
    }
    
  })
  .catch(error => {
    console.log('An error occurred:', error);
  });