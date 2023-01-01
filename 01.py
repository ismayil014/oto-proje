import pygame as pg
import sys
pg.init()
clock = pg.time.Clock()

en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255

ekran = pg.display.set_mode( (en,boy)  )

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(siyah)
    pg.draw.circle(ekran,beyaz,( en//2 , boy //2  ),20)
    pg.display.flip()
    clock.tick(30)
    def draw_score(current_score, high_score):

    # Create a font object using the font name and size
    font  = pygame.font.SysFont(font_name, font_size)

    # Render the current score as text
    score_text = font.render(f'Score: {current_score}', True, text_color)

    # Get the rectangular bounding box of the text surface
    score_rect = score_text.get_rect()

    # Set the position of the text at the top-right of the screen
    score_rect.right = window_width - 20
    score_rect.top = 20

    # Draw the text on the screen
    screen.blit(score_text, score_rect)

    # Render the high score as text
    high_score_text = font.render(f'High Score: {high_score}', True, text_color)

    # Get the rectangular bounding box of the text surface
    high_score_rect = high_score_text.get_rect()

    # Set the position of the text at the top-left of the screen
    high_score_rect.left = 20
    high_score_rect.top = 20

    # Draw the text on the screen
    screen.blit(high_score_text, high_score_rect)
