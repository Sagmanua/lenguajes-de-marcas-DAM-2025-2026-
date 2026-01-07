# Indroduccion brece y contexalizacion

En este vamos a empesar trabajar y aprender los basicos de Javasript  
Aprenderemos cómo trabajar con  contenido HTML dinámicamente .Estos conceptos son fundamentales para manejar datos y automatizar procesos en programación web.




# Desarrollo técnico correcto y preciso
## Structure de este ejersisio

002-Selección y acceso a elementos/
├─ explicacion.md
├─ 001-lectura.html
├─ 003-escribir.html 
└─ 004-microblog.html

## HTML
## Igual por 3 diferente html file 
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

## Explicar cada file por 1 
## 001-lectura.html 
### Dentro de `<sript>` escribo este codigo en la JS
```
<script>
    const elemento = document.querySelector("p");
    document.write(elemento.textContent);  
</script>
```


### Create `contenedor` con contenido `p` para hacer etiqutas `<p>`
```
const elemento = document.querySelector("p");
```

### Este linea `elemento.textContent` en la HTML file
```
document.write(elemento.textContent);  
```

## 004-microblog.html
### Dentro de `<sript>` escribo este codigo en la JS
### Create `<div>` dinamicas con contenidos que declaramos en `articulos`y hace contenido con `<p>`

```
<script>
    document.querySelector("div").innerHTML = "<p>Contenido nuevo</p>";
</script>
```
## 003-escribir.html 
### Dentro de `<sript>` escribo este codigo en la JS
```
const articulos = ["Primer artículo", "Segundo artículo", "Tercer artículo"];
const contenedor = document.querySelector("main");
for (let i = 0; i < articulos.length; i++) {
  document.querySelector("div").innerHTML = "<p>Contenido nuevo</p>";
}
```

### Create `articulos` array con constante 
```
const articulos = ["Primer artículo", "Segundo artículo", "Tercer artículo"];
```

### Create `contenedor` con contenido `main` para hacer etiqutas `<main>`
```
const contenedor = document.querySelector("main");
```


### Create `for` para hacer 3 `<div>` dinamicas con contenidos que declaramos en `articulos`y hace contenido con `<p>`
```
for (let i = 0; i < articulos.length; i++) {
  document.querySelector("div").innerHTML = "<p>Contenido nuevo</p>";
}
```


# Codigo completa
002-Selección y acceso a elementos/
├─ explicacion.md
├─ 001-lectura.html
├─ 003-escribir.html 
└─ 004-microblog.html
## 001-lectura.html
```
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Escribir contenido dinámico</title>
</head>
<body>

<div></div>

<script>
    const elemento = document.querySelector("p");
    document.write(elemento.textContent);  
</script>

</body>
</html>
```
## 003-escribir.html 
```
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Escribir contenido dinámico</title>
</head>
<body>

<script>
const articulos = ["Primer artículo", "Segundo artículo", "Tercer artículo"];
const contenedor = document.querySelector("main");
for (let i = 0; i < articulos.length; i++) {
  document.querySelector("div").innerHTML = "<p>Contenido nuevo</p>";
}
</script>

</body>
</html>
```

## 004-microblog.html
```
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Escribir contenido dinámico</title>
</head>
<body>

<div></div>

<script>
    document.querySelector("div").innerHTML = "<p>Contenido nuevo</p>";
</script>

</body>
</html>
```

# 4.-Cierre/Conclusión enlazando con la unidad

Con esta práctica se refuerzan los conceptos de manipulación cómo trabajar con  contenido HTML dinámicamente para programar en JavaScript.  