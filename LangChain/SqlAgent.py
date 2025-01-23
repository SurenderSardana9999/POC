import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
import mysql.connector

os.environ['OPENAI_API_KEY'] = "x"
#os.environ["SERPAPI_API_KEY"] = "your_serpapi_api_key"


db_user = "X"
db_password = "XX"
db_host = "X"
db_name = "XX"
#db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
print(db_host)
connection = mysql.connector.connect(host='localhost',
                                         database='demo_finance',
                                         user='root',
                                         password='Avinash@123')
        

#db = SQLDatabase.from_uri(f"mysql://{db_user}:{db_password}@{db_host}/{db_name}")
print(connection)
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

#toolkit = SQLDatabaseToolkit(db=db)
toolkit = SQLDatabaseToolkit(db=connection)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True
)
agent_executor.run("Find the top 5 products with the highest total sales revenue")
