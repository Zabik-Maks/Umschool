import telebot

bot = telebot.TeleBot('6976617046:AAGHB1JUaHsypfZGGE6hHIsyYcbtOP4t0FA')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, "*Hello my friend. Let's begin our journey into a Python!*\nWrite this command firstly:\n/commands", parse_mode='Markdown')

@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'This is [My VK page](https://vk.com/zabik_maks)', parse_mode='Markdown')

@bot.message_handler(commands=['commands'])
def main(message):
    bot.send_message(message.chat.id, 'This is commands that you can use:\n/start\n/link\n/commands\n/if\n/for\n/while\n/continue\n/break\n/stop', parse_mode='Markdown')

@bot.message_handler(commands=['if'])
def main(message):
    bot.send_message(message.chat.id, '*if a == b:*\nIf any condition is true, the code after the colon will be executed.', parse_mode='Markdown')

@bot.message_handler(commands=['for'])
def main(message):
    bot.send_message(message.chat.id, '*for i in range(0, 5):*\nThis cycle will work a certain number of times prescribed in range. \nPlease note that the last number in range is not taken into account, since in python the count starts from 0.', parse_mode='Markdown')

@bot.message_handler(commands=['while'])
def main(message):
    bot.send_message(message.chat.id, '*while a != 0:*\nThe loop is still running until the condition inside it is met. \nPlease note that you need to have a changeable parameter otherwise the loop will be infinite.', parse_mode='Markdown')

@bot.message_handler(commands=['continue'])
def main(message):
    bot.send_message(message.chat.id, 'if a == 0:\n     *continue*\nThis command skips a step and the code will continue to execute.', parse_mode='Markdown')

@bot.message_handler(commands=['break'])
def main(message):
    bot.send_message(message.chat.id, 'if a == 0:\n     *break*\nThis command immediately stops the program in a certain place.', parse_mode='Markdown')

@bot.message_handler(commands=['stop'])
def main(message):
    bot.send_message(message.chat.id, 'Relax!\nWe all need some lemon water)))', parse_mode='Markdown')

bot.infinity_polling()
