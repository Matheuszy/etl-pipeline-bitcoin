import os
from dotenv import load_dotenv
load_dotenv()

COINBASE_API_URL = "https://api.coinbase.com/v2/prices/spot"
DATABASE_URL = os.getenv("DATA_BASE_URL")