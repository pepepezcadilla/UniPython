document.addEventListener('DOMContentLoaded', function() {
    // Obtén la referencia a la tabla por su ID
    const table = document.getElementById('tabla');

    // Datos para llenar la tabla de forma dinámica
    const tablaData = [
        ['Nuevo Dato 1, js', 'Nuevo Dato 2, js'],
        ['Nuevo Dato 3, js', 'Nuevo Dato 4, js']
    ];

    // Limpia la tabla actual
    table.innerHTML = '';

    // Llena la tabla con los nuevos datos
    for (let i = 0; i < tablaData.length; i++) {
        const row = table.insertRow();
        for (let j = 0; j < tablaData[i].length; j++) {
            const cell = row.insertCell(j);
            cell.innerHTML = tablaData[i][j];
        }
    }

    // Obtén referencias a las listas por sus IDs
    const ul = document.getElementById('lista-no-ordenada');
    const ol = document.getElementById('lista-ordenada');
    const dl = document.getElementById('lista-definicion');

    // Datos para llenar las listas de forma dinámica
    const listaNoOrdenadaData = ['Nuevo elemento 1, js', 'Nuevo elemento 2, js', 'Nuevo elemento 3, js'];
    const listaOrdenadaData = ['Nuevo elemento numerado 1, js', 'Nuevo elemento numerado 2, js', 'Nuevo elemento numerado 3, js'];
    const listaDefinicionData = [
        ['Nuevo término 1, js', 'Nueva definición 1, js'],
        ['Nuevo término 2, js', 'Nueva definición 2, js'],
        ['Nuevo término 3, js', 'Nueva definición 3, js']
    ];

    // Limpia las listas actuales
    ul.innerHTML = '';
    ol.innerHTML = '';
    dl.innerHTML = '';

    // Llena las listas con los nuevos datos
    for (let i = 0; i < listaNoOrdenadaData.length; i++) {
        const li = document.createElement('li');
        li.textContent = listaNoOrdenadaData[i];
        ul.appendChild(li);
    }

    for (let i = 0; i < listaOrdenadaData.length; i++) {
        const li = document.createElement('li');
        li.textContent = listaOrdenadaData[i];
        ol.appendChild(li);
    }

    for (let i = 0; i < listaDefinicionData.length; i++) {
        const dt = document.createElement('dt');
        dt.textContent = listaDefinicionData[i][0];
        const dd = document.createElement('dd');
        dd.textContent = listaDefinicionData[i][1];
        dl.appendChild(dt);
        dl.appendChild(dd);
    }

    // Modificar el enlace a la página de contacto
    const footerLink = document.getElementById('footerLink');
    footerLink.href = 'https://es.wikipedia.org/wiki/JavaScript';

    // Modificar el src de la imagen
    const image = document.getElementById('imagen');
    image.src = 'https://www.tshirtgeek.com.br/wp-content/uploads/2021/03/com019.jpg';

    // Crear un elemento link para el favicon
    const favicon = document.createElement('link');
    favicon.rel = 'icon';
    favicon.href = 'favicon.ico';
    const head = document.querySelector('head');
    head.appendChild(favicon);

});
