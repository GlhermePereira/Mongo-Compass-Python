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
