
# heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )), ("Добрыня Н.", (2, 3)))'
# mission = 'mission = (1,1,2)'

heroes = 'heroes = (("Илья М.", (1, 2, 3)),)'
mission = 'mission = (1,)'

# heroes = 'heroes = (("Илья М.", (1, 2, 3)), ("Алёша П.", (1, )),)'
# mission = 'mission = (1, 2)'

skills = []
names = []
skills_req = []


def distribute():
    skills_req = mission[mission.index("(")+1:mission.rindex(")")]
    skills_req = skills_req.split(",")
    for i in range(len(skills_req)):
        skills_req[i] = skills_req[i].replace(" ", "")
        skills_req[i] = skills_req[i].replace(")", "")
        skills_req[i] = skills_req[i].replace(",", "")
        if (skills_req[i]) == "":
            skills_req.pop(i)
        # print(skills_req[i])
    parse_heroes_skills(heroes, names, skills)
    counter = [0]*len(skills)
    # for skill in skills_req:
    #     print(skill)
    # for skill in skills:
    #     print(skill)
    # for name in names:
    #     print(name)
    print(names)
    print(skills_req)
    print(skills)
    for i, skill_r in enumerate(skills_req):
        for skill in skills:
            if skill_r in skill:
                counter[i] += 1
    print(counter)


def parse_heroes_skills(heroes, names, skills):
    heroes = heroes[8:]
    heroes_cut = heroes.split("),")
    for h in heroes_cut:
        # print(h)
        try:
            names.append(h[h.index('"')+1: h.rindex('"')])
        except Exception:
            pass
        try:
            skills.append(h[h.index(",")+3:h.rindex(")")])
        except Exception:
            pass


distribute()
