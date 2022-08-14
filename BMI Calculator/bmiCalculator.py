def bmiCaculator(height,weight):
    return weight/(height)**2
def bodyHealth(bmi):
    if bmi<18.5:
        print('Underweight'+' and your BMI is '+'%.2f'%bmi)
    elif bmi>=18.5 and bmi<25:
        print('Normal')
    elif bmi>=25 and bmi<30:
        print('Over Weight'+' and your BMI is '+'%.2f'%bmi)
    else:
        print('Obesity'+' and your BMI is '+'%.2f'%bmi)

def main():
    print('Welcome at BMI calculator')
    try:
        height = float(input('Enter your height : '))
        weight=float(input('Enter your weight : '))
    except:
        print('Enter a valid input (number)\ntry again')
        main()
    bodyHealth(bmiCaculator(height,weight))
main()

