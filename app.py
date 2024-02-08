from flask import Flask,render_template,request,redirect
# import os
# from azure.search.documents.indexes._generated.models import TextWeights
# from openai import AzureOpenAI
# import tiktoken
# from azure.core.credentials import AzureKeyCredential  
# from azure.search.documents import SearchClient
# from azure.search.documents.indexes import SearchIndexClient  
# from azure.search.documents.models import VectorizedQuery
# from azure.data.tables import TableServiceClient
# import uuid
# from dotenv import load_dotenv

app = Flask(__name__)
# load_dotenv()
 
# cog_service_endpoint = os.getenv('cog_service_endpoint')
# cog_search_key = os.getenv('cog_search_key')
# openai_api_key = os.getenv('openai_api_key')
# openai_deployment_name = os.getenv('openai_deployment_name')
# openai_endpoint=os.getenv('openai_endpoint')
# connection_string =os.getenv('connection_string')
# cog_search_credential = AzureKeyCredential(cog_search_key)
# index_name='exampleindex'
# conversations=[]
# messages = []
# max_response_tokens = 500 
# overall_max_tokens = 4096
# prompt_max_tokens=overall_max_tokens - max_response_tokens
# token_count=0
# cog_result=''
# user_query=''

# client = AzureOpenAI(
#   api_key =   openai_api_key,
#   api_version = "2023-05-15",
#   azure_endpoint = openai_endpoint
# )

# def connect_to_cosmos():
#     connection_str = connection_string
#     table_name = "userConversation"
#     table_service_client = TableServiceClient.from_connection_string(connection_str)
#     table_client = table_service_client.get_table_client(table_name)
#     return table_client

# def entity_create(userId,role,message):
#     table_client=connect_to_cosmos()
#     my_entity1 = {
#         'PartitionKey': '{}'.format(userId),
#         "RowKey":'{}'.format(uuid.uuid4()),
#         'userId': userId,
#         'role' : role,
#         'message':message
#            }
#     entity = table_client.create_entity(entity=my_entity1)
#     print("successfuly inserted the entity")

# def get_user_conversation(userId):
#     table_client=connect_to_cosmos()
#     my_filter = "userId eq {}".format(userId)
#     entities = table_client.query_entities(my_filter)
#     for entity in entities:
#         conversations.append({"role": entity['role'], "content": entity['message']})
    
#     return conversations


# def completion_api(prompt):
#     completion = client.chat.completions.create(messages=prompt,temperature=0.2,
#     max_tokens=max_response_tokens,model="AzOpenai-gpt-35-turbo")
#     return completion.choices[0].message.content

# def generate_embeddings(text, model=openai_deployment_name): 
#     return client.embeddings.create(input = [text], model=model).data[0].embedding

# def query_cog_search(index_name,query):
#     search_client = SearchClient(cog_service_endpoint, index_name, credential=cog_search_credential)
#     vector_query = VectorizedQuery(vector=generate_embeddings(query), k_nearest_neighbors=3, fields="content_vector")
#     results = search_client.search(  
#         search_text=query,  
#         vector_queries= [vector_query],
#         select=["id","page_no","file_name","content"],
#         # query_type="semantic", 
#         # semantic_configuration_name='my-semantic-config', 
#         # query_caption="extractive", 
#         # query_answer="extractive",
#         # facets=["id"],
#         top=1
#         #filter="id eq '1'"
#     )  
  
#     return results

# def estimate_tokens(prompt):
#     cl100k_base = tiktoken.get_encoding("cl100k_base")
#     tokens = cl100k_base.encode(prompt)
#     return len(tokens)

# def gpt_messages(role,text):
#     global messages
#     messages.append({"role": role, "content": text})

# def create_prompt(messages,cog_result):
#     prompt = """
#     # You are an Assistant who helps the company employees with their questions.Porvide brief answers only related to  Follow below points while answering questions.
#     1) Create your answer with the facts listed in the sources given below. If there isn't enough information below, say you don't know.
#     2) Do not generate answers that don't use the sources below.
#     3) If asking a clarifying question to the user would help, ask the question.
#     Conversation history
#     {}
#     Below is the source.
#     {}""".format(messages,cog_result)

#     return prompt

@app.route('/', methods=["GET", "POST"])
def query():
    # return 'hello world'
    return render_template('login.html')

# @app.route('/query', methods=["GET", "POST"])
# def get_query():

#     cog_result=''
#     query = request.values.get("query")
#     userID = request.values.get("userID")
#     global messages 
#     results=query_cog_search(index_name,query)

#     for result in results:
#         cog_result+=result['content']

#     conversations=get_user_conversation(userID)
#     prompt=create_prompt(conversations,cog_result)
#     token_count = estimate_tokens(prompt)
#     print()

#     while token_count > prompt_max_tokens:
#         conversations.pop(0)
#         prompt=create_prompt(conversations,cog_result)
#         token_count = estimate_tokens(prompt)


#     gpt_messages("system",prompt)
#     gpt_messages("user",query)
#     # conversations.append({"role": 'user', "content": query})
#     entity_create(userID,'user',query)
#     gpt_response=completion_api(messages)
#     # conversations.append({"role": 'assistant', "content": gpt_response})
#     entity_create(userID,'assistant',gpt_response)
#     print(gpt_response)
#     return gpt_response
# Conversation_history("assistant",gpt_response)

# @app.route('/get_query', methods=["GET", "POST"])
# def get_query():
#     # print(request.args)
#     # print(request.form)
#     # print(request.files)
#     # print(request.values)
#     # print(request.values.get("username"))
#     # return "You're successfully registered."
#     user_query = request.values.get("query")
#     return redirect("/process_request")

# @app.route('/process_request')
# def process_request():
#     # return render_template("request.html")

# query='Continue'
# while query!='stop':
#     messages = []
#     print('Please ask your question.\n')
#     query=str(input())
#     results=query_cog_search(index_name,query)

#     for result in results:
#         cog_result+=result['content']

#     conversations=get_user_conversation(1)
#     prompt=create_prompt(conversations,cog_result)
#     token_count = estimate_tokens(prompt)

#     while token_count > prompt_max_tokens:
#         conversations.pop(0)
#         prompt=create_prompt(conversations,cog_result)
#         token_count = estimate_tokens(prompt)


#     gpt_messages("system",prompt)
#     gpt_messages("user",query)
#     # conversations.append({"role": 'user', "content": query})
#     entity_create(1,'user',query)
#     gpt_response=completion_api(messages)
#     # conversations.append({"role": 'assistant', "content": gpt_response})
#     entity_create(1,'assistant',gpt_response)
#     print(gpt_response)
# Conversation_history("assistant",gpt_response)


if __name__ == '__main__':
    app.run()




