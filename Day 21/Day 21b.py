def fight(player, boss):
    player_hp = player[0]
    player_at = player[1]
    player_ar = player[2]
    boss_hp = boss[0]
    boss_at = boss[1]
    boss_ar = boss[2]
    while True:
        # Players turn:
        boss_hp -= max(1, player_at - boss_ar)
        if boss_hp <= 0:
            return True
        # Boss turn
        player_hp -= max(1, boss_at - player_ar)
        if player_hp <= 0:
            return False


weapon = ((8, 4), (10, 5), (25, 6), (40, 7), (74, 8))
armor = ((0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5))
ring = ((0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3))

boss = (100, 8, 2)

sets = []

for i in range(len(weapon)):
    for j in range(len(armor)):
        for k in range(len(ring)):
            ring_2 = list(ring)
            if ring[k] != (0, 0, 0):
                ring_2.remove(ring[k])
                ring_2 = tuple(ring_2)
            for l in range(len(ring_2)):
                # items = (weapon[i], armor[j], ring[k], ring_2[l])
                price = weapon[i][0] + armor[j][0] + ring[k][0] + ring_2[l][0]
                damage = weapon[i][1] + ring[k][1] + ring_2[l][1]
                armor_rate = armor[j][1] + ring[k][2] + ring_2[l][2]
                sets.append((price, damage, armor_rate))
                # print(price, damage, armor_rate)

sets.sort(reverse=True)

for line in sets:
    print(line)

for item in sets:
    player = (100, item[1], item[2])
    if not fight(player, boss):
        print(f'Boss wins, gold spend = {item[0]}')
        print(item)
        exit()

