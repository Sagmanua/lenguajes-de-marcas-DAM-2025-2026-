# Indroduccion brece y contexalizacion

El manejo de errores en estructuras de datos es esencial para asegurar que los programas funcionen de manera confiable y segura. Permite detectar y corregir fallos al insertar, eliminar o acceder a elementos, evitando pérdidas de datos y comportamientos inesperados. Además, facilita la depuración y mejora la calidad del código, asegurando un aprendizaje más efectivo de cómo manipular correctamente los datos.


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
¡Excelente! Siguiendo con tu estilo, aquí tienes la explicación paso a paso para eliminar un elemento de la pantalla al hacer clic.

### 005-eliminar elemento.html
```
<script>
    const boton = document.getElementById("eliminar");
    const elemento = document.getElementById("elemento");

    boton.addEventListener("click", () => {
        elemento.remove();
    });
</script>
```
### Selecciona el botón y el elemento a borrar Primero identifico los dos protagonistas: el botón que tiene la acción y el elemento que quiero que desaparezca.


const boton = document.getElementById("eliminar");
const elemento = document.getElementById("elemento");

### Escucha el evento de "click"
```
boton.addEventListener("click", () => { ... });
```
### Elimina el elemento de la pantalla

```
elemento.remove();
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
### Inicia el primer temporizador
```
let temporizador = setTimeout("bucle()",1000);
```
### Crea la función bucle para mover al `jugador` en valor de `jugador` es random 
```
document.querySelector("#jugador").style.left = Math.random()*500+"px"
document.querySelector("#jugador").style.top = Math.random()*500+"px"
```
### Limpia el temporizador viejo Uso clearTimeout para borrar el rastro del temporizador anterior
```
clearTimeout(temporizador)
```
Llama a la función de nuevo que Crea el bucle
```
temporizador = setTimeout("bucle()",1000);
```
### 007-minijuego.html
```
<script>
    let tabla = document.querySelector("tbody");

    for (let i = 0; i < 20; i++) {
        let fila = document.createElement("tr");
        fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>";
        
        fila.addEventListener("click", function() {
            this.remove();
        });

        tabla.appendChild(fila);
    }
</script>
```
### Seleccionamos el <tbody>, no la tabla directamente
```
let tabla = document.querySelector("tbody");
```
### crear tabla de wo valores uso `for`.  
```
    for (let i = 0; i < 20; i++) {
        let fila = document.createElement("tr");
        fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>";
```

### Añadimos un evento para eliminar la fila al hacer click
```
fila.addEventListener("click", function() {
    this.remove();
```
# Codigo completa
Project/
├─ explicacion.md
├─ 001-Primero creo un elemento.html
├─ 002-eliminamos el elemento.html
├─ 007-minijuego.html
└─ 004-click para eliminar.html
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
</scri
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
### 007-minijuego.html
```
<script>
    let tabla = document.querySelector("tbody");

    for (let i = 0; i < 20; i++) {
        let fila = document.createElement("tr");
        fila.innerHTML = "<td>Prueba</td><td>Prueba</td><td>Prueba</td>";
        
        fila.addEventListener("click", function() {
            this.remove();
        });

        tabla.appendChild(fila);
    }
</script>
```

# 4.-Cierre/Conclusión enlazando con la unidad

Al completar estos ejercicios, asegúrate de entender cómo seleccionar elementos, crear eventos de clic, manipular el DOM y añadir retardo en la ejecución del código JavaScript. Esto te ayudará a dominar los conceptos de eliminación de elementos en documentos web y a aplicarlos prácticamente en diferentes contextos