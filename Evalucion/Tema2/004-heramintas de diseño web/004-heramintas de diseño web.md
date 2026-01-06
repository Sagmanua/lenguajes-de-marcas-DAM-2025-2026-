```
<!-- 
    004-Herramientas de diseño web
    (c) Bogdan Sydorenko
    
    Que hago:
    1.Crear un structura basica
    2.Identificar el Bloque
    3.Modificar el Contenido
    4.Mejorar la Apariencia
    5.Incluir Metadatos


    
-->
<!doctype html>
<html lang="es">
 <head>
  <meta charset="UTF-8">
  <meta name="description" content="Pagina sobre mi">
  <meta name="keywords" content="HTML, yo,mi pagina, ejemplo">
  <meta name="author" content="Bohdan Sydorenko">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi primer sitio web</title>
  <style>
    body{
      background-color: blanchedalmond;
      font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
      margin: 20px;

    }
    body p {
      color: chocolate;
    }
    body h1{
      color: brown;
    }
    .bloque {
    margin: 20px;
    padding: 10px;
    background-color: wheat;
    }

    #desarrollo img {
      width: 100px;
      height: auto;
      display: block;
      margin-bottom: 10px;
    }
    #desarrollo p {
      color: aquamarine;
    }
</style>
</head>
  <body>
  <h1>Bienvenido a mi sitio web</h1>
  <p>Este es un párrafo de texto.</p>
  <main>
    <section id="desarrollo">
    <h3>Desarrollo</h3>
    <div class="bloque">
        <img src="descarga.jfif" alt="Texto alternativo">
        <p>Soy un desarrollador con experiencia en varios lenguajes de programación y frameworks. Mi objetivo es crear soluciones innovadoras y eficientes.</p>
    </div>
</section>


  </main>
</body>
</html>
```

##1.-Indroduccion brece y contexalizacion
---
En este actividad voy a trabar con seccion en HTML. Voy a estudiar como se funciona para que sirve.Para indentificar el bloque uasamos id="(nombre de bloque)".Por  este puedo usar este un CSS llamado el #(nombre de bloque).Tambien puedo anadir texto y imagen en este bloque para hacer mejor



##2.-Desarrollo técnico correcto y preciso
---
1.Crear un structura basica para trabajar luego con esto 
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
2.Identificar el Bloque desarrollo que luego pùede trabar espisica con este bloque con CSS JavaSript etc.
```
 <section id="desarrollo">
    <h3>Desarrollo</h3>
</section>


3.Modificar el Contenido para saber los dotos que vamos a trabajar 
<div class="bloque">
        <img src="descarga.jfif" alt="Texto alternativo">
        <p>Soy un desarrollador con experiencia en varios lenguajes de programación y frameworks. Mi objetivo es crear soluciones innovadoras y eficientes.</p>
</div>


```
4.Mejorar la Apariencia con css. Usa CSS internos para mejorar visualmente los pagina web.Trabajo con body y .bloque y seccion #desarrollo
```
  <style>
    body{
      background-color: blanchedalmond;
      font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
      margin: 20px;

    }
    body p {
      color: chocolate;
    }
    body h1{
      color: brown;
    }
    .bloque {
    margin: 20px;
    padding: 10px;
    background-color: wheat;
    }

    #desarrollo img {
      width: 100px;
      height: auto;
      display: block;
      margin-bottom: 10px;
    }
    #desarrollo p {
      color: aquamarine;
    }
</style>
```
5.Incluir Metadatos.Proporciona información sobre una página web, lo que ayuda a los navegadores, motores de búsqueda y plataformas de redes sociales a comprender su contenido.
```
<meta charset="UTF-8">
<meta name="description" content="Pagina sobre mi">
<meta name="keywords" content="HTML, yo,mi pagina, ejemplo">
<meta name="author" content="Bohdan Sydorenko">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

```


##-3.-Aplicacion practica
---
```
<!doctype html>
<html lang="es">
 <head>
  <meta charset="UTF-8">
  <meta name="description" content="Pagina sobre mi">
  <meta name="keywords" content="HTML, yo,mi pagina, ejemplo">
  <meta name="author" content="Bohdan Sydorenko">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi primer sitio web</title>
  <style>
    body{
      background-color: blanchedalmond;
      font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
      margin: 20px;

    }
    body p {
      color: chocolate;
    }
    body h1{
      color: brown;
    }
    .bloque {
    margin: 20px;
    padding: 10px;
    background-color: wheat;
    }

    #desarrollo img {
      width: 100px;
      height: auto;
      display: block;
      margin-bottom: 10px;
    }
    #desarrollo p {
      color: aquamarine;
    }
</style>
</head>
  <body>
  <h1>Bienvenido a mi sitio web</h1>
  <p>Este es un párrafo de texto.</p>
  <main>
    <section id="desarrollo">
    <h3>Desarrollo</h3>
    <div class="bloque">
        <img src="descarga.jfif" alt="Texto alternativo">
        <p>Soy un desarrollador con experiencia en varios lenguajes de programación y frameworks. Mi objetivo es crear soluciones innovadoras y eficientes.</p>
    </div>
</section>


  </main>
</body>
</html>
```

##4.-Cierre/Conclusión enlazando con la unidad
---
Esta actividad me permitió comprender cómo la correcta estructuración y semántica del HTML impacta directamente en la claridad y accesibilidad de un sitio web. Al identificar el bloque de desarrollo y modificar su contenido con etiquetas adecuadas, así como mejorar su presentación mediante CSS y agregar metadatos, reforcé la importancia de organizar la información de manera lógica y visualmente atractiva.