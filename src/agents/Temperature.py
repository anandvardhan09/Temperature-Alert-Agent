from uagents import Agent, Context
import requests
from uagents.setup import fund_agent_if_low
# import os
# from dotenv import load_dotenv, dotenv_values

# os.getenv("API_key")


api_key="d"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = input("Enter city name : ")
 
# complete url address
url = base_url + "appid=" + api_key + "&q=" + city_name
     


# creating a agent for temperature info
temperature = Agent(name="Temperature",
                    seed="Temperature recovery phrase",
                    endpoint=["http://127.0.0.1:8000/submit"],
                    port=8000,                                   
                    )

fund_agent_if_low(temperature.wallet.address())


@temperature.on_interval(period=100.0)
async def fetch_temperature(ctx: Context):
        res = requests.get(url)
        
        if res.json()['cod'] == '404':
             print("No City found")
        else:
          temp_in_kelvin=round(res.json()['main']['temp'])
          print(temp_in_kelvin)



if __name__ == "__main__":
    temperature.run()