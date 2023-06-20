import pygame
from random import randint


class Cell:
    def __init__(self):
        self.collapsed = False
        self.options = [0, 1, 2, 3, 4]


class Rules:
    def __init__(self, opt: int):
        match opt:
            case 0:
                opt = "blank"
            case 1:
                opt = "up"
            case 2:
                opt = "right"
            case 3:
                opt = "down"
            case 4:
                opt = "left"

        self.opts = dict(
            blank=[
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4]
            ],
            up=[
                [2, 3, 4],
                [1, 3, 4],
                [0, 3],
                [1, 2, 3]
            ],
            right=[
                [2, 3, 4],
                [1, 3, 4],
                [1, 2, 4],
                [0, 4]
            ],
            down=[
                [0, 1],
                [1, 3, 4],
                [1, 2, 4],
                [1, 2, 3]
            ],
            left=[
                [2, 3, 4],
                [0, 2],
                [1, 2, 4],
                [1, 2, 3]
            ]
        )

        self.res = self.opts[opt]


def check_valid(arr: list, valid: list):
    for j in range(len(arr)-1, -1, -1):
        if valid.count(arr[j]) < 1:
            arr.pop(j)


pygame.init()
clock = pygame.time.Clock()

screen_width = 1024
screen_height = 764
screen = pygame.display.set_mode((screen_width, screen_height))

# Grid
grid = []
dim = 16
cell_width = screen_width / dim
cell_height = screen_height / dim

# Tiles
tiles = [pygame.image.load("sprites/tile_0.png").convert_alpha(),
         pygame.image.load("sprites/tile_1.png").convert_alpha(),
         pygame.image.load("sprites/tile_2.png").convert_alpha(),
         pygame.image.load("sprites/tile_3.png").convert_alpha(),
         pygame.image.load("sprites/tile_4.png").convert_alpha()]

for i in range(dim * dim):
    grid += [Cell()]

while True:
    screen.fill((105, 105, 105))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            grid.clear()
            for i in range(dim * dim):
                grid += [Cell()]
        if event.type == pygame.KEYDOWN:
            pass
    grid_copy = grid.copy()
    grid_filtered = filter(lambda a: not a.collapsed, grid_copy)
    grid_copy = []
    for i in grid_filtered:
        grid_copy.append(i)

    grid_copy.sort(key=lambda a: len(a.options))
    if len(grid_copy) > 0:
        base_len = len(grid_copy[0].options)
        grid_filtered = filter(lambda a: len(a.options) <= base_len, grid_copy)
        grid_copy = []
        for i in grid_filtered:
            grid_copy.append(i)

        cell_pick = grid_copy[randint(0, max(len(grid_copy) - 1, 0))]
        cell_pick.collapsed = True
        pick = cell_pick.options[randint(0, max(len(cell_pick.options) - 1, 0))]
        cell_pick.options = [pick]

    new_tiles = []
    for y in range(dim):
        for x in range(dim):
            index = x + y * dim
            if grid[index].collapsed:
                new_tiles.insert(index, grid[index])
            else:
                my_options = [0, 1, 2, 3, 4]
                # Look up
                if y > 0:
                    valid_options = []
                    up = grid[x + (y - 1) * dim]
                    for option in up.options:
                        rules = Rules(option).res
                        valid = rules[2]
                        valid_options.extend(valid)
                    check_valid(my_options, valid_options)
                # Look right
                if x < dim - 1:
                    valid_options = []
                    right = grid[x + 1 + y * dim]
                    for option in right.options:
                        rules = Rules(option).res
                        valid = rules[3]
                        valid_options.extend(valid)
                    check_valid(my_options, valid_options)
                # Look down
                if y < dim - 1:
                    valid_options = []
                    down = grid[x + (y + 1) * dim]
                    for option in down.options:
                        rules = Rules(option).res
                        valid = rules[0]
                        valid_options.extend(valid)
                    check_valid(my_options, valid_options)
                # Look left
                if x > 0:
                    valid_options = []
                    left = grid[x - 1 + y * dim]
                    for option in left.options:
                        rules = Rules(option).res
                        valid = rules[1]
                        valid_options.extend(valid)

                    check_valid(my_options, valid_options)

                new_tiles += [Cell()]
                new_tiles[index].options = my_options
                new_tiles[index].collapsed = False

    grid = new_tiles

    for y in range(dim):
        for x in range(dim):
            cell = grid[y + x * dim]
            if cell.collapsed:
                index = cell.options[0]
                tile_scale = pygame.transform.scale(tiles[index], (cell_width, cell_height))
                screen.blit(tile_scale, (y * cell_width, x * cell_height))
            else:
                pygame.draw.rect(screen, "White", (y * cell_width, x * cell_height, 512, 382), 1)

    pygame.display.update()

pygame.quit()