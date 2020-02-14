import random
seed = int(input('Enter the seed to run the fight with: '))
random.seed(seed)
num = int(random.random() * 100)
hp1 = int(input('Enter the attacker\'s hp: '))
strength1 = int(input('Enter the attacker\'s strength: '))
accuracy1 = int(input('Enter the attacker\'s accuracy: '))
crit_chance1 = int(input('Enter the attacker\'s crit chance: '))
dodge_rate1 = int(input('Enter the attacker\'s dodge rate: '))
hp2 = int(input('Enter the defender\'s hp: '))
strength2 = int(input('Enter the defender\'s strength: '))
accuracy2 = int(input('Enter the defender\'s accuracy: '))
crit_chance2 = int(input('Enter the defender\'s crit chance: '))
dodge_rate2 = int(input('Enter the defender\'s dodge rate: '))
guarding_status = str(input('Is the defender guarding? Y for yes, n for no: '))
B_hurt1 = strength1 + 1
B_hurt2 = strength2 + 1
N_hurt1 = random.randint((strength1 // 2), strength1)
N_hurt2 = random.randint((strength2 // 2), strength2)

if guarding_status.lower() == 'y':
    if num <= crit_chance1:
        if B_hurt1 >= hp2:
            print('attacker crit defender for', B_hurt1, 'points of damage')
            print('After fighting the attacker has', hp1, 'hp left and the defender has 0 hp left')
        else:
            hp2 = hp2 - B_hurt1
            if num >= crit_chance2:
                if num >= accuracy2:
                    if num <= dodge_rate1 :
                        hp1 = hp1 - N_hurt2
                        hp2 = hp2 - B_hurt1
                        if hp1 <= 0:
                            hp1 = 0
                            print('attacker crit defender for', B_hurt1, 'points of damage')
                            print('defender hit attacker for', N_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                        else:
                            hp1 = hp1
                            print('attacker crit defender for', B_hurt1, 'points of damage')
                            print('defender hit attacker for', N_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                    else:
                        print('attacker crit defender for', B_hurt1, 'points of damage')
                        print('attacker dodged defender\'s attack')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    print('attacker crit defender for', B_hurt1, 'points of damage')
                    print('defender missed attacker')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
            else:
                hp1 = hp1 - B_hurt2
                hp2 = hp2 - B_hurt1
                if hp1 <= 0:
                    hp1 = 0
                    print('attacker crit defender for', B_hurt1, 'points of damage')
                    print('defender crit attacker for', B_hurt2, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    hp1 = hp1
                    print('attacker crit defender for', B_hurt1, 'points of damage')
                    print('defender crit attacker for', B_hurt2 ,'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
    else:
        if num <= accuracy1:
            if num >= dodge_rate2:
                if N_hurt1 >= hp2 :
                    print('attacker hit defender for', N_hurt1, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has 0 hp left')
                else:
                    if num >= crit_chance2:
                        if num >= accuracy2:
                            if dodge_rate1 <= 80:
                                hp2 = hp2 - N_hurt1
                                hp1 = hp1 - 7
                                if hp1 <= 0:
                                    print('attacker hit defender for', N_hurt1, 'points of damage')
                                    print('defender hit attacker for 7 points of damage')
                                    print('After fighting the attacker has 0 hp left and the defender has', hp2,
                                          'hp left')
                                else:
                                    print('attacker hit defender for', N_hurt1, 'points of damage')
                                    print('defender hit attacker for 7 points of damage')
                                    print('After fighting the attacker has', hp1,  'hp left and the defender has', hp2,
                                    'hp left')
                            else:
                                hp1 = hp1
                                hp2 = hp2 - N_hurt1
                                print('attacker hit defender for', N_hurt1, 'points of damage')
                                print('attacker dodged defender\'s attack')
                                print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                      'hp left')
                        else:
                            print('attacker hit defender for', N_hurt1, 'points of damage')
                            print('defender missed attacker')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                    else:
                        hp1 = hp1 - B_hurt2
                        hp2 = hp2 - N_hurt1
                        if hp1 <= 0:
                            hp1 = 0
                            print('attacker hit defender for', N_hurt1, 'points of damage')
                            print('defender crit attacker for', B_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has ', hp2,
                                  'hp left')
                        else :
                            hp1 = hp1
                            print('attacker hit defender for', N_hurt1, 'points of damage')
                            print('defender crit attacker for', B_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has ', hp2, 'hp left')
            else:
                if num >= crit_chance2:
                    if num <= accuracy2:
                        if num >= dodge_rate1:
                            hp1 = hp1 - N_hurt2
                            hp2 = hp2 - N_hurt1
                            if hp1 <= 0:
                                hp1 = 0
                            else:
                                hp1 = hp1
                                print('defender dodged attacker\'s attack')
                                print('defender hit attacker for', N_hurt2, 'points of damage')
                                print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                        else:
                            print('defender dodged attacker\'s attack')
                            print('attacker dodged defender\'s attack')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                    else:
                        print('defender dodged attacker\'s attack')
                        print('defender missed attacker')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    if hp1 <= 0:
                        hp1 = 0
                        hp2 = hp2 - N_hurt1
                        print('defender dodged attacker\'s attack')
                        print('defender crit attacker for', B_hurt2, 'points of damage')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has ', hp2,
                              'hp left')
                    else:
                        hp1 = hp1
                        print('defender dodged attacker\'s attack')
                        print('defender crit attacker for', B_hurt2, 'points of damage')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has ', hp2, 'hp left')

        else:
            if num <= crit_chance2:
                if num <= accuracy2:
                    if num >= dodge_rate1:
                        hp1 = hp1 - N_hurt2
                        if hp1 <= 0:
                            hp1 = 0
                        else:
                            hp1 = hp1
                            print('attacker missed defender')
                            print('defender hit attacker for', N_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                    else:
                        print('attacker missed defender')
                        print('attacker dodged defender\'s attack')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    print('attacker missed defender')
                    print('defender missed attacker')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
            else:
                hp1 = hp1 - B_hurt2
                if hp1 <= 0:
                    hp1 = 0
                    print('attacker missed defender')
                    print('defender crit attacker for ', B_hurt2, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    hp1 = hp1
                    print('attacker missed defender')
                    print('defender crit attacker for', B_hurt2, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
else:
    if num <= crit_chance1:
        hp2 = hp2 - B_hurt1
        if hp2 <= 0:
            hp2 = 0
            print('attacter crit defender for', B_hurt1, 'points of damage')
            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
        else:
            hp2 = hp2
            print('attacter crit defender for', B_hurt1, 'points of damage')
            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
    else:
        if num <= accuracy1:
            if num >= dodge_rate2:
                hp2 = hp2 - N_hurt1
                if hp2 <= 0:
                    hp2 = 0
                    print('attacker hit defender for', N_hurt1, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    hp2 = hp2
                    print('attacker hit defender for', N_hurt1, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
            else:
                if num >= crit_chance2:
                    if num <= accuracy2:
                        if num >= dodge_rate1:
                            hp1 = hp1 - N_hurt2
                            if hp2 <= 0:
                                hp2 = 0
                                print('defender dodged attacker\'s attack')
                                print('defender hit attacker for', N_hurt2, 'points of damage')
                                print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                      'hp left')
                            else:
                                 hp2 = hp2
                                 print('defender dodged attacker\'s attack')
                                 print('defender hit attacker for', N_hurt2, 'points of damage')
                                 print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                        else:
                            print('defender dodged attacker\'s attack')
                            print('attacker dodged defender\'s attack')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                    else:
                        print('defender dodged attacker\'s attack')
                        print('defender missed attacker')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    hp1 = hp1 - B_hurt2
                    if hp1 <= 0:
                        hp1 = 0
                        print('defender dodged attacker\'s attack')
                        print('defender crit attacker for ', B_hurt2, 'points of damage')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                    else:
                        hp1 = hp1
                        print('defender dodged attacker\'s attack')
                        print('defender crit attacker for ', B_hurt2, 'points of damage')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
        else:
            if num >= crit_chance2:
                hp1 = hp1 - B_hurt2
                if hp1 <= 0:
                    hp1 = 0
                    print('attacker missed defender')
                    print('defender crit attacker for', B_hurt2, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')

                else:
                    hp1 = hp1
                    print('attacker missed defender')
                    print('defender crit attacker for', B_hurt2, 'points of damage')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
            else:
                if num <= accuracy2:
                    if num >= dodge_rate1:
                        hp1 = hp1 - N_hurt2
                        if hp1 <= 0:
                            hp1 = 0
                            print('attacker missed defender')
                            print('defender hit attacker for', N_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2,
                                  'hp left')
                        else:
                            hp1 = hp1
                            print('attacker missed defender')
                            print('defender hit attacker for', N_hurt2, 'points of damage')
                            print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                    else:
                        print('attacker missed defender')
                        print('attacker dodged defender\'s attack')
                        print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')
                else:
                    print('attacker missed defender')
                    print('defender missed attacker')
                    print('After fighting the attacker has', hp1, 'hp left and the defender has', hp2, 'hp left')

