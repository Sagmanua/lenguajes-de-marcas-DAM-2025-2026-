# Indroduccion brece y contexalizacion
En esta actividad se aplica el sistema de cuadrícula para diseñar un layout básico que incluye encabezado, menú de navegación, contenido principal y pie de página, publicando posteriormente el proyecto en GitHub Pages para su visualización en línea.El diseño web actual busca crear interfaces organizadas y adaptables. Para ello, CSS ofrece herramientas como Grid Layout, que permite distribuir elementos en filas y columnas de manera sencilla, logrando una estructura clara y visualmente equilibrada.

# Desarrollo técnico correcto y preciso
Publica la página: Ve a la configuración de tu repositorio en GitHub, navega hasta la pestaña "Pages", y activa la opción para publicar desde la rama main. Espera unos minutos y accede a tu página web en https://sagmanua.github.io/Webasirwork-2023-/.

Prueba y ajusta: Abre tu página en diferentes dispositivos y navegadores para asegurarte de que el diseño se adapta correctamente. Ajusta los estilos según sea necesario.

### Al primero creo una nuevo  repositorio GitHub. Sigo los pasos descritos en el archivo Cómo publicar en GitHub Pages.md para crear un nuevo repositorio en GitHub.

### Creo una structura de este git hub 
```
/Webasirwork-2023-
    index.html
    styles.css
```

## Html 
### Despues de crear una gile `index.html` voy a hacer una pagina
### Código básico para una estructura de documento HTML
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
## CSS 
### Body 
#### `grid-template-columns: 1fr 3fr`la columna del nav es más estrecha y la del main es más ancha.
#### `gap: 20px`  espacio entre las áreas.
#### `min-height: 100vh` ocupa todo el alto de la pantalla.
#### `margin: 0`  sin márgenes en el body.
body {
    display: grid;
    grid-template-areas:
        "header header"
        "nav main"
        "footer footer";
    grid-template-columns: 1fr 3fr;
    gap: 20px;
    min-height: 100vh;
    margin: 0;
}
### En `header`,`nav`,`main`,`footer`
#### `grid-area` sirve para asignar un elemento a una zona del grid definida con
#### `background-color` para cambiar color del fondo 
```
header {
    grid-area: header;
    background-color: #f1f1f1;
}

nav {
    grid-area: nav;
    background-color: #ddd;
}

main {
    grid-area: main;
    background-color: #fff;
}

footer {
    grid-area: footer;
    background-color: #f1f1f1;
}
```

# Codigo completa
## HTML
```
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
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
</html>
```
## CSS
```
body {
    display: grid;
    grid-template-areas:
        "header header"
        "nav main"
        "footer footer";
    grid-template-columns: 1fr 3fr;
    gap: 20px;
    min-height: 100vh;
    margin: 0;
}

header {
    grid-area: header;
    background-color: #f1f1f1;
}

nav {
    grid-area: nav;
    background-color: #ddd;
}

main {
    grid-area: main;
    background-color: #fff;
}

footer {
    grid-area: footer;
    background-color: #f1f1f1;
}
```

# 4.-Cierre/Conclusión enlazando con la unidad
El uso de CSS Grid Layout facilita la organización y distribución del contenido dentro de una página web, permitiendo crear diseños más ordenados y adaptables a diferentes pantallas. Esta actividad permitió reforzar los conceptos trabajados en la unidad relacionados con la estructura visual y la maquetación web, demostrando cómo las herramientas de CSS son esenciales para lograr interfaces claras, funcionales y coherentes con los principios del diseño web moderno.