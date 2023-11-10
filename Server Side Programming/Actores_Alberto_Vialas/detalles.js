// actor-details.js

const urlParams = new URLSearchParams(window.location.search);
const actorId = urlParams.get('id');

// Datos de actores ficticios (igual que en actors.js, puedes crear una lista de actores ficticios)
const actorsData = [
    { id: 1, name: "John Doe", age: 35 },
    { id: 2, name: "Jane Smith", age: 28 },
    { id: 3, name: "Bob Johnson", age: 45 },
];

// Función para obtener los detalles de un actor ficticio
function getActorDetails(id) {
    return actorsData.find(actor => actor.id == id);
}

// Función para mostrar los detalles de un actor y sus películas
function showActorDetails() {
    const actorDetails = document.getElementById('actor-details');
    const actor = getActorDetails(actorId);

    if (actor) {
        actorDetails.innerHTML = `
            <h2>${actor.name}</h2>
            <p>Edad: ${actor.age}</p>
            <!-- Otros detalles del actor -->
        `;
    } else {
        actorDetails.innerHTML = '<p>Actor no encontrado.</p>';
    }
}

// Llama a la función para mostrar los detalles del actor al cargar la página
window.onload = showActorDetails;
