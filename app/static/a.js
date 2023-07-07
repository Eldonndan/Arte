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
    
    function validarFormularioRegistro() {
        const form = document.getElementById('register-form');
        form.addEventListener('submit', function(event) {
        event.preventDefault();
    
        const nombre = document.getElementById('nombre').value;
        const apellido = document.getElementById('apellido').value;
        const telefono = document.getElementById('telefono').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
    
        // Validar que todos los campos estén rellenados
        if (nombre.trim() === '' || apellido.trim() === '' || telefono.trim() === '' || email.trim() === '' || password.trim() === '') {
            showModal('Por favor, completa todos los campos');
            return;
        }
    
        // Validar el formato del número de teléfono
        const telefono_regex = /^[0-9]{9}$/;
        if (!telefono_regex.test(telefono)) {
            showModal('El número de teléfono debe tener 9 dígitos');
            return;
        }
    
        // Validar el formato del correo electrónico
        const email_regex = /^[^\s@]+@(duocuc\.cl|profesor\.duoc\.cl|gmail\.com|yahoo\.com)$/;
        if (!email_regex.test(email)) {
            showModal('El correo electrónico no tiene un formato válido');
            return;
        }
    
        // Validar que la contraseña tenga al menos 8 caracteres
        if (password.length < 8) {
            showModal('La contraseña debe tener al menos 8 caracteres');
            return;
        }
    
        // Si llegamos hasta aquí, entonces el formulario es válido y podemos enviarlo
        showModal('Registro exitoso, usted será redireccionado');
        setTimeout(function() {
            form.submit();
        }, 2000); // Redireccionar después de 2 segundos
        });
    }
    
    validarFormularioRegistro()
