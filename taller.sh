#! /bin/bash

mkdir -p ./Taller_clase_3/Archivos 
mkdir -p ./Taller_clase_3/Mover_Imagen1_aqui

cd ./Taller_clase_3/Archivos
touch Texto_plano.txt
echo "Hola Texto_plano" > Texto_plano.txt
cd Texto_plano.txt ./Copia_texto_plano.txt

cd ..
url=https://www.tecnologia-informatica.com/wp-content/uploads/2018/01/que-es-meme-como-hacer-memes-1.jpg
curl -o Imagen1.jpg $url 

mv Imagen1.jpg ./Mover_Imagen1_aqui

tree ./ > estructura.txt