import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from movie_search import get_movie_download_link
from config import BOT_TOKEN

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi! Send me the name of the movie you want to download.")

# Search for the movie and send download link
def search_movie(update: Update, context: CallbackContext):
    movie_name = update.message.text
    update.message.reply_text(f"Searching for {movie_name}...")
    
    # Get the download link (this is just a placeholder)
    download_link = get_movie_download_link(movie_name)
    
    if download_link:
        update.message.reply_text(f"Here is your download link: {download_link}")
    else:
        update.message.reply_text("Sorry, I couldn't find a download link for that movie.")

# Error handler
def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Create Updater and pass in your bot's token.
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_movie))

    # Log all errors
    dp.add_error_handler(error)

    # Start polling for updates
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
