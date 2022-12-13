fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then(response => response.json())
  .then(data => {

    $('DIV#hello').text(`${data.hello}`);
  })
  .catch(error => {
    console.log('An error occurred:', error);
  });
