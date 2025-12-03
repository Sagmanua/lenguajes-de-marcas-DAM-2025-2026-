# Indroduccion brece y contexalizacion

El presente trabajo consiste en la recreación de una plantilla de Currículum Vitae utilizando HTML y CSS, con el objetivo de aplicar los conocimientos adquiridos sobre maquetación web, diseño visual y estructura semántica del código.
A través de esta actividad, se busca demostrar la capacidad para construir una página web bien organizada, visualmente atractiva y completamente personalizada con mis propios datos personales, académicos y profesionales.
Este ejercicio forma parte del proceso de evaluación en la plataforma eval.jocarsa.com, siguiendo la rúbrica establecida para valorar aspectos técnicos, estéticos y de presentación del CV digital.


# Desarrollo técnico correcto y preciso
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
## CSS
### Dentor de html escibe css 
```
<style>
  body{background-color: antiquewhite;}
  body{
  text-align: center;
  }
  header,main,footer{
background-color: aquamarine;
  padding: 20px;
   width: 800px;
  margin: auto;
   text-align: center;     
   }
    main{
    display: grid;
   grid-template-columns: auto auto auto;
     gap: 20px;
     }
   </style>
```
### Body
#### `display` Define cómo se comporta un elemento en la página, es decir, cómo se muestra y cómo afecta al resto de elementos.
#### `text-align` sirve para alinear el texto dentro de un elemento.
```
<style>
  body{background-color: antiquewhite;}
  body{
  text-align: center;
  }
```
### header,main,footer
#### `background-color` para cambiar color del fondo 
#### `padding` Agrega espacio interno entre el contenido y el borde del elemento.
#### `width` Define el ancho de un elemento.
#### `margin`  sin márgenes en el body.
#### `text-align` sirve para alinear el texto dentro de un elemento.
```
  header,main,footer{
  background-color: aquamarine;
  padding: 20px;
   width: 800px;
  margin: auto;
   text-align: center;     
   }
```
### Main
#### `display` Define cómo se comporta un elemento en la página, es decir, cómo se muestra y cómo afecta al resto de elementos.
#### `gap`  espacio entre las áreas.

```
    main{
    display: grid;
    grid-template-columns: auto auto auto;
    gap: 20px;
     }
```

# Codigo completa
```
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Examen</title>
        <meta charset="utf-8">
        <style>
            body{background-color: antiquewhite;}
            body{
                text-align: center;
            }
            header,main,footer{
                background-color: aquamarine;
                padding: 20px;
                width: 800px;
                margin: auto;
                text-align: center;
            }
            main{
                display: grid;
                grid-template-columns: auto auto auto;
                gap: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Bohdan Sydorenko</h1>
        <h2>mailnose@mail.com</h2>
    </body>
    </header>
    <main>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article><article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
      
      <article>
        <p>Categoria</p>
        <h3>Titulo</h3>
        <p>Descripcion</p>
        <img src="josevicente.jpg">
      </article>
    </main>
    <footer>
      (c) Bohdan Sydorenko
    </footer>



</html>
```

# Cierre/Conclusión enlazando con la unidad

La elaboración de esta plantilla de currículum en HTML y CSS ha permitido poner en práctica los contenidos vistos en la unidad sobre estructuración y diseño de páginas web.
A través de esta actividad, he podido reforzar conceptos como el uso adecuado de etiquetas semánticas, la organización del contenido mediante hojas de estilo en cascada y la importancia de la presentación visual en la comunicación profesional.
Además, la personalización del CV con mis propios datos ha sido un ejercicio útil para conectar la teoría con una aplicación real, mostrando cómo el desarrollo web puede emplearse p