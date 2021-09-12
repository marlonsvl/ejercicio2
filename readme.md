# Aplicación sobre el ejercicio2 para la posicion de Lide Tecnológico

Esta aplicación se basa en obtener datos de (dweet.io) usando thecore, la idea es obtener los valores temperature y humidity y almacenarlos en una base de datos. Estos valores deben obtenerse cada minuto durante 15 minutos y golpear el webhook con todos los valores almacenados en la base de datos

## Instalación

La aplicación se ha desarrollado usando [*Dweepy*](https://github.com/paddycarey/dweepy) 

Las librerías se instalan usando el archivo requerimientos.txt. Se puede ejecutar la siguiente línea
en el terminal

`pip install -r requerimientos.txt`

## Configuración

Al estar en un ambiente en producción nos ubicamos en la carpeta *ejercicio2* y ejecutamos 

`python retriever.py`

Esto obtiene los datos y golpea al webhook (https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9)

Eso es todo!!




