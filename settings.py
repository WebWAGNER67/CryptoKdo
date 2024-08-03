import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

LINKS = {
    'category_farming': 'https://t.me/Airdrops_CryptOKdo/7/18',  # Remplacez par le lien réel vers le sujet "Farming"
    'category_tap_to_earn': 'https://t.me/Airdrops_CryptOKdo/3/19',  # Remplacez par le lien réel vers le sujet "Tap to Earn"
    'category_play_to_earn': 'https://t.me/Airdrops_CryptOKdo/5/20',  # Remplacez par le lien réel vers le sujet "Play to Earn"
    'category_swipe_to_earn': 'https://t.me/Airdrops_CryptOKdo/46/48'  # Remplacez par le lien réel vers le sujet "Swipe to Earn"
}