#Práctico 2: Git y GitHub 
#Actividades 1) Contestar las siguientes preguntas utilizando las guias y documentacion proporcionada.

#¿Qué es GitHub? 

Git es una plataforma en  linea que se utiliza para trabajos colaborativos en los que se puede compartirar y guardar proyectos de software, es como una red social pero se suben proyectos de programacion.

#¿Cómo crear un repositorio en GitHub? 

Primero vas a la pagina de github.com, inicias sesion, vas al boton "NEW", nombras el repositorio como prefieras, clickeas en "create repository" luego en la consola git bash colocas "git init" para iniciar un repositorio en github.

#¿Cómo crear una rama en Git? 

Abrimos la consola de git, creamos una rama nueva con el comando "git branch (nombre de la rama nueva)" luego para trabajar sobre la nueva rama tenes que utilizar el comando "git checkout (nombre de la rama a trabajar)"

#¿Cómo fusionar ramas en Git?

Nos posicionamos en la rama principal y luego con el comando "git merge (nombre de la rama)".

#¿Cómo crear un commit en Git?

Primero agregamos todos los archivos modificados con el comando "git add ." luego creamos el commit con el comando "git commit -m (nombre para el commit)"

#¿Cómo enviar un commit a GitHub? 

Para subir el archivo a git tenes que colocar el comando "git add ." para agregar todos los archivos modificados, luego con el comando "commit -m" para registrar los cambios y despues tener puntos donde volver atras y ver cuando se hicieron lso cambios en el proyecto con un mensaje, luego usar el comando "git push origin master" para subir el commit en github.

#¿Qué es un repositorio remoto? 

Es un lugar donde guardar una copia de un proyecto de software, es una version guardada en una nube como github.

#¿Cómo agregar un repositorio remoto a Git? 

Se agregan con el comando "git remote add origin url"

#¿Cómo empujar cambios a un repositorio remoto? 

Se empujan los cambios con el comando "git push -u origin master"

#¿Cómo tirar de cambios de un repositorio remoto?

Se tiran cmabios con el comando "git fetch"

#¿Qué es un fork de repositorio? 

Un fork es una copia del repositorio de otra persona en tu cuenta de GitHub

#¿Cómo crear un fork de un repositorio? 

Ingresas al repositorio que queres hacer Fork, luego clickeas en la opcion "fork", elegis si es en tu cuenta o una organizacion y listo. 

#¿Cómo enviar una solicitud de extracción (pull request) a un repositorio? 