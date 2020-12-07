# PotatoBot [![Build Status] 

# Requirements
You must have Python 3 to launch server. Also before launching you have to install requirements via pip3:
```Bash
pip3 install -r requirements.txt
```

Than you have to create `config.py`:

```Python
# Token of your telegram bot
# (https://core.telegram.org/bots#6-botfather)
TELEGRAM_TOKEN = 'Your token'

# Credtals for logging to vk
VK_LOGIN = 'bot@bot.ry'
VK_PASS = 'bot_password'

# List of admins and moders
# Example: [ '66303244', 'vk1' ]
ADMINS_IDS = [  ]
MODERS_IDS = ADMINS_IDS + [  ]

DATABASE_PATH = 'db.json'
USERS_PATH = 'users'
```

You don't have to write vk login and pass, if you wouldn't use it. Same with telegram token.

# Launching

To launch telegram bot:
```Bash
python3 ./main.py
```

or

To launch vk bot:
```Bash
python3 ./main_vk.py
```

You can also build all bot to pyc files (Just for fun):
```Bash
python3 ./build.py
cd build
python3 main.pyc
```

That's it.
My VK https://vk.com/id94357295
"# PotatoMMORPG-bot" 
"# PotatoMMORPG-bot" 
