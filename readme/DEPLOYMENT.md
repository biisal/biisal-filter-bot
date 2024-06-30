# Atfirst we need some requirements to deploy our bot

<h3 align="center" style="color:skyblue">IMPORTANT THINGS</h3>

- Atfist get <b>Telegram APP ID or API ID</b> And <b> APP HASH or API HASH</b> from [Here](https://my.telegram.org/auth?to=apps)

- Get a <b>Bot Token</b> from [Here](https://telegram.me/BotFather)

- Obtain a <b>MongoDB connection string</b> from [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). If you're unsure how to create one, you can search for tutorials('how to make a mongodb connection string') on YouTube or ask for help in our support group at [Bisal Files Talk](https://t.me/Bisal_Files_Talk). Ensure that you've configured the IP whitelist to allow connections from anywhere (0.0.0.0/0).

- If you don't have a <b>File to Link</b> Bot Then You can make it from [Here](https://t.me/Bisal_Files_Talk) ,It will help you to <b>Stream</b> your files in Auto Filter Bot.
- <b style="color:red"> Don't public this things, Never !</b>

<hr>
<h3 align="center" style="color:skyblue">How Many Channels Do U Need ?</h3>

- You can use 1 channel for every Logs But My Suggestion is to use Atleast 4 private channels to handle all the logs.

<hr>
<h3 align="center" style="color:skyblue; font-size: 1.5em;">Required Configuration Fields</h3>

- **API_ID** <span style="color: green">#<i>get it from telegram app</i></span>
- **API_HASH** <span style="color: green">#<i>get it from telegram app</i></span>
- **BOT_TOKEN** <span style="color: green">#<i>get it from telegram app</i></span>
- **ADMINS** <span style="color: green">#<i>for 2 or more '12345678 89674523' add space between ids</i></span>
- **LOG_CHANNEL** <span style="color: green">#<i>add a private channel id</i></span>
- **CHANNELS** <span style="color: green">#<i>add your database channel id ,if u will share your file here the bot will add the file in database autometiccaly</i></span>
- **DATABASE_URI** <span style="color: green">#<i>if you dont know how to get it, read this documentation from scratch</i></span>
- **LOG_API_CHANNEL** <span style="color: green">#<i>add a private channel id</i></span>
- **DELETE_CHANNELS** <span style="color: green">#<i>Add a private channel id, This Channel is used to delete files from database, If you share your file here the bot will Delete the file from database autometiccaly</i></span>
- **URL** <span style="color: green">#<i>Your File to Link bot's Url</i></span>
- **LOG_VR_CHANNEL** <span style="color: green">#<i>add a private channel id</i></span>
- **TUTORIAL** <span style="color: green">#<i>a tutorial video link for Downloading files</i></span>
- **SHORTENER_API** <span style="color: green">#<i>add your first shortner api</i></span>
- **SHORTENER_WEBSITE** <span style="color: green">#<i>add your first shortner website url</i></span>
- **SHORTENER_API2** <span style="color: green">#<i>add your second shortner api</i></span>
- **SHORTENER_WEBSITE2** <span style="color: green">#<i>add your second shortner website url</i></span>
- **SHORTENER_API3** <span style="color: green">#<i>add your third shortner api</i></span>
- **SHORTENER_WEBSITE3** <span style="color: green">#<i>add your third shortner website url</i></span>
- **UPI_PAY_LOGS** <span style="color: green">#<i>add your telegram channel id to get payment screenshots</i></span>

# Example Code For Fillling Fields In info.py File

```py
API_ID = int(environ.get('API_ID', '12345678'))
API_HASH = environ.get('API_HASH', 'cgr055a6b7fhghgtddafb8bfdb8a3yty6')
BOT_TOKEN = environ.get('BOT_TOKEN', 'fvbuuferd:b4256terjhbhnbjfrh')
ADMINS = list(set(int(x) for x in environ.get('ADMINS', '12345678 89674523').split()))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001234567890'))
CHANNELS = list(set(int(x) for x in environ.get('CHANNELS', '-1001234567890 -1001234567890').split()))
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://username:password@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1001234567890'))
DELETE_CHANNELS = list(set(int(x) for x in environ.get('DELETE_CHANNELS', '-1001234567890 -1001234567890').split()))
URL = environ.get('URL', 'stream-bot-nv.urgent-gena.koyeb')
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1001234567890'))
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/bisal_files/12345')
SHORTENER_API = environ.get('SHORTENER_API', '34t54hgrfbhfdbn')
SHORTENER_WEBSITE = environ.get('SHORTENER_WEBSITE', 'shortslink.in')
SHORTENER_API2 = environ.get('SHORTENER_API2', '34t54hgrfbhfdbn')
SHORTENER_WEBSITE2 = environ.get('SHORTENER_WEBSITE2', 'shortslink.in')
SHORTENER_API3 = environ.get('SHORTENER_API3', '34t54hgrfbhfdbn')
SHORTENER_WEBSITE3 = environ.get('SHORTENER_WEBSITE3', 'shortslink.in')
UPI_PAY_LOGS = environ.get('UPI_PAY_LOGS', '-1001234567890')
```

- Or If you are deploying on any server like <b>Heroku or Koyeb or Render</b> etc. In Environment Variables Add the Variable Name As A Key Like `API_ID` And Value As A Value Like `12345678`
  and you dont need to fill all the fields in Repo.

# Deployment Steps

<details>
<summary>For VPS</summary>

### First, install Python And Pip if you haven't already.

#### For Ubuntu/Debian

1. **Update the package list:**
   ```sh
   sudo apt update
   ```
2. **Install Python 3:**
   ```sh
   sudo apt install python3
   ```
3. **Install `pip` for Python 3:**
   ```sh
   sudo apt install python3-pip
   ```

#### For CentOS/RHEL

1. **Install the EPEL repository:**
   ```sh
   sudo yum install epel-release
   ```
2. **Install Python 3:**
   ```sh
   sudo yum install python3
   ```
3. **Install `pip` for Python 3:**
   ```sh
   sudo yum install python3-pip
   ```

#### For Fedora

1. **Update the package list:**
   ```sh
   sudo dnf update
   ```
2. **Install Python 3:**
   ```sh
   sudo dnf install python3
   ```
3. **Install `pip` for Python 3:**
   ```sh
   sudo dnf install python3-pip
   ```

#### For Arch Linux

1. **Update the package list:**
   ```sh
   sudo pacman -Syu
   ```
2. **Install Python and `pip`:**
   ```sh
   sudo pacman -S python python-pip
   ```

After running these commands, you should have both Python and `pip` installed on your VPS. You can verify the installations by running:

```sh
python3 --version
pip3 --version
```

### Now Create a Folder Named 'myBots' You can use any name you want.

To create a folder (directory) in Linux Vps, you need to use the `mkdir` command.

1. **Create a directory:**
   ```sh
   mkdir myBots
   ```
2. **Verify if directory is created or not:**
   ```sh
   ls
   ```

### Lets Enter To The Folder

1. **Change directory:**
   ```sh
   cd ./myBots
   ```
2. **Verify if directory is changed or not:**
   ```sh
   pwd
   ```

### Clone the Repo In The Folder `myBots` In Your VPS

1. **Clone the Repo Using this:**
   ```sh
   git clone https://github.com/biisal/biisal-filter-bot
   ```
2. **Verify if Repo is cloned or not:**
   ```sh
   ls
   ```

### Now Create A Virtual Environment

1. **Create A Virtual Environment:**
   ```sh
   python3 -m venv venv
   ```
2. **Verify if Virtual Environment is created or not:**
   ```sh
   ls
   ```
3. **Activate Virtual Environment:**
   ```sh
   source venv/bin/activate
   ```

### Now Enter To Our Bot Folder 'biisal-filter-bot'

```sh
cd ./biisal-filter-bot
```

### Edit info.py For Variables <span style="color:red ;opacity:0.5">#Optional</span>

If you want to edit any variable in your VPS then you can edit it here using:

```sh
nano ./info.py
```

Edit the Variables as per your need.

- To Save The edit use `Ctrl+O` then `Enter` and `Ctrl+X`

### Now Install All Requirements

```sh
pip3 install -r requirements.txt
```

### Now Run The Bot

```sh
python3 bot.py
```

<b style="color:skyblue">**Now Your Bot Is Ready 🔥**</b>

</details>

<details>
<summary>For Koyeb Or Render</summary>

### Deploying this bot in Render is Almost same as deploying it in Koyeb. You Just need to Follow the Steps.

- Fork the Repo And Import it in Koyeb or Render By Choosing Web Services.
- Choose python if any Server Asks For it.
- For Koyeb In Builder Section Choose Buildpack option.
- For Render Use This Build Command: `pip install -r requirements.txt`.
- For Koyeb You don't need to add Any Build Command.
- For run or start command, use this command: `gunicorn -b 0.0.0.0:5001 app:app & python3 bot.py`. If you encounter a "same port error," change the port number (5001). In Koyeb, you need to enable it.
- If you are using Render then add a Variable in Environment named `PYTHON_VERSION` with value `3.10.8`.
- Add All Env Variables In Environment Variables Section.

### Now Your Bot Is Ready To Deploy🔥

</details>

<details>
<summary>For Heroku</summary>

- Create A new app in Heroku.
- Import the forked repo.
- Deploy it.
- Add all Env Variables in app settings in Heroku.
- Check Resources if the dyno is on or off. If off, then turn it on.

### Now Your Bot Is Ready In Heroku Server🔥

</details>
