# Indroduccion brece y contexalizacion

El objetivo de este ejercicio es familiarizarte con la definición de esquemas y vocabularios en lenguajes de marcas utilizando un documento XML como ejemplo.


# Desarrollo técnico correcto y preciso
## Structure

Project/
├─ explicacion.md
├─ 001-documento de referencia.xml
└─ 002-esquema.xsd
## 001-documento de referencia.xml
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
### 002-esquema.xsd
```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xs:element name="persona">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nombre" type="xs:string"/>
        <xs:element name="apellidos" type="xs:string"/>
        <xs:element name="telefonos">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="telefono" type="xs:string" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```
#### declara XSD format  
```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
```

#### declara elemento `persona`raiz  que contiene la `nombre` `apellidos` `telefonos`  
```
<xs:element name="persona">
    <xs:complexType>
        <xs:sequence>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

#### crear elementos con type sting
```
<xs:element name="nombre" type="xs:string"/>
<xs:element name="apellidos" type="xs:string"/>
```
#### declara elemento `telofonos`raiz de `telefono`
```
<xs:element name="telefonos">
    <xs:complexType>
        <xs:sequence>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```
#### crear elementos con type sting con minOccurs y maxOccurs que significa max y min posibles numeros de valores en nuestro caso es 1 es minimo y valor maximo es ilimitado
```
<xs:element name="telefono" type="xs:string" minOccurs="1" maxOccurs="unbounded"/>
```

# Codigo completa
## 001-documento de referencia.xml
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
## 002-esquema.xsd
```
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xs:element name="persona">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="nombre" type="xs:string"/>
        <xs:element name="apellidos" type="xs:string"/>
        <xs:element name="telefonos">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="telefono" type="xs:string" minOccurs="1" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```


# 4.-Cierre/Conclusión enlazando con la unidad

Este ejercicio te ayudará a entender cómo definir y utilizar esquemas XML para validar la estructura de documentos XML. Aprenderás sobre los tipos de datos admitidos, las restricciones y las relaciones entre elementos en un documento XML.

