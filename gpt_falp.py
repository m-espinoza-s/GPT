import openai
import config
import pandas as pd
from db_conn import Innova
from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent


openai.api_key=config.API_KEY
query=config.query


conn=Innova(config.usr,config.pwd)

df=conn.innovacion(query=query)

agent=create_pandas_dataframe_agent(OpenAI(temperature=0,openai_api_key=openai.api_key,model="text-davinci-003"),df,verbose=True)


list=[]

for i in range(len(df)):
    res=agent.run(f"can you detect the medical procedures in these texts :{df['EVOLUCION'][i]}?")
    list.append((df['EVOLUCION'].iloc[i],res))


df_res = pd.DataFrame(list, columns=['EVOLUCION', 'RESULTADO'])
print(df_res)

df_res.to_excel('resultados.xlsx')





