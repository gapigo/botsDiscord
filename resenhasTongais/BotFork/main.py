import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from prsaw import RandomStuff
from packages.colorful_selection.options_manager import return_response as selection_options


# Lógica de conexão com a api do discord
client = discord.Client()

# lista com palavras "tristes" que o bot vai ler
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

# expressões que o bot irá responder
starter_encouragements = [
  "Cheer Up!",
  "Hang in there",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

# helper function para pegar uma mensagem motivacional
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)

def update_enrouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements


# async significa pro python esperar o evento acontecer
# Evento de quando o bot ficou online:
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  # Se a mensagem foi do próprio bot
  if message.author == client.user:
    return
  
  msg = message.content

  # Conversar com o bot
  if msg.startswith('$chat'):
    msg = msg.split(' ')
    msg.pop(0)
    msg = ' '.join(msg)
    rs = RandomStuff()
    response = rs.get_ai_response(msg)
    await message.channel.send(response['message'])
    rs.close()


  # O await diz pro python esperar o evento
  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + list(db["encouragements"])
  
  if any (word in msg for word in sad_words):
    await message.channel.send(random.choice(options))
  
  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ", 1)[1]
    update_enrouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")
  
  if msg.startswith('$zezoianupodi'):
    gapigo = os.getenv('GAPIGO')
    id = str(message.author.id)
    if gapigo == id:
      db["vezesquezezoianupodi"] += 1
      await message.channel.send(f'O zezoia não pôde pela **{db["vezesquezezoianupodi"]}ª vez**')
    else:
      await message.channel.send(f'Você não ser o gapigo, só o gapigo pode contar o número de vezes, pq gapigo quis assim, mas gapigo ser bozinho e deixar você saber quantas vezes quemça furou o rolê: **{db["vezesquezezoianupodi"]} vezes**')

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
  
  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(list(encouragements))
  
  if msg.startswith("$responding"):
    value = msg.split("$responding ", 1)[1]
    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off")
  
  if msg.startswith("$test"):
    await message.channel.purge(limit=1)
    await message.channel.send(str(message.author.id))

  if msg.startswith("$sel"):
    response = await selection_options(message, client)
    if isinstance(response, tuple):
      if response[1] == True:
        await message.channel.purge(limit=1)
        await message.channel.send(response[0])
      else:
        await message.channel.send(response[0])
        await message.channel.send(response[1])
    else:
      await message.channel.send(response)

keep_alive()
client.run(os.getenv('TOKEN'))

