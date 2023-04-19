
# heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))'
# mission = 'mission = (1,1,2)'

# heroes = 'heroes = (("Илья М.", (1, 2, 3)),)'
# mission = 'mission = (1,)'

heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)'
mission = 'mission = (1, 2)'

skills = []
names = []
skills_reqiredired = []


def distribute():
    skills_reqired = mission[mission.index("(")+1:mission.rindex(")")]
    skills_reqired = skills_reqired.split(",")
    parse_mission(skills_reqired, mission)
    parse_heroes_skills(heroes, names, skills)
    counter = [0]*len(skills)
    skill_counter(counter, skills_reqired)

    # counter = [0]*len(skills)
    # for i, skill_r in enumerate(skills_reqired):
    #     for skill in skills:
    #         if skill_r in skill:
    #             counter[i] += 1
    print(counter)
    print(skills_reqired)
    print(skills)
    print(names)


def parse_heroes_skills(heroes, names, skills):
    heroes = heroes[8:]
    heroes_cut = heroes.split("),")
    for h in heroes_cut:
        try:
            names.append(h[h.index('"')+1: h.rindex('"')])
        except Exception:
            pass
        try:
            skills.append(h[h.index(",")+3:h.rindex(")")])
        except Exception:
            pass


def parse_mission(skills_reqired, mission):
    for i in range(len(skills_reqired)):
        skills_reqired[i] = skills_reqired[i].replace(" ", "")
        skills_reqired[i] = skills_reqired[i].replace(")", "")
        skills_reqired[i] = skills_reqired[i].replace(",", "")
        if (skills_reqired[i]) == "":
            skills_reqired.pop(i)


def skill_counter(counter, skills_reqired):

    for i, skill_r in enumerate(skills_reqired):
        for skill in skills:
            if skill_r in skill:
                counter[i] += 1


distribute()
