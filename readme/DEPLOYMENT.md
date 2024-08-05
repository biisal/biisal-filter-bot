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


# Deployment Steps

<details>
<summary>For VPS</summary>
<p>
<pre>
git clone https://github.com/TeamHMT/Auto-search-tamil-bot
# Install Packages
pip3 install -U -r requirements.txt
Edit info.py with variables as given below then run bot
python3 bot.py
</pre>
</p>
</details>

<b style="color:skyblue">**Now Your Bot Is Ready 🔥**</b>

</details>

<details>
<summary>For Koyeb Or Render</summary>

### Deploying this bot in Render is Almost same as deploying it in Koyeb. You Just need to Follow the Steps.

- Fork the Repo And Import it in Koyeb or Render By Choosing Web Services.
- Choose dockerfile if any Server Asks For it.
- For Koyeb In Builder Section Choose Buildpack option.
- For use koyeb then add port 8000 
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
