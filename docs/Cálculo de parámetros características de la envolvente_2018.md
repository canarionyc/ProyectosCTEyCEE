# Ministerio de Fomento
Secretaría de Estado de Infraestructuras, Transporte y Vivienda  
Dirección General de Arquitectura, Vivienda y Suelo

Documento de Apoyo al Documento Básico  
DB-HE Ahorro de energía  
Código Técnico de la Edificación

## DA DB-HE / 1

### Cálculo de parámetros características de la envolvente

**Marzo 2018**

#### Índice

- **Objeto**
- **Cálculo de los parámetros característicos de la envolvente**
  - 2.1 Transmitancia térmica
  - 2.2 Transmitancia de la energía solar de elementos semitransparentes
  - 2.3 Irradiación solar media acumulada en el mes de julio (H50/Jul)
- **Resistencia térmica total de un elemento de edificación constituido por capas homogéneas y heterogéneas**
  - 3.1 Límite superior de la resistencia térmica total R⁺r
  - 3.2 Límite inferior de la resistencia térmica total R⁺r
  - 3.3 Resistencia térmica de cavidades de aire sin ventilar R₀
- **Notaciones y unidades**
- **Otros documentos relacionados**

---

## 1 Objeto

Este documento describe varios métodos simplificados que se pueden emplear para el cálculo de los parámetros característicos de los diferentes elementos que componen la envolvente térmica del edificio, lo que no impide el uso de otros métodos contrastados, sean simplificados o detallados.

## 2 Cálculo de los parámetros características de la envolvente

### 2.1 Transmitancia térmica

#### 2.1.1 Cerramientos en contacto con el aire exterior

Este cálculo es aplicable a la parte opaca de todos los cerramientos en contacto con el aire exterior tales como muros de fachada, cubiertas y suelos en contacto con el aire exterior.

La transmitancia térmica U (W/m²·K) viene dada por:

\[ U = \frac{1}{R_T} \] (1)

siendo \( R_T \) la resistencia térmica total del componente constructivo [m²·K/W].

La resistencia térmica total \( R_T \) de un componente constituido por capas térmicamente homogéneas se calcula mediante:

\[ R_T = R_{si} + R_1 + R_2 + \ldots + R_n + R_{se} \] (2)

siendo:

- \( R_1, R_2, \ldots, R_n \): las resistencias térmicas de cada capa definidas según la expresión (3) [m²·K/W]
- \( R_{si} \) y \( R_{se} \): las resistencias térmicas superficiales correspondientes al aire interior y exterior respectivamente

La resistencia térmica de una capa térmicamente homogénea:

\[ R = \frac{e}{\lambda} \] (3)

siendo:

- \( e \): espesor de la capa [m]
- \( \lambda \): conductividad térmica de diseño del material [W/m·K]

**Tabla 1: Resistencias térmicas superficiales de cerramientos en contacto con el aire exterior [m²·K/W]**

| Posición del cerramiento y sentido del flujo de calor | R_se | R_si |
|---------------------------------------------------|------|------|
| Cerramientos verticales o con pendiente >60° y flujo horizontal | 0,04 | 0,13 |
| Cerramientos horizontales o con pendiente ≤60° y flujo ascendente (techo) | 0,04 | 0,10 |
| Cerramientos horizontales y flujo descendente (suelo) | 0,04 | 0,17 |

#### Cámaras de aire

**a) Cámara de aire sin ventilar**: Resistencia térmica según Tabla 2.

**b) Cámara de aire ligeramente ventilada**: Resistencia térmica = mitad de los valores de la Tabla 2.

**c) Cámara de aire muy ventilada**: Se desprecia la resistencia térmica de la cámara.

### 2.1.2 Cerramientos en contacto con el terreno

#### 2.1.2.1 Suelos en contacto con el terreno

**CASO 1**: Soleras o losas apoyadas sobre el nivel del terreno o como máximo 0,50 m por debajo.

**CASO 2**: Soleras o losas a una profundidad superior a 0,5 m.

Longitud característica:

\[ B' = \frac{A}{P} \] (4)

#### 2.1.2.2 Muros en contacto con el terreno

Transmitancia térmica \( U_T \) [W/m²·K] obtenida de la Tabla 5 en función de la profundidad z y resistencia térmica del muro \( R_m \).

#### 2.1.2.3 Cubiertas enterradas

Se calcula como cerramiento en contacto con el aire exterior, considerando el terreno como capa térmicamente homogénea de conductividad \( \lambda = 2 \, \text{W/m·K} \).

### 2.1.3 Particiones interiores en contacto con espacios no habitables

#### 2.1.3.1 Particiones interiores (excepto suelos en contacto con cámaras sanitarias)

\[ U = U_p \cdot b \] (6)

siendo:

- \( U_p \): transmitancia térmica de la partición interior
- \( b \): coeficiente de reducción de temperatura

### 2.2 Transmitancia de la energía solar de elementos semitransparentes

#### 2.2.1 Transmitancia total de energía solar del acristalamiento

Valores representativos para diferentes tipos de vidrio (Tabla 11).

#### 2.2.2 Transmitancia total de energía solar del acristalamiento con dispositivo de sombra móvil

Valores para diversos acristalamientos y dispositivos de sombra (Tabla 12).

#### 2.2.3 Transmitancia total media mensual de energía solar

\[ g_{gl,wif,m} = (1 - f_{sh,wif}) \cdot g_{gl,wif} + f_{sh,wif} \cdot g_{gl,sh,wif} \]

### 2.3 Irradiación solar media acumulada en el mes de julio (Hsol;jul)

Valores en función de la orientación y zona climática (Tabla 19).

## 3 Resistencia térmica total de un elemento de edificación constituido por capas homogéneas y heterogéneas

\[ R_T = \frac{R'_T + R''_T}{2} \] (12)

### 3.1 Límite superior de la resistencia térmica total \( R'_T \)

\[ \frac{1}{R'_T} = \frac{f_a}{R_{Ta}} + \frac{f_b}{R_{Tb}} + \ldots + \frac{f_q}{R_{Tq}} \] (13)

### 3.2 Límite inferior de la resistencia térmica total \( R''_T \)

\[ \frac{1}{R_j} = \frac{f_a}{R_{aj}} + \frac{f_b}{R_{bj}} + \ldots + \frac{f_q}{R_{qj}} \] (14)

\[ R''_T = R_{si} + R_{j1} + R_{j2} + \ldots + R_{jn} + R_{se} \] (15)

### 3.3 Resistencia térmica de cavidades de aire sin ventilar \( R_g \)

\[ R_g = \frac{1}{h_c + h_r} \] (17)

\[ E = \frac{1}{\frac{1}{\varepsilon_1} + \frac{1}{\varepsilon_2} - 1} \] (18)

## Notaciones y unidades

| Símbolo | Descripción | Unidad |
|---------|-------------|--------|
| α | Absortividad | adimensional |
| λ | Conductividad térmica | W/m·K |
| ψ_v | Transmitancia térmica lineal (marco-acristalamiento) | W/m·K |
| U | Transmitancia térmica | W/m²·K |
| R | Resistencia térmica | m²·K/W |

## Otros documentos relacionados

- UNE EN ISO 6946:2012 - Componentes y elementos para la edificación. Resistencia y transmitancia térmica.
- UNE EN ISO 13370:2017 - Prestaciones térmicas de edificios. Transmisión de calor por el terreno.
- UNE EN 673:2011 - Vidrio en la construcción. Determinación del coeficiente de transmisión térmica.
- UNE EN ISO 10077-1:2010 - Comportamiento térmico de ventanas, puertas y persianas.
- UNE EN 410:2011 - Vidrio para la edificación. Determinación de características luminosas y solares.