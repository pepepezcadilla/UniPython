import React from 'https://esm.sh/react@18.2.0';
import ReactDOM from 'https://esm.sh/react-dom@18.2.0/client';
import {getJuego} from './bdd.js';

const appDomElement = document.getElementById('juego');

const root = ReactDOM.createRoot(appDomElement);
const App = () => {

    // Obtener la cadena de consulta de la URL
    const queryString = window.location.search;
    
    // Crear un objeto URLSearchParams
    const params = new URLSearchParams(queryString);

    // Obtener los valores de plataforma, consola y nombre
    const plataforma = params.get('plataforma');
    const consola = params.get('consola');
    const nombre = params.get('nombre');

    var juegoData = getJuego(plataforma, consola, nombre);
    const iframeProps = {
        src: juegoData.videoURL,
        width: "560", // Ancho deseado
        height: "315", // Alto deseado
        frameborder: "0",
        allowfullscreen: true,
      };

    if (juegoData.stock > 0) {
        juegoData.canPurchase = true;
    } else {
        juegoData.canPurchase = false;
    }

    return (
        React.createElement('div', {className: 'father'},
            React.createElement('h1', {className: 'nombre'}, juegoData.nombre),
            React.createElement('hr'),
            React.createElement('div', {className: 'wrap'},
                React.createElement('div', {className: 'left'},
                    React.createElement('img', {className: 'imagen', src: juegoData.src, alt: 'Imagen del Juego' })
                ),
                React.createElement('div', {className: 'right'},
                    React.createElement('div', {className: 'plataformas'}, 'PLATAFORMA:',
                        React.createElement('p', {className: 'consola'}, consola),
                        React.createElement('hr'),
                    ),
                    React.createElement('p', {className: 'descripcion'}, juegoData.descripcion),
                    React.createElement('p', {className: 'precio'}, `Precio: $${juegoData.precio}`),
                    React.createElement('button', {
                            className: `btn ${juegoData.canPurchase ? 'btn-primary' : 'btn-secondary'} mt-3`,
                            onClick: handleClick
                        },
                        'Comprar'),
                    React.createElement('p', null, `Unidades Disponibles: ${juegoData.stock}`)
                ),
            ),
            React.createElement('hr'),
            React.createElement('div', {className: 'iframe-container'},
                React.createElement('iframe', iframeProps)
            ),
        )
    )
};

function handleClick(){
}
root.render(App())
