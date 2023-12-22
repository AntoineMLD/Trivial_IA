import pygame

# Board's dimensions and coordinates
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 600
WIDTH, HEIGHT = 600, 600
BOARD_RADIUS = 250
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

BOX_RADIUS = 18
RING_WIDTH = 4
RING_COLOR = (255, 0, 0)
BORDER_THICKNESS = 2

# Palette and color mapping
BACKGROUND = (29, 62, 71)
WHITE = (255, 255, 255)
BLUE = (68, 202, 219)
ORANGE = (253, 139, 80)
GREEN = (101, 183, 65)
YELLOW = (254, 232, 37)
PINK = (252, 111, 163)
BROWN = (190, 124, 67)
GREY = (176, 166, 149)
RED = (255, 0, 0)

# Points
BROWN_POINT = pygame.image.load('emojis/brown.png')
BLUE_POINT = pygame.image.load('emojis/blue.png')
ORANGE_POINT = pygame.image.load('emojis/orange.png')
YELLOW_POINT = pygame.image.load('emojis/yellow.png')
PINK_POINT = pygame.image.load('emojis/pink.png')
GREEN_POINT = pygame.image.load('emojis/green.png')



THEMES = ["Marché du travail", "SQL", "IA", "Commande Linux", "Git_Github", "Python"]

# Mappings
THEME_TO_POINT = {
    "Marché du travail": BROWN_POINT,
    "SQL": BLUE_POINT,
    "Actualité IA": ORANGE_POINT,
    "Commande Linux": YELLOW_POINT,
    "Git_Github": PINK_POINT,
    "Python": GREEN_POINT,
    
}

BOX_TYPE_TO_COLOR = {
    "*Spé": BROWN,
    "Spé": BROWN,
    "*SQL": BLUE,
    "SQL": BLUE,
    "*IA": ORANGE,
    "IA": ORANGE,
    "*Shell": YELLOW,
    "Shell": YELLOW,
    "*Git": PINK,
    "Git": PINK,
    "*Python": GREEN,
    "Python": GREEN,
    "Again": GREY
}

# Box type mapping
INDEX_TO_BOX_TYPE = {
	0: "*Spé",
	1: "Shell",
	2: "Again",
	3: "IA",
	4: "Python",
	5: "Again",
	6: "Git",
	7: "*SQL",
	8: "Git",
	9: "Again",
	10: "Shell",
	11: "Spé",
	12: "Again",
	13: "Python",
	14: "*IA",
	15: "Python",
	16: "Again",
	17: "Git",
	18: "SQL",
	19: "Again",
	20: "Spé",
	21: "*Shell",
	22: "Spé",
	23: "Again",
	24: "Python",
	25: "IA",
	26: "Again",
	27: "SQL",
	28: "*Git",
	29: "SQL",
	30: "Again",
	31: "Spé",
	32: "Shell",
	33: "Again",
	34: "IA",
	35: "*Python",
	36: "IA",
	37: "Again",
	38: "SQL",
	39: "Git",
	40: "Again",
	41: "Shell",
	42: "Shell",
	43: "Git",
	44: "IA",
	45: "SQL",
	46: "Python",
	47: "IA",
	48: "Git",
	49: "Python",
	50: "SQL",
	51: "Spé",
	52: "Git",
	53: "Python",
	54: "Shell",
	55: "IA",
	56: "Spé",
	57: "Shell",
	58: "Python",
	59: "Spé",
	60: "IA",
	61: "SQL",
	62: "Python",
	63: "Spé",
	64: "Git",
	65: "Shell",
	66: "SQL",
	67: "Git",
	68: "Spé",
	69: "SQL",
	70: "Shell",
	71: "IA",
	72: "Again"
}

# To translate board themes to db themes
TRANSLATE_THEMES = {
    "Spé": "Marché du travail",
    "IA": "Actualité IA",
    "Shell": "Commande Linux",
    "Git": "Git_Github",
    "SQL": "SQL",
    "Python": "Python"
    
}
