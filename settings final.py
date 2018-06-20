from os import path
import pygame as pg
vec = pg.math.Vector2

#sprites do jogador e zumbis retirados do Kenney
#sons obtidos pelo Github de=o canal Kids Can Code, em:https://github.com/kidscancode/pygame_tutorials/tree/master/tilemap/part%2001




# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
CYAN = (0, 255, 255)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Ele ta loko, ele ta crazy"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 280
PLAYER_HEALTH = 100
PLAYER_ROT_SPEED = 200.0
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
PLAYER_IMG = 'hitman1_gun.png'
BARREL_OFFSET = vec(30, 10)
#Muro
WALL_IMG = 'tileGreen_39.png'

#status zumbis

MOB_IMG = 'zoimbie1_hold.png'
MOB_SPEEDS = [150, 100, 75, 125]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 10000000

# Status da arma
BULLET_IMG = 'bullet.png'
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10


#efeitos

MUZZLE_FLASHES = ['whitePuff15.png', 'whitePuff16.png', 'whitePuff17.png',
                  'whitePuff18.png']
FLASH_DURATION = 50
SPLAT = 'splat green.png'
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
MONSTRO_LAYER = 2
CRIATURA_LAYER=2
ESQUELETO_LAYER=2

EFFECTS_LAYER = 4   
ITEMS_LAYER = 1
# Itens
ITEM_IMAGES = {'vida': 'health_pack.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.4

#atributos monstro
MONSTRO_IMG = 'monstro.png' #retirado de: http://defenderoftexel.wikia.com/wiki/File:Typhon_Monster-Sire_Sprite.png
MONSTRO_SPEED = 75
MONSTRO_HIT_RECT = pg.Rect(0, 0, 30, 30)
MONSTRO_HEALTH = 750
MONSTRO_DAMAGE = 40
MONSTRO_KNOCKBACK = 30
AVOID_RADIUS_MONSTRO = 10000
DETECT_RADIUS = 10000000
#atributos CRIATURA
CRIATURA_IMG = 'dragao.png'# retirado do Pinterest, em: https://i.pinimg.com/originals/66/72/d9/6672d911a5ba93ca478ccabf69374d2b.png
CRIATURA_SPEED = 100
CRIATURA_HIT_RECT = pg.Rect(0, 0, 30, 30)
CRIATURA_HEALTH = 450
CRIATURA_DAMAGE = 20
CRIATURA_KNOCKBACK = 30
AVOID_RADIUS_CRIATURA = 10000
DETECT_RADIUS = 10000000

#atributos esqueleto
ESQUELETO_IMG = 'esqueleto.png' #retirado de: https://br.pinterest.com/pin/554646510341864204/
ESQUELETO_SPEED = 120
ESQUELETO_HIT_RECT = pg.Rect(0, 0, 30, 30)
ESQUELETO_HEALTH = 300
ESQUELETO_DAMAGE = 15
ESQUELETO_KNOCKBACK = 15
AVOID_RADIUS_ESQUELETO = 10000
DETECT_RADIUS = 10000000


# Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/9.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-5.wav', 'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = ['shotgun.wav']
EFFECTS_SOUNDS = {'level_start': 'level_start.wav',
                  'health_up': 'health_pack.wav'}





