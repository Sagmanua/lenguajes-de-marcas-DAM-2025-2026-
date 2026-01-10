# Indroduccion brece y contexalizacion
Para practicar el concepto de estilo condicional y cómo aplicarlo en JavaScript para manipular clases CSS dinámicamente, sigue estos pasos:


# Desarrollo técnico correcto y preciso
##


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
### 001-estilo en javascript.html
#### selecto etiquata `p`
```
let parrafo = document.querySelector("p"); 
```
#### añaodo de esto qtiquita color `red`
```
parrafo.style.color = "red";
```


### 002-anadir clase.html
### selecto etiquata `p`
```
let parrafo = document.querySelector("p"); 
```
#### añaod de esta etiquta class `rojo`
```
parrafo.classList.add("rojo")
``` 
### en CSS cambia color de texto a rojo
```
<style>
    .rojo{color:red;}
</style>
``` 

### 003-quitar clase.html
### 002-anadir clase.html
### selecto etiquata `p`
```
let parrafo = document.querySelector("p"); 
```
#### remove de esta etiquta class `rojo`
```
parrafo.classList.remove("rojo")
``` 
#### en CSS cambia color de texto a rojo (pero text va a negro)
```
<style>
    .rojo{color:red;}
</style>
``` 


### 004-estilo condicional.html
```
let entrada = document.querySelector("input")
```
#### Selecciono la entrada
```
let entrada = document.querySelector("input")
``` 
#### creo una funcion
```
entrada.onkeyup = function()
``` 
#### Cuando despulse tecla
```
entrada.onkeyup = function(){								
``` 
####  Cojo el valor
```
let valor = this.value;									
``` 
#### Saco la lon del valor
```
let longitud = valor.length								
``` 
#### crear `if`y `else`para probar longitud de input
```
if(longitud == 9){			
```
#### Te añado la clase verde
```
this.classList.add("verde")	
``` 
#### Te quito la clase rojo
```
this.classList.remove("rojo")
``` 
#### En caso contrario
```
else
``` 
#### Te quito la clase verde
```
this.classList.remove("verde")						

``` 
#### Te añado la clase rojo
```
this.classList.add("rojo")
``` 
#### Verde clarito
```
ç.verde{background:rgb(200,255,200);} 
``` 
####  Rojo clarito
```
.rojo{background:rgb(255,200,200);} 
``` 



### 005-variables en css.html
#### CSS
##### creo una `root` donde gurda una color con nombre 
```
:root{
      	--color_primario:#ff0000;
     	}
```
##### llamo gurdado color en eqtiqutas `p` y `div`
```
p{color:var(--color_primario);}
div{color:var(--color_primario);}
```
### 006-funcion de calculo en css.html
#### CSS
##### en div cambia color de `background` a red y cambia `width` a 50% de tamaño de pagina + 100px
```
    div{width:calc(50% + 100px);background:red;}
```


# Codigo completa
Project/
├─ explicacion.md
├─ 001-estilo en javascript.html
├─ 002-anadir clase.html
├─ 003-quitar clase.html
├─ 004-estilo condicional.html
├─ 005-variables en css.html
└─ 006-funcion de calculo en css.html
### 001-estilo en javascript.html
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <p>Este es otro texto</p>
    <script>
      let parrafo = document.querySelector("p"); 
      parrafo.style.color = "red";
    </script>
  </body>
</html>
```
### 002-anadir clase.html
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .rojo{color:red;}
    </style>
  </head>
  <body>
    <p>Esto es un párrafo o parágrafo</p>
    <script>
      let parrafo = document.querySelector("p"); // Selecciono lo que sea
      parrafo.classList.add("rojo")
    </script>
  </body>
</html>
```
### 003-quitar clase.html
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .rojo{color:red;}
    </style>
  </head>
  <body>
    <p class="rojo">Esto es un párrafo o parágrafo</p>
    <script>
      let parrafo = document.querySelector("p"); // Selecciono lo que sea
      parrafo.classList.remove("rojo")
    </script>
  </body>
</html>
```
### 004-estilo condicional.html
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .rojo{background:rgb(255,200,200);} 
      .verde{background:rgb(200,255,200);} 
    </style>
  </head>
  <body>
    <p>Este es otro texto</p>
    <input class="rojo">
    <script>
      let entrada = document.querySelector("input")
      entrada.onkeyup = function(){								
      	let valor = this.value;									
        let longitud = valor.length								
        if(longitud == 9){										
        	this.classList.add("verde")							
          this.classList.remove("rojo")							
        }else{																
        	this.classList.remove("verde")						
          this.classList.add("rojo")								
        }
      }
    </script>
  </body>
</html>
```
### 005-variables en css.html
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      :root{
      	--color_primario:#ff0000;
     	}
      p{color:var(--color_primario);}
      div{color:var(--color_primario);}
    </style>
  </head>
  <body>
    <p>Este es un texto</p>
    <div>Este es otro texto</div>
  </body>
</html>
```
### 006-funcion de calculo en css.html
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      div{width:calc(50% + 100px);background:red;}
    </style>
  </head>
  <body>
    <div>Este es otro texto</div>
  </body>
</html>
```
# 4.-Cierre/Conclusión enlazando con la unidad
Al completar estos ejercicios, tendrás prácticado cómo manipular clases CSS dinámicamente con JavaScript, lo que es fundamental para crear interfaces interactivas y responsivas.
