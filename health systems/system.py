from models import Client, Program

class HealthSystem:
    def __init__(self):
        self.clients = {}
        self.programs = {}

    def create_program(self, name):
        if name in self.programs:
            print(f"Program {name} already exists.")
        else:
            self.programs[name] = Program(name)
            print(f"Program {name} created successfully.")

    def register_client(self, client_id, name, age):
        if client_id in self.clients:
            print(f"Client ID {client_id} already exists.")
        else:
            self.clients[client_id] = Client(client_id, name, age)
            print(f"Client {name} registered successfully.")

    def enroll_client_in_program(self, client_id, program_name):
        client = self.clients.get(client_id)
        program = self.programs.get(program_name)
        if not client:
            print("Client not found.")
        elif not program:
            print("Program not found.")
        else:
            client.enroll_program(program)
            print(f"Client {client.name} enrolled in {program.name}.")

    def search_client(self, keyword):
        results = [c for c in self.clients.values() if keyword.lower() in c.name.lower()]
        if results:
            for client in results:
                print(f"Found: {client.client_id} - {client.name}")
        else:
            print("No matching clients found.")

    def view_client_profile(self, client_id):
        client = self.clients.get(client_id)
        if client:
            print(f"Client ID: {client.client_id}")
            print(f"Name: {client.name}")
            print(f"Age: {client.age}")
            print("Enrolled Programs:")
            for p in client.enrolled_programs:
                print(f"- {p.name}")
        else:
            print("Client not found.")

    def get_client_profile(self, client_id):
        """Return client profile as dictionary for API"""
        client = self.clients.get(client_id)
        if not client:
            return None
        return {
            "client_id": client.client_id,
            "name": client.name,
            "age": client.age,
            "programs": [p.name for p in client.enrolled_programs]
        }