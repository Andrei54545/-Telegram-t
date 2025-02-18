from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Токен вашего бота
TOKEN = 'ВАШ_ТОКЕН_ЗДЕСЬ'

# Команда /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я твой бот. Как дела?')

# Команда /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Вот что я могу:\n/start - начать общение\n/help - показать помощь')

# Приветствие новых участников
def greet_new_members(update: Update, context: CallbackContext) -> None:
    for user in update.message.new_chat_members:
        update.message.reply_text(f'Привет, {user.first_name}! Добро пожаловать в группу!')

# Основная функция
def main() -> None:
    # Инициализация бота
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Регистрируем обработчик новых участников
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, greet_new_members))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()