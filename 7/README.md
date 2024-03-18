# Gestión de Programa de Lealtad App

### Objetivos

Proponer un reto técnico para candidatos que aspiren a los puestos de desarrollo de software. La tarea tratará de exponer las habilidades técnicas del candidato en varios rubros del ciclo de desarrollo:
- Lenguaje de programación: debe ser Java en versiones 8 o superiores con cualquier
  framework (preferentemente spring). Se evaluará las buenas prácticas, diseño y
  funcionalidad.
- Base de datos, utilizando cualquier manejador (preferentemente MySQL)
- Exposición de WebServices REST
- Habilidades de despliegue: indicar requisitos y guía de despliegue de la solución para su
  evaluación operativa.

### Reto

`Desafío:` Gestión de programa de lealtad

### Descripción

Debes desarrollar un backend que permita gestionar un programa de lealtad mediante servicios REST. El programa de lealtad se enfoca en la acumulación y canje de puntos por parte de los usuarios. La aplicación debe cumplir con los siguientes requisitos:

1. `Registro de usuarios:` Los usuarios deben poder registrarse en el programa de lealtad proporcionando un nombre de usuario único y una contraseña.
2. `Acumulación de puntos:` Los usuarios registrados deben poder acumular puntos realizando ciertas acciones (realizar compras). Las acciones que generan puntos pueden ser definidas previamente en la aplicación.
3. `Consulta de saldo de puntos:` Los usuarios deben poder consultar su saldo actual de puntos acumulados.
4. `Canje de puntos:` Los usuarios deben poder canjear sus puntos acumulados por recompensas. Las recompensas disponibles y su valor en puntos deben ser definidos previamente en la aplicación.

### Requisitos

- Utiliza Java (8 o superior) para desarrollar el backend.
- Utiliza el framework Spring Boot para crear una aplicación basada en Spring RESTful.
- Utiliza una base de datos relacional (por ejemplo, MySQL, PostgreSQL) para almacenar la información de los usuarios, puntos acumulados y recompensas.
- Implementa los controladores REST utilizando la anotación `@RestController` de Spring.
- Utiliza la anotación `@RequestMapping` para mapear las URL y los métodos HTTP a las operaciones correspondientes.
- Utiliza JPA (Java Persistence API) y Spring Data JPA para interactuar con la base de datos.
- El desarrollo deberá publicarse en cualquier plataforma de gestión de código (bitbucket, github,…)
- Parte del entregable deberá ser una guia de implementación que deberá incluir requisitos y pasos a seguir para desplegar el aplicativo.

### Ejemplo de estructura de datos:

`Usuario:`
- id (generado automáticamente)
- nombre de usuario (cadena de texto)
- contraseña (cadena de texto)

`Puntos:`
- id (generado automáticamente)
- usuario (referencia al usuario que acumuló los puntos)
- cantidad (número entero que representa la cantidad de puntos acumulados)

`Recompensa:`
- id (generado automáticamente)
- nombre (cadena de texto)
- valorEnPuntos (número entero que representa la cantidad de puntos requeridos para canjear la recompensa)

`Puntos extra:`

Si deseas agregar más complejidad al desafío, considera los siguientes puntos:

- El modo de depliegue como contenedor Docker. Con esto, además de la publicación del código en repositorio git, se requiere la publicación de la imagen del contenedor para descargarla y ejecutarla.
- Implementar autenticación y autorización de usuarios utilizando Spring Security.
- Agregar la capacidad de registrar y rastrear las acciones que generan puntos en la aplicación.
- Implementar pruebas unitarias para validar el funcionamiento de los servicios REST.

Recuerda proporcionar una solución bien estructurada y documentada, y asegúrate de que los servicios REST sean fácilmente consumibles por otros clientes. ¡Buena suerte con el desafío!