import bot
import utils

utils.debugging = True

# text processing functions
def clean_capitalize(str):
    result = ""
    list_of_words = str.split()
    for elem in list_of_words:
        if len(result) > 0:
            result = result + " " + elem.strip().capitalize()
        else:
            result = elem.capitalize()
    if not result:
        return str
    return result

# main bot function
if __name__ == "__main__":
    # run
    #message = "how much 40mm to kill trench"
    #print(parse.slang_dict)
    #implement move string to rear
    #print(move_string_to_rear("how many 40 to kill entrenched bb 3x2"))
    #print(bot.handle_response(message))
    bot.run_discord_bot()
