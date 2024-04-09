
def start_message(username: str):
    return "Welcome <b>{username}!</b>\nThis is 📺 TransleerBOT talking... \nI'm going to help anyone who needs to translate your group's messages in real time.\n Just add me to your groups and learn the main commands. \n /help".replace("{username}", username)

def not_replying_error_message():
    return "❌ You must reply to a message in order to translate it"

def unspecified_language_error_message():
    return "❌ No language specified. (/translate &lt;language&gt;)"

def general_error_message(error: str):
    return "❌ " + error


def help_message():
    return "<b>IMPORTANT:</b> <i>You must reply to a message in order to perform these commands.</i>\n\n<b>•</b> <i>/translate &lt;language&gt;</i>\n<b>•</b> <i>/tr &lt;language&gt;</i>"