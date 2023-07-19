from auto.robot import Robot
import pandas as pd

# Temporary fix in case program fails mid-execution,
# sets the index from which the iteration must restart.
restart_index = 0

def main():
    
    # Iterate over the suite of tests.
    df = pd.read_csv('input/input.csv')
    for i in range(len(df)-restart_index):
        
        # Instantiate the "client/person"
        person = df.iloc[i+restart_index,0:2]
        name, surname = person['name'], person['surname']
        print(surname) # Track progress
        
        # Instantiate my program
        bot = Robot(name,surname)
        bot.flow()
        
    df = pd.read_csv('input/input.csv')
    # Show results
    print(df[['name', 'surname', 'output_manual', 'output_program', 'valid']])
    
if __name__ == '__main__':
    main()