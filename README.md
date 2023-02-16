# PushUpCounterDiscordBot
## Current Features
- Add or take away n pushups from a database (w/ ur discord user and current time recorded with it) using "pushups!add n" or "pushups!remove n" in discord channel with the bot  
- See a leaderboard to see who is doing the most using "pushups!leaderboard"
## END GOAL FEATURES
- Add (and take away ONLY UR OWN if by accident (admins can take away anyone's) ) pushups to a collective counter easily
- Leaderboard feature
- Calender feature with contribution levels for each person AND collective one
- Projected finish time according to push up rate so far
## DEVELOPMENT
### to set up in development:
Create .env file in root, see .gitignore comments  
```./pocketbase serve``` to create db  
```python3 bot.py``` to start bot  
## DEPLOYMENT
### this is how i chose to deploy (free for small scale testing):
for my pocketbase backend: https://github.com/pocketbase/pocketbase/discussions/537  
for the bot script: https://replit.com/@Zi-TongDeng/PushUpCounterDiscordBot  (remember to create repl secrets instead of .env for your tokens!)
