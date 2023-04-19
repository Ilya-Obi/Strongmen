# Список входных данных по примеру

# heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))'
# mission = 'mission = (1,1,2)'

# heroes = 'heroes = (("Илья М.", (1, 2, 3)),)'
# mission = 'mission = (1,)'

# heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)'
# mission = 'mission = (1, 2)'

# heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)'
# mission = 'mission = (1, 5)'

# Входные данные
heroes = input()
mission = input()

# Главный метод, вызывающий остальные, обрабатыващие данные. Также реализует те функции, которые не удалось
# выполнить в подметодах


def distribute():
    skills = []
    names = []
    skills_reqired = []
    skills_reqired = mission[mission.index("(")+1:mission.rindex(")")]
    skills_reqired = skills_reqired.split(",")
    parse_heroes_skills(heroes, names, skills)
    parse_mission(skills_reqired, mission)
    counter = [0]*len(skills)
    skill_counter(counter, skills_reqired, skills)
    counter, skills_reqired = zip(
        *sorted(zip(counter, skills_reqired)))
    skills, names = zip(
        *sorted(zip(skills, names), key=lambda x: len(x[0])))
    logger(counter, skills_reqired, skills, names)
    answer_writer(counter, skills_reqired, skills, names)
    print(answer_writer(counter, skills_reqired, skills, names))
    return (answer_writer(counter, skills_reqired, skills, names))

# Разбивает и парсит имена героев и их скилы


def parse_heroes_skills(heroes, names, skills):
    heroes = heroes[8:]
    heroes_cut = heroes.split("),")
    for hero in heroes_cut:
        try:
            names.append(hero[hero.index('"')+1: hero.rindex('"')])
        except Exception:
            pass
        try:
            skills.append(hero[hero.index(",")+3:hero.rindex(")")])
        except Exception:
            pass
    skills[len(skills)-1] = skills[len(skills)-1].replace("))", "")

# Разбивает и парсит строку миссии


def parse_mission(skills_reqired, mission):
    for i in range(len(skills_reqired)):
        skills_reqired[i] = skills_reqired[i].replace(" ", "")
        skills_reqired[i] = skills_reqired[i].replace(")", "")
        skills_reqired[i] = skills_reqired[i].replace(",", "")
        if (skills_reqired[i]) == "":
            skills_reqired.pop(i)

# Считает сколько героев могут выполнить задания определенного уровня


def skill_counter(counter, skills_reqired, skills):

    for i, skill_r in enumerate(skills_reqired):
        for skill in skills:
            if skill_r in skill:
                counter[i] += 1

# Выводит промежуточные обработанные данные


def logger(counter, skills_reqired, skills, names):
    print(counter)
    print(skills_reqired)
    print(skills)
    print(names)

# Выводит ответ


def answer_writer(counter, skills_reqired, skills, names):
    answ = []
    names_copy = list(names)
    skills_reqired_copy = list(skills_reqired)
    skills_copy = list(skills_reqired)
    if counter[0] == 0:
        return answ
    else:
        for skill_req in skills_reqired_copy:
            for index, skill in enumerate(skills_copy):
                if skill_req in skill:
                    try:
                        answ.append(names_copy.pop(index))
                        skills_copy.pop(index)
                    except Exception:
                        pass
    if names_copy == []:
        return answ
    else:
        return []


# Вызов главного метода
distribute()
