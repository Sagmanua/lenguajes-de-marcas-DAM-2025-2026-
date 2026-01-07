# Indroduccion brece y contexalizacion

En este vamos a empesar trabajar y aprender los basicos de Javasript  
Aprenderemos cómo obtener la fecha actual y cómo crear funciones que devuelvan valores.Estos conceptos son fundamentales para manejar datos y automatizar procesos en programación web.

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
### Esribo `<script>` que es contiene el JavaSript codigo dentro de etiqutas 
```
let hoy = new Date();
console.log(hoy);
```
### Aqui declara una variable `hoy` con let que da valor de Date y luego imprime en console

```
function diHola (nombre,edad){
    return "Hola, " + nombre + " tienes " + edad + " años, ¿como estás?";
}
```
### Agui creao una funvion con nombre `diHola` con variable `edad` `nombre` dentro de este funcion hace una return con nobre que yo voy a dar este funcion 

```
document.write(diHola("Jose Vicente", 47));
```
### Aqui imprimir en la pantala de broweser funcion de `diHola` con la values `nombre = Jose Visente` y `edad= 47` 

# Codigo completa
```
<!DOCTYPE html>
<html>
<head>

</head>
<body>
    <script>
        let hoy = new Date();
        console.log(hoy);

        function diHola (nombre,edad){
            return "Hola, " + nombre + " tienes " + edad + " años, ¿como estás?";
        }
        document.write(diHola("Jose Vicente", 47));

    </script>
</body>
</html>
```

# 4.-Cierre/Conclusión enlazando con la unidad

Con esta práctica se refuerzan los conceptos de manipulación de fechas y creación de funciones con retorno, herramientas esenciales para programar en JavaScript. Aprender a obtener la fecha actual y a generar mensajes dinámicos con funciones permite construir aplicaciones más interactivas y personalizadas