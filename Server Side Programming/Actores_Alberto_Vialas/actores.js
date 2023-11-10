// actors.js

// Datos de actores ficticios
const actorsData = [
    { id: 1, name: "John Doe", age: 35 },
    { id: 2, name: "Jane Smith", age: 28 },
    { id: 3, name: "Bob Johnson", age: 45 },
];

// Función para mostrar la lista de actores
function showActorList() {
    const actorList = document.getElementById('actor-list');
    actorsData.forEach(actor => {
        const actorItem = document.createElement('li');
        actorItem.innerHTML = `<a href="detalles.html?id=${actor.id}">${actor.name}</a>`;
        actorList.appendChild(actorItem);
    });
}

// Llama a la función para mostrar la lista de actores al cargar la página
window.onload = showActorList;
