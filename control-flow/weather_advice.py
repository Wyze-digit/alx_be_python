# Weather Advice program
# Request for weather condition from user and take input
weather = str(input("What's the weather like today? (sunny/rainy/cold):."), )

# check the input response and provide clothing recommendations
if weather == 'sunny':
      print(f"Wear a t-shirt and sunglasses")
elif weather == 'rainy':
      print(f"Dont forget your umbrella and a raincoat")
elif weather == 'cold':
      print(f"Make sure to wear a warm coat and a Scarf")
else: print(f'Sorry, I dont have recommendations for this weather!')
