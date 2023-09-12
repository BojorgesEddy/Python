#! /bin/bash

read -p "Introduce tu edad: " age
echo "Tu edad es de $age"

: '
    Comentario multilinea

    -eq : igual (equal)}
    -le : lower or equal
    -ge : Grether or equal
    -lt : Lower than
    -gt : Grether than
'

if (( $age >= 31 ))
    then
        echo "Tienes 31 o mas"
elif [[ $age -eq 30  || $age -eq 29 ]]
    then
        echo "Eres Treintañero"
else
    echo "No tienes 20 años"
fi


: '
if [ $age -ge 31 ]
    then
        echo "Tienes 31 o mas"
elif [[ $age -eq 30  || $age -eq 29 ]]
    then
        echo "Eres Treintañero"
else
    echo "No tienes 20 años"
fi
'


    
