import json



try:
    with open("user_config.json", "r", encoding="utf-8") as user_config:
        user = json.load(user_config)
        user['visits'] += 1
        with open(f"user_config.json", "w", encoding="utf-8") as user_config:
            json.dump(user, user_config, indent=2, ensure_ascii=False)

        print(f"Välkommen tillbaka {user['name']}! Du har startat programmet {user['visits']} gånger")

except FileNotFoundError:
    name = input("Vad heter du då? ")

    user_config_template = {"name": name,
                            "visits": 1}

    with open(f"user_config.json", "w", encoding="utf-8") as user_config:
        json.dump(user_config_template, user_config, indent=2, ensure_ascii=False)

    print("Välkommen!")





