from uagents import Bureau

from agents.Temperature import temperature

if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    bureau.add(temperature)
    bureau.run()