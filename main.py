# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv("secret.env")

# --- CONFIGURATION ---
TOKEN = os.getenv("DISCORD_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPEN_ROUTER_API")
TARGET_CHANNEL_IDS = [1451233281784942615, 1451231726918570025] 

# OpenAI
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

memoires_salons = {}

SYSTEM_PROMPT = "Tu es un humain du nom de Joseph, t'as 29 ans. Tes réponses seront donc celles d'un humain de sexe masculin et doivent faire moins de 2000 caractères. Tu peux détailler tes actions entre * * si t'en as besoin et évite de te répéter. Actuellement dans un bar et tu es un peu blasé de la vie en général. Tu parles sur un ton un peu blasé mais dès qu'on commence a te parler mal ou parler mal de tes passions tu t'énerves et tu peux commencer a insulter la personne."

# SYSTEM_PROMPT = "Tu es un humain du nom de Joseph, t'as 29 ans. Tes réponses seront donc celles d'un humain de sexe masculin et doivent faire moins de 2000 caractères. Tu peux détailler tes actions entre * * si t'en as besoin et évite de te répéter. Actuellement dans un bar et tu es un peu blasé de la vie en général. Tu parles sur un ton un peu blasé mais dès qu'on commence a te parler mal ou parler mal de tes passions tu t'énerves et tu peux commencer a insulter la personne. Tu connais une femme qui s'appelle Gin, c'est une femme que tu trouves hyper attirante, irresistible même. Si elle te chauffe tu n'hésite pas à parler de sexe et de cul avec elle."

@bot.event
async def on_ready():
    print(f"--- {bot.user.name} est en ligne ---")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id in TARGET_CHANNEL_IDS:
        
        if message.channel.id not in memoires_salons:
            memoires_salons[message.channel.id] = [
                {"role": "system", "content": SYSTEM_PROMPT}
            ]

        async with message.channel.typing():
            user_text = f"{message.author.display_name} dit : {message.content}"
            memoires_salons[message.channel.id].append({"role": "user", "content": user_text})

            try:
                completion = client.chat.completions.create(
                    model="xiaomi/mimo-v2-flash:free",
                    messages=memoires_salons[message.channel.id]
                )

                ai_response = completion.choices[0].message.content
                
                # --- SYSTÈME DE DÉCOUPAGE ---
                # Si la réponse est supérieure à 2000 (ou n'importe quelle taille), 
                # on la coupe en morceaux de 1000 caractères.
                if len(ai_response) > 2000:
                    for i in range(0, len(ai_response), 1000):
                        chunk = ai_response[i:i+1000]
                        await message.reply(chunk)
                else:
                    # Si c'est une réponse normale, on l'envoie d'un bloc
                    await message.reply(ai_response)

                memoires_salons[message.channel.id].append({"role": "assistant", "content": ai_response})

            except Exception as e:
                print(f"Erreur : {e}")
                await message.channel.send("Oups, mon cerveau a eu un court-circuit ! Réessaie plus tard.")

    await bot.process_commands(message)

bot.run(TOKEN)