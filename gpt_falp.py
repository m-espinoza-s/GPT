import openai
import config
from db_conn import Innova

openai.api_key=config.API_KEY
query=config.query


conn=Innova(config.usr,config.pwd)

df=conn.innovacion(query=query)

