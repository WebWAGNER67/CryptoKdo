<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://scontent-fra5-2.xx.fbcdn.net/v/t39.30808-1/450332430_10234490213624715_3695103274582084169_n.jpg?stp=dst-jpg_p200x200&_nc_cat=107&ccb=1-7&_nc_sid=f4b9fd&_nc_ohc=mUuWYy97v-EQ7kNvgGb2cO0&_nc_ht=scontent-fra5-2.xx&oh=00_AYBWHf2d2QlRqnetNz_m56oVqj7AHtxRx5Qk6kfsHoEjbQ&oe=66B45F77" alt="Bot logo"></a>
</p>

<h3 align="center">CryptoKdo BOT Telegram Python</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Platform](https://img.shields.io/badge/platform-telegram-blue.svg)](https://t.me/Airdrops_CryptOKdo)
[![GitHub Issues](https://img.shields.io/github/issues/WebWAGNER67/CryptoKdo.svg)](https://github.com/WebWAGNER67/CryptoKdo/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/WebWAGNER67/CryptoKdo.svg)](https://github.com/WebWAGNER67/CryptoKdo/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 🤖 This bot is designed to redirect users from one link to another in a telegram group where there are many channels.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Demo / Working](#demo)
- [How it works](#working)
- [Usage](#usage)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This bot was created as part of a Telegram group to better organize Crypto channels. The messages sent by the bot are only used to redirect the user.

## 🎥 Demo / Working <a name = "demo"></a>

![Working](https://media.giphy.com/media/20NLMBm0BkUOwNljwv/giphy.gif)

## 💭 How it works <a name = "working"></a>

The bot first extracts the word from the comment and then fetches word definitions, part of speech, example and source from the Oxford Dictionary API.

If the word does not exist in the Oxford Dictionary, the Oxford API then returns a 404 response upon which the bot then tries to fetch results form the Urban Dictionary API.

The bot uses the Pushshift API to fetch comments, PRAW module to reply to comments and Heroku as a server.

The entire bot is written in Python 3.6

## 🎈 Usage <a name = "usage"></a>

To use the bot, type:

```
/start
```

The bot will then give you the Welcome message.

### Example:

> /start

**Definition:**

Bienvenue! Utilisez le bouton ci-dessous pour afficher les catégories de jeux.
Afficher les catégories de jeux

---

<sup>Beep boop. I am a bot. If there are any issues, contact my [Master](mailto:wagner-fabien@orange.fr)</sup>

<sup>Want to make a similar telegram bot? Check out: [GitHub](https://github.com/WebWAGNER67/CryptoKdo)</sup>

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites <a name = "prerequis">

What things you need to install the software and how to install them.

```
pip install pyhton-dotenv
pip install python-telegram-bot --upgrade
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Create a new environment

```
python3 -m venv myenv
```

Connect to the environment

```
source myenv/bin/activate
```


Install de dependencies

[Prerequisites](#prerequis)

Run the bot

```
python ./main.py #Here ./NonoCryptoKdo.py
```

## ⛏️ Built Using <a name = "built_using"></a>

- [BotFather](https://t.me/@BotFather) - Create a Telegram bot

## ✍️ Authors <a name = "authors"></a>

- [Fabien WAGNER]() - Idea & Initial work
- [Eric WAGNER](https://github.com/WebWAGNER67) - Production start-up

See also the list of [contributors](https://github.com/WebWAGNER67/CryptoKdo/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- ChatGPT (Code helping)
- Eric WAGNER (Production)
