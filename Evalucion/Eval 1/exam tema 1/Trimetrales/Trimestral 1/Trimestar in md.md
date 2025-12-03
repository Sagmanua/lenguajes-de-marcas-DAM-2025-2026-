# Indroduccion brece y contexalizacion
El presente trabajo consiste en la recreación de una plantilla de Portflolio personal Vitae utilizando HTML y CSS, con el objetivo de aplicar los conocimientos adquiridos sobre maquetación web, diseño visual y estructura semántica del código.
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
### Para primero boy crear todo la structura de portoflio personal 
### Crear en `body` `main` con todo contenido y `foter` con link a mis contactos
```
<body>
    <main></main>
    <footer></foter>
</body>
```
### Sombre mi en este bloque escribe en poco sobre mi 
```
 <div id="sobremi">
        <h1></h1>
        <h2></h2>
        <h5></h5>
        <hr>
      </div>
```
### voy a hecer arcticle que luego copiar para mis proectos
```
<section id="portfolio">
        <div id="container">

          <article class="item">
            <div id="titulo">
              <h1></h1>
              <h2></h2>
              <h5></h5>
            </div>
            <div id="descripcion">
              <p></p>
              <div id="fecha">
                <p></p>
              </div>
            </div>
            <div id="categoria">
              <p></p>
            </div>
            <div id="imagen">
              <img src="" alt="" width="200" height="200">
            </div>
            <hr>
          </article>
</section>
```
### Hago `footer` con mis contactos
```
    <footer>
      <a href=""></a>
      <a href=""></a>
      <a href=""></a>
    </footer>
```
### todo mis contactos
```
    <footer>
      <a href=""></a>
      <a href=""></a>
      <a href=""></a>
    </footer>
```
## Todo la structura de mi pagina 
```
<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
    <style>
      /* CSS remains unchanged, text removed where possible */
    </style>
  </head>
  <body>
    <main>
      <div id="sobremi">
        <h1></h1>
        <h2></h2>
        <h5></h5>
        <hr>
      </div>

      <section id="portfolio">
        <div id="container">

          <article class="item">
            <div id="titulo">
              <h1></h1>
              <h2></h2>
              <h5></h5>
            </div>
            <div id="descripcion">
              <p></p>
              <div id="fecha">
                <p></p>
              </div>
            </div>
            <div id="categoria">
              <p></p>
            </div>
            <div id="imagen">
              <img src="" alt="" width="200" height="200">
            </div>
            <hr>
          </article>

          <article class="item">
            <div id="titulo">
              <h2></h2>
              <h5></h5>
            </div>
            <div id="descripcion">
              <p></p>
              <div id="fecha">
                <p></p>
              </div>
            </div>
            <div id="categoria">
              <p></p>
            </div>
            <div id="imagen">
              <img src="" alt="" width="200" height="200">
            </div>
            <hr>
          </article>

          <article class="item">
            <div id="titulo">
              <h2></h2>
              <h5></h5>
            </div>
            <div id="descripcion">
              <p></p>
              <div id="fecha">
                <p></p>
              </div>
            </div>
            <div id="categoria">
              <p></p>
            </div>
            <div id="imagen">
              <img src="" alt="" width="200" height="200">
            </div>
            <hr>
          </article>

        </div>
      </section>

    </main>

    <footer>
      <a href=""></a>
      <a href=""></a>
      <a href=""></a>
    </footer>
  </body>
</html>
```

### ahora voy añadir contenito en este strustura
```
<!doctype html>
<html lang="es">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio</title>
  <title>Mi primer sitio web</title>
  <style>
html{
    background-color: blanchedalmond;
}
footer{
    background-color: #00bcd4; /* New cyan color */
}


footer{
padding: 20px 0; /* Add some padding for height */
text-align: center; /* Center the text */
}


footer a {
color: white;
}


body{
    width: 600px;background: wheat;margin: auto;
    display: flex;
    flex-direction: column; /* Important: Stacks the main content and footer */
}

main{
    background-color: cornsilk ;
}
footer{background-color: aquamarine;}
/* Contenedor */
#container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: stretch;
  align-content: center;
}

/* Items */
.item {
  order: 0;
  flex-grow: 0;
  flex-shrink: 1;
  flex-basis: auto;
  align-self: auto;
  grid-template-columns: auto auto auto;

  /* flex: 0 1 auto; */
}
footer{
padding: 20px 0; /* Add some padding for height */
text-align: center; /* Center the text */
}


footer a {
color: white;
}

hr{
padding-left: 10px;
}
p{
    padding-left: 20px;
            }


body{
    width: 600px;background: white;margin: auto;
    display: flex;
}


  </style>
</head>
  <body>
    <main>
        <div id="sobremi">
            <h1>Bohdan SYdorenko</h1>
            <h2>Full stack developer</h2>
            <h5>            SOBRE MÍ
                Estudiante de
                Deserolla de apllicasiones
                multi platforma.
                Me considero una persona
                responsable y ordenado.
                Buscando mi primera
                experiencia laboral.
            </h5>
            <hr style="border: 2px solid black;">

        </div>
        <section id="portfolio">
        <div id="container">
            <article class="item">
                <div id="titulo">
                    <h1>Proyecto 1</h1>
                    <h2>Full stack developer</h2>
                    <h5>Aplicación Web de Gestión de Tareas</h5>
                </div>
                <div id="descripcion">
                        <p>Aplicación web creada con React y Firebase para gestionar tareas en tiempo real, permitiendo crear, editar y eliminar entradas fácilmente.</p>
                <div id="fecha">
                </div>
                            <p>Fecha de creación: junio de 2025</p>
                </div>
                <div id="categoria ">
                        <p>Categoría: Desarrollo Web</p>
                </div>
                <div id="imagen">
                        <img src="project1.jpg" alt="Captura del proyecto 1" width="200" height="200">
                </div>
                <hr style="border: 2px solid black;">

            </article>
            <article class="item">
                <div id="titulo">
                    <h2>Proyecto 2</h2>
                    <h5>Aplicación Móvil de Fitness</h5>
                </div>
                <div id="descripcion">
                    <p>App móvil desarrollada con React Native que permite registrar rutinas de ejercicio, seguimiento de progreso y objetivos personales.</p>
                    <div id="fecha">
                        <p>Fecha de creación: septiembre de 2025</p>
                    </div>
                </div>
                <div id="categoria">
                    <p>Categoría: Desarrollo Móvil</p>
                </div>
                <div id="imagen">
                    <img src="project2.jpg" alt="Captura del proyecto 2" width="200" height="200">
                </div>
                <hr style="border: 2px solid black;">

            </article>

            <!-- Proyecto 3 -->
            <article class="item">
                <div id="titulo">
                    <h2>Proyecto 3</h2>
                    <h5>Plataforma de E-commerce</h5>
                </div>
                <div id="descripcion">
                    <p>Desarrollo de una plataforma de comercio electrónico con Node.js, Express y MongoDB, con gestión de usuarios y carrito de compras.</p>
                    <div id="fecha">
                        <p>Fecha de creación: noviembre de 2025</p>
                    </div>
                </div>
                <div id="categoria">
                    <p>Categoría: Backend / Full Stack</p>
                </div>
                <div id="imagen">
                    <img src="project3.jpg" alt="Captura del proyecto 3" width="200" height="200">
                </div>
                <hr style="border: 2px solid black;">

            </article>
            </section>
        </div>
    
    </main>
    <footer>
        <a href="https://github.com/Sagmanua">github</a>
        <a href="https://t.me/Sagmanua">Telegram</a>
        <a href="https://www.linkedin.com/in/bohdan-sydorenko-6993b1397">LinkedIN</a>
        
    </footer>
</body>
</html>
```
### crear CSS dentro de html
```
  <style>
html{
    background-color: blanchedalmond;
}
footer{
    background-color: #00bcd4; /* New cyan color */
}


footer{
padding: 20px 0; /* Add some padding for height */
text-align: center; /* Center the text */
}


footer a {
color: white;
}


body{
    width: 600px;background: wheat;margin: auto;
    display: flex;
    flex-direction: column; /* Important: Stacks the main content and footer */
}

main{
    background-color: cornsilk ;
}
footer{background-color: aquamarine;}
/* Contenedor */
#container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: stretch;
  align-content: center;
}

/* Items */
.item {
  order: 0;
  flex-grow: 0;
  flex-shrink: 1;
  flex-basis: auto;
  align-self: auto;
  grid-template-columns: auto auto auto;

  /* flex: 0 1 auto; */
}
footer{
padding: 20px 0; /* Add some padding for height */
text-align: center; /* Center the text */
}


footer a {
color: white;
}

hr{
padding-left: 10px;
}
p{
    padding-left: 20px;
            }


body{
    width: 600px;background: white;margin: auto;
    display: flex;
}


  </style>
```
# Codigo completa
## Html
```
<!doctype html>
<html lang="es">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Portafolio</title>
  <title>Mi primer sitio web</title>
  <style>
html{
    background-color: blanchedalmond;
}
footer{
    background-color: #00bcd4; /* New cyan color */
}


footer{
padding: 20px 0; /* Add some padding for height */
text-align: center; /* Center the text */
}


footer a {
color: white;
}


body{
    width: 600px;background: wheat;margin: auto;
    display: flex;
    flex-direction: column; /* Important: Stacks the main content and footer */
}

main{
    background-color: cornsilk ;
}
footer{background-color: aquamarine;}
/* Contenedor */
#container {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: stretch;
  align-content: center;
}

/* Items */
.item {
  order: 0;
  flex-grow: 0;
  flex-shrink: 1;
  flex-basis: auto;
  align-self: auto;
  grid-template-columns: auto auto auto;

  /* flex: 0 1 auto; */
}
footer{
padding: 20px 0; /* Add some padding for height */
text-align: center; /* Center the text */
}


footer a {
color: white;
}

hr{
padding-left: 10px;
}
p{
    padding-left: 20px;
            }


body{
    width: 600px;background: white;margin: auto;
    display: flex;
}


  </style>
</head>
  <body>
    <main>
        <div id="sobremi">
            <h1>Bohdan SYdorenko</h1>
            <h2>Full stack developer</h2>
            <h5>            SOBRE MÍ
                Estudiante de
                Deserolla de apllicasiones
                multi platforma.
                Me considero una persona
                responsable y ordenado.
                Buscando mi primera
                experiencia laboral.
            </h5>
            <hr style="border: 2px solid black;">

        </div>
        <section id="portfolio">
        <div id="container">
            <article class="item">
                <div id="titulo">
                    <h1>Proyecto 1</h1>
                    <h2>Full stack developer</h2>
                    <h5>Aplicación Web de Gestión de Tareas</h5>
                </div>
                <div id="descripcion">
                        <p>Aplicación web creada con React y Firebase para gestionar tareas en tiempo real, permitiendo crear, editar y eliminar entradas fácilmente.</p>
                <div id="fecha">
                </div>
                            <p>Fecha de creación: junio de 2025</p>
                </div>
                <div id="categoria ">
                        <p>Categoría: Desarrollo Web</p>
                </div>
                <div id="imagen">
                        <img src="project1.jpg" alt="Captura del proyecto 1" width="200" height="200">
                </div>
                <hr style="border: 2px solid black;">

            </article>
            <article class="item">
                <div id="titulo">
                    <h2>Proyecto 2</h2>
                    <h5>Aplicación Móvil de Fitness</h5>
                </div>
                <div id="descripcion">
                    <p>App móvil desarrollada con React Native que permite registrar rutinas de ejercicio, seguimiento de progreso y objetivos personales.</p>
                    <div id="fecha">
                        <p>Fecha de creación: septiembre de 2025</p>
                    </div>
                </div>
                <div id="categoria">
                    <p>Categoría: Desarrollo Móvil</p>
                </div>
                <div id="imagen">
                    <img src="project2.jpg" alt="Captura del proyecto 2" width="200" height="200">
                </div>
                <hr style="border: 2px solid black;">

            </article>

            <!-- Proyecto 3 -->
            <article class="item">
                <div id="titulo">
                    <h2>Proyecto 3</h2>
                    <h5>Plataforma de E-commerce</h5>
                </div>
                <div id="descripcion">
                    <p>Desarrollo de una plataforma de comercio electrónico con Node.js, Express y MongoDB, con gestión de usuarios y carrito de compras.</p>
                    <div id="fecha">
                        <p>Fecha de creación: noviembre de 2025</p>
                    </div>
                </div>
                <div id="categoria">
                    <p>Categoría: Backend / Full Stack</p>
                </div>
                <div id="imagen">
                    <img src="project3.jpg" alt="Captura del proyecto 3" width="200" height="200">
                </div>
                <hr style="border: 2px solid black;">

            </article>
            </section>
        </div>
    
    </main>
    <footer>
        <a href="https://github.com/Sagmanua">github</a>
        <a href="https://t.me/Sagmanua">Telegram</a>
        <a href="https://www.linkedin.com/in/bohdan-sydorenko-6993b1397">LinkedIN</a>
        
    </footer>
</body>
</html>
```

# 4.-Cierre/Conclusión enlazando con la unidad
La elaboración de esta plantilla de currículum en HTML y CSS ha permitido poner en práctica los contenidos vistos en la unidad sobre estructuración y diseño de páginas web.
A través de esta actividad, he podido reforzar conceptos como el uso adecuado de etiquetas semánticas, la organización del contenido mediante hojas de estilo en cascada y la importancia de la presentación visual en la comunicación profesional.
Además, la personalización del CV con mis propios datos ha sido un ejercicio útil para conectar la teoría con una aplicación real, mostrando cómo el desarrollo web puede emplearse para crear herramientas funcionales y representativas en el ámbito laboral.
