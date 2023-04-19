from distribute_heroes_to_mission import distribute_heroes_to_mission

if __name__ == '__main__':
    INPUT_HEROES_MESSAGE = "Введите строку героев"
    INPUT_MISSION_MESSAGE = "Введите строку миссии"
    answer = distribute_heroes_to_mission(
        input(INPUT_HEROES_MESSAGE), input(INPUT_MISSION_MESSAGE))
    print(answer)
