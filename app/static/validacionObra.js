document.addEventListener('DOMContentLoaded', function() {
    var formulario = document.getElementById('formulario-obra');
    
    formulario.addEventListener('submit', function(event) {
      event.preventDefault(); // Evita que se envíe el formulario normalmente
      
      // Aquí puedes agregar tu lógica para verificar los datos y enviar el formulario mediante AJAX
      
      // Si llegamos hasta aquí, entonces el formulario es válido y podemos enviarlo
      mostrarModalExitoso('Obra agregada exitosamente, usted será redirigido');
      setTimeout(function() {
        formulario.submit();
      }, 2000); // Redireccionar después de 2 segundos
    });
  });
  
  function mostrarModalExitoso(mensaje) {
    var modal = document.getElementById('exampleModalCenter');
    var modalMessage = document.getElementById('modal-message');
    
    modalMessage.innerText = mensaje;
    $(modal).modal('show'); // Utiliza jQuery para mostrar el modal
  }
  