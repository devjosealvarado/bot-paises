from urllib import response
import discord

from dotenv import load_dotenv
import os

import requests

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$calc'):
        operation = message.content.split(' ')[1]
        
    if message.content.startswith('$pais'):
        
        otra = str(message.content.split(' ')[1])
        country = otra.replace('-', ' ')
        response_raw = requests.get(f'https://restcountries.com/v3.1/name/{country}')
        response = response_raw.json()
        
        print(response[0]['capital'])

        # try:
        #     getattr(response[0], 'capital')         
        # except AttributeError:
        #     print ("Doesn't exist")
        # elif:
        #     print ("Exists")
        
        country_name = response[0]['name']['common']
        flag = response[0]['flags']['png']
 #       capital_name = response[0]['capital'][0]
        region = response[0]['region']
        population = response[0]['population']
        lat = response[0]['latlng'][0]
        long = response[0]['latlng'][1]

        response_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&lang=es&appid=a305efb8c52bdd249b267b26eef91154')
        response_weather_f = response_weather.json()
        temp = format(response_weather_f['main']['temp'] - 273.15, ".2f")
        weather_current = response_weather_f['weather'][0]['description']
        id_icon_weather = response_weather_f['weather'][0]['icon']
        icon_weather = f'http://openweathermap.org/img/wn/{id_icon_weather}@2x.png'
        

        await message.channel.send(country_name)
        await message.channel.send(flag)
  #      await message.channel.send(f'Capital: {capital_name}')
        await message.channel.send(f'Región: {region}')
        await message.channel.send(f'Población: {population}')
        await message.channel.send(f'Temperatura actual: {temp} C°')
        await message.channel.send(f'Clima actual: {weather_current}')
        await message.channel.send(icon_weather)
    
    if message.content.startswith('$help'):
        await message.channel.send('''
        *Comandos*:
            $pais: Para llamar a un pais debes colocar el comando $pais seguido del nombre del cual quieres saber información
        ''')

client.run(os.environ['TOKEN'])