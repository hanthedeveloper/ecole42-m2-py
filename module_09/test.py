import json

from data_generator.generated_data.space_stations import SPACE_STATIONS
from data_generator.generated_data.alien_contacts import ALIEN_CONTACTS
from data_generator.generated_data.space_missions import SPACE_MISSIONS

from pydantic import ValidationError

from ex0.space_station import SpaceStation
from ex1.alien_contact import AlienContact
from ex2.space_crew import SpaceMission


print("space stations:")
for record in SPACE_STATIONS:
    try:
        SpaceStation(**record)
        print("OK")
    except ValidationError as e:
        print("FAIL:", e.errors()[0]["msg"])

print()
print("alien contact:")
for record in ALIEN_CONTACTS:
    try:
        AlienContact(**record)
        print("OK")
    except ValidationError as e:
        print("FAIL:", e.errors()[0]["msg"])

print()
print("space mission:")
for record in SPACE_MISSIONS:
    try:
        SpaceMission(**record)
        print("OK")
    except ValidationError as e:
        print("FAIL:", e.errors()[0]["msg"])

print()
print("invalid olanlar:")

with open("data_generator/generated_data/invalid_stations.json") as f:
    stations = json.load(f)

with open("data_generator/generated_data/invalid_contacts.json") as f:
    contacts = json.load(f)

for rec in stations:
    try:
        SpaceStation(**rec)
        print("yanlıs")
    except ValidationError as e:
        print("FAIL (beklenen):", e.errors()[0]["msg"])

for rec in contacts:
    try:
        AlienContact(**rec)
        print("yanlıs")
    except ValidationError as e:
        print("FAIL (beklenen):", e.errors()[0]["msg"])