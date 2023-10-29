function mostrarContenido(identificador) {
  // Obtén una referencia a los elementos de contenido
  let ps5 = document.querySelector('#contenidoPS5');
  let xbox = document.querySelector('#contenidoXbox');
  let nintendoSwitch = document.querySelector('#contenidoSwitch');
  let ps4 = document.querySelector('#contenidoPS4');
  let nintendo3ds = document.querySelector('#contenido3ds');

  // Oculta todos los elementos de contenido usando un bucle for o forEach
  [ps5, xbox, nintendoSwitch, ps4, nintendo3ds].forEach(element => {
    element.style.display = 'none';
  });

  // Muestra el elemento seleccionado
  let elemento = document.querySelector('#contenido' + identificador);
  if (elemento) {
    elemento.style.display = 'block';
  }
}

function cambiarColor(color) {

  cuerpo = document.querySelector("body");
  if (color == 'black') {
    cuerpo.style.backgroundColor = color;
    cuerpo.style.color = "white";
  }
  if (color == 'white') {
    cuerpo.style.backgroundColor = color;
    cuerpo.style.color = "black";
  }
}
