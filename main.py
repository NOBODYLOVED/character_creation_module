from random import randint

from graphic_arts.start_game_banner import run_screensaver

msg = 'нанёс урон противнику равный'

used = 'применил специальное умение'

atk = 'attack — чтобы атаковать противника'

defe = 'defence — чтобы блокировать атаку противника'

spe = 'special — чтобы использовать свою суперсилу.'

cha_name = 'Введи название персонажа, за которого хочешь играть:'

war = 'Воитель — warrior'

mag = 'Маг — mage'

heal = 'Лекарь — healer'

war_spe = 'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный'

ma_spe = 'Маг — находчивый воин дальнего боя. Обладает высоким интеллектом'

heal_spe = 'Лекарь — могущественный заклинатель.'

heal_spe2 = 'Черпает силы из природы, веры и духов'

apt = 'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '

apt2 = 'чтобы выбрать другого персонажа'


def attack(char_name: str, char_class: str) -> str:
    """Do attack action."""
    if char_class == 'warrior':
        return (f'{char_name} {msg} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {msg} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {msg} {5 + randint(-3, -1)}')
    return None


def defence(char_name: str, char_class: str) -> str:
    """Do defence action."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return None


def special(char_name: str, char_class: str) -> str:
    """Cast special."""
    if char_class == 'warrior':
        return (f'{char_name} {used} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {used} «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {used} «Защита {10 + 30}»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Actually the tree of the game."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(f'Введи одну из команд: {atk}, {defe} или {spe}.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Class selection module."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(f'{cha_name} {war}, {mag}, {heal}: ')
        if char_class == 'warrior':
            print(f'{war_spe}.')
        if char_class == 'mage':
            print(f'{ma_spe}.')
        if char_class == 'healer':
            print(f'{heal_spe} {heal_spe2}.')
        approve_choice = input(f'{apt} {apt2} ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
