# Главный метод, вызывающий остальные, обрабатыващие и выводящие данные.


def distribute_heroes_to_mission(heroes, mission):
    skills = []
    names = []
    skills_reqired = parse_mission(mission)
    parse_heroes_skills(heroes, names, skills)
    available_hero_counter = count_skills(skills_reqired, skills)
    available_hero_counter, skills_reqired, skills, names = sort_result(
        available_hero_counter, skills_reqired, skills, names)

    return prepare_answer(available_hero_counter, skills_reqired, skills, names)

# Сортирует две пары списков для дальнейшего распределения героев по заданиям.


def sort_result(available_hero_counter, skills_reqired, skills, names):
    available_hero_counter, skills_reqired = zip(
        *sorted(zip(available_hero_counter, skills_reqired)))
    skills, names = zip(
        *sorted(zip(skills, names), key=lambda x: len(x[0])))
    return available_hero_counter, skills_reqired, skills, names

# Разбивает и парсит имена героев и их скилы.


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

# Разбивает и парсит строку миссии.


def parse_mission(mission):
    skills_reqired = mission[mission.index("(")+1:mission.rindex(")")]
    skills_reqired = skills_reqired.split(",")
    for i in range(len(skills_reqired)):
        skills_reqired[i] = skills_reqired[i].replace(" ", "")
        skills_reqired[i] = skills_reqired[i].replace(")", "")
        skills_reqired[i] = skills_reqired[i].replace(",", "")
        if (skills_reqired[i]) == "":
            skills_reqired.pop(i)
    return skills_reqired

# Считает сколько героев могут выполнить задания определенного уровня.


def count_skills(skills_reqired, skills):
    result = [0]*len(skills)
    for i, skill_r in enumerate(skills_reqired):
        for skill in skills:
            if skill_r in skill:
                result[i] += 1
    return result


# Подготавливает строку ответа со списком героев, если они могут выполнить миссию.


def prepare_answer(counter, skills_reqired, skills, names):
    answer = []
    names_copy = list(names)
    skills_reqired_copy = list(skills_reqired)
    skills_copy = list(skills_reqired)
    if counter[0] == 0:
        return answer
    else:
        for skill_req in skills_reqired_copy:
            for index, skill in enumerate(skills_copy):
                if skill_req in skill:
                    try:
                        answer.append(names_copy.pop(index))
                        skills_copy.pop(index)
                    except Exception:
                        pass
    if names_copy == []:
        return answer
    else:
        return []
