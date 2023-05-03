import openai
import requests
import typer
from rich import print
from rich.table import Table
from pydub import AudioSegment
from pydub.playback import play
import os 
from playsound import playsound




# URL de la API de texto a voz
TTS_API_URL = 'https://api.elevenlabs.io/v1/text-to-speech/D-DE-LA-VOZ-CLONADA'

# Cabeceras de la solicitud HTTP
TTS_API_HEADERS = {
    'accept': 'audio/mpeg',
    'xi-api-key': 'TU-API-KEY-ELEVENLABS',
    'Content-Type': 'application/json'
}

def main():
    
    openai.api_key = "TU-API-KEY"
    print("💬 [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir")
    table.add_row("new", "Crear una nueva conversación")

    print(table)
    audio_file = AudioSegment.from_file("audio/bienvenida.mp3", format="mp3")
    play(audio_file)
    # Contexto del asistente
    context = {"role": "system", "content": "You are helpful assistant on a conversation. Answer shoul be short and concise."}
    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        # Generar el audio con la respuesta del asistente virtual y reproducirlo
        response = requests.post(TTS_API_URL, headers=TTS_API_HEADERS, json={
            'text': response_content, 
            'model_id': 'eleven_multilingual_v1', 
            'voice_settings': {'stability': 0.38, 'similarity_boost': 1}
        })
        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
        if response.status_code == 200:
            with open("speech.mpeg", "wb") as f:
                f.write(response.content)
            playsound("speech.mpeg", True)
            os.remove("speech.mpeg")
            
        else:
            print("Request failed with status code:", response.status_code)
            print("Response content:", response.content)
            return False
        

def __prompt() -> str:
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")
    
    if prompt == "exit":
        audio_file = AudioSegment.from_file("audio/estas_seguro.mp3", format="mp3")
        play(audio_file)
        exit = typer.confirm("✋ ¿Estás seguro?")
        
        if exit:
            audio_file = AudioSegment.from_file("audio/hasta_luego.mp3", format="mp3")
            play(audio_file)
            print("👋 ¡Hasta luego!, que tengas un buen día")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)