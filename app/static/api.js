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



