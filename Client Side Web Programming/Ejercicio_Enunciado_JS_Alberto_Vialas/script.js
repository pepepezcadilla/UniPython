// Enunciado: Crea una función que, al hacer clic en el botón "Contar", cuente del 1 al 10 uno detrás de otro y muestre cada número en el párrafo con id "demo" en el DOM utilizando un bucle for.

// Declaración de variables
var count = 1;

// Declaración de función que cuenta y actualiza el DOM
function contarHastaDiez() {
    var aux = '', demoElement = null;
    demoElement = document.getElementById("demo");

    for (count = 1; count <= 10; count++) {
        // Actualizar el contenido del párrafo en el DOM
        aux = aux + '' + count
        demoElement.innerHTML = "Contando: " + aux;
        
    }
}

// Asociar la función al evento click del botón
document.getElementById("countButton").addEventListener("click", contarHastaDiez);
