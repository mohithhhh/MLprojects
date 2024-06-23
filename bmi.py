import streamlit as st

def bmicalculator():
    st.title('BMI Calculator')

    st.write("Enter your details below to calculate your BMI:")

    age = st.number_input('Age', min_value=0, max_value=120, value=25)
    weight = st.number_input('Weight (kg)', min_value=0.0, value=70.0, step=0.1)
    height = st.number_input('Height (meters)', min_value=0.0, value=1.75, step=0.01)

    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)

        st.write(f'Your BMI is {bmi:.2f}')

        if bmi < 18.5:
            st.write('You are underweight.')
        elif 18.5 <= bmi < 24.9:
            st.write('You have normal weight.')
        elif 25 <= bmi < 29.9:
            st.write('You are overweight.')
        elif 30 <= bmi < 34.9:
            st.write('You are obese.')
        else:
            st.write('You are severely obese.')
    else:
        st.write('Please enter valid height and weight.')

if __name__ == '__main__':
    bmicalculator()


"""Calorie calculator

"""

import streamlit as st

def calorie_calculator():
    st.title('BMR Calculator')

    inputage = st.number_input('What is your age?', min_value=0, max_value=120, value=25)
    inputweight = st.number_input('What is your weight (kg)?', min_value=0.0, step=0.1)
    inputheight = st.number_input('What is your height (cm)?', min_value=0.0, step=0.1)
    inputgender = st.selectbox('What is your gender?', ['M', 'F'])

    age = int(inputage)
    weight = float(inputweight)
    height = float(inputheight)
    gender = str(inputgender)

    if gender == 'M':
        calorie = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        st.write(f'Your calorie intake should be {calorie:.2f} calories.')
    elif gender == 'F':
        calorie = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        st.write(f'Your calorie intake should be {calorie:.2f} calories.')

if __name__ == '__main__':
    calorie_calculator()





import streamlit as st



import streamlit as st

def weight_loss_gain():
    st.title("Weight Loss/Gain Program Calculator")

    inputage = st.number_input('What is your age?', min_value=0, step=1, key='age')
    inputweight = st.number_input('What is your weight (kg)?', min_value=0.0, step=0.1, key='weight')
    inputheight = st.number_input('What is your height (m)?', min_value=0.01, step=0.01, key='height')
    inputgender = st.selectbox('What is your gender?', ['M', 'F'], key='gender')
    inputprogram = st.selectbox('What is your program?', ['GAIN', 'LOSE'], key='program')

    age = int(inputage)
    weight = float(inputweight)
    height = float(inputheight)
    gender = str(inputgender)
    program = str(inputprogram)

    bmi = weight / height ** 2

    if program == 'LOSE' and gender == 'M':
        calorieM = 66 + (13.7 * weight) + (5 * height * 100) - (6.8 * age)
        if bmi > 30:
            calories = calorieM - 1250
            st.write(f'You should consume {calories:.2f} calories')
        elif 24 < bmi < 29:
            calories1 = calorieM - 850
            st.write(f'You should consume {calories1:.2f} calories')
        elif bmi < 25:
            calories2 = calorieM - 500
            st.write(f'You should consume {calories2:.2f} calories')

    elif program == 'GAIN' and gender == 'F':
        caloriesF = 655 + (9.6 * weight) + (1.8 * height * 100) - (4.7 * age)
        if bmi > 30:
            calories3 = caloriesF + 500
            st.write(f'You should consume {calories3:.2f} calories')
        elif 24 < bmi < 29:
            calories4 = caloriesF + 850
            st.write(f'You should consume {calories4:.2f} calories')
        elif bmi < 25:
            calories5 = caloriesF + 1250
            st.write(f'You should consume {calories5:.2f} calories')

if __name__ == '__main__':
    weight_loss_gain()
