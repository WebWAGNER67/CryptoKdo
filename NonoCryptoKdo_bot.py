from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import logging

# Configurez le niveau de journalisation
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Remplacez 'YOUR_TELEGRAM_BOT_API_TOKEN' par le token de votre bot
TOKEN = 'TOKEN'

# Liens vers les sujets spécifiques dans votre groupe Telegram
LINKS = {
    'category_farming': 'https://t.me/Airdrops_CryptOKdo/7/18',  # Remplacez par le lien réel vers le sujet "Farming"
    'category_tap_to_earn': 'https://t.me/Airdrops_CryptOKdo/3/19',  # Remplacez par le lien réel vers le sujet "Tap to Earn"
    'category_play_to_earn': 'https://t.me/Airdrops_CryptOKdo/5/20',  # Remplacez par le lien réel vers le sujet "Play to Earn"
    'category_swipe_to_earn': 'https://t.me/Airdrops_CryptOKdo/46/48'  # Remplacez par le lien réel vers le sujet "Swipe to Earn"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Afficher les catégories de jeux", callback_data='show_categories')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Envoi d'un nouveau message
    await update.message.reply_text(
        'Bienvenue! Utilisez le bouton ci-dessous pour afficher les catégories de jeux.',
        reply_markup=reply_markup
    )

async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Farming", callback_data='category_farming')],
        [InlineKeyboardButton("Tap to Earn", callback_data='category_tap_to_earn')],
        [InlineKeyboardButton("Play to Earn", callback_data='category_play_to_earn')],
        [InlineKeyboardButton("Swipe to Earn", callback_data='category_swipe_to_earn')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Utilisation de edit_message_text pour mettre à jour le message existant
    query = update.callback_query
    await query.answer()
    try:
        await query.edit_message_text(
            'Choisissez une catégorie de jeux:',
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Erreur lors de l'édition du message : {e}")

async def handle_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    link = LINKS.get(query.data, None)
    category_name = {
        'category_farming': 'Farming',
        'category_tap_to_earn': 'Tap to Earn',
        'category_play_to_earn': 'Play to Earn',
        'category_swipe_to_earn': 'Swipe to Earn'
    }.get(query.data, 'Unknown Category')

    if link:
        # Formate le texte avec un lien intégré
        message_text = f"Cliquez sur le lien : [{category_name}]({link})"
        try:
            await query.edit_message_text(
                text=message_text,
                parse_mode='Markdown'
            )
        except Exception as e:
            logger.error(f"Erreur lors de l'édition du message : {e}")
    else:
        await query.edit_message_text(text="Désolé, une erreur s'est produite.")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    if query.data == 'show_categories':
        await show_categories(update, context)
    else:
        await handle_category(update, context)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    # Ajouter le gestionnaire pour la commande /start
    application.add_handler(CommandHandler('start', start))
    
    # Ajouter le gestionnaire pour les interactions des boutons
    application.add_handler(CallbackQueryHandler(button))
    
    application.run_polling()

if __name__ == '__main__':
    main()
