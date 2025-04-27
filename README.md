Health Information System

A simple Health Information Management System for managing clients and health programs/services.

Features

Create health programs (e.g., TB, Malaria, HIV, etc.)

Register new clients

Enroll clients into one or more programs

Search for registered clients

View client profiles (including enrolled programs)

Expose client profiles via a REST API for integration with other systems

Technologies Used

Python 3

Flask (for API)

In-memory storage (Python dictionaries)

Getting Started

Prerequisites

Python 3 installed

Flask installed

Install Flask if you don't have it:

pip install flask

Running the Application

Clone the repository:
git clone https://github.com/Alianda20/Basic-Health-System.git cd health-information-system

Run the Flask app:
python app.py

Access the API:
Get client profile: Visit http://127.0.0.1:5000/api/client/<client_id> in your browser or Postman.

Example:

GET http://127.0.0.1:5000/api/client/C001
