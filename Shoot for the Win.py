# чета мишени от конзолата, разделям със сплит и превръщам в инт
# правя while цикъл докато не получа команда Енд
# превръщам командата в инт и проверявам дали е валиден индекс
# проверявам дали мишената не е = -1
# фор цикъл за определяне на по-големите мишени и намалявам ст-стта им със стойността на отстреляната мишена
# фор цикъл за определяне на по-малките или равни мишени, но различни от -1 и увеличавам ст-стта им със стойността на отстреляната мишена
# отстреляната мишена става = -1
#
#
#
targets = input().split()
targets = [int(n) for n in targets]
command = input()
while not command == "End":
    index_to_shoot = int(command)
    if index_to_shoot < len(targets):
        if not targets[index_to_shoot] == -1:
            target_value = targets[index_to_shoot]
            targets[index_to_shoot] = -1
            for index in range(len(targets)):
                if not targets[index] == -1:
                    if targets[index] > target_value:
                        targets[index] -= target_value
                    else:
                        targets[index] += target_value

    command = input()
shot_targets = targets.count(-1)
targets = [str(n) for n in targets]
print(f"Shot targets: {shot_targets} -> {' '.join(targets)}")
