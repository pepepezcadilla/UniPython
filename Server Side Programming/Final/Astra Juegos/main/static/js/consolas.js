carrito=new Array()



function comprar(objeto){
    swal({
      title: "Añadido correctamente",
      text: "La consola se añadió correctamente al carrito",
      icon: "success",
      button: "Volver",
    });

    carrito.push(objeto)
    console.log(carrito)
}

function sesion(){
    swal({
      title: "Bienvenido",
      text: "Iniciaste sesión correctamente",
      icon: "success",
      button: "Volver",
    });
}

function comprarconsola(consola){
    modal=document.getElementById("myModal");
    span=document.getElementById("cosoventa");
    while (span.firstChild) {
      span.removeChild(span.firstChild);
    }
    imagen=document.createElement("img");
    imagen.src=`src/imagenes/consolas/${consola}.jpg`;
    if (screen.width<1115){
        imagen.width=screen.width/1.65}
    span.appendChild(imagen);
    descripcion=document.createElement("h1")
    switch (consola){
        case "play4":
            precio=150
            break
        case "play5":
            precio=500
            break
        case "xbox1":
            precio=100
            break
        case "wiiu":
            precio=150
            break
        case "nintendo3ds":
            precio=100
            break
        case "nintendoswitch":
            precio=300
            break
    }
    aux=document.createTextNode(`Precio:${precio}€`)
    descripcion.appendChild(aux)
    span.appendChild(descripcion)

    carro=document.createElement("button")
    carro.id="boton"
    aux=document.createTextNode("Comprar")
    carro.appendChild(aux)
    span.appendChild(carro)
    switch (consola){
        case "play4":
            document.getElementById("boton").setAttribute("onclick","comprar('PlayStation 4')");
            break
        case "play5":
            document.getElementById("boton").setAttribute("onclick","comprar('PlayStation 5')");
            break
        case "xbox1":
            document.getElementById("boton").setAttribute("onclick","comprar('Xbox 1')");
            break
        case "wiiu":
            document.getElementById("boton").setAttribute("onclick","comprar('Wii U')");
            break
        case "nintendo3ds":
            document.getElementById("boton").setAttribute("onclick","comprar('Nintendo 3ds')");
            break
        case "nintendoswitch":
            document.getElementById("boton").setAttribute("onclick","comprar('Nintendo Switch')");
            break
    }


    modal.style.display="block";

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

}

function perfil(){
    modal=document.getElementById("myModal");
    span=document.getElementById("cosoventa");
    while (span.firstChild) {
      span.removeChild(span.firstChild);
    }
    lista=document.createElement("ul");
    nombrelista=document.createElement("li");
    label=document.createElement("label");
    label.for="name"
    nombrelista.appendChild(label)
    inputn=document.createElement("input")
    inputn.type=="text"
    inputn.name="nombre"
    inputn.placeholder="Nombre de usuario"
    inputn.id="name"
    nombrelista.appendChild(inputn)
    lista.appendChild(nombrelista)
    label.for="contrasena"
    contralista=document.createElement("li");
    input=document.createElement("input")
    input.type=="text"
    input.name="contrasena"
    input.placeholder="Contraseña"
    input.id="contrasena"
    contralista.appendChild(input)
    lista.appendChild(contralista)
    span.appendChild(lista)

    enviar=document.createElement("button")
    aux=document.createTextNode("Iniciar sesión")
    enviar.appendChild(aux)
    enviar.id="iniciosesion"
    span.appendChild(enviar)


    modal.style.display="block";

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    document.getElementById("iniciosesion").setAttribute("onclick","sesion()")

}

function vercarro(){
    modal=document.getElementById("myModal");
    span=document.getElementById("cosoventa");
    while (span.firstChild) {
      span.removeChild(span.firstChild);
    }

    lista=document.createElement("ul")
    fila=document.createElement("li")
    if (carrito.length==0){
        nomayuda=document.createTextNode("El carrito está vacío")
        fila.appendChild(nomayuda)
        lista.appendChild(fila)
    }else{
        for (let i=0;i<carrito.length;i++){
            nomayuda=document.createTextNode(`${carrito[i]}`)
            fila.appendChild(nomayuda)
            lista.appendChild(fila)
            fila=document.createElement("li")
        }
    }
    span.appendChild(lista)
    modal.style.display="block";

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

