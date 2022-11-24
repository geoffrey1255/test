import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print("test")
test = os.getenv('DISCORD_ID')
print(test)

