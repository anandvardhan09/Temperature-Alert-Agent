from uagents import Agent, Context
import requests
from uagents.setup import fund_agent_if_low
import os,sys
from dotenv import load_dotenv
# from uagents.resolver import get_agent_address

load_dotenv()

api_key = os.getenv("API_KEY")

base_url = "http://api.openweathermap.org/data/2.5/weather?"  # base_url variable to store api url
 

city_name = input("Enter city name : ")  # Give city name
max_temp = int(input("Set the maximum temperature in Celsius : ")) # Set maximum temperature
min_temp = int(input("Set the minimum temperature in Celsius : ")) # Set minimum temperature
 

# complete url address
url = base_url + "appid=" + api_key + "&q=" + city_name
     


# creating a agent for temperature info
temperature = Agent(name="Temperature",
                    seed="Temperature recovery phrase",
                    endpoint=["http://127.0.0.1:8000/submit"],
                    port=8000,                                   
                    )

# fund_agent_if_low(temperature.wallet.address())


@temperature.on_interval(period=5.0)
async def fetch_and_check_temperature(ctx: Context):
        res = requests.get(url)
        
        ctx.logger.info("start")

        if res.json()['cod'] == '404':
          ctx.logger.info("No City found")
          os.execl(sys.executable, sys.executable, *sys.argv) 
        else:
          temp = round(res.json()['main']['temp']) - 273
          ctx.logger.info(temp)

        if temp > max_temp:
            ctx.logger.info("hey its too hot here")
        if temp < min_temp:
            ctx.logger.info("ohhh its cold")    




if __name__ == "__main__":
    temperature.run()