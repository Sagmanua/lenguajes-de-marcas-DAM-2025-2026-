# Indroduccion brece y contexalizacion

En este vamos a empesar trabajar y aprender los basicos de XML  
Aprenderemos cómo declara la XML como crear la etiqetas y elmentos estudio baisc structura de al XML .Estos conceptos son fundamentales para manejar datos en la pagina web.


# Desarrollo técnico correcto y preciso
##

Project/
├─ explicacion.md
├─ 001.xml
├─ 002.xml
├─ varios_telefonos.xml
├─ debe_haber_una_etiqueta_raiz.xml
└─ 004-microblog.html
## XML Explicar cada file por 1 
### 001.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>
```
#### declara XML 
```
<?xml version="1.0" encoding="UTF-8"?>
```

#### Crear elemento raiz
```
<persona>

</persona>
```

#### Crear elemntos `nombre` `apelidos`
```
<nombre>Jose Vicente</nombre>
<apellidos>Carratala Sanchis</apellidos>
```
### 002.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>
```
#### declara XML 
```
<?xml version="1.0" encoding="UTF-8"?>
```

#### Crear elemento raiz
```
<persona>

</persona>
```

#### Crear elemntos `nombre` `apelidos`
```
<nombre>Jose Vicente</nombre>
<apellidos>Carratala Sanchis</apellidos>
```
### 004.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>
```
#### declara XML 
```
<?xml version="1.0" encoding="UTF-8"?>
```

#### Crear elemento raiz
```
<persona>

</persona>
```

#### Crear elemntos `nombre` `apelidos`
```
<nombre>Jose Vicente</nombre>
<apellidos>Carratala Sanchis</apellidos>
```
#### Crear elemento `telefonos` que es la raiz de la elemento `telefono`
```
<telefonos>
  <telefono>12345567</telefono>
  <telefono>6534646</telefono>
</teleffonos>
```
### varios_telefonos.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
    <telefono>98765432</telefono>
  </telefonos>
</persona>
```
#### declara XML 
```
<?xml version="1.0" encoding="UTF-8"?>
```

#### Crear elemento raiz
```
<persona>

</persona>
```

#### Crear elemntos `nombre` `apelidos`
```
<nombre>Jose Vicente</nombre>
<apellidos>Carratala Sanchis</apellidos>
```
#### Crear elemento `telefonos` que es la raiz de la elemento `telefono`
```
<telefonos>
  <telefono>12345567</telefono>
  <telefono>6534646</telefono>
  <telefono>98765432</telefono>
</telefonos>
```
### debe_haber_una_etiqueta_raiz.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>
```

#### declara XML 
```
<?xml version="1.0" encoding="UTF-8"?>
```

#### Crear elemento raiz
```
<persona>

</persona>
```

#### Crear elemntos `nombre` `apelidos`
```
<nombre>Jose Vicente</nombre>
<apellidos>Carratala Sanchis</apellidos>
```

# Codigo completa
Project/
├─ explicacion.md
├─ 001.xml
├─ 002.xml
├─ 004.xml
├─ varios_telefonos.xml
└─ debe_haber_una_etiqueta_raiz.xml

## 001.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>

```
## 002.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>

```
## 004.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>
```
## varios_telefonos,xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
</persona>
```
## debe_hacer_una_etiquetas_raiz.xml
```
<?xml version="1.0" encoding="UTF-8"?>
<persona>
  <nombre>Jose Vicente</nombre>
  <apellidos>Carratala Sanchis</apellidos>
  <telefonos>
    <telefono>12345567</telefono>
    <telefono>6534646</telefono>
  </telefonos>
</persona>
```

# 4.-Cierre/Conclusión enlazando con la unidad

En este ejercicio, hemos aprendido cómo estructurar datos en XML utilizando etiquetas personalizables. Es importante recordar que el contenido debe estar dentro de una etiqueta raíz y que los elementos pueden contener subetiquetas para organizar la información de manera jerárquica.

Practica estos ejemplos y asegúrate de entender cómo se relacionan con los conceptos de XML que hemos estudiado en clase.