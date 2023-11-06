
## ¡Bienvenido/a al proyecto de darle voz a ChatGPT utilizando tu propia voz clonada!

Este proyecto utiliza los servicios de Elevenlabs para crear una voz clonada y darle una voz humana a ChatGPT. En lugar de leer las respuestas en formato de texto, podrás escuchar las respuestas con una voz sintetizada, lo que mejora la experiencia de usuario y facilita la comprensión.


## Características

- ChatGPT con voz
- Mayor facilidad para comprender las respuestas
- Experiencia de usuario mejorada

## Requisitos
- Tener una cuenta en OpenAI (Para obtener la API-KEY)
- Tener una cuenta en Elevenlabs (Para clonar la voz y obtener la API-KEY)
- Tener un editor de texto para configurar tus API keys
- Tener instalado Python
- Tener instalado Git

Para obtener la API key de OpenAI, los usuarios deberán seguir los siguientes pasos:

1. Crear una cuenta en la página web de OpenAI (https://platform.openai.com/account/api-keys).
2. Acceder al panel de control y crear una nueva API key
3. Copiar la API key generada para utilizarla en el proyecto

Para obtener la API key de Elevenlabs, los usuarios deberán seguir los siguientes pasos:

1. Crear una cuenta en la página web de Elevenlabs (https://beta.elevenlabs.io).
2. Acceder al panel de control y crear una nueva API key
3. Copiar la API key generada para utilizarla en el proyecto

Para instalar los requisitos necesarios, los usuarios deberán seguir los siguientes pasos:

1. Descargar o clonar el repositorio del proyecto en su sistema
2. Acceder a la carpeta del proyecto utilizando la terminal
3. Ejecutar el comando "pip install -r requirements.txt" para instalar las dependencias necesarias

Con estos requisitos cumplidos, los usuarios podrán utilizar el proyecto para clonar la voz y utilizar ChatGPT con voz clonada.

## Instalación


1. Descargar o clonar el repositorio del proyecto en su sistema:

Para clonar el repositorio utilizando (Git), ejecute el siguiente comando en su terminal:

``` bash
git clone https://github.com/gadivalr/ChatbotIA.git
```


2. Acceder a la carpeta del proyecto utilizando la terminal:

Una vez que el repositorio se haya clonado o descargado en su sistema, acceda a la carpeta del proyecto utilizando el siguiente comando:

``` bash
cd proyecto
```

Reemplace "proyecto" con el nombre de la carpeta del proyecto que acabas de clonar o descargar.

3. Ejecutar el comando "pip install -r requirements.txt" para instalar las dependencias necesarias:

Para instalar las dependencias del proyecto, ejecute el siguiente comando en su terminal:

``` bash
pip install -r requirements.txt
```

Este comando instalará todas las dependencias necesarias para el proyecto que se encuentran en el archivo "requirements.txt"

Una vez que haya completado estos tres pasos, su proyecto estará casi listo para usar solo nos queda configurar las APIS KEYS.

## Configuración
Para configurar la API key de OpenAI y la API key de Elevenlabs en el proyecto, deberás seguir los siguientes pasos:


- Busca la línea que contiene "openai.api_key" y reemplaza "TU-API-KEY" con la API key que obtuviste de OpenAI.

``` python
openai.api_key = "TU-API-KEY"
```

- Busca la línea que contiene "xi-api-key" y reemplaza "TU-API-KEY-ELEVENLABS" con la API key que obtuviste de Elevenlabs.

``` python
'xi-api-key': 'TU-API-KEY-ELEVENLABS',
```

- Busca la línea que contiene "https://api.elevenlabs.io/v1/text-to-speech/" y agrega el ID de la voz clonada que quieres utilizar al final de la URL.

``` python
'https://api.elevenlabs.io/v1/text-to-speech/ID-DE-LA-VOZ-CLONADA'
```

Reemplaza "ID-DE-LA-VOZ-CLONADA" con el ID de la voz clonada que quieres utilizar. Este ID lo encontrarás ejecutando el siguiente comando:

``` python
import requests

url = "https://api.elevenlabs.io/v1/voices"

headers = {
  "Accept": "application/json",
  "xi-api-key": "TU-API-KEY-ELEVENLABS"
}

response = requests.get(url, headers=headers)

print(response.text)
```
Te aparecerán todas las voces que puedes usar con sus respectivos "voice_id"

Una vez que hayas completado estos pasos, ya tendrás configuradas las API keys necesarias y el ID de la voz clonada para utilizar en tu proyecto.
## Ejecutar 
Lo ejecutamos con el siguiente comando
``` bash
python chat.py
```


## Licencia

Este proyecto está bajo una licencia de código abierto y es gratuito para su uso y modificación.
