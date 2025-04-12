# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "24186652")

API_HASH = os.environ.get("API_HASH", "f0693307dc4bb4157ef07c41df9f0d0e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7836976455:AAGmeRICg89SjOvwgGnplGGkasgEIm5NB8w") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Ard_Anime") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://atlas-sample-dataset-load-67fa4ce04e33ef295908aceb:<db_password>@renamerbot.gtx5ofm.mongodb.net/?retryWrites=true&w=majority&appName=RenamerBot")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6370782041').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
