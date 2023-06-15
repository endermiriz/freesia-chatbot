
![Logo](https://github.com/endermiriz/freesia-chatbot/blob/main/image/FREESIACHATBOT.png?raw=true)

    
# About

This repository integrates ChatGPT, which is accessible within WhatsApp, using the OPENAI API. To use it, you need to first create an API key on OPENAI and then create a Twilio account to obtain a phone number.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
## Install

Clone the project.

```bash
git clone https://github.com/endermiriz/freesia-chatbot
```

Go to the project directory.

```bash
cd freesia-chatbot
```

Install the necessary packages.

```bash
pip install -r requirements.txt
```

If the Twilio configurations, OpenAI API key, and NGROK setup (or your own server and domain if available) have been configured beforehand, you can run the app.py file.

```bash
python app.py
```
  

**Make sure you have entered the API Key in the *`OPENAI_KEY`* variable in the *`.env`* file.**
## Before Using

- In order to use the repository, you need to acquire an **OpenAI API Key** first. > [OpenAI API](https://openai.com/blog/openai-api)

- Create a **Twilio account** and obtain a phone number for WhatsApp. Set up Twilio for WhatsApp using the acquired **phone number**. > [Twilio docs](https://www.twilio.com/docs/whatsapp)

- If you are going to use **NGROK**, you need to have a **registered account** and **download NGROK**. > [NGROK docs](https://ngrok.com/docs)

## Setup & Screenshots
### Setup
####  **1.** We need to create a *WEBHOOK URL* using *NGROK*. `ngrok http 8000` > [Twilio Docs for NGROK](https://www.twilio.com/blog/using-ngrok-2022)
![NGROK](https://github.com/endermiriz/freesia-chatbot/blob/main/image/1.png?raw=true)
####  **2.**.The URL that you see next to “*Forwarding*” is the publicly available URL that Ngrok assigned to the application. This URL can be used anywhere in the world. > [Twilio Docs for NGROK](https://www.twilio.com/blog/using-ngrok-2022)
![NGROK-URL](https://github.com/endermiriz/freesia-chatbot/blob/main/image/2.png?raw=true)

####  **3.** Go to the *Whatsapp Senders* section in the *Twilio Console* , enter the WEBHOOK URL we generated on NGROK in the designated field, and save the settings. > [Twilio Docs](https://www.twilio.com/docs/whatsapp )

![TWILIO](https://github.com/endermiriz/freesia-chatbot/blob/main/image/3.png?raw=true)

####  **3.** After completing all these steps, you can run the `app.py` file and start using **Freesia**.

### Screenshots
![WHATSAPP](https://github.com/endermiriz/freesia-chatbot/blob/main/image/Screenshot.png?raw=true)
