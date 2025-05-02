#Práctico 2: Git y GitHub 
#Actividades 1) Contestar las siguientes preguntas utilizando las guias y documentacion proporcionada.

#¿Qué es GitHub? 

Git es una plataforma en  linea que se utiliza para trabajos colaborativos en los que se puede compartirar y guardar proyectos de software, es como una red social pero se suben proyectos de programacion.

#¿Cómo crear un repositorio en GitHub? Primero vas a la pagina de github.com, inicias sesion, vas al boton "NEW", nombras el repositorio como prefieras, clickeas en "create repository" luego en la consola git bash colocas "git init" para iniciar un repositorio en github.

luego con el comando "git add ." para agregar todos los archivos y carpetas para que git registre sus cambios, luego con el comando "commit -m" para registrar los cambios y despues tener puntos donde volver atras y ver cuando se hicieron lso cambios en el proyecto con un mensaje, tambien tener que configurar la ruta de usuario usanto los comandos "git config --global user.email (mail)" y el comando "git config --global user.name (nombre)", luego copias el comando proportcionado en la pagina de github una vez creado el repositorio para vincular el archivo.

#¿Cómo crear una rama en Git? 

Abrimos la consola de git, creamos una rama nueva con el comando "git branch (nombre de la rama nueva)" luego para trabajar sobre la nueva rama tenes que utilizar el comando "git checkout (nombre de la rama a trabajar)"

#¿Cómo fusionar ramas en Git?

Nos posicionamos en la rama principal y luego con el comando "git merge (nombre de la rama)".

#¿Como crear un commit en Git?

Primero agregamos todos los archivos modificados con el comando "git add ." luego creamos el commit con el comando "git commit -m (nombre para el commit)" y para subir el archivo a git tenes que colocar el comando "git push origin (nombre de la rama)"

<<<<<<< HEAD
=======
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

Ingresas al fork desde la pagina de git, clickeas en el cartel que dice "Pull requests" y elegis "Newpull request".

#¿Qué es un etiqueta en Git? 

Una etiqueta en git un comentario o tag que sirve para guiarte en un punto epecifico del proyecto. 

#¿Cómo crear una etiqueta en Git? 

Podes crear una etiqueta con "git tag (nombre de la etiqueta)" para marcar el ultimo commit automaticamente.

#¿Cómo enviar una etiqueta a GitHub?

Con el comando "git push origin --tags".

#¿Qué es un historial de Git? 

Es el registro de cambios que se hicieron en el trabajo y sirve para no perderse. 

#¿Cómo ver el historial de Git? 

Para ver el historial usas el comando "git reflog".
#¿Cómo buscar en el historial de Git?

El comando "git log" tiene varias formas de busqueda, puede ser por mensaje con el comando "git log --grep= (palabra)", tambien podes buscar por archivo o commits por autor

#¿Cómo borrar el historial de Git? 

Creas una rema nueva y borras el repositorio anterior luego forzas el push para guardar nuevos commits.

#¿Qué es un repositorio privado en GitHub? 

Un repositorio privado es un repositorio que solo yo o las personas autorizadas por mi pueden revisar el repositorio. 

#¿Cómo crear un repositorio privado en GitHub? 

Cuando creas el repositorio solo tenes que seleccionar si lo queres crear publico o privado.

#¿Cómo invitar a alguien a un repositorio privado en GitHub? 

Vas a la configuracion del repositorio, en la parte de colaboradores, agregar usuario y agregas el nombre de usuario o el mail de git, luego seleccionas el nivel de permisos si de lectura o de escritura y lectura.

#¿Qué es un repositorio público en GitHub? 

Es un repositorio que cualquier persona con o sin cuenta de git puede ingresar y ver el repositorio, incluyendo archivos, historial de cambios y ver el codigo. 

#¿Cómo crear un repositorio público en GitHub?

Es de la misma forma que creas un repositorio privado pero seleccionas la opcion de Publico. 

#¿Cómo compartir un repositorio público en GitHub?

Copias el url desde git y pegas donde lo quieras compartir. 

>>>>>>> 8fa9a22 (Se agrego archivo txt y se agrego en py todas las preguntas del cuestionario)
