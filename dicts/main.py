user = {"id": 101, "name": "Rahul"}

email = user.get("email", "not_provided@test.com")
print(email)

config = {"host": "localhost", "port": 8000}
config.update({"port": 5432, "db": "postgres"})

db_name = config.pop("db", "default_db")
print(db_name)

stats = {"views": 1500, "likes": 230, "shares": 45}

for key in stats:
    print(key, "->", stats[key])

for val in stats.values():
    print(val)

for metric, count in stats.items():
    print(f"{metric}: {count}")
