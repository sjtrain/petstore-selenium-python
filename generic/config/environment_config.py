from faker import Faker
from random import randint

fake = Faker()
random = randint(12345, 99999)

class DevConfig:
    environment = "dev"
    url = 'https://petstore.octoperf.com/actions/Catalog.action'
    username = "devUser5"
    password = "Dev.1232"
    first_name = f"{fake.first_name()}"
    last_name = f"{fake.last_name()}"
    email = f"dev-{fake.email()}"
    phone = f"{fake.phone_number()}"
    address_1 = "Fake street123"
    address_2 = "Fake address2"
    city = "Buenos Aires"
    state = "CABA"
    zip = random
    country = "Argentina"


class TestConfig:
    environment = "test"
    url = 'https://petstore.octoperf.com/actions/Catalog.action'
    username = "TestUser"
    password = "Test.123"
    first_name = f"{fake.first_name()}"
    last_name = f"{fake.last_name()}"
    email = f"test-{fake.email()}"
    phone = f"{fake.phone_number()}"
    address_1 = "Fake street"
    address_2 = "Fake address2"
    city = "Buenos Aires"
    state = "CABA"
    zip = "1223"
    country = "Argentina"


class StageConfig:
    environment = "stage"
    url = 'https://petstore.octoperf.com/actions/Catalog.action'
    username = "StageUser"
    password = "Stage.123"
    first_name = f"{fake.first_name()}"
    last_name = f"{fake.last_name()}"
    email = f"stage-{fake.email()}"
    phone = f"{fake.phone_number()}"
    address_1 = "Stage Fake street"
    address_2 = "Stage Fake address2"
    city = "Buenos Aires"
    state = "CABA"
    zip = "1223"
    country = "Argentina"
