# Modelos-SRI
Proyecto de Sistema de Recuperación de Información:

## Autores:
- Marco Antonio Ochil Trujillo C-412
- Jan Carlos Perez Lorenzo C-412
- Kevin Majim Ortega Alvarez C-412

## Definición del modelo de SRI implementado:
El modelo implementado es un sistema de recomendación basado en la técnica de Indexación de Semántica Latente (LSI). LSI es una técnica de procesamiento de lenguaje natural que utiliza descomposición de valores singulares (SVD) para representar términos y documentos en un espacio vectorial de menor dimensión, lo que permite encontrar relaciones semánticas entre ellos.

## Consideraciones tomadas a la hora de desarrollar la solución:
- Se han considerado las limitaciones de recursos computacionales disponibles para la implementación del modelo.
- Se ha tenido en cuenta la escalabilidad del sistema para manejar grandes volúmenes de datos.
- Se utilizó otro modelo implementado en clases (Modelo Booleano) para realizar la comparación con el nuestro
- Se les realiza la comparación utilizando las métricas estándar (Precisión, Recobrado)

## Explicación de cómo ejecutar el proyecto:
1. Clonar este repositorio en tu máquina.
2. Instalar las dependencias del proyecto utilizando el archivo requirements.txt: `pip install -r requirements.txt`.
3. Seguir los pasos que indica el archivo `startup.md`.
4. Seguir las instrucciones en la interfaz de usuario para interactuar con el sistema de recuperación.

## Definición de la consulta:
El sistema de recuperación tiene como objetivo recomendar películas a los usuarios basándose en sus preferencias históricas de calificación de películas.

## Explicación de la solución desarrollada:
El sistema de recuperación utiliza la técnica de Indexación de Semántica Latente (LSI) para calcular la similitud entre las consultas de los usuarios y los documentos disponibles en la colección. Esto se logra representando tanto las consultas como los documentos en un espacio vectorial de menor dimensión y calculando la similitud coseno entre ellos.\
Matemáticamente, LSI utiliza la descomposición en valores singulares (SVD) para representar la matriz término-documento AA como el producto de tres matrices:

$$ A = U \cdot \Sigma \cdot V^T $$

Donde:
- $ U $ es la matriz de vectores singulares izquierdos.
- $ \Sigma $ es la matriz diagonal de valores singulares.
- $ V^T $ es la matriz de vectores singulares derechos transpuesta.

## Cálculo de la similitud del coseno

La similitud del coseno es una medida comúnmente utilizada para evaluar la similitud entre dos vectores en un espacio de características. En el contexto del sistema de recomendación, la similitud del coseno se utiliza para medir la similitud entre la consulta del usuario y los documentos en el espacio semántico latente.

La fórmula para calcular la similitud del coseno entre dos vectores $ \mathbf{a}$  y  $\mathbf{b}$ se define como:

$$\text{similitud}( \mathbf{a}, \mathbf{b} ) = \frac{ \mathbf{a} \cdot \mathbf{b} }{ \| \mathbf{a} \| \cdot \| \mathbf{b} \| } $$

Donde:
- $ \cdot $ representa el producto punto entre dos vectores.
- $ \| \mathbf{a} \| $ y $ \| \mathbf{b} \| $ son las normas euclidianas de los vectores $ \mathbf{a} $ y $ \mathbf{b} $, respectivamente.

## Insuficiencias de la solución y mejoras propuestas:
A pesar de los esfuerzos realizados en el desarrollo de la solución, hay áreas que podrían mejorarse:

- **Precisión:** Aunque el sistema de recomendación basado en LSI es efectivo, aún existe margen para mejorar la precisión de los datos recuperados. Se observa que en algunos casos, las sugerencias pueden no ser completamente relevantes para las consultas de los usuarios. Esto podría abordarse explorando técnicas más avanzadas de procesamiento de lenguaje natural o considerando información contextual adicional para personalizar los datos recuperados.

- **Interfaz de usuario:** Aunque el sistema cuenta con una interfaz funcional, podría beneficiarse de mejoras en términos de usabilidad y experiencia del usuario. Se podría considerar la implementación de características adicionales, para mejorar la satisfacción del usuario.

- **Evaluación del modelo:** Se necesita una evaluación más exhaustiva del rendimiento del modelo implementado. Además de métricas estándar como precisión y recall, sería útil realizar pruebas de usuario y análisis de retroalimentación para comprender mejor cómo los usuarios interactúan con el sistema y cómo se pueden realizar mejoras adicionales en función de sus necesidades y comentarios.






