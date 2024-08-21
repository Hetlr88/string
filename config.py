
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID",6151017))
API_HASH = getenv("API_HASH","5d125071b09e07b14a7837a2de4c6dad")

BOT_TOKEN = getenv("BOT_TOKEN","7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE")
OWNER_ID = int(getenv("OWNER_ID",6169288210))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://admin:admin123@cluster0.025ahvi.mongodb.net/")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/movies0x3")
