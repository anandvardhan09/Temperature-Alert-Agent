from uagents import Bureau

from agents.Temperature import agent as temperature_agent

if __name__ == "__main__":
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    bureau.add(temperature_agent)
    bureau.run()