# Weather Advice program
# Request for weather condition from user and take input
weather = str(input("What's the weather like today? (sunny/rainy/cold):."), )

# check the input response and provide clothing recommendations
if weather == 'sunny': print("Wear a t-shirt and sunglasses")
elif weather == 'rainy': print("Dont forget your umbrella and a raincoat")
elif weather == 'cold': print("Make sure to wear a warm coat and a Scarf")
else: print('Sorry, I dont have recommendations for this weather!')
