# Indroduccion brece y contexalizacion

El objetivo de este ejercicio es hace la validator para saber si xsd file es escribo correcta de la file xml


# Desarrollo técnico correcto y preciso
## Structure

Project/
├─ explicacion.md
├─ 001-documento de referencia.xml
├─ 002-esquema.xsd
└─ 003-validador.py

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
### 003-validador.py
```
from lxml import etree

xml_doc = etree.parse("001-documento de referencia.xml")
xsd_doc = etree.parse("002-esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
```

### import lxml que puede realizar la validator de xml y xsd

```
from lxml import etree
```

### crear variable for more fasil llamar la file con pasos 
```
xml_doc = etree.parse("001-documento de referencia.xml")
xsd_doc = etree.parse("002-esquema.xsd")
```

### crear `schema` que es la xsd file que debe conectar co la xml
```
schema = etree.XMLSchema(xsd_doc)
```

### llamar funcion de la lxml que es la validator y imprimir en la console
```
print(schema.validate(xml_doc))
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
### 003-validador.py
```
from lxml import etree

xml_doc = etree.parse("001-documento de referencia.xml")
xsd_doc = etree.parse("002-esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
```

# 4.-Cierre/Conclusión enlazando con la unidad

Este ejercicio te permitirá validar un documento XML contra un esquema XSD, lo que es crucial para asegurar la integridad y coherencia de los datos en aplicaciones basadas en lenguajes de marcas. Asegúrate de entender cómo se asocian las descripciones con los documentos y cómo se realiza la validación utilizando lxml.
