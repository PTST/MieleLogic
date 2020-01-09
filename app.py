from mielelogic import MieleLogic
import time
miele = MieleLogic("Annapatrick", "annapatrick")

initial_states = miele.Get_Laundry_State()

while True:
    # print("Checking")
    time.sleep(30)
    cur_states = miele.Get_Laundry_State()

    for i in range(len(cur_states)):
        if initial_states[i] != cur_states[i]:
            print(cur_states[i])
