import pygame

print("Setup started...")
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Pygame Window")
print("Pygame initialized and window created.")


running = True
while running:  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  # Fill the window with black
    pygame.display.flip()  # Update the display 