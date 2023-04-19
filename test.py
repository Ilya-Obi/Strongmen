from distribute_heroes_to_mission import distribute_heroes_to_mission

heroes_list = ['heroes = (("Илья М.", (1, 2, 3)),)', 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)',
               'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))', 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)']
mission_list = ['mission = (1,)', 'mission = (1, 2)',
                'mission = (1, 1, 2)', 'mission = (1, 5)']

if __name__ == '__main__':
    INPUT_HEROES_MESSAGE = "Введите строку героев"
    INPUT_MISSION_MESSAGE = "Введите строку миссии"        
    for i in range(len(heroes_list)):
        answer = distribute_heroes_to_mission(
            heroes_list[i], mission_list[i])
        print(answer)
