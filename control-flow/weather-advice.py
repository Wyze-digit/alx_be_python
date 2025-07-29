# Weather Advice program
# Request for weather condition from user and take input
weather = str(input('What is the weather like? (sunny/rainy/cold):.'), )

# Response to user
recommend_sunny = 'Wear a t-shirt and sunglasses.'
recommend_rainy = 'Dont forget your umbrella and a raincoat'
recommend_cold = 'Make sure to wear a warm coat and a Scarf'

# check the input response and provide clothing recommendations
if weather == 'sunny':
      print({recommend_sunny})
elif weather == 'rainy':
      print(f"{recommend_rainy}")
elif weather == 'cold':
      print(f'{recommend_cold}')
else: print(f'Sorry, I dont have recommendations for this weather!')
