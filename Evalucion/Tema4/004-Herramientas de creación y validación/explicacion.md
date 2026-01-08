# Indroduccion brece y contexalizacion

Para este ejercicio, debes crear un curriculum vitae (CV) en formato XML siguiendo las estructuras y etiquetas proporcionadas en el archivo 002-curriculum.xml. Asegúrate de completar todos los campos solicitados, como nombre, apellidos, fecha de nacimiento, nacionalidad, etc.


# Desarrollo técnico correcto y preciso
## Structure

Project/
├─ explicacion.md
├─ 002-curriculum.xml
├─ curricukumn.xsd
└─ 003-validador.py
## 002-curriculum.xml
### declara la xml file 
```
<?xml version="1.0" encoding="UTF-8"?>
<curriculum xmlns="https://ejemplo.com/curriculum" version="1.0">
```
### crear una etiqieta raiz `datosPersonales` que contiene la informcaio de la persona 
```
<datosPersonales>
</datosPersanales> 
```
#### dentro de la `datosPersonales` crear elemntos de la persona 
```
<nombre>Bohdan</nombre>
<apellidos>Sydorenko</apellidos>
<fechaNacimiento>19.19.2005</fechaNacimiento>
<nacionalidad>Ucrañano</nacionalidad>
<email>mose@gmail.com</email>
<telefono>123456789</telefono>
<webPersonal>https://bohdansydorenko.com</webPersonal>
<linkedin>https://www.linkedin.com/in/bohdan-sydorenko-6993b1397/</linkedin>
```
#### dentro de la `datosPersonales` crear una nuevo rtiqueta raiz `direccion` en que creo elementos  
```
<direccion>
    <calle>nose</calle>
    <codigoPostal>46011</codigoPostal>
    <ciudad>Valencia</ciudad>
    <pais>España</pais>
</direccion>
```

### crear una elemnto nuevo
```
<perfilProfesional>
    Estudiante de Desarrollo de 
    Aplicaciones Multiplataforma (DAM) con actitud proactiva y 
    fuerte motivación por aprender. 
    Apasionado por la tecnología y la programación, 
    busco mi primera experiencia profesional en el sector 
    tecnológico para aplicar y ampliar mis conocimientos en 
    desarrollo de software. Destaco por mi capacidad de trabajo en 
    equipo, resolución de problemas y aprendizaje continuo. 
    Manejo tecnologías como Java, Python, SQL, HTML, CSS y 
    herramientas como Git y Visual Studio Code.
</perfilProfesional>
```

### crear una etiqieta raiz `formacionAcademica` que contiene la informcaio de la estudios 
```
<formacionAcademica>
</formacionAcademica>
```

#### dentro de `formacionAcademica` etiquetas de la raiz que contine elementos de la mis estudios 
```
<estudio>
    <titulo>Desarrollo de Aplicaciones Multiplataforma (DAM)</titulo>
    <centro>Universidad Borcelle</centro>
    <localizacion>Valencia, España</localizacion>
    <fechaInicio>2025</fechaInicio>
    <fechaFin>Actualidad</fechaFin>
</estudio>
<estudio>
    <titulo>Bachillerato</titulo>
    <centro>Escuela Secundaria Borcelle de Matemáticas</centro>
    <localizacion>Ucrania</localizacion>
    <fechaInicio>2020</fechaInicio>
    <fechaFin>2022</fechaFin>
</estudio>
```

### crear una etiqieta raiz `publicaciones` que contiene la informcaio de la mis posibles 
```
<publicaciones>
</publicaciones>
```

#### dentro de `publicaciones` etiquetas de la raiz que contine elementos de la mis posibles  
```
    <publicacion>
        <tipo>Libro</tipo>
        <titulo>Aprende programación con Python</titulo>
        <editorial>Editorial Ejemplo</editorial>
        <anio>2025</anio>
        <descripcion>
            Manual práctico de introducción a la programación con Python
            orientado a estudiantes y profesionales que se inician en el
            desarrollo de software.
        </descripcion>
    </publicacion>
    <publicacion>
        <tipo>Artículo</tipo>
        <titulo>Introducción a Java y desarrollo multiplataforma</titulo>
        <editorial>Blog Personal / Medium</editorial>
        <anio>2024</anio>
        <descripcion>
            Artículo explicativo sobre conceptos básicos de Java y su aplicación
            en proyectos multiplataforma, con ejemplos prácticos.
        </descripcion>
    </publicacion>
```

## curricukumn.xsd

### declara la xml file 
```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="https://ejemplo.com/curriculum"
           xmlns="https://ejemplo.com/curriculum"
           elementFormDefault="qualified">
            <xs:element name="curriculum">
                <xs:complexType>
                    <xs:sequence>
                    </xs:sequence>
                </xs:complexType>
            <xs:attribute name="version" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

</xs:schema>
```
### crear una etiqieta raiz `datosPersonales` que contiene la informcaio de la persona 
```
<xs:element name="datosPersonales">
    <xs:complexType>
        <xs:sequence>
        </xs:sequence>
</xs:complexType>
```
#### dentro de la `datosPersonales` crear elemntos de la persona 
```
<xs:element name="nombre" type="xs:string"/>
<xs:element name="apellidos" type="xs:string"/>
<xs:element name="fechaNacimiento" type="xs:string"/>
<xs:element name="nacionalidad" type="xs:string"/>
<xs:element name="email" type="xs:string"/>
<xs:element name="telefono" type="xs:string"/>
<xs:element name="webPersonal" type="xs:anyURI"/>
<xs:element name="linkedin" type="xs:anyURI"/>
```
#### dentro de la `datosPersonales` crear una nuevo rtiqueta raiz `direccion` en que creo elementos  
```
<xs:element name="direccion">
<xs:complexType>
    <xs:sequence>
        <xs:element name="calle" type="xs:string"/>
        <xs:element name="codigoPostal" type="xs:string"/>
        <xs:element name="ciudad" type="xs:string"/>
        <xs:element name="pais" type="xs:string"/>
    </xs:sequence>
</xs:complexType>
</xs:element>
```

### crear una elemnto nuevo
```
<xs:element name="perfilProfesional" type="xs:string"/>
```

### crear una etiqieta raiz `formacionAcademica` que contiene la informcaio de la estudios 
```
 <xs:element name="formacionAcademica">
    <xs:complexType>
        <xs:sequence>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

#### dentro de `formacionAcademica` etiquetas de la raiz que contine elementos de la mis estudios 
```
<xs:element name="estudio" maxOccurs="unbounded">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="titulo" type="xs:string"/>
            <xs:element name="centro" type="xs:string"/>
            <xs:element name="localizacion" type="xs:string"/>
            <xs:element name="fechaInicio" type="xs:string"/>
            <xs:element name="fechaFin" type="xs:string"/>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

### crear una etiqieta raiz `publicaciones` que contiene la informcaio de la mis posibles 
```
 <xs:element name="publicaciones">
    <xs:complexType>
        <xs:sequence>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

#### dentro de `publicaciones` etiquetas de la raiz que contine elementos de la mis posibles  
```
    <publicacion>
        <tipo>Libro</tipo>
        <titulo>Aprende programación con Python</titulo>
        <editorial>Editorial Ejemplo</editorial>
        <anio>2025</anio>
        <descripcion>
            Manual práctico de introducción a la programación con Python
            orientado a estudiantes y profesionales que se inician en el
            desarrollo de software.
        </descripcion>
    </publicacion>
    <publicacion>
        <tipo>Artículo</tipo>
        <titulo>Introducción a Java y desarrollo multiplataforma</titulo>
        <editorial>Blog Personal / Medium</editorial>
        <anio>2024</anio>
        <descripcion>
            Artículo explicativo sobre conceptos básicos de Java y su aplicación
            en proyectos multiplataforma, con ejemplos prácticos.
        </descripcion>
    </publicacion>
```


# Codigo completa
## 002-curriculum.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<curriculum xmlns="https://ejemplo.com/curriculum" version="1.0">
    <datosPersonales>
        <nombre>Bohdan</nombre>
        <apellidos>Sydorenko</apellidos>
        <fechaNacimiento>19.19.2005</fechaNacimiento>
        <nacionalidad>Ucrañano</nacionalidad>
        <email>mose@gmail.com</email>
        <telefono>123456789</telefono>
        <webPersonal>https://bohdansydorenko.com</webPersonal>
        <linkedin>https://www.linkedin.com/in/bohdan-sydorenko-6993b1397/</linkedin>
        <direccion>
            <calle>nose</calle>
            <codigoPostal>46011</codigoPostal>
            <ciudad>Valencia</ciudad>
            <pais>España</pais>
        </direccion>
    </datosPersonales>

    
    <perfilProfesional>
        Estudiante de Desarrollo de 
        Aplicaciones Multiplataforma (DAM) con actitud proactiva y 
        fuerte motivación por aprender. 
        Apasionado por la tecnología y la programación, 
        busco mi primera experiencia profesional en el sector 
        tecnológico para aplicar y ampliar mis conocimientos en 
        desarrollo de software. Destaco por mi capacidad de trabajo en 
        equipo, resolución de problemas y aprendizaje continuo. 
        Manejo tecnologías como Java, Python, SQL, HTML, CSS y 
        herramientas como Git y Visual Studio Code.
    </perfilProfesional>

    <formacionAcademica>
    <estudio>
        <titulo>Desarrollo de Aplicaciones Multiplataforma (DAM)</titulo>
        <centro>Universidad Borcelle</centro>
        <localizacion>Valencia, España</localizacion>
        <fechaInicio>2025</fechaInicio>
        <fechaFin>Actualidad</fechaFin>
    </estudio>
    <estudio>
        <titulo>Bachillerato</titulo>
        <centro>Escuela Secundaria Borcelle de Matemáticas</centro>
        <localizacion>Ucrania</localizacion>
        <fechaInicio>2020</fechaInicio>
        <fechaFin>2022</fechaFin>
    </estudio>
    </formacionAcademica>
    <publicaciones>
    <publicacion>
        <tipo>Libro</tipo>
        <titulo>Aprende programación con Python</titulo>
        <editorial>Editorial Ejemplo</editorial>
        <anio>2025</anio>
        <descripcion>
            Manual práctico de introducción a la programación con Python
            orientado a estudiantes y profesionales que se inician en el
            desarrollo de software.
        </descripcion>
    </publicacion>
    <publicacion>
        <tipo>Artículo</tipo>
        <titulo>Introducción a Java y desarrollo multiplataforma</titulo>
        <editorial>Blog Personal / Medium</editorial>
        <anio>2024</anio>
        <descripcion>
            Artículo explicativo sobre conceptos básicos de Java y su aplicación
            en proyectos multiplataforma, con ejemplos prácticos.
        </descripcion>
    </publicacion>
    </publicaciones>

```
## curricukumn.xsd
```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
           targetNamespace="https://ejemplo.com/curriculum"
           xmlns="https://ejemplo.com/curriculum"
           elementFormDefault="qualified">

    <xs:element name="curriculum">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="datosPersonales">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="nombre" type="xs:string"/>
                            <xs:element name="apellidos" type="xs:string"/>
                            <xs:element name="fechaNacimiento" type="xs:string"/>
                            <xs:element name="nacionalidad" type="xs:string"/>
                            <xs:element name="email" type="xs:string"/>
                            <xs:element name="telefono" type="xs:string"/>
                            <xs:element name="webPersonal" type="xs:anyURI"/>
                            <xs:element name="linkedin" type="xs:anyURI"/>
                            <xs:element name="direccion">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="calle" type="xs:string"/>
                                        <xs:element name="codigoPostal" type="xs:string"/>
                                        <xs:element name="ciudad" type="xs:string"/>
                                        <xs:element name="pais" type="xs:string"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>

                <xs:element name="perfilProfesional" type="xs:string"/>

                <xs:element name="formacionAcademica">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="estudio" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="titulo" type="xs:string"/>
                                        <xs:element name="centro" type="xs:string"/>
                                        <xs:element name="localizacion" type="xs:string"/>
                                        <xs:element name="fechaInicio" type="xs:string"/>
                                        <xs:element name="fechaFin" type="xs:string"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>

                <xs:element name="publicaciones">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="publicacion" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="tipo" type="xs:string"/>
                                        <xs:element name="titulo" type="xs:string"/>
                                        <xs:element name="editorial" type="xs:string"/>
                                        <xs:element name="anio" type="xs:gYear"/>
                                        <xs:element name="descripcion" type="xs:string"/>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>

            </xs:sequence>
            <xs:attribute name="version" type="xs:string" use="required"/>
        </xs:complexType>
    </xs:element>

</xs:schema>

```


# 4.-Cierre/Conclusión enlazando con la unidad
Como conclusión, este ejercicio permite aplicar de forma práctica los conceptos estudiados en la Unidad 4, relacionados con la estructuración de datos mediante XML y su validación usando esquemas XSD. La creación del curriculum en XML demuestra la importancia de definir correctamente la jerarquía y las etiquetas, mientras que el uso del XSD garantiza la integridad, coherencia y reutilización de los datos. Además, la validación del documento refuerza la necesidad de trabajar con estándares que aseguren la correcta interpretación de la información en distintos sistemas.

