// Agrega tu clave y secreto aquí
const apiKey = '652d2ca85985f01fb73763ab61ccfb66';
const apiSecret = '390fc6f601a98afb';

// Función para hacer una llamada a la API de Flickr y obtener fotos
async function getFlickrPhotos(searchTerm) {
  // Construye la URL de la API
  const url = `https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=${apiKey}&text=${searchTerm}&format=json&nojsoncallback=1`;

  // Realiza una llamada a la API utilizando fetch
  const response = await fetch(url);
  
  // Convierte la respuesta en un objeto JSON
  const data = await response.json();
  
  // Obtén las fotos de la respuesta
  const photos = data.photos.photo;
  
  // Crea un array de objetos que contienen información de las fotos
  const photoData = photos.map(photo => ({
    id: photo.id,
    title: photo.title,
    url: `https://live.staticflickr.com/${photo.server}/${photo.id}_${photo.secret}.jpg`
  }));
  
  return photoData;
}

// Ejemplo de uso de la función getFlickrPhotos
getFlickrPhotos('Vincent van Gogh').then(photos => {
  // Muestra los títulos y URLs de las fotos en la consola
  photos.forEach(photo => {
    // Crea un elemento img y establece su src a la URL de la foto
    const img = document.createElement('img');
    img.src = photo.url;
    img.alt = photo.title;

    // Agrega el elemento img al div #photos
    const photosDiv = document.getElementById('photos');
    photosDiv.appendChild(img);
  });
});


// Obtener la tabla
var tabla = document.getElementById("tabla-datos");

// Crear una solicitud para leer el archivo JSON
var solicitud = new XMLHttpRequest();
solicitud.open("GET", "datos.json");

// Cuando se carga el archivo JSON, generar la tabla
solicitud.onload = function() {
  if (solicitud.status == 200) {
    // Convertir el texto JSON a un objeto JavaScript
    var datos = JSON.parse(solicitud.responseText);
    // Generar las filas de la tabla
    for (var i = 0; i < datos.length; i++) {
      var fila = tabla.insertRow();
      
      // Agregar checkbox a la primera celda
      var checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.name = "seleccionado";
      checkbox.value = datos[i].nombre_obra;
      var cell = fila.insertCell();
      cell.classList.add("checkbox-container");
      cell.appendChild(checkbox);
      
      fila.insertCell().innerHTML = datos[i].nombre_artista;
      fila.insertCell().innerHTML = datos[i].nombre_obra;
      fila.insertCell().innerHTML = '<img src="' + datos[i].foto_obra + '" alt="Foto de la obra" width="100">';
      fila.insertCell().innerHTML = datos[i].curriculum_vitae;
      fila.insertCell().innerHTML = datos[i].descripcion_obra;
    }
  }
};

// Enviar la solicitud
solicitud.send();