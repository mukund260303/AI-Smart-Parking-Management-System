from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
parkingdb = client.get_database("parkingdb")
parking_collection = parkingdb.get_collection("parking")

# Sample data for parking spots
parking_spots = [
    {'id': 'OP-1', 'status': 'empty', 'type': 'open roof'},
    {'id': 'OP-2', 'status': 'empty', 'type': 'open roof'},
    {'id': 'OP-3', 'status': 'empty', 'type': 'open roof'},
    {'id': 'OP-4', 'status': 'empty', 'type': 'open roof'},
    {'id': 'OP-5', 'status': 'empty', 'type': 'open roof'},
    {'id': 'OP-6', 'status': 'empty', 'type': 'open roof'},
    {'id': 'IP-1', 'status': 'empty', 'type': 'inner parking'},
    {'id': 'IP-2', 'status': 'empty', 'type': 'inner parking'},
    {'id': 'IP-3', 'status': 'empty', 'type': 'inner parking'},
    {'id': 'IP-4', 'status': 'empty', 'type': 'inner parking'}
]

# Insert parking spots
print("Initializing parking spaces...")
for spot in parking_spots:
    existing_spot = parking_collection.find_one({'id': spot['id']})
    
    if not existing_spot:
        parking_collection.insert_one(spot)
        print(f"✓ Created parking spot {spot['id']} ({spot['type']})")
    else:
        print(f"- Parking spot {spot['id']} already exists")

# Check total count
total_spaces = parking_collection.count_documents({})
print(f"\nTotal parking spaces in database: {total_spaces}")
print("Initialization complete!")
