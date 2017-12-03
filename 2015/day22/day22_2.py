spells = ((53,4,0,-1,0),(73,2,2,-1,0),(113,0,0,0,6),(173,0,0,1,6),(229,0,0,2,5))

def f(hp, mana, boss_hp, timers, turn, current_cost, max_cost):
    global spells
    if(turn):
        hp -= 1
    if hp <= 0 or current_cost > max_cost and boss_hp > 0:
        return -1

    timers[0] = max(timers[0]-1,0)
    if timers[1] > 0:
        boss_hp -= 3
        timers[1] -= 1
    if timers[2] > 0:
        mana += 101
        timers[2] -= 1
    
    if boss_hp <= 0:
        return current_cost

    if turn:
        min_cost = -1
        for m,d,h,i,r in spells:
            if mana >= m:
                t = timers[:]
                if i >= 0:
                    t[i] = r
                cost = f(hp+h, mana-m, boss_hp-d, t, False, current_cost+m, max_cost)
                if cost >= 0 and (cost < min_cost or min_cost < 0):
                    min_cost = cost
                    max_cost = cost
        return min_cost

    else:
        hp -= 2 if timers[0]>0 else 9
        return -1 if hp <= 0 else f(hp, mana, boss_hp, timers, True, current_cost, max_cost)

print f(50, 500, 51, [0,0,0], True, 0, 9999)
