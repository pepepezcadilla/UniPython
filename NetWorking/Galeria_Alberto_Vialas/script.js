// JS para generar el enlace de descarga y mostrar imágenes en un modal
document.getElementById("contactForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const exposicionFavorita = document.getElementById("exposicionFavorita").value;

    // Aquí puedes generar el enlace personalizado como desees
    const link = `https://tupaginaweb.com/entradas?nombre=${nombre}&exposicion=${exposicionFavorita}`;

    const entradasDiv = document.getElementById("entradas");
    entradasDiv.innerHTML = `<p>Descarga tus entradas <a href="${link}" target="_blank">aquí</a></p>`;
});

// JS para mostrar imágenes en un modal y centrarlas
document.querySelectorAll(".artwork img").forEach((img, index) => {
    img.addEventListener("click", () => {
        const modal = document.createElement("div");
        modal.className = "modal";
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close-modal">&times;</span>
                <img src="${img.src}" alt="Imagen en modal">
            </div>
        `;
        document.body.appendChild(modal);

        // Cierra el modal al hacer clic en la "X" (botón de cierre)
        modal.querySelector(".close-modal").addEventListener("click", () => {
            modal.remove();
        });
    });
});
