#!/bin/python3
# github.com/MrHacker-X

from telethon import TelegramClient, events
import openai

openai.api_key = 'openai_api_key'
api_id = 123456
api_hash = 'telegram_id_api_hash'
phone = '+9x_telegram_number'

client = TelegramClient('session1', api_id, api_hash)

async def main():
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        await client.sign_in(phone, input('Enter the code: '))

    print("Bot activated")
    @client.on(events.NewMessage)
    async def handle_new_message(event):
        sender = await event.get_sender()
        if not sender.bot and not sender.is_self:
            print(f"New message from {sender.username}: {event.text}")

            prompt = event.text
            response = openai.Completion.create(
                model='gpt-3.5-turbo-instruct',
                prompt=prompt,
                max_tokens=3048,
                top_p=1.0,
                presence_penalty=0.0
            )

            generated_response = response['choices'][0]['text']
            await event.reply(generated_response)
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
  
