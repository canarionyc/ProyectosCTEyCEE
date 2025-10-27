# HERRAMIENTA UNIFICADA LIDER-CALENER (HULC)
## Manual de Usuario
### Versión 0.1 / DB-HE 2019 / Aug 2025

---

## Índice General

### 1. Introducción
- [1.1 Requisitos de la Aplicación](#11-requisitos-de-la-aplicación)
- [1.2 Alcance](#12-alcance)
- [1.3 Limitaciones](#13-limitaciones)
- [1.4 Instalación](#14-instalación)
- [1.5 Configuración Regional](#15-configuración-regional)
- [1.6 Descripción y estructura de la Herramienta Unificada](#16-descripción-y-estructura-de-la-herramienta-unificada)

### 2. ¿Cómo se usa la herramienta unificada?
- [2.1 ¿Lo que se ve es lo que se calcula?](#21-lo-que-se-ve-es-lo-que-se-calcula)

### 3. Creación y descripción de un proyecto

### 4. Datos generales
- [4.1 Datos Administrativos](#41-datos-administrativos)
- [4.2 Datos Generales](#42-datos-generales)
- [4.3 Factores de paso](#43-factores-de-paso)
- [4.4 Producción de energía](#44-producción-de-energía)
- [4.5 Opciones Generales del Edificio](#45-opciones-generales-del-edificio)
- [4.6 Imágenes y Otros datos](#46-imágenes-y-otros-datos)

### 5. Definición Geométrica, Constructiva y Condiciones Operacionales
- [5.1 Gestión de las Bases de Datos](#51-gestión-de-las-bases-de-datos)
- [5.2 Definición del edificio](#52-definición-del-edificio)
- [5.3 Condiciones Operacionales](#53-condiciones-operacionales)
- [5.4 Elementos Especiales de la Envolvente Térmica](#54-elementos-especiales-de-la-envolvente-térmica)

### 6. Verificación HE1
- [6.1 Cálculo de indicadores HE1](#61-cálculo-de-indicadores-he1)

### 7. Definición de Sistemas, Cálculo de Consumos

### 8. Sistemas de Climatización, ACS y ventilación
- [8.1 Definición de los Sistemas](#81-definición-de-los-sistemas)
- [8.2 Definición de Equipos](#82-definición-de-equipos)
- [8.3 Definición de Unidades Terminales](#83-definición-de-unidades-terminales)
- [8.4 Definición de Factores de Corrección](#84-definición-de-factores-de-corrección)

### 9. Componentes de la instalación
- [9.1 Sistemas](#91-sistemas)
- [9.2 Equipos](#92-equipos)
- [9.3 Uso de multiplicadores en sistemas](#93-uso-de-multiplicadores-en-sistemas)
- [9.4 Unidades Terminales](#94-unidades-terminales)
- [9.5 Factores de Corrección](#95-factores-de-corrección)
- [9.6 Sistema Exclusivo para Ventilación](#96-sistema-exclusivo-para-ventilación)

### 10. Verificación HEO, HE4 y HES
- [10.1 Verificación de límites de HEO, HE4 y HES](#101-verificación-de-límites-de-heo-he4-y-hes)
- [10.2 Resultados de demandas, consumos y emisiones](#102-resultados-de-demandas-consumos-y-emisiones)

### 11. Documentación Administrativa
- [11.1 Informe de verificación](#111-informe-de-verificación)
- [11.2 Certificación de eficiencia energética de edificios](#112-certificación-de-eficiencia-energética-de-edificios)
- [11.3 Archivo XML](#113-archivo-xml)

### 12. Exportación, Importación

### 13. Acerca de

### 14. Preguntas Frecuentes

### 15. Índice de términos

---

## 1. Introducción

La HERRAMIENTA UNIFICADA LIDER Y CALENER (HULC) es una implementación informática que permite obtener los resultados necesarios para la verificación de las Secciones HE0, HE1, HE4 y HES del Documento Básico de Ahorro de Energía (DB-HE) del Código Técnico de la Edificación (CTE).

### 1.1 Requisitos de la Aplicación

- **Sistema operativo**: Windows 10 o posterior
- **Procesador**: Intel Centrino o equivalente
- **Memoria**: 128MB de memoria de vídeo y 1500MB de RAM (preferible 2 GB)
- **Pantalla**: Resolución 1280x768 / Color verdadero
- **Disco duro**: Suficiente espacio libre
- **Internet**: Para instalación de actualizaciones
- **Cuenta**: Con privilegios de administrador

### 1.2 Alcance

- Modelos recomendados: máximo 100 espacios
- Elementos recomendados: máximo 500 elementos
- Para edificios más complejos: usar multiplicadores o simplificaciones

### 1.3 Limitaciones

**Definición geométrica:**
1. No pueden definirse elementos constructivos interiores geométricamente singulares no verticales ni rectangulares
2. No pueden definirse forjados o suelos inclinados
3. No pueden definirse ventanas no rectangulares
4. Espacios con altura no constante requieren definición especial
5. Problemas en cálculo de valor n50 al unir espacios verticalmente

### 1.4 Instalación

Ejecutar `ICTEHE2019.exe` como administrador. Directorios creados:
```
C:\
├── ProgramasCTEyCEE
│   ├── CALENER-GT
│   ├── CTEHE2019
│   └── DatosClimaticos
└── ProyectosCTEyCEE
    ├── CTEHE2019
    │   ├── Librería
    │   ├── Proyectos
    │   └── Temporales
```

### 1.5 Configuración Regional

El programa utiliza la configuración regional del ordenador. Configuraciones admitidas:
- Coma y punto
- Punto y coma
- Punto y punto

### 1.6 Descripción y estructura de la Herramienta Unificada

**Barra de herramientas principal:**
- `Nuevo proyecto` - Crear nuevo proyecto
- `Abrir` - Abrir proyecto existente
- `Guardar` - Guardar proyecto actual
- `Datos Generales` - Datos generales del proyecto
- `Def. Geométrica` - Representación 3D y definición geométrica
- `Base de Datos` - Acceso a bases de datos
- `Opciones` - Propiedades generales y valores por defecto
- `Cond. Operacionales` - Condiciones operacionales (solo GT)
- `Elementos Especiales` - Soluciones especiales de envolvente
- `CTE HE-1` - Verificación HE1
- `CTE HE-0` - Verificación HE0
- `Documentación` - Informes y certificación
- `Sistemas` - Definición de sistemas energéticos
- `CALENER-GT` - Exportación a CALENER-GT
- `Export/Import` - Exportación e importación de datos
- `Ayuda` - Información de ayuda
- `Acerca de` - Información del programa

---

## 2. ¿Cómo se usa la herramienta unificada?

**Flujo de trabajo sistemático:**

1. **Análisis preliminar**
   - Selección de zona climática (Anejo B DB-HE)
   - Simplificaciones y divisiones del edificio
   - Clasificación de espacios según DB-HE1
   - Recopilación de propiedades higrotérmicas

2. **Configuración inicial**
   - Crear proyecto nuevo
   - Completar las 6 pestañas de Datos Generales

3. **Base de datos**
   - Configurar materiales y productos
   - Definir composiciones constructivas

4. **Definición geométrica** (planta por planta, de abajo a arriba)
   - Cargar planos DXF/BMP
   - Crear planta especificando cota
   - Definir espacios (con líneas auxiliares si es necesario)
   - Modificar condiciones operacionales
   - Definir particiones horizontales
   - Generar cerramientos verticales automáticamente
   - Definir huecos
   - Definir cubiertas

5. **Elementos adicionales**
   - Obstáculos que generan sombras
   - Elementos singulares de sombra
   - Elementos especiales de envolvente térmica

6. **Cálculos y verificaciones**
   - Calcular HE1
   - Definir sistemas de climatización, ventilación, ACS, iluminación
   - Calcular HE0

7. **Documentación**
   - Generar informe de verificación
   - Certificado de eficiencia energética
   - Archivo XML para registro

### 2.1 ¿Lo que se ve es lo que se calcula?

**Consideraciones importantes:**
- Los elementos deben estar asociados a un espacio concreto
- Las cubiertas inclinadas sobre varios espacios deben estar divididas entre ellos
- Los tabiques divisores deben llegar hasta la cubierta
- Elementos que no forman parte de la envolvente térmica deben definirse como elementos singulares

---

## 3. Creación y descripción de un proyecto

**Tipos de archivos de apertura:**
- Archivos HULC (.CTEHEXML)
- Archivos .CTE (se importan y generan automáHEXML)
- Archivos CALENER-GT (.PD2)

**NOTA IMPORTANTE:** Revisar todos los datos de entrada en casos importados, especialmente zona climática y altitud.

---

## 4. Datos generales

### 4.1 Datos Administrativos

**Dos pestañas:**
1. **Datos del Proyecto**
   - Localización, uso del edificio, situación
   - Normativa vigente
   - Superficie construida y de cubierta (para cálculo HES)

2. **Datos del Certificador**
   - Datos del autor y titulación habilitante
   - Pueden almacenarse para futuros proyectos

### 4.2 Datos Generales

**Parámetros principales:**
- **Tipo de caso**: Verificación DB-HE y certificación, o solo certificación
- **Tipo de edificio**: Vivienda unifamiliar, en bloque, o terciario
- **Localidad**: Selección de comunidad autónoma, provincia, localidad
- **Zona climática y altitud**: Deben ser acordes con Anejo B DB-HE
- **Ventilación**: Caudal en l/s para residencial
- **Permeabilidad**: Valores por defecto o según ensayo
- **Tipo de uso por defecto**: Residencial o tipos terciarios

### 4.3 Factores de paso

**Factores de energía final a primaria:**
- No editables por usuarios excepto combustibles genéricos RED1 y RED2
- Varían según localidad peninsular o extrapeninsular
- Factores específicos para cogeneración

### 4.4 Producción de energía

**Producción eléctrica:**
- Fotovoltaica in situ
- Eólica in situ
- Cogeneración (solo con fuentes renovables)

**Producción térmica:**
- Solar térmica ACS

**Campos adicionales:**
- Potencia eléctrica renovable instalada (para HE5)
- Irradiación solar diaria media anual (solo terciario)

### 4.5 Opciones Generales del Edificio

**Configuraciones:**
- Periodo de aplicación de elementos estacionales de sombras
- Uso de dispositivos de sombra móviles (factores fijos o cálculo dinámico)
- Ventilación nocturna en edificios residenciales
- Activación de sistemas de sustitución

### 4.6 Imágenes y Otros datos

- Imágenes representativas del proyecto (300x400 píxeles recomendado)
- Anotaciones sobre hipótesis de cálculo
- Edición manual de fecha de certificación

---

## 5. Definición Geométrica, Constructiva y Condiciones Operacionales

### 5.1 Gestión de las Bases de Datos

**Estructura de la base de datos:**
- Opacos
  - Materiales y productos
  - Cerramientos
- Semitransparentes
  - Vidrios
  - Marcos
  - Huecos y lucernarios
- Puentes térmicos

#### 5.1.1 Materiales

**Propiedades:**
- Conductividad (W/(m·K))
- Densidad (Kg/m³)
- Calor específico (J/(kg·K))
- Resistencia térmica (m²·K/W)
- Factor de resistencia a la difusión del vapor de agua (adimensional)

#### 5.1.2 Cerramientos

Composiciones de materiales que forman un cerramiento, en orden de exterior a interior.

#### 5.1.3 Vidrios

**Propiedades:**
- Transmitancia térmica (W/(m²·K))
- Factor solar

#### 5.1.4 Marcos

**Propiedades:**
- Transmitancia térmica (W/(m²·K))
- Absortividad

#### 5.1.5 Huecos

**Componentes y propiedades:**
- Vidrio (selección de base de datos)
- Marco (selección de base de datos)
- Porcentaje de hueco ocupado por marco
- Incremento de transmitancia por intercalarios y cajones
- Permeabilidad al aire (m³/(hm²))
- Transmitancia total con dispositivos de sombra móvil

#### 5.1.6 Puentes Térmicos

**Tipos de definición:**
- Valor por defecto
- Valor por usuario
- Valor por catálogo (DA DB-HE/3)

**Cálculo de longitudes:** Necesario recalcular después de cambios geométricos.

### 5.2 Definición del edificio

#### 5.2.1 Estructura general

**Elementos del edificio:**
- Plantas (polígonos azules)
- Espacios (polígonos verdes)
- Suelos (color rosa claro)
- Cerramientos interiores (verde caqui)
- Cerramientos exteriores (gris)
- Huecos (azul claro)
- Sombras (negro)

#### 5.2.2 Medidas del Edificio

**Convenciones:**
- **Plantas**: Origen a altura del suelo, medidas interiores
- **Espacios**: Medidas interiores en cerramientos exteriores, mediatriz en interiores
- **Cerramientos**: Altura por defecto igual al espacio

#### 5.2.3 Grandes Edificios. Uso de multiplicadores

**Recomendaciones:**
- Usar multiplicadores para plantas o espacios repetidos
- Límite recomendado: 100 espacios
- Cerramientos entre espacios repetidos deben ser adiabáticos
- Considerar efecto en cálculo de sombras

#### 5.2.4 Definición geométrica

**Métodos:**
- Manual ("a mano alzada")
- Con introducción de coordenadas
- A partir de planos DXF/BMP

#### 5.2.5 Plantas

**Propiedades:**
- Nombre
- Planta anterior
- Multiplicador
- Altura de espacios
- Cota

**Recomendaciones:**
- Definir vértices en sentido antihorario
- Máximo 30 vértices por polígono
- Usar líneas auxiliares para plantas complejas

#### 5.2.6 Líneas auxiliares (Líneas 2D)

Para división de espacios y definición precisa de vértices.

#### 5.2.7 Espacios

**Propiedades:**
- Tipo de espacio (Acondicionado, No acondicionado, No habitable)
- Tipo de uso
- Número de pilares
- Multiplicador
- Número de renovaciones hora (terciarios)
- Sistema de iluminación (terciarios)

**Espacios multiplicados:** Para representar espacios repetidos en grandes edificios.

#### 5.2.8 Particiones horizontales

**Generación automática o manual de:**
- Suelos
- Techos
- Forjados

#### 5.2.9 Generación automática de Cerramientos Verticales

Tipos automáticos:
- Cerramiento exterior (cota ≥ 0 m)
- Cerramiento en contacto con terreno (cota < 0 m)
- Medianerías (deben cambiarse manualmente a adiabáticas)

#### 5.2.10 Ventanas y Puertas

**Definición en cerramientos convencionales:**
- Gráficamente con el botón correspondiente
- Propiedades: posición, dimensiones, retranqueo
- Dispositivos de sombra estacional

**Definición en elementos singulares:** Mediante edición de propiedades del elemento.

#### 5.2.11 Definición de Cubiertas

**Métodos:**
- Horizontales: como particiones horizontales
- Inclinadas: como elementos singulares con líneas 3D

#### 5.2.12 Elementos singulares

**Tipos:**
- Elementos de envolvente térmica (no rectangulares/no verticales)
- Elementos de sombra propios del edificio

#### 5.2.13 Unión de espacios

**Proceso irreversible** para unir dos espacios en uno.

#### 5.2.14 Obstáculos Remotos

Elementos externos que proyectan sombras sobre el edificio.

### 5.3 Condiciones Operacionales

Solo para edificios terciarios.

**Condiciones a definir:**
- Cargas internas (ocupación, iluminación, equipos)
- Ventilación/Infiltración
- Equipo de acondicionamiento

**Horarios:** Definición semanal tipo con posibilidad de horarios personalizados.

### 5.4 Elementos Especiales de la Envolvente Térmica

**Tipos disponibles:**
- Fachada ventilada
- Muro solar
- Muro Trombe
- Acristalamientos especiales

---

## 6. Verificación HE1

### 6.1 Cálculo de indicadores HE1

Verificación de:
- Apartado 3.1.1.3
- Apartado 3.1.1.4
- Apartado 3.1.2
- Apartado 3.1.3.3

de la sección HE1 del DB-HE.

---

## 7. Definición de Sistemas, Cálculo de Consumos

Definición de sistemas energéticos del edificio.

---

## 8. Sistemas de Climatización, ACS y ventilación

### 8.1 Definición de los Sistemas

**Tipos de sistemas disponibles:**
- Climatización unizona
- Calefacción multizona por agua
- Climatización multizona por expansión directa
- Sistemas mixtos
- Sistemas para terciarios

### 8.2 Definición de Equipos

**Tipos de equipos:**
- Calderas eléctricas o de combustible
- Equipos de expansión directa
- Bombas de calor
- Equipos de acumulación
- Equipos ideales

### 8.3 Definición de Unidades Terminales

**Tipos:**
- Unidad terminal de agua caliente
- Unidad terminal de impulsión de aire
- Unidad terminal en expansión directa

### 8.4 Definición de Factores de Corrección

**Métodos:**
- Tablas de comportamiento
- Curvas de comportamiento

---

## 9. Componentes de la instalación

### 9.1 Sistemas

Descripción detallada de cada tipo de sistema disponible.

### 9.2 Equipos

Especificaciones técnicas de cada tipo de equipo.

### 9.3 Uso de multiplicadores en sistemas

Aplicación de multiplicadores a sistemas repetitivos.

### 9.4 Unidades Terminales

Configuración de unidades terminales.

### 9.5 Factores de Corrección

Ajuste de rendimientos mediante factores de corrección.

### 9.6 Sistema Exclusivo para Ventilación

Sistemas dedicados únicamente a ventilación.

---

## 10. Verificación HEO, HE4 y HES

### 10.1 Verificación de límites

Comprobación de cumplimiento de límites reglamentarios.

### 10.2 Resultados

Presentación de resultados de demandas, consumos y emisiones.

---

## 11. Documentación Administrativa

### 11.1 Informe de verificación

Generación del informe de verificación del DB-HE.

### 11.2 Certificación de eficiencia energética

Generación del certificado de eficiencia energética.

### 11.3 Archivo XML

Generación del archivo XML para registro oficial.

---

## 12. Exportación, Importación

Intercambio de datos con otros programas y formatos.

---

## 13. Acerca de

Información sobre el programa y versiones.

---

## 14. Preguntas Frecuentes

Soluciones a problemas comunes:
- Errores de acceso violation
- Definición de espacios
- Cerramientos horizontales adiabáticos
- Cubiertas que sobresalen
- Problemas con ventanas en cubiertas
- Importación de planos DXF
- Y muchos más...

---

## 15. Índice de términos

Glosario de términos técnicos utilizados en el manual.

---

*© 2009-2024 Ministerio de Vivienda y Agenda Urbana. Documento distribuido bajo licencia Creative Commons Reconocimiento 4.0 Internacional (CC BY 4.0).*