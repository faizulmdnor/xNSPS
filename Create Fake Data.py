import csv
import random
from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Define possible values for Gender, Race, and Nationality
genders = ['Male', 'Female']
races = ['Asian', 'Black', 'Caucasian', 'Hispanic', 'Mixed', 'Native American']
nationalities = ['American', 'Canadian', 'British', 'Australian', 'Malaysian', 'Indian', 'Chinese', 'Brazilian',
                 'Nigerian', 'German']
occupations = ['Engineer', 'Doctor', 'Teacher', 'Artist', 'Software Developer', 'Nurse', 'Journalist', 'Accountant',
               'Designer', 'Chef']

# Open a CSV file to write the data
file_path = '/X-NSPS/Python - Scripting/pythonProject/xNSPS/test_data.csv'

# Generate 10,000 rows of fake data
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Name', 'Age', 'Gender', 'Race', 'Nationality', 'Occupation', 'Date of Birth'])

    for _ in range(10000):
        name = fake.name()
        age = random.randint(25, 65)
        gender = random.choice(genders)
        race = random.choice(races)
        nationality = random.choice(nationalities)
        occupation = random.choice(occupations)
        dob = fake.date_of_birth(minimum_age=age - 5, maximum_age=age).strftime('%Y-%m-%d')
        # Write the row
        writer.writerow([name, age, gender, race, nationality, occupation, dob])

file_path
