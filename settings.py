import pygame as pg

vec = pg.math.Vector2
COLORS = ['red', 'blue', 'orange', 'green', 'white']

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24, 89, 117)
ANIMATION_TIME_INTERVAL = 150 # in miliseconds
FAST_ANIMATION_TIME_INTERVAL = 15

FONT_PATH = 'assets/font/Brick_Tetris.ttf'

TILE_SIZE = 30
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RES = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_WIDTH, WIN_HEIGHT = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

MOVE_DIRECTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}
INIT_POS_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_WIDTH * 1.3, FIELD_HEIGHT * 0.45)
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
