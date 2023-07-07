function showModal(message) {
    const modalBody = document.getElementById('modal-message');
    modalBody.innerText = message;
    
    // Verificar si es un mensaje de "Registro exitoso"
    if (message === 'Registro exitoso, usted será redireccionado') {
      // Ocultar el botón del modal
      const modalFooter = document.querySelector('#exampleModalCenter .modal-footer');
      modalFooter.style.display = 'none';
    } else {
      // Mostrar el botón del modal para otros mensajes
      const modalFooter = document.querySelector('#exampleModalCenter .modal-footer');
      modalFooter.style.display = 'block';
    }
    
    $('#exampleModalCenter').modal('show');
  }
  


function validarFormularioInicioSesion() {
  const form = document.getElementById('login-form');
  
  if (!form) {
    console.error('No se encontró el formulario con el ID "login-form"');
    return;
  }
  
  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Validar que el correo electrónico y la contraseña estén rellenados
    if (email.trim() === '') {
      showModal('Por favor, ingresa tu correo electrónico');
      return;
    }

    if (password.trim() === '') {
      showModal('Por favor, ingresa tu contraseña');
      return;
    }

    // Si llegamos hasta aquí, entonces el formulario es válido y podemos enviarlo
    form.submit();
  });
}

// Llamar a la función de validación del formulario de inicio de sesión
validarFormularioInicioSesion();
