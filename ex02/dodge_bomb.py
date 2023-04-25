import random
import sys
import pygame as pg


delta = {
    pg.K_UP: (0, -1),
    pg.K_DOWN: (0, +1),
    pg.K_LEFT: (-1, 0),
    pg.K_RIGHT: (+1, 0),
}

def check_bound(scr_rct: pg.rect, obj_rct: pg.rect) -> tuple[bool, bool]:
    '''
オブジェクトが画面内をOR画面外を判断し真理値タプルを返す関数
引数１：画面SURAFACEのRECT
引数２：こうかとん、または、爆弾のSURAFACEのRECT
戻り値　横方向、縦方向のはみ出し判定結果（画面内、TRUE,画面外、FALSE）
'''
    yoko , tate = True, True
    if obj_rct.left <scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate
def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bb_img = pg.Surface((20, 20))
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)
    bb_img.set_colorkey((0, 0, 0)) #爆弾の四偶を透明にした
    x, y = random.randint(0, 1600), random.randint(0, 900)#ｘ、ｙを１６００，９００のランダム設定
    screen.blit(bb_img,[x, y])#練習２
    vx, vy = +1, +1
    bb_rct  =bb_img.get_rect()#RECTクラスに変更
    bb_rct.center = x, y# 初期位置をランダムに設定
    kk_rct = kk_img.get_rect()#rectクラスに変更
    kk_rct.center = 900, 400#初期位置を９００，４００に変更
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        key_lst = pg.key.get_pressed()
        for k, mv in delta.items():
            if key_lst[k]:
                kk_rct.move_ip(mv)
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx, vy)
        screen.blit(bb_img, bb_rct)
        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
   