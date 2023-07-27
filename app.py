
import chainlit as cl
import requests

API_URL = "https://flowiseai-docker.onrender.com/api/v1/prediction/a396d64e-8a11-4467-88dc-df31507ce447"

@cl.on_message
async def main(message: str):
    # Your custom logic goes here...
   
    response = requests.post(API_URL, 
                             json={"question": message})  
    
    # Send a response back to the user
    await cl.Message(
        content=response.text
    ).send()
