import openai
import discord

client = discord.Client()
openai.api_key = "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"

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ai'):
        prompt = message.content[6:]
        completions = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = completions.choices[0].text
        await message.channel.send(message)

client.run('MTA5MTMyMjg3NjY2MzE4OTU5NA.GRmhLU.E2M7QaVZrnvv5iCmMHifTXU5B3TJh1Wv4d1Nz0')
