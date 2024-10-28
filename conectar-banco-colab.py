from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB connection URI with authentication details
uri = "mongodb+srv://guilhermeaqw24:QecII8Ow51jOOePs@cluster0.zile7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new MongoDB client and connect to the server using the specified API version
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping command to confirm a successful connection to the MongoDB server
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    # If there is an error during connection, print the error message
    print(e)

# Get the database named 'Escola'
db = client.get_database('Escola')
print(db)  # Prints the database object

# Create a list of new students to be inserted into the 'Alunos' collection
novos_alunos = [
    {
        "nome": "Maria da silva",
        "curso": "ADS",
        "semestre": "3",
        "ano": "2024",
        "local": "Fatec",
    },
    {
        "nome": "Maria Maria da silva",
        "curso": "ADM",
        "semestre": "5",
        "ano": "2023",
        "local": "Fatec Santos",  
    }
]

# Check the type of the 'novos_alunos' variable (should be a list)
type(novos_alunos)

# Insert the new students into the 'Alunos' collection
db.Alunos.insert_many(novos_alunos)

# Print the contents of the 'Alunos' collection to confirm the insertion
print(db.Alunos.find())
