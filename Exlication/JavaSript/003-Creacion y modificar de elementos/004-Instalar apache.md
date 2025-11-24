En terminal:

sudo apt install apache2

DE ahi en adelante ,todos los archivos que habias tendran que estan /var/www/html

/var/www/html

Liberación de permisos:

cd /var/www
cd = change directory (win Linux macOS)
sudo chmod 777 -R html

sudo = El super usuario va a hacer algo
chmod = cambiamos permisos de archivo y carpeta
777 = los tres grupos pueden hacer de todo
-R = recursivo (se aplica a todo lo contenido)
html = la carpeta de destino