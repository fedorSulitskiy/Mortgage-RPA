from auto.robot import Robot
import pandas as pd

def main():
    df = pd.read_csv('input/input.csv')
    for i in range(len(df)):
        person = df.iloc[i,0:2]
        name = person['name']
        surname = person['surname']
        print(surname)
        bot = Robot(name,surname)
        bot.flow()
        
    df = pd.read_csv('input/input.csv')
    print(df[['name', 'surname', 'output_manual', 'output_program', 'valid']])
    
if __name__ == '__main__':
    main()