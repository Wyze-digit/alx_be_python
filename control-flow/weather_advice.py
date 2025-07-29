# Weather Advice program
# Request for weather condition from user and take input
#weather = input("What's the weather like today? (sunny/rainy/cold):").lower()

# check the input response and provide clothing recommendations

#if weather == "sunny":
#      print("Wear a t-shirt and sunglasses")
#elif weather == "rainy":
#      print("Don't forget your umbrella and a raincoat")
#elif weather == "cold":
#      print("Make sure to wear a warm coat and a scarf")
#else:
#      print("Sorry, I dont have recommendations for this weather")

# Request for weather condition from user and take input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Check the input response and provide clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
