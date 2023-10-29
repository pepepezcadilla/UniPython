// JS para generar el enlace de descarga y mostrar imágenes en un modal
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("contactForm").addEventListener("submit", function (event) {
        event.preventDefault();

        const nombre = document.getElementById("nombre").value;
        const exposicionFavorita = document.getElementById("exposicionFavorita").value;

        // Aquí puedes generar el enlace personalizado como desees
        const link = `https://tupaginaweb.com/entradas?nombre=${nombre}&exposicion=${exposicionFavorita}`;

        const entradasDiv = document.getElementById("entradas");
        entradasDiv.innerHTML = `<p>Descarga tus entradas <a href="${link}" target="_blank">aquí</a></p>`;
    });

    // Obtenemos los elementos del DOM
    var imagenes = document.querySelectorAll(".imagen");
    var modal = document.getElementById("modal");
    var imagenModal = document.getElementById("imagen-modal");

    // Función para abrir el modal
    function abrirModal(imagen) {
        modal.style.display = "block";
        imagenModal.src = imagen.src;

        // Asignar el evento "cerrar" dentro de abrirModal
        var cerrar = document.getElementById("cerrar");
        cerrar.onclick = function() {
            cerrarModal();
        }
    }

    // Función para cerrar el modal
    function cerrarModal() {
        modal.style.display = "none";
    }

    // Agregamos un manejador de eventos a cada imagen
    imagenes.forEach(function(imagen) {
        imagen.onclick = function() {
            abrirModal(this);
        }
    });

    // También podemos cerrar el modal haciendo clic en cualquier parte fuera de la imagen modal
    window.onclick = function(event) {
        if (event.target == modal) {
            cerrarModal();
        }
    }

     // Obtener los enlaces de las exposiciones
     var exposicion1Link = document.getElementById("exposicion1-tab");
     var exposicion2Link = document.getElementById("exposicion2-tab");
 
// Agregar un manejador de eventos para el enlace de Exposición 1
exposicion1Link.addEventListener("click", function() {
    // Hacer que Exposición 1 sea activa y Exposición 2 no
    exposicion1Link.classList.add("active");
    exposicion2Link.classList.remove("active");

    // Mostrar el contenido de Exposición 1 y ocultar el contenido de Exposición 2
    document.querySelector("#exposicion1").classList.add("show", "active");
    document.querySelector("#exposicion2").classList.remove("show", "active");
});

// Agregar un manejador de eventos para el enlace de Exposición 2
exposicion2Link.addEventListener("click", function() {
    // Hacer que Exposición 2 sea activa y Exposición 1 no
    exposicion2Link.classList.add("active");
    exposicion1Link.classList.remove("active");

    // Mostrar el contenido de Exposición 2 y ocultar el contenido de Exposición 1
    document.querySelector("#exposicion2").classList.add("show", "active");
    document.querySelector("#exposicion1").classList.remove("show", "active");
});

})
