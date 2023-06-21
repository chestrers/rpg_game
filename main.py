import pygame
import sys

# import haracteristiki

# from haracteristiki import strength, attack, agility, hp, mana, intelligence, experience, defence, lvl


shirina = 700
visota = 400

clock = pygame.time.Clock()


def run():
    pygame.init()
    # инициализация
    screen = pygame.display.set_mode((shirina, visota), pygame.RESIZABLE)
    # отображение и размер дисплея
    tekushi_razmer = screen.get_size()
    # для растягивания дисиплея
    virtual_poverhnost = pygame.Surface((shirina, visota))
    # виртуальная поверхность для игры
    pygame.display.set_caption("rpg")
    # название игры

    walk_right = [
        pygame.image.load("char right/1r.png"),
        pygame.image.load("char right/2r.png"),
        pygame.image.load("char right/3r.png"),
        pygame.image.load("char right/4r.png")

    ]
    # движение перса в право
    walk_left = [
        pygame.image.load("char left/l1.png"),
        pygame.image.load("char left/l2.png"),
        pygame.image.load("char left/l3.png"),
        pygame.image.load("char left/l4.png")
    ]
    #     движение перса в лево
    player_wait = pygame.image.load("char wait/wait.png")
    enemy = pygame.image.load('enemy/враги.png')

    # меню
    start_button = pygame.image.load("menu/start.png")

    # локация
    location = [
        pygame.image.load("menu/menu.png"),
        pygame.image.load("image fon/location1.png"),
        pygame.image.load("image fon/location1,2.png"),
        pygame.image.load("image fon/location1,3.png"),
        pygame.image.load("image fon/location1,4.png")

    ]

    start = 0
    location_animation = 0
    location_animation2 = 0
    position_start = 400
    position_menu1 = 0
    position_menu2 = 120
    walk_enemy = 0
    enemyx = 500
    enemyy = 315
    walk_rect = 500
    playerx = -50
    playery = -65
    speed = 5
    hp_enemy = 10
    hod = 1
    BLUE = (0, 0, 255)
    # счетчик локации
    player_animation_count = 0
    # счетчик анимации персонажа
    # характеристики и лвлап
    strength = 0
    agility = 0
    intelligence = 0
    attack = 5 + strength
    defence = 0 + agility
    hp = 10 + strength * 4
    mana = 0 * intelligence * 4
    lvl = 1
    experience = 0
    exp2 = 50

    while True:
        # бесконечый цицл

        clock.tick(30)

        # загрузка заднего фона
        # player = pygame.image.load("char right/1r.png")
        # отображение персонажа
        virtual_poverhnost.blit(location[0], (0, position_menu1))
        virtual_poverhnost.blit(location[1], (location_animation, position_start))
        virtual_poverhnost.blit(location[2], (location_animation + 700, 0))
        virtual_poverhnost.blit(location[3], (location_animation + 1400, 0))
        virtual_poverhnost.blit(location[4], (location_animation + 2100, 0))
        # virtual_poverhnost.blit(fight_location, (0, -360))
        virtual_poverhnost.blit(enemy, (walk_enemy + enemyx, enemyy))
        # отображение картинки по координатам (заднего фона)

        virtual_poverhnost.blit(start_button, (225 + location_animation, position_menu2))

        # кнопки меню

        player_rect = walk_right[0].get_rect(topleft=(250, 325))
        enemy_rect = enemy.get_rect(topleft=(walk_rect, enemyy))
        start_rect = start_button.get_rect(topleft=(225, position_menu2))
        # отслеживание прикосновений

        keys = pygame.key.get_pressed()
        key = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()


        # назначение клавиш
        if keys[pygame.K_RIGHT] and start == 1:
            virtual_poverhnost.blit(walk_right[player_animation_count], (250, 325))
        elif keys[pygame.K_LEFT] and start == 1:
            virtual_poverhnost.blit(walk_left[player_animation_count], (250, 325))
        else:
            virtual_poverhnost.blit(player_wait, (250, 325))

        # if mouse[0]:
        #
        #     print(mouse)



        #  отображение персонажа по координатам

        if keys[pygame.K_RIGHT] and start == 1:
            location_animation -= speed
            location_animation2 -= speed
            player_animation_count += 1
            walk_enemy -= speed
            walk_rect -= speed
            # if location_animation == -600:
            #     location_animation = 0
        if player_animation_count == 3:
            player_animation_count = 0

        elif keys[pygame.K_LEFT] and start == 1:
            location_animation += speed
            location_animation2 += speed
            player_animation_count += 1
            walk_enemy += speed
            walk_rect += speed
            # if location_animation == 600:
            #     location_animation = 0
        if player_animation_count == 3:
            player_animation_count = 0

        if key[0] and start_rect.collidepoint(pos):
            print("1")
            start = 1
            position_start = 0
            position_menu2 += 400
            position_menu1 += 400
            print(start_rect.height)






        # иф с назначеными клавешами



        # if location_animation == -20 and not hp_enemy == 0 or location_animation == -50 and not hp_enemy == 0:
        if player_rect.colliderect(enemy_rect) and hp_enemy >= 1:
            speed = 0
            virtual_poverhnost.blit(location[1], (0, 0))
            virtual_poverhnost.blit(player_wait, (50, 325))
            virtual_poverhnost.blit(enemy, (enemyx, enemyy))
            if keys[pygame.K_DOWN]:
                hp_enemy -= attack


                if hp_enemy <= 0 or hp_enemy < 0:
                    location_animation = location_animation2
                    virtual_poverhnost.blit(location[1], (location_animation2, 0))
                    virtual_poverhnost.blit(player_wait, (-80, +29))
                    speed = 5
                    experience += 50

        if location_animation == 450 or location_animation == -560 or location_animation == 90:
            hp_enemy = 10

        if experience >= exp2:
            lvl += 1
            exp2 *= 1.7
            strength += 4
            agility += 4
            intelligence += 4
            hp += strength * 4
            attack += strength
            defence += agility * 0.5
            mana += intelligence * 4
            print("опыт", experience)
            print("нужен опыт", exp2)
            print("уровень", lvl)
            print("сила", strength)
            print("ловкость", agility)
            print("интелект", intelligence)
            print("здоровье", hp)
            print("защита", defence)
            print("мана", mana)
            print("атака", attack)

        # механика боя

        # загрузка боя
        # иф взаимодействие с врагами

        for event in pygame.event.get():
            # цикл обработки события
            if event.type == pygame.QUIT:
                sys.exit()
            # иф выходи из игры

            elif event.type == pygame.VIDEORESIZE:
                tekushi_razmer = event.size


            # элиф ратсягивабщегося экрана

        pygame.display.update()
        # обновление экрана
        pygame.display.flip()
        # отображение экрана
        scaled_surface = pygame.transform.scale(virtual_poverhnost, tekushi_razmer)
        screen.blit(scaled_surface, (0, 0))
        # отображение виртуального экрана


run()
