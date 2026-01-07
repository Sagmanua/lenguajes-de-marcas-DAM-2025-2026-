# Indroduccion brece y contexalizacion




# Desarrollo técnico correcto y preciso
##

Project/
├─ explicacion.md
├─ 001-Primero creo un elemento.html
├─ 002-eliminamos el elemento.html
├─ 007-minijuego.html
└─ 004-click para eliminar.html
## HTML
### Despues de crear una gile `index.html` voy a hacer una pagina
### Código básico para una estructura de do
```
<!doctype html>
<html lang="es">
  <head>
    <!-- Añade tu contenido aquí -->
  </head>
  <body>
    <!-- Añade tu contenido aquí -->
  </body>
</html>
```
### Esribo `head` en que guardo configuraciones y enlaces necesarios para que la página funcione y se vea bien, pero no muestra contenido en la pantalla.
```
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
```
### Esribo `<body>` que es contiene todo lo que se muestra en la pantalla: encabezado, menú, contenido principal y pie de página
```
<body>
    <header>Encabezado</header>
    <nav>Menú Navegación</nav>
    <main>
        <section class="item">Sección 1</section>
        <section class="item">Sección 2</section>
        <section class="item">Sección 3</section>
    </main>
    <footer>Pie de página</footer>
</body>
```
### Esribo `<script>` que es contiene el JavaSript codigo dentro de etiqutas 
```
let hoy = new Date();
console.log(hoy);
```
## Explicar cada file por 1 
### 001-Primero creo un elemento.html
```
    <script>
        const contenedor = document.getElementById("contenedor");
         const nuevoElemento = document.createElement("p");
        nuevoElemento.textContent = "Este elemento fue creado con JavaScript";
        contenedor.appendChild(nuevoElemento);
    </script>
```
### 002-eliminamos el elemento.html
```
    <script>
        const boton = document.getElementById("eliminar");
        const elemento = document.getElementById("elemento");

        boton.addEventListener("click", () => {
            elemento.remove();
        });
    </script>
```
### 007-minijuego.html
```
    <script>
        // Seleccionamos el <tbody>, no la tabla directamente
        let tabla = document.querySelector("tbody");

        for (let i = 0; i < 20; i++) {
            let fila = document.createElement("tr");
            fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>";
            
            // Añadimos un evento para eliminar la fila al hacer click
            fila.addEventListener("click", function() {
                this.remove();
            });

            tabla.appendChild(fila);
        }
    </script>
```
### 004-click para eliminar.html
```
   	<script>
      let temporizador = setTimeout("bucle()",1000);	
      
      function bucle(){
      	document.querySelector("#jugador").style.left = Math.random()*500+"px"
        document.querySelector("#jugador").style.top = Math.random()*500+"px"
        clearTimeout(temporizador) // Elimino temporizador para no acumular
        temporizador = setTimeout("bucle()",1000); // Llamo a bucle de nuevo
      }
      
    </script>
```
# Codigo completa
```

```

# 4.-Cierre/Conclusión enlazando con la unidad

