function validarFormulario() {
  const form = document.getElementById('register-form');
  form.addEventListener('submit', function(event) {
    // Prevenir el envío del formulario
    event.preventDefault();
    
    const nombre = document.getElementById('nombre').value;
    const apellido = document.getElementById('apellido').value;
    const telefono = document.getElementById('telefono').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Validar que el nombre y el apellido no estén vacíos
    if (nombre.trim() === '') {
      alert('El nombre es obligatorio');
      return;
    }
    if (apellido.trim() === '') {
      alert('El apellido es obligatorio');
      return;
    }

    // Validar el formato del número de teléfono
    const telefono_regex = /^[0-9]{9}$/;
    if (!telefono_regex.test(telefono)) {
      alert('El número de teléfono debe tener 9 dígitos');
      return;
    }

    // Validar el formato del correo electrónico
    const email_regex = /^[^\s@]+@(duocuc\.cl|profesor\.duoc\.cl|gmail\.com|yahoo\.com)$/;
    if (!email_regex.test(email)) {
      alert('El correo electrónico no tiene un formato válido');
      return;
    }

    // Validar que la contraseña tenga al menos 8 caracteres
    if (password.length < 8) {
      alert('La contraseña debe tener al menos 8 caracteres');
      return;
    }
    
    // Si llegamos hasta aquí, entonces el formulario es válido y podemos enviarlo
    form.submit();
  });
}

validarFormulario();

