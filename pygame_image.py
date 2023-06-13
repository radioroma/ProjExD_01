import sys
import pygame as pg
bg_x =0
kk_x =0
kk_y=0
def main():
    global bg_x,kk_x,kk_y
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img =pg.image.load("ex01/fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)
    kt_img=pg.transform.rotozoom(kk_img,10,1.0)
    kk_imgs=[ pg.transform.flip(pg.image.load("ex01/fig/3.png"),True,False),
        pg.transform.rotozoom(kk_img,10,1.0)
    ]
    tmr = 0
    tmr2 =0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if 0-bg_x ==1400:
                bg_x = 0
        bg_x = (bg_x+4)%1600

        screen.blit(bg_img, [0-bg_x, 0])
        screen.blit(kk_imgs[tmr%2],[300,+200])
        # bg_x = (bg_x+4)%1600
        #screen.blit(bg_img, [bg_x-1600, 0])
        pg.display.update()
        tmr += 1        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()