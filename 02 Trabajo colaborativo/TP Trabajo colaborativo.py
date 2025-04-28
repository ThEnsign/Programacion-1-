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

#¿Cómo crear un commit en Git?

Primero agregamos todos los archivos modificados con el comando "git add ." luego creamos el commit con el comando "git commit -m (nombre para el commit)" y para subir el archivo a git tenes que colocar el comando "git push origin (nombre de la rama)"

