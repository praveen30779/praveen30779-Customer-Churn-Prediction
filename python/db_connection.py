from sqlalchemy import create_engine
from config import HOST, USER, PASSWORD, DATABASE

DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(DATABASE_URL)

print("✅ Database Engine Created Successfully")