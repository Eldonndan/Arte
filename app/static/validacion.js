function validarRUT(rut) {
    // Eliminamos los puntos y guiones del RUT y lo convertimos a mayúsculas
    rut = rut.replace(/\./g, '').replace(/-/g, '').toUpperCase();
  
    if (!/^[0-9]+[0-9K]{1}$/.test(rut)) {
      // El formato del RUT no es válido
      return false;
    }
  
    // Separamos el número y el dígito verificador
    const numero = rut.slice(0, -1);
    const dv = rut.slice(-1);
  
    // Calculamos el dígito verificador esperado
    let suma = 0;
    let multiplicador = 2;
    for (let i = numero.length - 1; i >= 0; i--) {
      suma += multiplicador * parseInt(numero.charAt(i));
      multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
    }
    const dvEsperado = 11 - (suma % 11);
    const dvCalculado = dvEsperado === 11 ? '0' : dvEsperado === 10 ? 'K' : dvEsperado.toString();
  
    // Comparamos el dígito verificador calculado con el ingresado por el usuario
    return dv.toUpperCase() === dvCalculado;
  }
  
  function validarFormulario() {
    const form = document.getElementById('register-form');
    form.addEventListener('submit', function(event) {
      // Prevenir el envío del formulario
      event.preventDefault();
  
      const rut = document.getElementById('rut').value;
      const nombre = document.getElementById('nombre').value;
      const apellido = document.getElementById('apellido').value;
      const telefono = document.getElementById('telefono').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const confirm_password = document.getElementById('confirm_password').value;
  
      // Validar el formato del RUT chileno
      if (!validarRUT(rut)) {
        alert('El RUT no es válido');
        return;
      }
  
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
  
      // Validar que la confirmación de la contraseña coincida con la contraseña
      if (password !== confirm_password) {
        alert('Las contraseñas no coinciden');
        return;
      }
  
      // Si llegamos hasta aquí, entonces el formulario es válido y podemos enviarlo
      form.submit();
    });
  }
  
  validarFormulario();

