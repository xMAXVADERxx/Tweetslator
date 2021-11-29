# Tweetslator
A Twitter Bot that automatically translates Tweets it's mentioned in

# Setup:
The bot was designed for use with Heroku, though any hosting platform may be used

Config Information:
  When setting up time, the ISO-8601 format is used (i.e YYYY-MM-DDTHH:MM:SSZ; e.g 2020-11-07T01:35:43Z)
  The "GoogleCodes" file has all the different identifiers for languages (that are supported by GoogleTrans), edit as you wish

# Heroku:
Fork the main branch
Start a project over at dashboard.heroku.com
![image](https://user-images.githubusercontent.com/42118429/143934196-fa1799bc-5379-4790-b1bc-e6acc43d7986.png)

Name your project, and set region (USA or Europe)
![image](https://user-images.githubusercontent.com/42118429/143934441-1e1be8a2-c39d-48d9-9ed6-c1e95d407107.png)

Once setup, choose GitHub as your deployment method (You can use CLI for Git or Container Registry, if you know what you're doing!)
![image](https://user-images.githubusercontent.com/42118429/143934628-8096dd38-0e9f-4ae9-9ae5-0a2d26a7cd46.png)

Once GitHub is chosen, you can choose "Tweetslator" as the project
(If you wish, you can use automatic deploys, or deploy manually, depending on how you wish to use your bot)

Once setup, go to the "Settings" tab and edit the "Config Vars"
![image](https://user-images.githubusercontent.com/42118429/143935262-23eb49f5-829c-4686-809b-ec0766f3dcb5.png)

Add each of these config vars, which will be setup once you've made your Twitter Bot (developer.twitter.com, but I assume you know what you're doing!)
(You can get your SELF_ID by putting your handle (@) into any ID Finding website)
![image](https://user-images.githubusercontent.com/42118429/143935501-fc8a802a-bb62-4474-b3da-c5e5ba8002f6.png)

Once done, the bot will run, and should work!

# Using a custom server
Clone the project to a folder (git clone github.com/xMAXVADERxx/Tweetslator)

Create a file named ".env" in the root of the Tweetslator folder, this'll be the config
![image](https://user-images.githubusercontent.com/42118429/143936123-2ba4b33d-18ab-4c6c-b0d4-6b8e0398fbf2.png)

Setup the config as below, replacing the red boxes with the equivalent Twitter information
![image](https://user-images.githubusercontent.com/42118429/143936398-95075aa4-cbd2-4a54-b9df-5ebd6f331610.png)
