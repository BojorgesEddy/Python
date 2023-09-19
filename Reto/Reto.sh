#! /bin/bash

mkdir -p Taller_clase_3/Archivos/Textos_planos
mkdir -p Taller_clase_3/Archivos/Pdf
mkdir -p Taller_clase_3/Mover_imagen_aqui

cd ./Taller_clase_3/Archivos/Textos_planos
touch Texto_plano1.txt
touch Texto_plano2.txt

cd ..
cd ./Pdf
url=https://training.github.com/downloads/es_ES/github-git-cheat-sheet.pdf
curl -o Explicaciones.pdf $url

cd ..
cd ..
url=https://e00-elmundo.uecdn.es/assets/multimedia/imagenes/2018/03/28/15222363072573.jpg
curl -o Imagen1.jpg $url

mv Imagen1.jpg ./Mover_imagen_aqui

tree ./ > estructura.txt


