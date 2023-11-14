// Obtén una referencia a los elementos de contenido
let nosotros = document.querySelector('#nosotros');
let contacto = document.querySelector('#contacto');
let servicios = document.querySelector('#servicios');
let productos = document.querySelector('#productos');
let aviso = document.querySelector('#aviso');
let privacidad = document.querySelector('#privacidad');
let condiciones = document.querySelector('#condiciones');

// Oculta todos los elementos de contenido usando un bucle forEach
[nosotros, contacto, servicios, productos, aviso, condiciones, privacidad].forEach(element => {
    element.style.display = 'none';
});

function mostrarContenido(identificador) {
  // Oculta todos los elementos de contenido
  [nosotros, contacto, servicios, productos, aviso, condiciones, privacidad].forEach(element => {
    element.style.display = 'none';
  });

  // Muestra el elemento seleccionado
  let elemento = document.querySelector(identificador);
  if (elemento) {
    elemento.style.display = 'block';
  }
}


