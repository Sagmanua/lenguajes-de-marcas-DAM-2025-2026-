# Indroduccion brece y contexalizacion
En esta unidad se aborda la creación y manipulación dinámica de elementos HTML mediante JavaScript, así como el consumo de datos externos en formato JSON para generar interfaces interactivas y visualmente estructuradas. El objetivo principal es que el estudiante pueda comprender cómo integrar HTML, CSS y JavaScript de manera que se logre construir interfaces dinámicas, desde la generación de botones hasta la creación de tablas a partir de archivos JSON. Este conocimiento es fundamental para el desarrollo de aplicaciones web modernas donde la interacción y la actualización de datos en tiempo real son esenciales.



# Desarrollo técnico correcto y preciso
##

003-Creación y modificación de elementos/
├─ explicacion.md
├─ 002-crear varios botones.html
├─ 005-consumo json.html
├─ 007-recuperamos json tabla.html
├─ 008-creamos tabla.html
├─ 009-estilo en la tabla.html 
├─ 010-creo interfaz base.html
├─ botones.json
└─ tabla.json

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
###  002-crear varios botones.html

```
<script>
    let botones = ['clientes','productos','pedidos'];
    let contenedor = document.querySelector("nav");
    botones.forEach(function(texto_boton){
        let boton = document.createElement("button");
        boton.textContent = texto_boton;
        contenedor.appendChild(boton);
    })
</script>
```
#### Delcara una array de `botones`
```
let botones = ['clientes','productos','pedidos'];
```

#### declara `<nav>` en la dinamica contenido  
```
let contenedor = document.querySelector("nav");
```

#### Hoy boy a crear botones y mustra en la pantalla. Creo una funcion en que declara  `boton` que contiene element `<button>` luego en este `boton` anadir la text de array `botones` en contenido de `<button>`
```
botones.forEach(function(texto_boton){
    let boton = document.createElement("button");
    boton.textContent = texto_boton;
    contenedor.appendChild(boton);
})
```


###  005-consumo json.html
```
<script>
    fetch("botones.json")
    .then(function(respuesta){
        return respuesta.json(); // La resp viene en JSON
    })
    .then(function(datos){
        console.log(datos);
    })
</script>
```

#### la primero gue hace es load a json file `botones.json` que contiene 
```
[
   	"clientes",
	"pedidos",
    "productos",
    "stock",
    "empleados",
    "estanterias"
]
```

### uso este fetch enviar HTTP-Solicitudes
```
fetch("botones.json")
```
### ahora conventir HTTP en la datos que con que puede trabajar 
```
.then(function(respuesta){
    return respuesta.json();
})
```

### ahora estos datos que responde de la Json imprimir en la consola 
```
.then(function(datos){
    console.log(datos);
})
```


###  007-recuperamos json tabla.html
```
<script>
    fetch("tabla.json")
    .then(function(respuesta){
        return respuesta.json(); 
    })
    .then(function(datos){
        console.log(datos);
    })
</script>
```
#### la primero gue hace es load a json file `botones.json` que contiene 
```
[
  ["id", "nombre", "email", "telefono", "direccion", "fecha_alta"],
  [1, "María López García", "maria.lopez@example.com", "+34 612 345 678", "Calle Mayor 12, 46001 Valencia", "2024-01-15"],
  [2, "Javier Martínez Ruiz", "javier.martinez@example.com", "+34 699 123 456", "Avenida del Puerto 88, 46022 Valencia", "2024-02-03"],
  [3, "Lucía Fernández Torres", "lucia.fernandez@example.com", "+34 644 987 321", "Calle Colón 5, 46004 Valencia", "2024-03-21"],
  [4, "Carlos Navarro Giménez", "carlos.navarro@example.com", "+34 622 111 222", "Plaza del Ayuntamiento 3, 46002 Valencia", "2024-04-10"],
  [5, "Elena Serrano Vidal", "elena.serrano@example.com", "+34 633 555 999", "Calle San Vicente 45, 46007 Valencia", "2024-05-02"]
]
```

### uso este fetch enviar HTTP-Solicitudes
```
fetch("tabla.json")
```
### ahora conventir HTTP en la datos que con que puede trabajar 
```
.then(function(respuesta){
    return respuesta.json();
})
```

### ahora estos datos que responde de la Json imprimir en la consola 
```
.then(function(datos){
    console.log(datos);
})
```
###  008-creamos tabla.html
```
<script>
    fetch("tabla.json")
    .then(function(respuesta){
        return respuesta.json();  
    })
    .then(function(datos){
        let contenedor = document.querySelector("body");
        let tabla = document.createElement("table");
        contenedor.appendChild(tabla); 
        datos.forEach(function(linea){
            let fila = document.createElement("tr");
            linea.forEach(function(celda){
                    let data = document.createElement("td");
                    data.textContent = celda
                    fila.appendChild(data);
            })
            tabla.appendChild(fila)
        })
    })
</script>
```
#### la primero gue hace es load a json file `botones.json` que contiene 
```
[
  ["id", "nombre", "email", "telefono", "direccion", "fecha_alta"],
  [1, "María López García", "maria.lopez@example.com", "+34 612 345 678", "Calle Mayor 12, 46001 Valencia", "2024-01-15"],
  [2, "Javier Martínez Ruiz", "javier.martinez@example.com", "+34 699 123 456", "Avenida del Puerto 88, 46022 Valencia", "2024-02-03"],
  [3, "Lucía Fernández Torres", "lucia.fernandez@example.com", "+34 644 987 321", "Calle Colón 5, 46004 Valencia", "2024-03-21"],
  [4, "Carlos Navarro Giménez", "carlos.navarro@example.com", "+34 622 111 222", "Plaza del Ayuntamiento 3, 46002 Valencia", "2024-04-10"],
  [5, "Elena Serrano Vidal", "elena.serrano@example.com", "+34 633 555 999", "Calle San Vicente 45, 46007 Valencia", "2024-05-02"]
]
```

#### uso este fetch enviar HTTP-Solicitudes
```
fetch("tabla.json")
```
#### ahora conventir HTTP en la datos que con que puede trabajar 
```
.then(function(respuesta){
    return respuesta.json();
})
```





#### declara varibles para hacer etiqetas `<body>` `<table>` 
```
let contenedor = document.querySelector("body");
let tabla = document.createElement("table");
```

#### hacer una contenador de la `<tabla>` en que luqgo añado `<tr>` `<td>`
```
contenedor.appendChild(tabla); 
```

#### informacion que carge es datos  de JSON file usamos para hacer una tabla por cada linea hace este codigo
```
datos.forEach(function(linea){
```
#### declara `<tr>`
```
let fila = document.createElement("tr");
```
#### informacion que carge de celda  de JSON file usamos para hacer una tabla por cada linea hace este codigo 
```
linea.forEach(function(celda){
```

#### declara `<td>`
```
let data = document.createElement("td");
```

#### declara que es `celda`
```
data.textContent = celda
```
#### envio a la informacion a la fila 
```
fila.appendChild(data);
```

###  009-estilo en la tabla.html 
#### HTML JS 
```
<script>
    fetch("tabla.json")
    .then(function(respuesta){
        return respuesta.json();  
    })
    .then(function(datos){
        let contenedor = document.querySelector("body");
        let tabla = document.createElement("table");
        contenedor.appendChild(tabla); 
        datos.forEach(function(linea){
            let fila = document.createElement("tr");
            linea.forEach(function(celda){
                    let data = document.createElement("td");
                    data.textContent = celda
                    fila.appendChild(data);
            })
            tabla.appendChild(fila)
        })
    })
</script>

```
#### CSS
#### la primero gue hace es load a json file `botones.json` que contiene 
```
[
  ["id", "nombre", "email", "telefono", "direccion", "fecha_alta"],
  [1, "María López García", "maria.lopez@example.com", "+34 612 345 678", "Calle Mayor 12, 46001 Valencia", "2024-01-15"],
  [2, "Javier Martínez Ruiz", "javier.martinez@example.com", "+34 699 123 456", "Avenida del Puerto 88, 46022 Valencia", "2024-02-03"],
  [3, "Lucía Fernández Torres", "lucia.fernandez@example.com", "+34 644 987 321", "Calle Colón 5, 46004 Valencia", "2024-03-21"],
  [4, "Carlos Navarro Giménez", "carlos.navarro@example.com", "+34 622 111 222", "Plaza del Ayuntamiento 3, 46002 Valencia", "2024-04-10"],
  [5, "Elena Serrano Vidal", "elena.serrano@example.com", "+34 633 555 999", "Calle San Vicente 45, 46007 Valencia", "2024-05-02"]
]
```

#### uso este fetch enviar HTTP-Solicitudes
```
fetch("tabla.json")
```
#### ahora conventir HTTP en la datos que con que puede trabajar 
```
.then(function(respuesta){
    return respuesta.json();
})
```





#### declara varibles para hacer etiqetas `<body>` `<table>` 
```
let contenedor = document.querySelector("body");
let tabla = document.createElement("table");
```

#### hacer una contenador de la `<tabla>` en que luqgo añado `<tr>` `<td>`
```
contenedor.appendChild(tabla); 
```

#### informacion que carge es datos  de JSON file usamos para hacer una tabla por cada linea hace este codigo
```
datos.forEach(function(linea){
```
#### declara `<tr>`
```
let fila = document.createElement("tr");
```
#### informacion que carge de celda  de JSON file usamos para hacer una tabla por cada linea hace este codigo 
```
linea.forEach(function(celda){
```

#### declara `<td>`
```
let data = document.createElement("td");
```

#### declara que es `celda`
```
data.textContent = celda
```
#### envio a la informacion a la fila 
```
fila.appendChild(data);
```

```
<style>
    table{border:3px solid blue;border-collapse:collapse;background:white;}
    table tr:first-child{background:blue;color:white;}
    table tr td{padding:10px;border-right:1px solid blue;}
</style>
```
#### `border` agrega un borde alrededor del elemento.
#### `border-collapse` controla si los bordes de las celdas de una tabla se muestran separados o colapsados en un solo borde.
#### `background-color` para cambiar color del fondo 
#### `color` Define el color del texto dentro del elemento.
#### `padding` Agrega espacio interno entre el contenido y el borde del elemento.
#### `border` agrega un borde alrededor del elemento.

###  010-creo interfaz base.html
```
<script>

fetch("tabla.json")
    .then(response => response.json())
    .then(datos => {
        const tabla = document.getElementById("tabla");

        if(datos.length > 0){
            const encabezado = document.createElement("tr");
            datos[0].forEach(celda => {
                const th = document.createElement("th");
                th.textContent = celda;
                encabezado.appendChild(th);
            });
            tabla.appendChild(encabezado);

            for(let i = 1; i < datos.length; i++){
                const fila = document.createElement("tr");
                datos[i].forEach(celda => {
                    const td = document.createElement("td");
                    td.textContent = celda;
                    fila.appendChild(td);
                });
                tabla.appendChild(fila);
            }
        }
    })
</script>
```

# Codigo completa
003-Creación y modificación de elementos/
├─ explicacion.md
├─ 002-crear varios botones.html
├─ 005-consumo json.html
├─ 007-recuperamos json tabla.html
├─ 008-creamos tabla.html
├─ 009-estilo en la tabla.html 
├─ 010-creo interfaz base.html
├─ botones.json
└─ tabla.json
002-crear varios botones.htm
```
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           let botones = ['clientes','productos','pedidos'];
           let contenedor = document.querySelector("nav");
           botones.forEach(function(texto_boton){
           		let boton = document.createElement("button");
           		boton.textContent = texto_boton;
           		contenedor.appendChild(boton);
           })
       </script>
   </body>
</html>
```
005-consumo json.html
```
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           // Ves y busca
           fetch("botones.json")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
           		console.log(datos);
           })
       </script>
   </body>
</html>
```
007-recuperamos json tabla.html
```
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
           // En primer lugar cargamos datos de un json
           fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json(); // La resp viene en JSON
           })
           .then(function(datos){
               console.log(datos);
           })
       </script>
   </body>
</html>
```
008-creamos tabla.html
```
<!doctype html>
<html>
   <head>
   </head>
   <body>
       <nav></nav>
       <script>
            fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json();  
           })
           .then(function(datos){
                let contenedor = document.querySelector("body");
                let tabla = document.createElement("table");
                contenedor.appendChild(tabla); 
                datos.forEach(function(linea){
                    let fila = document.createElement("tr");
                    linea.forEach(function(celda){
                    		let data = document.createElement("td");
                        	data.textContent = celda
                        	fila.appendChild(data);
                   })
                    tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>



```
009-estilo en la tabla.html
```
<!doctype html>
<html>
   <head>
       <style>
           table{border:3px solid blue;border-collapse:collapse;background:white;}
           table tr:first-child{background:blue;color:white;}
           table tr td{padding:10px;border-right:1px solid blue;}
       </style>
   </head>
   <body>
       <nav></nav>
       <script>
            fetch("tabla.json")
           .then(function(respuesta){
               return respuesta.json();  
           })
           .then(function(datos){
                let contenedor = document.querySelector("body");
                let tabla = document.createElement("table");
                contenedor.appendChild(tabla); 
                datos.forEach(function(linea){
                    let fila = document.createElement("tr");
                    linea.forEach(function(celda){
                    		let data = document.createElement("td");
                        	data.textContent = celda
                        	fila.appendChild(data);
                   })
                    tabla.appendChild(fila)
               })
           })
       </script>
   </body>
</html>



```
010-creo interfaz base.html
```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Tabla Básica</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #333;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #555;
            color: white;
        }
    </style>
</head>
<body>
    <table id="tabla"></table>

    <script>
        fetch("tabla.json")
            .then(response => response.json())
            .then(datos => {
                const tabla = document.getElementById("tabla");

                if(datos.length > 0){
                    const encabezado = document.createElement("tr");
                    datos[0].forEach(celda => {
                        const th = document.createElement("th");
                        th.textContent = celda;
                        encabezado.appendChild(th);
                    });
                    tabla.appendChild(encabezado);

                    for(let i = 1; i < datos.length; i++){
                        const fila = document.createElement("tr");
                        datos[i].forEach(celda => {
                            const td = document.createElement("td");
                            td.textContent = celda;
                            fila.appendChild(td);
                        });
                        tabla.appendChild(fila);
                    }
                }
            })
    </script>
</body>
</html>
```
botones.json
```
[
   	"clientes",
	"pedidos",
    "productos",
    "stock",
    "empleados",
    "estanterias"
]
```
tabla.json
```
[
  ["id", "nombre", "email", "telefono", "direccion", "fecha_alta"],
  [1, "María López García", "maria.lopez@example.com", "+34 612 345 678", "Calle Mayor 12, 46001 Valencia", "2024-01-15"],
  [2, "Javier Martínez Ruiz", "javier.martinez@example.com", "+34 699 123 456", "Avenida del Puerto 88, 46022 Valencia", "2024-02-03"],
  [3, "Lucía Fernández Torres", "lucia.fernandez@example.com", "+34 644 987 321", "Calle Colón 5, 46004 Valencia", "2024-03-21"],
  [4, "Carlos Navarro Giménez", "carlos.navarro@example.com", "+34 622 111 222", "Plaza del Ayuntamiento 3, 46002 Valencia", "2024-04-10"],
  [5, "Elena Serrano Vidal", "elena.serrano@example.com", "+34 633 555 999", "Calle San Vicente 45, 46007 Valencia", "2024-05-02"]
]
```

# 4.-Cierre/Conclusión enlazando con la unidad
A lo largo de esta unidad se han adquirido habilidades para crear y modificar elementos HTML de manera dinámica utilizando JavaScript, así como para consumir y manipular datos en formato JSON. Aprendimos a generar interfaces interactivas, como botones y tablas, y a aplicar estilos CSS básicos para mejorar la presentación visual. Todo esto enlaza directamente con la unidad al demostrar cómo los conocimientos de HTML, CSS y JavaScript se integran para construir aplicaciones web funcionales y dinámicas, sentando las bases para proyectos más complejos en el desarrollo frontend.
