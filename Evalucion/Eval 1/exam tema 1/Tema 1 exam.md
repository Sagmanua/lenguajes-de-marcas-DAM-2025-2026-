## Indroduccion brece y contexalizacion

El presente trabajo consiste en la recreación de una plantilla de Currículum Vitae utilizando HTML y CSS, con el objetivo de aplicar los conocimientos adquiridos sobre maquetación web, diseño visual y estructura semántica del código.
A través de esta actividad, se busca demostrar la capacidad para construir una página web bien organizada, visualmente atractiva y completamente personalizada con mis propios datos personales, académicos y profesionales.
Este ejercicio forma parte del proceso de evaluación en la plataforma eval.jocarsa.com, siguiendo la rúbrica establecida para valorar aspectos técnicos, estéticos y de presentación del CV digital.


## Desarrollo técnico correcto y preciso
### En primero empezar con estructura basica de Html
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
</body>
</html>
```
### Voy añadir tiitle y meta y conectar css (en mi caso escribo css  dentro de html) dentro de `<head>`
```
<head>
    <title>Curiculum</title>
    <meta charset="utf-8">
    <style>
    </style>
</head
```
### Añodo `<section>` de CV isquirda y derecha dentro de `<body>` 
```
<body>
    <section id="izquierda_botom">
    </setion>
    <section id="derecha">
    </setion>
</body>


```
### voy a escribir estructuras de `<section>` para puede facil gurdar  con `<div>` , listas `<ul>` , si sabe tonde pone texto escribo `<p>`

#### en estructura  `<setcion id="izquierda_botom" >` tiene `<img>` tiene `<div>` contactos idiomas 

#### en estrurtuera `<section id="derecha">` tiene todo informacion sobre mis por eso esta mas completo u tiene `<div<` `experencia` `Education` `Expertise `

```
<body>
    <setcion id="izquierda_botom" >
    <!-- añado img -->
    <img src="descarga.jfif">
            <div class="contatanct"></div>
                <h3></h3>
                <ul>
                    <li>/li>
                    <li></li>
                    <li></li>
                    <li></li>
                       
                </ul>
            <h3></h3>
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
        </section>
        <section id="derecha">
           <div class="info">
           <h1></h1>
           <h2></h2>
           </div>
           <div class="Education">
           </div>
           <div class="Education">
                <H3</H3>
                <ul>
                    <li></li>
                </ul>
                <H3></H3>
           </div>
            <div class="experencia">
                <ul>
                <li> </li>
            </ul>
            </div>
           
            <div class="Expertise">
            <h3></h3>
            
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>     
                </ul>
            </div>
            </setion>
</body>


```
### Ahora voy escibir todo informcion sombre mi en estructura que hace antes
```
<body>
        <!-- Este es un comentario que no se verá en la página web -->
        <section id="izquierda_botom">
            <img src="descarga.jfif">
            <div class="contatanct"></div>
                <div class="contatanct">
                <h3>Contatanct</h3>
                <hr style="border: 2px solid black;">

                <ul>
                    <li>Número de teléfono/li>
                    <P>645573661</P>
                    <li>Email</li>
                    <p>Sidorenko.bohdan.05@gmailc.com
                    <li>Adress</li>
                    <p>Valencia Malvarosa
                    <li><a href="https://github.com/Sagmanua"  style=”text-decoration:none” >Git hub</a></li>
                    <p>Git hub con mis trabojos</p>
                    <p>https://github.com/Sagmanua</p>
                    
                </ul>
            </div>
            <div class="idiomas">
            <h3>Idiomas</h3>
            <hr style="border: 2px solid black;">

                <ul>
                    <li>Ukrainano Nativo</li>
                    <li>Ruso nativo</li>
                    <li>Espanol medio</li>
                    <li>Ingles medio</li>
                </ul>
            </div>
            

        </section>
        <p>


        </p>
        <section id="derecha">
            <div class="info">
                <h1>Bohdan SYdorenko</h1>
           <h2>Full stack developer</h2>
           <h5>            SOBRE MÍ
                Estudiante de
                Deserolla de apllicasiones
                multi platforma.
                Me considero una persona
                responsable y ordenado.
                Buscando mi primera
                experiencia laboral.</h5>
            </div>
           <div class="Education">
                <H3>UNIVERSIDADES BORCELLE</H3>
                <hr style="border: 2px solid black;">

                <ul>
                    <li>2025-actulidad</li>
                    <p>Deserolla de aplicaciones multi platforfa</p>
                </ul>
                <H3>
                    ESCUELA SECUNDARIA BORCELLE
                </H3>
            <hr style="border: 2px solid black;">

           </div>
           
            <div class="experencia">
                 <ul>
                <li>
                    <p>Volutario en Educaion Infantil
                    <p>Aydaba a organizar las fiestas para ninos y cuisaba de los ninos en ella 
                    </li>
            </ul>
            </div>
            <div class="Expertise">
            <h3>Expertise</h3>
            <hr style="border: 2px solid black;">
                <ul>
                    <li>Python</li>
                        <p>Puedo crear una calculadora, un generador de contraseñas o un web scraper</p>
                    <li>Java</li>
                        <p>Puedo escribir código limpio, ayudar a depurar y solucionar problemas, escribir pruebas unitarias y colaborar con desarrolladores senior en el desarrollo de nuevas funcionalidades y el mantenimiento.
                    <li>Mysql</li>
                        <p>Puedo crear y manipular tablas, escribir consultas SQL para la recuperación y modificación de datos, y comprender los fundamentos del diseño de bases de datos.
                    <li>Html</li>
                        <p>Sé escribir HTML. HTML es fundamental para una web. Sin saber HTML, no se pueden mostrar datos en la web.</p>
                    <li>Css</li>
                        <p>Sé cómo dar estilo a tu HTML con CSS. El estilo es muy importante en la web. Permite que el usuario perciba tu sitio web y que se sienta cómodo al usarlo.</p>
                </ul>
            </div>  
        </section>
    </body>
```
### ahora boy a +rabajar con estilos Css. 


#### `#izquierda_botom a {color: white;}` cambiar color de a de url
#### `#izquierda_botom ul {list-style-type: none;padding-left: 10px;}` borar * en la listas en `<setion id="izquierda_botom"">` 
#### padding left en `hr` , `p` `ul`
#### añado `background-color`en `izquierda_botom` , `derecha` y `body`
#### cambiar tamño de img 
#### cambiar color de texto en `izquierda_botom`
```
<style>
            #izquierda_botom a {
                color: white;
            }
            #izquierda_botom ul {
                list-style-type: none;
                padding-left: 10px;
                }
            #izquierda_botom hr{
                padding-left: 10px;
            }
            #izquierda_botom p{
                padding-left: 20px;
            }
            #derecha p{
                padding-left: 20px;
            }
            html{background-color: grey;font-family: sans-serif;font-size: 11px;}
            body{
                    width: 600px;background: white;margin: auto;
                    display: flex;
                }
            #izquierda_botom {flex:1;background-color:#333a49;padding: 20px; color: white;}
            #derecha{flex:4;padding: 20px;background-color: rgb(97, 157, 212);}
            #derecha article{display: flex;align-items: center;gap:20px}
            #dercha article img{width: 50px;height: 50px;}
        </style>
  
```

## Codigo completa
```
<!DOCTYPE html>
<html lang="es">
    <head>
        <title>Curiculum</title>
        <meta charset="utf-8">
        <style>
            /* para borar ul *  */
            #izquierda_botom a {
                color: white;
            }
            #izquierda_botom ul {
                list-style-type: none;
                padding-left: 10px;
                }
            #izquierda_botom hr{
                padding-left: 10px;
            }
            #izquierda_botom p{
                padding-left: 20px;
            }
            #derecha p{
                padding-left: 20px;
            }
            html{background-color: grey;font-family: sans-serif;font-size: 11px;}
            body{
                    width: 600px;background: white;margin: auto;
                    display: flex;
                }
            #izquierda_botom {flex:1;background-color:#333a49;padding: 20px; color: white;}
            #derecha{flex:4;padding: 20px;background-color: rgb(97, 157, 212);}
            #derecha article{display: flex;align-items: center;gap:20px}
            #dercha article img{width: 50px;height: 50px;}


        </style>
    </head>
    <body>
                    <!-- Este es un comentario que no se verá en la página web -->

        
        <section id="izquierda_botom">
            <img src="descarga.jfif">
            <div class="contatanct"></div>
                <div class="contatanct">
                <h3>Contatanct</h3>
                <hr style="border: 2px solid black;">

                <ul>
                    <li>Número de teléfono/li>
                    <P>645573661</P>
                    <li>Email</li>
                    <p>Sidorenko.bohdan.05@gmailc.com
                    <li>Adress</li>
                    <p>Valencia Malvarosa
                    <li><a href="https://github.com/Sagmanua"  style=”text-decoration:none” >Git hub</a></li>
                    <p>Git hub con mis trabojos</p>
                    <p>https://github.com/Sagmanua</p>   
                </ul>
            </div>
            <div class="idiomas">
            <h3>Idiomas</h3>
            <hr style="border: 2px solid black;">
                <ul>
                    <li>Ukrainano Nativo</li>
                    <li>Ruso nativo</li>
                    <li>Espanol medio</li>
                    <li>Ingles medio</li>
                </ul>
            </div>
        </section>
        <p>
        </p>
        <section id="derecha">
            <div class="info">
                <h1>Bohdan SYdorenko</h1>
           <h2>Full stack developer</h2>
           <h5>            SOBRE MÍ
                Estudiante de
                Deserolla de apllicasiones
                multi platforma.
                Me considero una persona
                responsable y ordenado.
                Buscando mi primera
                experiencia laboral.</h5>
            </div>

           <div class="Education">
                <H3>UNIVERSIDADES BORCELLE</H3>
                <hr style="border: 2px solid black;">

                <ul>
                    <li>2025-actulidad</li>
                    <p>Deserolla de aplicaciones multi platforfa</p>
                </ul>
                <H3>
                    ESCUELA SECUNDARIA BORCELLE
                </H3>
            <hr style="border: 2px solid black;">

           </div>
           
            <div class="experencia">
                 <ul>
                <li>
                    <p>Volutario en Educaion Infantil
                    <p>Aydaba a organizar las fiestas para ninos y cuisaba de los ninos en ella 
                    </li>
            </ul>
            </div>
           
            <div class="Expertise">
            <h3>Expertise</h3>
            <hr style="border: 2px solid black;">
                <ul>
                    <li>Python</li>
                        <p>Puedo crear una calculadora, un generador de contraseñas o un web scraper</p>
                    <li>Java</li>
                        <p>Puedo escribir código limpio, ayudar a depurar y solucionar problemas, escribir pruebas unitarias y colaborar con desarrolladores senior en el desarrollo de nuevas funcionalidades y el mantenimiento.
                    <li>Mysql</li>
                        <p>Puedo crear y manipular tablas, escribir consultas SQL para la recuperación y modificación de datos, y comprender los fundamentos del diseño de bases de datos.
                    <li>Html</li>
                        <p>Sé escribir HTML. HTML es fundamental para una web. Sin saber HTML, no se pueden mostrar datos en la web.</p>
                    <li>Css</li>
                        <p>Sé cómo dar estilo a tu HTML con CSS. El estilo es muy importante en la web. Permite que el usuario perciba tu sitio web y que se sienta cómodo al usarlo.</p>
                </ul>
            </div>
            
        </section>
    </body>

</html>
```


## 4.-Cierre/Conclusión enlazando con la unidad
La elaboración de esta plantilla de currículum en HTML y CSS ha permitido poner en práctica los contenidos vistos en la unidad sobre estructuración y diseño de páginas web.
A través de esta actividad, he podido reforzar conceptos como el uso adecuado de etiquetas semánticas, la organización del contenido mediante hojas de estilo en cascada y la importancia de la presentación visual en la comunicación profesional.
Además, la personalización del CV con mis propios datos ha sido un ejercicio útil para conectar la teoría con una aplicación real, mostrando cómo el desarrollo web puede emplearse para crear herramientas funcionales y representativas en el ámbito laboral.