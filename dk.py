import pygame

pygame.init()

# Set the window dimensions
window_width = 800
window_height = 600

# Set the background color
bg_color = (0, 0, 0)

# Set the font and font size for the score table
font_name = 'arial'
font_size = 32

# Set the text color for the score table
text_color = (255, 255, 255)

   
def draw_score(current_score, high_score):  
    # Create a font object using the font name and size
    font = pygame.font.SysFont(font_name, font_size)

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


while True:
    # Update the game state

    # Draw the score table
    draw_score (current_score, high_score)

    # Update the display
    pygame.display.update()
 