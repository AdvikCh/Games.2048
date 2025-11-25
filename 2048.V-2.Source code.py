import pygame; import pygame.freetype; import random; import os; pygame.init(); pygame.freetype.init()
WINDOW_WIDTH = pygame.display.Info().current_w; WINDOW_HEIGHT = pygame.display.Info().current_h; WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN | pygame.SRCALPHA); OVERLAY = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA); pygame.display.set_caption("2048", "2048"); LOGO = pygame.image.load("Branding/Logo.png"); pygame.display.set_icon(LOGO); MARGIN = WINDOW_WIDTH / 100; OPTIONS_WIDTH = WINDOW_WIDTH / 20

BLACK = (0, 0, 0); DARK = (30, 30, 30); WHITE = (255, 255, 255)
FONT_SIZE_1 = pygame.freetype.Font("Assets/Font.otf", WINDOW_HEIGHT / 4); FONT_SIZE_1_HEIGHT = FONT_SIZE_1.render("")[0].get_height(); FONT_SIZE_2 = pygame.freetype.Font("Assets/Font.otf", WINDOW_HEIGHT / 6); FONT_SIZE_2_HEIGHT = FONT_SIZE_2.render("")[0].get_height(); FONT_SIZE_3 = pygame.freetype.Font("Assets/Font.otf", WINDOW_HEIGHT / 8); FONT_SIZE_3_HEIGHT = FONT_SIZE_3.render("")[0].get_height(); FONT_SIZE_4 = pygame.freetype.Font("Assets/Font.otf", WINDOW_HEIGHT / 10); FONT_SIZE_4_HEIGHT = FONT_SIZE_4.render("")[0].get_height()
def image_shaders(image, colour): image = image.copy(); image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT); image.fill(colour + (0,), None, pygame.BLEND_RGBA_ADD); return image
IMAGE_BUTTONS_CLOSE = pygame.transform.scale(pygame.image.load("Assets/Close#Button.png").convert_alpha(), (OPTIONS_WIDTH, OPTIONS_WIDTH)); IMAGE_BUTTONS_HELP = pygame.transform.scale(pygame.image.load("Assets/Settings-Help#Button.png").convert_alpha(), (OPTIONS_WIDTH, OPTIONS_WIDTH)); IMAGE_BUTTONS_DARK_MODE_ON = pygame.transform.scale(pygame.image.load("Assets/Settings-Dark mode-On#Button.png"), (OPTIONS_WIDTH, OPTIONS_WIDTH)); IMAGE_BUTTONS_DARK_MODE_OFF = pygame.transform.scale(pygame.image.load("Assets/Settings-Dark mode-Off#Button.png"), (OPTIONS_WIDTH, OPTIONS_WIDTH)); IMAGE_BUTTONS_RESET = pygame.transform.scale(pygame.image.load("Assets/Reset#Button.png"), (OPTIONS_WIDTH * 2, OPTIONS_WIDTH * 2)); IMAGE_BUTTONS_CHECKED = pygame.transform.scale(pygame.image.load("Assets/Checked#Button.png"), (OPTIONS_WIDTH, OPTIONS_WIDTH))

COLOUR_0 = (255, 255, 255); COLOUR_2 = (155, 155, 155); COLOUR_4 = (155, 155, 155); COLOUR_8 = (255, 175, 120); COLOUR_16 = (255, 145, 100); COLOUR_32 = (249, 123, 100); COLOUR_64 = (225, 30, 35); COLOUR_128 = (235, 200, 115); COLOUR_256 = (235, 200, 100); COLOUR_512 = (235, 200, 80); COLOUR_1024 = (235, 200, 65); COLOUR_2048 = WHITE
BOARD_WIDTH = (WINDOW_WIDTH / 3) + (WINDOW_WIDTH / 8); BOARD_X = (WINDOW_WIDTH / 2) - (BOARD_WIDTH / 2); BOARD_Y = WINDOW_HEIGHT - BOARD_WIDTH - MARGIN; SPACE_WIDTH = (BOARD_WIDTH - ((MARGIN / 2) * 5)) / 4
SPACE_1_X = BOARD_X + (MARGIN / 2); SPACE_1_Y = BOARD_Y + (MARGIN / 2)
SPACE_2_X = BOARD_X + SPACE_WIDTH + MARGIN; SPACE_2_Y = BOARD_Y + (MARGIN / 2)
SPACE_3_X = BOARD_X + (SPACE_WIDTH * 2) + (MARGIN * 1.5); SPACE_3_Y = BOARD_Y + (MARGIN / 2)
SPACE_4_X = BOARD_X + (SPACE_WIDTH * 3) + (MARGIN * 2); SPACE_4_Y = BOARD_Y + (MARGIN / 2)
SPACE_5_X = BOARD_X + (MARGIN / 2); SPACE_5_Y = BOARD_Y + SPACE_WIDTH + MARGIN
SPACE_6_X = BOARD_X + SPACE_WIDTH + MARGIN; SPACE_6_Y = BOARD_Y + SPACE_WIDTH + MARGIN
SPACE_7_X = BOARD_X + (SPACE_WIDTH * 2) + (MARGIN * 1.5); SPACE_7_Y = BOARD_Y + SPACE_WIDTH + MARGIN
SPACE_8_X = BOARD_X + (SPACE_WIDTH * 3) + (MARGIN * 2); SPACE_8_Y = BOARD_Y + SPACE_WIDTH + MARGIN
SPACE_9_X = BOARD_X + (MARGIN / 2); SPACE_9_Y = BOARD_Y + (SPACE_WIDTH * 2) + (MARGIN * 1.5)
SPACE_10_X = BOARD_X + SPACE_WIDTH + MARGIN; SPACE_10_Y = BOARD_Y + (SPACE_WIDTH * 2) + (MARGIN * 1.5)
SPACE_11_X = BOARD_X + (SPACE_WIDTH * 2) + (MARGIN * 1.5); SPACE_11_Y = BOARD_Y + (SPACE_WIDTH * 2) + (MARGIN * 1.5)
SPACE_12_X = BOARD_X + (SPACE_WIDTH * 3) + (MARGIN * 2); SPACE_12_Y = BOARD_Y + (SPACE_WIDTH * 2) + (MARGIN * 1.5)
SPACE_13_X = BOARD_X + (MARGIN / 2); SPACE_13_Y = BOARD_Y + (SPACE_WIDTH * 3) + (MARGIN * 2)
SPACE_14_X = BOARD_X + SPACE_WIDTH + MARGIN; SPACE_14_Y = BOARD_Y + (SPACE_WIDTH * 3) + (MARGIN * 2)
SPACE_15_X = BOARD_X + (SPACE_WIDTH * 2) + (MARGIN * 1.5); SPACE_15_Y = BOARD_Y + (SPACE_WIDTH * 3) + (MARGIN * 2)
SPACE_16_X = BOARD_X + (SPACE_WIDTH * 3) + (MARGIN * 2); SPACE_16_Y = BOARD_Y + (SPACE_WIDTH * 3) + (MARGIN * 2)
spaces = {"space_1": 0, "space_2": 0, "space_3": 0, "space_4": 0, "space_5": 0, "space_6": 0, "space_7": 0, "space_8": 0, "space_9": 0, "space_10": 0, "space_11": 0, "space_12": 0, "space_13": 0, "space_14": 0, "space_15": 0, "space_16": 0}

CLOSE_X = (WINDOW_WIDTH - OPTIONS_WIDTH) - MARGIN

guide = open("Assets/Help.txt"); guide = guide.readlines(); times_won = guide[-2]; times_won = int(times_won[15:len(guide[-2])]); high_score = guide[-1]; high_score = int(high_score[16:len(guide[-1])]); score = 0

def main(direction: str | None = ""):
    global game_won, game_lost, score, times_won, high_score, spaces, space, SPACE_WIDTH, LOGO_X, SPACE_1_X, SPACE_2_X, SPACE_3_X, SPACE_4_X, SPACE_5_X, SPACE_6_X, SPACE_7_X, SPACE_8_X, SPACE_9_X, SPACE_10_X, SPACE_11_X, SPACE_12_X, SPACE_13_X, SPACE_14_X, SPACE_15_X, SPACE_16_X, SPACE_1_Y, SPACE_2_Y, SPACE_3_Y, SPACE_4_Y, SPACE_5_Y, SPACE_6_Y, SPACE_7_Y, SPACE_8_Y, SPACE_9_Y, SPACE_10_Y, SPACE_11_Y, SPACE_12_Y, SPACE_13_Y, SPACE_14_Y, SPACE_15_Y, SPACE_16_Y, TEMP_text_surface, TEMP_y, TEMP_text_surface_2
    
    WINDOW.fill(DARK if dark_mode else WHITE)
    WINDOW.blit(IMAGE_BUTTONS_CLOSE if dark_mode else image_shaders(IMAGE_BUTTONS_CLOSE, BLACK), (CLOSE_X, MARGIN)); WINDOW.blit(IMAGE_BUTTONS_DARK_MODE_ON if dark_mode else IMAGE_BUTTONS_DARK_MODE_OFF, (MARGIN, MARGIN)); WINDOW.blit(IMAGE_BUTTONS_HELP if dark_mode else image_shaders(IMAGE_BUTTONS_HELP, BLACK), (MARGIN, OPTIONS_WIDTH + (MARGIN * 2)))
    TEMP_text_surface = FONT_SIZE_1.render(f"{score}", WHITE if dark_mode else BLACK)[0]; WINDOW.blit(TEMP_text_surface, ((WINDOW_WIDTH / 2) - (TEMP_text_surface.get_width() / 2), (BOARD_Y / 2) - (TEMP_text_surface.get_height() / 2)))
    TEMP_text_surface = FONT_SIZE_1.render(f"{high_score}", WHITE if dark_mode else BLACK)[0]; WINDOW.blit(TEMP_text_surface, (BOARD_X + BOARD_WIDTH + ((WINDOW_WIDTH - BOARD_WIDTH) / 4) - (TEMP_text_surface.get_width() / 2), (WINDOW_HEIGHT / 2) - (TEMP_text_surface.get_height() / 2))); TEMP_text_surface_2 = FONT_SIZE_3.render("high score", WHITE if dark_mode else BLACK)[0]; WINDOW.blit(TEMP_text_surface_2, (BOARD_X + BOARD_WIDTH + ((WINDOW_WIDTH - BOARD_WIDTH) / 4) - (TEMP_text_surface_2.get_width() / 2), (WINDOW_HEIGHT / 2) - (TEMP_text_surface.get_height() / 2) - MARGIN - TEMP_text_surface_2.get_height()))
    if times_won > 0:
        LOGO_X = ((WINDOW_WIDTH - BOARD_WIDTH) / 4) - (OPTIONS_WIDTH * 2); LOGO_Y = (WINDOW_HEIGHT / 2) - (OPTIONS_WIDTH * 2); WINDOW.blit(pygame.transform.scale(pygame.image.load("Branding/Logo.png"), (OPTIONS_WIDTH * 4, OPTIONS_WIDTH * 4)), (LOGO_X, LOGO_Y))
        TEMP_text_surface = FONT_SIZE_3.render("times won", WHITE if dark_mode else BLACK)[0]; WINDOW.blit(TEMP_text_surface, (LOGO_X + (OPTIONS_WIDTH * 2) - (TEMP_text_surface.get_width() / 2), LOGO_Y - MARGIN - TEMP_text_surface.get_height()))
        TEMP_text_surface = FONT_SIZE_1.render(f"{times_won}", WHITE if dark_mode else BLACK)[0]; WINDOW.blit(TEMP_text_surface, (LOGO_X + (OPTIONS_WIDTH * 2) - (TEMP_text_surface.get_width() / 2), LOGO_Y + (OPTIONS_WIDTH * 4) + MARGIN))
    
    if direction == "U":
        for space in range(5, 17):
            if spaces[f"space_{space - 4}"] == 0: spaces[f"space_{space - 4}"] = spaces[f"space_{space}"]; spaces[f"space_{space}"] = 0
            elif spaces[f"space_{space - 4}"] == spaces[f"space_{space}"]: spaces[f"space_{space - 4}"] += spaces[f"space_{space}"]; score += (spaces[f"space_{space}"]) * 2; spaces[f"space_{space}"] = 0
    elif direction == "L":
        for space in range(1, 17):
            if space != 1 and space != 5 and space != 9 and space != 13:
                if spaces[f"space_{space - 1}"] == 0: spaces[f"space_{space - 1}"] = spaces[f"space_{space}"]; spaces[f"space_{space}"] = 0
                elif spaces[f"space_{space - 1}"] == spaces[f"space_{space}"]: spaces[f"space_{space - 1}"] += spaces[f"space_{space}"]; score += (spaces[f"space_{space}"]) * 2; spaces[f"space_{space}"] = 0
    elif direction == "R":
        for space in range(16, 0, -1):
            if space != 4 and space != 8 and space != 12 and space != 16:
                if spaces[f"space_{space + 1}"] == 0: spaces[f"space_{space + 1}"] = spaces[f"space_{space}"]; spaces[f"space_{space}"] = 0
                elif spaces[f"space_{space + 1}"] == spaces[f"space_{space}"]: spaces[f"space_{space + 1}"] += spaces[f"space_{space}"]; score += (spaces[f"space_{space}"]) * 2; spaces[f"space_{space}"] = 0
    elif direction == "D":
        for space in range(12, 0, -1):
            if spaces[f"space_{space + 4}"] == 0: spaces[f"space_{space + 4}"] = spaces[f"space_{space}"]; spaces[f"space_{space}"] = 0
            elif spaces[f"space_{space + 4}"] == spaces[f"space_{space}"]: spaces[f"space_{space + 4}"] += spaces[f"space_{space}"]; score += (spaces[f"space_{space}"]) * 2; spaces[f"space_{space}"] = 0
    if score > high_score: high_score = score; guide = open("Assets/help.txt", "w"); guide.write(f"2048 Guide\n===============================================================================\n\n* Key-board Controls:\n  0. Universal:\n    * 'esc' closes the game\n    * '-' & '=' toggle dark-mode\n    * '/' or 'h' opens this guide\n  1. In-game:\n    * 'w' or 'UP[-Arrow]' shift the blocks up\n    * 'a' or 'LEFT[-Arrow]' shift the blocks left\n    * 's' or 'DOWN[-Arrow]' shift the blocks down\n    * 'd' or 'RIGHT[-Arrow]' shift the blocks right\n\n* Stats:\n  * Times-won: {times_won}\n  * High-score: {high_score}"); guide.close()
    
    pygame.draw.rect(WINDOW, BLACK, (BOARD_X, BOARD_Y, BOARD_WIDTH, BOARD_WIDTH))
    for space in range(1, 17):
        eval(f"pygame.draw.rect(WINDOW, COLOUR_{spaces[f'space_{space}']}, (SPACE_{space}_X, SPACE_{space}_Y, SPACE_WIDTH, SPACE_WIDTH))")
        if spaces[f"space_{space}"] != 0:
            TEMP_text_surface = eval(f"FONT_SIZE_2.render(f'{spaces[f'''space_{space}''']}', WHITE)")[0]
            if TEMP_text_surface.get_width() > SPACE_WIDTH:
                TEMP_text_surface = eval(f"FONT_SIZE_3.render(f'{spaces[f'''space_{space}''']}', WHITE)")[0]
                if TEMP_text_surface.get_width() > SPACE_WIDTH: TEMP_text_surface = eval(f"FONT_SIZE_4.render(f'{spaces[f'''space_{space}''']}', WHITE)")[0]
            if spaces[f"space_{space}"] == 2048: game_won = [True, space]
            else: WINDOW.blit(TEMP_text_surface, (eval(f"SPACE_{space}_X + (SPACE_WIDTH / 2) - (TEMP_text_surface.get_width() / 2)"), eval(f"SPACE_{space}_Y + (SPACE_WIDTH / 2) - (TEMP_text_surface.get_height() / 2)")))
    pygame.display.update()
    
    if game_won[0]:
        SNAPSHOT = WINDOW.copy()
        eval(f"WINDOW.blit(pygame.transform.scale(LOGO, (SPACE_WIDTH, SPACE_WIDTH)), (SPACE_{game_won[1]}_X, SPACE_{game_won[1]}_Y))"); pygame.display.update(); pygame.time.wait(1000)
        TEMP_x = (LOGO_X - eval(f"SPACE_{game_won[1]}_X")) / 100; TEMP_y = (LOGO_Y - eval(f"SPACE_{game_won[1]}_Y")) / 100; TEMP_width = ((OPTIONS_WIDTH * 4) - SPACE_WIDTH) / 100
        for TEMP in range(1, 101):
            WINDOW.blit(SNAPSHOT); WINDOW.blit(pygame.transform.scale(LOGO, (SPACE_WIDTH + (TEMP_width * TEMP), SPACE_WIDTH + (TEMP_width * TEMP))), (eval(f"SPACE_{game_won[1]}_X") + (TEMP_x * TEMP), eval(f"SPACE_{game_won[1]}_Y") + (TEMP_y * TEMP)))
            pygame.display.update(); pygame.time.wait(10)
        times_won += 1; guide = open("Assets/help.txt", "w"); guide.write(f"2048 Guide\n===============================================================================\n\n* Key-board Controls:\n  0. Universal:\n    * 'esc' closes the game\n    * '-' & '=' toggle dark-mode\n    * '/' or 'h' opens this guide\n  1. In-game:\n    * 'w' or 'UP[-Arrow]' shift the blocks up\n    * 'a' or 'LEFT[-Arrow]' shift the blocks left\n    * 's' or 'DOWN[-Arrow]' shift the blocks down\n    * 'd' or 'RIGHT[-Arrow]' shift the blocks right\n\n* Stats:\n  * Times-won: {times_won}\n  * High-score: {high_score}"); guide.close()
        spaces = {"space_1": 0, "space_2": 0, "space_3": 0, "space_4": 0, "space_5": 0, "space_6": 0, "space_7": 0, "space_8": 0, "space_9": 0, "space_10": 0, "space_11": 0, "space_12": 0, "space_13": 0, "space_14": 0, "space_15": 0, "space_16": 0}; game_won = [False, 0]
    if (spaces["space_1"] != 0 and spaces["space_2"] != 0 and spaces["space_3"] != 0 and spaces["space_4"] != 0 and spaces["space_5"] != 0 and spaces["space_6"] != 0 and spaces["space_7"] != 0 and spaces["space_8"] != 0 and spaces["space_9"] != 0 and spaces["space_10"] != 0 and spaces["space_11"] != 0 and spaces["space_12"] != 0 and spaces["space_13"] != 0 and spaces["space_14"] != 0 and spaces["space_15"] != 0 and spaces["space_16"] != 0) and ((spaces["space_1"] != spaces["space_2"] and spaces["space_1"] != spaces["space_5"]) and (spaces["space_2"] != spaces["space_3"] and spaces["space_2"] != spaces["space_6"]) and (spaces["space_3"] != spaces["space_4"] and spaces["space_3"] != spaces["space_7"]) and (spaces["space_4"] != spaces["space_8"]) and (spaces["space_5"] != spaces["space_6"] and spaces["space_5"] != spaces["space_9"]) and (spaces["space_6"] != spaces["space_7"] and spaces["space_6"] != spaces["space_10"]) and (spaces["space_7"] != spaces["space_8"] and spaces["space_7"] != spaces["space_11"]) and (spaces["space_8"] != spaces["space_12"]) and (spaces["space_9"] != spaces["space_10"] and spaces["space_9"] != spaces["space_13"]) and (spaces["space_10"] != spaces["space_11"] and spaces["space_10"] != spaces["space_14"]) and (spaces["space_11"] != spaces["space_12"] and spaces["space_11"] != spaces["space_15"]) and (spaces["space_12"] != spaces["space_16"]) and (spaces["space_13"] != spaces["space_14"]) and (spaces["space_14"] != spaces["space_15"]) and (spaces["space_15"] != spaces["space_16"])):
        game_lost = True; pygame.time.wait(2000)
        OVERLAY.fill(DARK if dark_mode else WHITE); OVERLAY.set_alpha(0)
        for alpha in range(26):
            OVERLAY.set_alpha(alpha); WINDOW.blit(OVERLAY, (0, 0))
            pygame.time.wait(1); pygame.display.update()
        SNAPSHOT = WINDOW.copy(); pygame.time.wait(500); TEMP_text_surface = FONT_SIZE_2.render("you jammed the board!", WHITE if dark_mode else BLACK)[0]
        for TEMP_y in range(int(-TEMP_text_surface.get_height()), int(WINDOW_HEIGHT / 2) - int(TEMP_text_surface.get_height() / 2)): WINDOW.blit(SNAPSHOT); WINDOW.blit(TEMP_text_surface, ((WINDOW_WIDTH / 2) - (TEMP_text_surface.get_width() / 2), TEMP_y)); pygame.display.update()
        pygame.time.wait(2000)
        for TEMP_y in range(int(WINDOW_HEIGHT / 2) - int(TEMP_text_surface.get_height() / 2), WINDOW_HEIGHT): WINDOW.blit(SNAPSHOT); WINDOW.blit(TEMP_text_surface, ((WINDOW_WIDTH / 2) - (TEMP_text_surface.get_width() / 2), TEMP_y)); pygame.display.update()
        for TEMP_y in range(int(-OPTIONS_WIDTH * 2), int(WINDOW_HEIGHT / 2) - int(OPTIONS_WIDTH)): WINDOW.blit(SNAPSHOT); WINDOW.blit(IMAGE_BUTTONS_RESET if dark_mode else image_shaders(IMAGE_BUTTONS_RESET, BLACK), ((WINDOW_WIDTH / 2) - OPTIONS_WIDTH, TEMP_y)); pygame.display.update()
        TEMP_waiting = True
        while TEMP_waiting:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (WINDOW_WIDTH / 2) - OPTIONS_WIDTH <= mouse_x <= (WINDOW_WIDTH / 2) + OPTIONS_WIDTH and (WINDOW_HEIGHT / 2) - OPTIONS_WIDTH <= mouse_y <= (WINDOW_HEIGHT / 2) + OPTIONS_WIDTH and game_lost: waiting = False
                pressed_key = pygame.key.get_pressed()
                if pressed_key[pygame.K_r]: waiting = False
        WINDOW.blit(IMAGE_BUTTONS_CHECKED, ((WINDOW_WIDTH / 2) - (OPTIONS_WIDTH / 2), (WINDOW_HEIGHT / 2) - (OPTIONS_WIDTH / 2))); pygame.display.update(); pygame.time.wait(500)
        for TEMP_y in range(int(WINDOW_HEIGHT / 2) - int(OPTIONS_WIDTH), WINDOW_HEIGHT): WINDOW.blit(SNAPSHOT); WINDOW.blit(IMAGE_BUTTONS_RESET if dark_mode else image_shaders(IMAGE_BUTTONS_RESET, BLACK), ((WINDOW_WIDTH / 2) - OPTIONS_WIDTH, TEMP_y)); WINDOW.blit(IMAGE_BUTTONS_CHECKED, ((WINDOW_WIDTH / 2) - (OPTIONS_WIDTH / 2), TEMP_y + (OPTIONS_WIDTH / 2))); pygame.display.update()
        pygame.time.wait(500)
        for alpha in range(25, -1, -1):
            OVERLAY.set_alpha(alpha); WINDOW.blit(OVERLAY, (0, 0))
            pygame.time.wait(10); pygame.display.update()
        spaces = {"space_1": 0, "space_2": 0, "space_3": 0, "space_4": 0, "space_5": 0, "space_6": 0, "space_7": 0, "space_8": 0, "space_9": 0, "space_10": 0, "space_11": 0, "space_12": 0, "space_13": 0, "space_14": 0, "space_15": 0, "space_16": 0}; score = 0; game_lost = False
    pygame.display.update()

dark_mode = False; key_pressed = False; game_won = [False, 0]; game_lost = False; game_running = True; spaces[f"space_{random.randint(1, 16)}"] = random.choice((2, 4)); main()
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SLASH or event.key == pygame.K_h: key_pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if CLOSE_X <= mouse_x <= CLOSE_X + OPTIONS_WIDTH and MARGIN <= mouse_y <= MARGIN + OPTIONS_WIDTH: game_running = False
            if MARGIN <= mouse_x <= MARGIN + OPTIONS_WIDTH and MARGIN <= mouse_y <= MARGIN + OPTIONS_WIDTH: dark_mode = False if dark_mode else True; COLOUR_0 = DARK if dark_mode else WHITE; COLOUR_2048 = COLOUR_0; main()
            if MARGIN <= mouse_x <= MARGIN + OPTIONS_WIDTH and MARGIN + OPTIONS_WIDTH + MARGIN <= mouse_y <= MARGIN + (OPTIONS_WIDTH * 2) + MARGIN: os.startfile("Assets\\Help.txt") if hasattr(os, "startfile") else os.system("open Assets/Help.txt 2>/dev/null || xdg-open Assets/Help.txt 2>/dev/null")
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_ESCAPE]: game_running = False
    if (pressed_key[pygame.K_SLASH] or pressed_key[pygame.K_h]) and not key_pressed: key_pressed = True; os.startfile("Assets\\Help.txt") if hasattr(os, "startfile") else os.system("open Assets/Help.txt 2>/dev/null || xdg-open Assets/Help.txt 2>/dev/null")
    if pressed_key[pygame.K_MINUS] and not dark_mode: dark_mode = True; COLOUR_0 = DARK; COLOUR_2048 = COLOUR_0; main()
    if pressed_key[pygame.K_EQUALS] and dark_mode: dark_mode = False; COLOUR_0 = WHITE; COLOUR_2048 = COLOUR_0; main()
    if pressed_key[pygame.K_r]: spaces = {"space_1": 0, "space_2": 0, "space_3": 0, "space_4": 0, "space_5": 0, "space_6": 0, "space_7": 0, "space_8": 0, "space_9": 0, "space_10": 0, "space_11": 0, "space_12": 0, "space_13": 0, "space_14": 0, "space_15": 0, "space_16": 0}; score = 0; game_lost = False; main()
    if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
        for pressed_key in range(0, 5): main("U"); pygame.time.wait(20)
        pressed_key = pygame.key.get_pressed(); space = random.randint(16, 16)
        if spaces[f"space_{space}"] == 0: spaces[f"space_{space}"] = random.choice((2, 4))
    if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
        for pressed_key in range(0, 5): main("L"); pygame.time.wait(20)
        pressed_key = pygame.key.get_pressed(); space = random.randint(1, 16)
        if spaces[f"space_{space}"] == 0: spaces[f"space_{space}"] = random.choice((2, 4))
    if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
        for pressed_key in range(0, 5): main("D"); pygame.time.wait(20)
        pressed_key = pygame.key.get_pressed(); space = random.randint(1, 16)
        if spaces[f"space_{space}"] == 0: spaces[f"space_{space}"] = random.choice((2, 4))
    if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
        for pressed_key in range(0, 5): main("R"); pygame.time.wait(20)
        pressed_key = pygame.key.get_pressed(); space = random.randint(1, 16)
        if spaces[f"space_{space}"] == 0: spaces[f"space_{space}"] = random.choice((2, 4))
pygame.quit()