document.addEventListener('DOMContentLoaded', function() {
    var objectIds = ['459189', '436105', '436323', '13315', '437329']; // Reemplaza con los IDs de las obras de arte que deseas obtener

    objectIds.forEach(function(objectId) {
      var api_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/' + objectId;
  
      var request = new XMLHttpRequest();
      request.open('GET', api_url, true);
  
      request.onload = function() {
        if (request.status >= 200 && request.status < 400) {
          var data = JSON.parse(request.responseText);
          if ('artistDisplayName' in data) {
            var artist_name = data['artistDisplayName'];
            var artist_nationality = data['artistNationality'];
            var artist_birth_year = data['artistBeginDate'];
            var artist_death_year = data['artistEndDate'];
            var object_url = data['objectURL'];
            var primary_image_url = data['primaryImage'];
  
            var artistInfo = `
              <div class="artista">
                <h2>${artist_name}</h2>
                <p>Nacionalidad: ${artist_nationality}</p>
                <p>Año de nacimiento: ${artist_birth_year}</p>
                <p>Año de fallecimiento: ${artist_death_year}</p>
                <p>Enlace a la obra: <a href="${object_url}">${object_url}</a></p>
                <img src="${primary_image_url}" alt="Imagen de la obra">
              </div>
            `;
  
            document.getElementById('artistas-container').innerHTML += artistInfo;
          }
        } else {
          console.log('No se encontró información del artista con el ID: ' + objectId);
        }
      };
  
      request.onerror = function() {
        console.log('Error al realizar la solicitud');
      };
  
      request.send();
    });
  });
  