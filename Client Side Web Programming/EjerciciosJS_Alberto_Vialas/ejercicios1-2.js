function calcularTiempo(event) {
    event.preventDefault(); // Prevenir el envío predeterminado del formulario
    var aux = 0
    const segundos = parseInt(document.getElementById('segundos').value);
    aux = segundos
    const horas = Math.floor(aux / 3600);
    aux %= 3600;
    const minutos = Math.floor(aux / 60);
    aux %= 60;
    const resultado = `En ${segundos} segundos hay ${horas} horas, ${minutos} minutos y ${aux} segundos.`;
    document.getElementById('resultadoTiempo').textContent = resultado;
}

function obtenerUnidadesDecenasCentenas(event) {
    event.preventDefault(); // Prevenir el envío predeterminado del formulario
    const numero = parseInt(document.getElementById('numero').value);
    const unidades = numero % 10;
    const decenas = (Math.floor(numero / 10)) % 10;
    const centenas = (Math.floor(numero / 100)) % 10;
    const resultado = `Última unidad ${unidades}, última decena ${decenas}, última centena ${centenas}.`;
    document.getElementById('resultadoNumero').textContent = resultado;
}

document.getElementById('calcularTiempoButton').addEventListener('click', calcularTiempo);
document.getElementById('calcularNumeroButton').addEventListener('click', obtenerUnidadesDecenasCentenas);
