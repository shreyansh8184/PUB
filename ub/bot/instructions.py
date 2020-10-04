from ub import app
from pyrogram import filters

@app.on_message(filters.me & filters.command(["payment"], "."))
async def payment(client, message):
    await message.edit(PAYMENT_DETAILS)

@app.on_message(filters.me & filters.command(["how"], "."))
async def how(client, message):
    await message.edit(HOW)

@app.on_message(filters.me & filters.command(["cod"], "."))
async def cod(client, message):
    await message.edit(COD)

@app.on_message(filters.me & filters.command(["cod"], "."))
async def format(client, message):
    await message.edit(FORMAT)



