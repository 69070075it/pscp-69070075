'''Impostor'''
import json
def main():
    '''Impostor'''
    alive = {}
    dead = {}

    while True:
        line = input().strip()
        if line == "Start":
            break
        player_dict = json.loads(line)
        alive.update(player_dict)

    while True:
        name = input().strip()
        if name == "End":
            break
        if name in alive:
            dead[name] = alive[name]
            del alive[name]

    impostor_count = list(alive.values()).count("Impostor")

    print(f"{impostor_count} Impostor Remains")
    print("***Alive***")
    for name in sorted(alive.keys()):
        print(f"{name} : {alive[name]}")

    print("***Dead***")
    for name in sorted(dead.keys()):
        print(f"{name} : {dead[name]}")
main()
