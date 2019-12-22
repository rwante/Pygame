import pygame
import random

blue = (213,235,255)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
lacivert = (0,66,123)
Platform_Sol = (500,500,500,500)
class karakter(pygame.sprite.Sprite):
    def __init__(self,konum_x,konum_y,hız):
        pygame.sprite.Sprite.__init__(self)
        self.karakter_resimS = pygame.Surface((10, 600)).convert()
        self.karakter_resim_sag = pygame.image.load("karakter_sol.png").convert_alpha()
        self.karakter_resim_dur = pygame.image.load("karakter_dur.png").convert_alpha()
        self.karakter_resim_dur1 = pygame.image.load("karakter_dur1.png").convert_alpha()
        self.karakter_resim_sol = pygame.image.load("karakter_sağ.png").convert_alpha()
        self.karakter_resim_sag1 = pygame.image.load("karakter_sağ1.png").convert_alpha()
        self.karakter_resim_sol1 = pygame.image.load("karakter_sol1.png").convert_alpha()
        self.karakter_resim_zıpla = pygame.image.load("karakter_zıpla.png").convert_alpha()
        self.karakter_resim_zıpla1 = pygame.image.load("karakter_zıpla1.png").convert_alpha()
        self.rect = self.karakter_resimS.get_rect()
        self.rect.x = konum_x
        self.rect.y = konum_y
        self.x_hız = hız
        self.y_hız = hız
    def koordinatlar(self,x,y):
        return pygame.Rect(self.rect.x,self.rect.y,x,y)


class kasirga(pygame.sprite.Sprite):
    def __init__(self,x_kasırga,y_kasırga,hız_kasırga):
        pygame.sprite.Sprite.__init__(self)
        self.kasırga_hızx = hız_kasırga
        self.kasırga_hızy = hız_kasırga
        self.kasırga_resim = pygame.Surface((50, 50)).convert()
        self.kasırga_resim = pygame.image.load("kasırga.png")
        self.kasırga_resim.set_colorkey(black)
        self.rect = self.kasırga_resim.get_rect()
        self.rect.x = x_kasırga
        self.rect.y = y_kasırga
    def koordinatlar(self,x,y):
        return pygame.Rect(self.rect.x,self.rect.y,x,y)

class blocks():
    def __init__(self,konum_x,konum_y):
        self.platform_sol = pygame.image.load("Platform_sol.jpg")
        self.platform_orta = pygame.image.load("Platform_orta.jpg")
        self.platform_sag = pygame.image.load("Platform_sag.jpg")
        self.merdiven = pygame.image.load("merdiven.png")
        self.hareketli = pygame.image.load("hareketli.jpg").convert_alpha()
        #self.hareketliS = pygame.Surface((32,32)).convert_alpha()
        self.rect = self.hareketli.get_rect()
        self.rect.x = konum_x
        self.rect.y = konum_y


class arka_plan():
    def __init__(self):
        self.arka_plan = pygame.image.load("arka_plan.jpg")
        self.arka_plan_agac = pygame.image.load("arka_plan_agac1.png").convert_alpha()
        self.arka_plan_cim = pygame.image.load("cim1.png")
        self.arka_plan_tas = pygame.image.load("tas.png")
        self.arka_plan_cicek = pygame.image.load("cicek.png")
        self.arka_plan_tahta = pygame.image.load("tahta.png")
        self.arka_plan_sandik = pygame.image.load("sandik.png")
    def level_0(self,text,text2):
        pygame.draw.rect(screen,red,[450,300,500,100],0)
        screen.blit(text,[600,320])
        pygame.draw.rect(screen,black,[450,500,500,100],0)
        screen.blit(text2,[600,520])

    def level_1(self):
        screen.blit(arkaplan.arka_plan_agac, [32, 544])
        screen.blit(arkaplan.arka_plan_cim, [150, 654])
        screen.blit(arkaplan.arka_plan_cim, [200, 654])
        screen.blit(arkaplan.arka_plan_cim, [430, 654])
        screen.blit(arkaplan.arka_plan_tas, [614, 584])
        screen.blit(arkaplan.arka_plan_cicek, [590, 584])
        screen.blit(arkaplan.arka_plan_tahta, [548, 584])
        screen.blit(arkaplan.arka_plan_tahta, [670, 584])
        screen.blit(arkaplan.arka_plan_cim,[740,585])
        screen.blit(arkaplan.arka_plan_agac,[920,406])
        screen.blit(arkaplan.arka_plan_tas,[990,515])
        screen.blit(arkaplan.arka_plan_cicek,[1185,515])
        screen.blit(arkaplan.arka_plan_cim,[1150,305])
        screen.blit(arkaplan.arka_plan_tas,[940,265])
        screen.blit(arkaplan.arka_plan_tas,[925,265])
        screen.blit(arkaplan.arka_plan_cicek,[655,225])
        screen.blit(arkaplan.arka_plan_cim,[400,185])
        screen.blit(arkaplan.arka_plan_agac,[85,80])
        screen.blit(arkaplan.arka_plan_sandik,[0,172])
        screen.blit(blocklar.platform_sol, [0, 668])
        screen.blit(blocklar.platform_orta, [32, 668])
        screen.blit(blocklar.platform_orta, [64, 668])
        screen.blit(blocklar.platform_orta, [96, 668])
        screen.blit(blocklar.platform_orta, [128, 668])
        screen.blit(blocklar.platform_orta, [160, 668])
        screen.blit(blocklar.platform_orta, [192, 668])
        screen.blit(blocklar.platform_sag, [224, 668])
        screen.blit(blocklar.merdiven, [234, 652])
        screen.blit(blocklar.platform_sol, [405, 668])
        screen.blit(blocklar.platform_orta, [437, 668])
        screen.blit(blocklar.platform_sag, [469, 668])
        screen.blit(blocklar.platform_sol, [550, 600])
        screen.blit(blocklar.platform_orta, [582, 600])
        screen.blit(blocklar.platform_orta, [614, 600])
        screen.blit(blocklar.platform_sag, [646, 600])
        screen.blit(blocklar.platform_sol,[730,600])
        screen.blit(blocklar.platform_orta,[762,600])
        screen.blit(blocklar.platform_sag,[794,600])
        screen.blit(blocklar.platform_sol,[900,530])
        screen.blit(blocklar.platform_orta,[932,530])
        screen.blit(blocklar.platform_orta,[964,530])
        screen.blit(blocklar.platform_orta,[996,530])
        screen.blit(blocklar.platform_orta,[1028,530])
        screen.blit(blocklar.platform_sag,[1060,530])
        screen.blit(blocklar.platform_orta,[1180,530])
        screen.blit(blocklar.platform_sol,[1300,420])
        screen.blit(blocklar.platform_orta,[1332,420])
        screen.blit(blocklar.platform_sag,[1190,320])
        screen.blit(blocklar.platform_orta,[1158,320])
        screen.blit(blocklar.platform_orta,[1126,320])
        screen.blit(blocklar.platform_sol,[1094,320])
        screen.blit(blocklar.platform_sag,[968,280])
        screen.blit(blocklar.platform_orta,[936,280])
        screen.blit(blocklar.platform_sol,[904,280])
        screen.blit(blocklar.platform_orta,[800,240])
        screen.blit(blocklar.platform_orta,[650,240])
        screen.blit(blocklar.platform_orta,[520,240])
        screen.blit(blocklar.platform_sag,[420,200])
        screen.blit(blocklar.platform_orta,[388,200])
        screen.blit(blocklar.platform_sol,[356,200])
        screen.blit(blocklar.merdiven,[185,184])
        screen.blit(blocklar.platform_sag,[175,200])
        screen.blit(blocklar.platform_orta,[143,200])
        screen.blit(blocklar.platform_orta,[111,200])
        screen.blit(blocklar.platform_orta,[79,200])
        screen.blit(blocklar.platform_orta,[47,200])
        screen.blit(blocklar.platform_orta,[15,200])
        screen.blit(blocklar.platform_sol,[0,200])
    def level_2(self):
        screen.blit(arkaplan.arka_plan_cim,[1310,654])
        screen.blit(arkaplan.arka_plan_cicek,[1280,654])
        screen.blit(arkaplan.arka_plan_agac,[540,544])
        screen.blit(arkaplan.arka_plan_tas,[370,565])
        screen.blit(arkaplan.arka_plan_tas,[380,565])
        screen.blit(arkaplan.arka_plan_cicek,[205,465])
        screen.blit(arkaplan.arka_plan_cim,[35,465])
        screen.blit(arkaplan.arka_plan_tas,[5,345])
        screen.blit(arkaplan.arka_plan_cim,[90,285])
        screen.blit(arkaplan.arka_plan_cim,[130,285])
        screen.blit(arkaplan.arka_plan_agac,[435,180])
        screen.blit(arkaplan.arka_plan_tas,[500,285])
        screen.blit(arkaplan.arka_plan_cim,[650,185])
        screen.blit(arkaplan.arka_plan_cim,[690,185])
        screen.blit(arkaplan.arka_plan_cicek,[1005,185])
        screen.blit(arkaplan.arka_plan_sandik,[1300,172])
        screen.blit(blocklar.platform_orta,[1300,668])
        screen.blit(blocklar.platform_orta,[1332,668])
        screen.blit(blocklar.platform_sag,[1364,668])
        screen.blit(blocklar.platform_sol,[1268,668])
        screen.blit(blocklar.platform_sag,[600,668])
        screen.blit(blocklar.platform_orta,[568,668])
        screen.blit(blocklar.platform_sol,[536,668])
        screen.blit(blocklar.platform_sag,[400,580])
        screen.blit(blocklar.platform_orta,[368,580])
        screen.blit(blocklar.platform_sol,[336,580])
        screen.blit(blocklar.platform_orta,[200,480])
        screen.blit(blocklar.platform_sag,[70,480])
        screen.blit(blocklar.platform_orta,[38,480])
        screen.blit(blocklar.platform_orta,[6,480])
        screen.blit(blocklar.platform_sol,[0,480])
        screen.blit(blocklar.platform_sol,[0,360])
        screen.blit(blocklar.platform_sol,[80,300])
        screen.blit(blocklar.platform_orta,[112,300])
        screen.blit(blocklar.platform_orta,[144,300])
        screen.blit(blocklar.platform_sag,[176,300])
        screen.blit(blocklar.platform_sol,[300,300])
        screen.blit(blocklar.merdiven,[310,284])
        screen.blit(blocklar.platform_sol,[481,300])
        screen.blit(blocklar.platform_orta,[513,300])
        screen.blit(blocklar.platform_sag,[545,300])
        screen.blit(blocklar.platform_sol,[645,200])
        screen.blit(blocklar.platform_orta,[677,200])
        screen.blit(blocklar.platform_sag,[709,200])
        screen.blit(blocklar.platform_orta,[859,200])
        screen.blit(blocklar.platform_orta,[999,200])
        screen.blit(blocklar.platform_sol,[1131,200])
        screen.blit(blocklar.platform_sag,[1163,200])
        screen.blit(blocklar.platform_sol,[1286,200])
        screen.blit(blocklar.platform_orta,[1318,200])
        screen.blit(blocklar.platform_orta,[1350,200])
        screen.blit(blocklar.platform_sag,[1380,200])
    def level_3(self):
        screen.blit(arkaplan.arka_plan_agac,[112,544])
        screen.blit(arkaplan.arka_plan_agac,[373,544])
        screen.blit(arkaplan.arka_plan_agac,[549,544])
        screen.blit(arkaplan.arka_plan_agac,[810,544])
        screen.blit(arkaplan.arka_plan_agac,[922,544])
        screen.blit(arkaplan.arka_plan_agac,[1183,544])
        screen.blit(arkaplan.arka_plan_cim,[270,535])
        screen.blit(arkaplan.arka_plan_cim,[310,535])
        screen.blit(arkaplan.arka_plan_cim,[650,535])
        screen.blit(arkaplan.arka_plan_cim,[680,535])
        screen.blit(arkaplan.arka_plan_cim,[1020,535])
        screen.blit(arkaplan.arka_plan_cim,[1050,535])
        screen.blit(arkaplan.arka_plan_tas,[115,417])
        screen.blit(arkaplan.arka_plan_tas,[130,417])
        screen.blit(arkaplan.arka_plan_tas,[1215,417])
        screen.blit(arkaplan.arka_plan_tas,[1230,417])
        screen.blit(arkaplan.arka_plan_cicek,[685,299])
        screen.blit(arkaplan.arka_plan_sandik,[657,122])
        screen.blit(blocklar.platform_sol,[0,668])
        screen.blit(blocklar.platform_orta,[32,668])
        screen.blit(blocklar.platform_orta,[64,668])
        screen.blit(blocklar.platform_orta, [96, 668])
        screen.blit(blocklar.platform_orta, [128, 668])
        screen.blit(blocklar.platform_orta, [160, 668])
        screen.blit(blocklar.platform_sag,[192,668])
        screen.blit(blocklar.merdiven,[202,652])
        screen.blit(blocklar.platform_sol,[373,668])
        screen.blit(blocklar.platform_orta,[405,668])
        screen.blit(blocklar.platform_orta,[437,668])
        screen.blit(blocklar.platform_orta,[469,668])
        screen.blit(blocklar.platform_orta,[501,668])
        screen.blit(blocklar.platform_orta,[533,668])
        screen.blit(blocklar.platform_orta,[565,668])
        screen.blit(blocklar.platform_orta,[597,668])
        screen.blit(blocklar.platform_sag,[629,668])
        screen.blit(blocklar.merdiven,[639,652])
        screen.blit(blocklar.platform_sol,[810,668])
        screen.blit(blocklar.platform_orta,[842,668])
        screen.blit(blocklar.platform_orta,[874,668])
        screen.blit(blocklar.platform_orta,[906,668])
        screen.blit(blocklar.platform_orta,[938,668])
        screen.blit(blocklar.platform_orta,[970,668])
        screen.blit(blocklar.platform_sag,[1002,668])
        screen.blit(blocklar.merdiven,[1012,652])
        screen.blit(blocklar.platform_sol,[1183,668])
        screen.blit(blocklar.platform_orta,[1215,668])
        screen.blit(blocklar.platform_orta,[1247,668])
        screen.blit(blocklar.platform_orta,[1279,668])
        screen.blit(blocklar.platform_orta,[1311,668])
        screen.blit(blocklar.platform_orta,[1343,668])
        screen.blit(blocklar.platform_sag,[1375,668])
        screen.blit(blocklar.platform_sol,[273,550])
        screen.blit(blocklar.platform_orta,[305,550])
        screen.blit(blocklar.platform_sag,[337,550])
        screen.blit(blocklar.platform_sol,[642,550])
        screen.blit(blocklar.platform_orta,[674,550])
        screen.blit(blocklar.platform_sag,[706,550])
        screen.blit(blocklar.platform_sol,[1011,550])
        screen.blit(blocklar.platform_orta,[1043,550])
        screen.blit(blocklar.platform_sag,[1075,550])
        screen.blit(blocklar.platform_sol,[104,432])
        screen.blit(blocklar.platform_sag,[136,432])
        screen.blit(blocklar.platform_sol,[472,432])
        screen.blit(blocklar.platform_sag,[504,432])
        screen.blit(blocklar.platform_sol,[840,432])
        screen.blit(blocklar.platform_sag,[872,432])
        screen.blit(blocklar.platform_sol,[1208,432])
        screen.blit(blocklar.platform_sag,[1240,432])
        screen.blit(blocklar.platform_orta, [305, 314])
        screen.blit(blocklar.platform_orta, [674, 314])
        screen.blit(blocklar.platform_orta, [1043, 314])
        screen.blit(blocklar.platform_sol,[467,196])
        screen.blit(blocklar.platform_sag,[499,196])
        screen.blit(blocklar.platform_sol,[826,196])
        screen.blit(blocklar.platform_sag,[858,196])
        screen.blit(blocklar.platform_orta,[660,150])
    def level_4(self,textt,text2):
        screen.blit(textt,[300,200])
        pygame.draw.rect(screen, black, [450, 500, 500, 100], 0)
        screen.blit(text2, [600, 520])

def level_1():
    level1 = [[0,668],[32,668],[64,668],[96,668],[128,668],[160,668],[192,668],[224,668],[234,668],[266,668],[298,668],[330,668],[362,668],[405,668],
              [437,668],[469,668],[550,600],[582,600],[614,600],[646,600],[730,600],[762,600],[794,600],[900,530],[932,530],[964,530],[996,530],
              [1028,530],[1060,530],[1180,530],[1300,420],[1190,320],[1158,320],[1126,320],[1094,320],[968,280],[936,280],[904,280],[800,240],[650,240],
              [520,240],[420,200],[388,200],[356,200],[324,200],[292,200],[260,200],[228,200],[196,200],[185,200],[175,200],[143,200],[111,200],
              [79,200],[47,200],[15,200],[0,200]]
    return level1
def level_2():
    level2 = [[1300,668],[1268,668],[600,668],[568,668],[536,668],[400,580],[368,580],[336,580],[200,480],[70,480],[38,480],[6,480],[0,360],[80,300],
              [112,300],[144,300],[176,300],[300,300],[310,300],[342,300],[374,300],[406,300],[438,300],[470,300],[481,300],[513,300],[545,300],
              [645,200],[677,200],[709,200],[859,200],[999,200],[1131,200],[1163,200],[1286,200],[1318,200],[1350,200],[1380,200]]
    return level2
def level_3():
    level3 = [[273,550],[305,550],[337,550],[642,550],[674,550],[706,550],[1011,550],[1043,550],[1075,550],[104,432],[136,432],[472,432],[504,432],
              [840,432],[872,432],[1208,432],[1240,432],[305,314],[674,314],[1043,314],[467,196],[499,196],[826,196],[858,196],[660,150]]
    for i in range(0,1380,32):
        level3.append([i,668])
    return level3


pygame.init()
size=[1380,700]
pygame.display.set_caption("Platform Game")
screen=pygame.display.set_mode(size)
font = pygame.font.Font(None,100)
text = font.render("OYNA",True,black)
text2 = font.render("ÇIKIŞ",True,white)
textt = font.render("Oyunu Bitirdiniz Tebrikler",True,black)
snow_list = []
toplam = 0
sayac_sol = 0
sayac_sağ = 0
sayac_üst = 0
tavsan = karakter(10,600,0)
fırtına = kasirga(50,50,5)
blocklar = blocks(1236,668)
arkaplan = arka_plan()
dur_deg = 0
zıplama_deg = 2
level1 = level_1()
level2 = level_2()
level3 = level_3()
level2.append([blocklar.rect.x,blocklar.rect.y])
seviye = 0
hareketli_hız = 5
level_carpisma = []
pygame.mixer.music.load("sess.mp3")
pygame.mixer.music.play(-1)

for j in range(100):
    x = random.randrange(0, 1380)
    y = random.randrange(0, 700)
    snow_list.append([x, y])

sonuc = True
zaman = pygame.time.Clock()

while sonuc:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or seviye == 5:
            sonuc = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            tavsan.x_hız = -5
            tavsan.y_hız = 5
            sayac_sol += 1
            sayac_sağ = 0
            zıplama_deg = 1
            dur_deg = 1
        if event.key == pygame.K_RIGHT:
            tavsan.x_hız = 5
            tavsan.y_hız = 5
            sayac_sağ += 1
            sayac_sol = 0
            zıplama_deg = 0
            dur_deg = 0
        if event.key == pygame.K_UP:
            if toplam < 11:
                tavsan.y_hız = -10
                toplam += 1
            else:
                tavsan.y_hız = 5
            sayac_üst += 1
            sayac_sağ = 0
            sayac_sol = 0
        if event.key == pygame.K_DOWN:
            tavsan.y_hız = 5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            tavsan.x_hız = 0
            tavsan.y_hız = 5
            sayac_sol = 0
        if event.key == pygame.K_RIGHT:
            tavsan.x_hız = 0
            tavsan.y_hız = 5
            sayac_sağ = 0
        if event.key == pygame.K_UP:
            tavsan.y_hız = 50
            toplam = 0
            sayac_üst = 0
            if zıplama_deg == 1:
                sayac_sol += 1
            elif zıplama_deg == 0:
                sayac_sağ += 1
        if event.key == pygame.K_DOWN:
            tavsan.y_hız = 5

    tavsan.rect.x = tavsan.rect.x + tavsan.x_hız
    tavsan.rect.y = tavsan.rect.y + tavsan.y_hız
    if tavsan.rect.x > 1300:
        tavsan.rect.x = 1300
    if tavsan.rect.x < 0:
        tavsan.rect.x = 0
    if tavsan.rect.y > 700:
        if seviye == 1:
            tavsan.rect.x = 10
            tavsan.rect.y = 600
        elif seviye == 2:
            tavsan.rect.x = 1300
            tavsan.rect.y = 600
        elif seviye == 3:
            tavsan.rect.x = 10
            tavsan.rect.y = 600
    if tavsan.rect.y < 0:
        tavsan.rect.y = 0

    carpisma = tavsan.koordinatlar(66,69).colliderect(fırtına.koordinatlar(100,100))
    if carpisma:
        if seviye == 1:
            tavsan.rect.x = 10
            tavsan.rect.y = 600
        elif seviye == 2:
            tavsan.rect.x = 1300
            tavsan.rect.y = 600
        elif seviye == 3:
            tavsan.rect.x = 10
            tavsan.rect.y = 600
    if seviye == 0:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pygame.rect.Rect(450,300,500,100).colliderect(pygame.rect.Rect(pos[0],pos[1],1,1)) and pressed1:
            seviye += 1
        elif pygame.rect.Rect(450,500,500,100).colliderect(pygame.rect.Rect(pos[0],pos[1],1,1)) and pressed1:
            seviye = 5
    elif seviye == 1:
        level_carpisma = level1
    elif seviye == 2:
        level2[-1] = [blocklar.rect.x,blocklar.rect.y]
        level_carpisma = level2
    elif seviye == 3:
        level_carpisma = level3
    elif seviye == 4:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if pygame.rect.Rect(450,500,500,100).colliderect(pygame.rect.Rect(pos[0],pos[1],1,1)) and pressed1:
            seviye = 5
    for i in level_carpisma:
        block_carpisma = tavsan.koordinatlar(32,66).colliderect(pygame.Rect(i[0],i[1],32,0))
        if block_carpisma:
            if tavsan.rect.y < i[1]:
                tavsan.rect.y = i[1]-66
                break
    if seviye == 1:
        level_atlama = tavsan.koordinatlar(32,66).colliderect(pygame.Rect(0,172,38,28))
        if level_atlama:
            seviye += 1
            tavsan.rect.x = 1300
            tavsan.rect.y = 600
    elif seviye == 2:
        level_atlama2 = tavsan.koordinatlar(32,66).colliderect(pygame.Rect(1300,172,38,28))
        if level_atlama2:
            seviye += 1
            tavsan.rect.x = 10
            tavsan.rect.y = 600
    elif seviye == 3:
        level_atlama3 = tavsan.koordinatlar(32,66).colliderect(pygame.Rect(657,122,38,28))
        if level_atlama3:
            seviye += 1
    screen.blit(arkaplan.arka_plan, [0, 0])
    if seviye == 0:
        arkaplan.level_0(text,text2)
    elif seviye == 1:
        arkaplan.level_1()
    elif seviye == 2:
        arkaplan.level_2()
        if blocklar.rect.x > 1236 or blocklar.rect.x < 632:
            hareketli_hız *= -1
        blocklar.rect.x += hareketli_hız
        screen.blit(blocklar.hareketli,[blocklar.rect.x,blocklar.rect.y])
    elif seviye == 3:
        arkaplan.level_3()
    elif seviye == 4:
        arkaplan.level_4(textt,text2)
    if seviye != 0 and seviye != 4 and seviye != 5:
        if sayac_sol != 0:
            if sayac_sol % 2:
                screen.blit(tavsan.karakter_resim_sag1,[tavsan.rect.x,tavsan.rect.y])
            else:
                screen.blit(tavsan.karakter_resim_sol1,[tavsan.rect.x,tavsan.rect.y])
        elif sayac_sağ != 0:
            if sayac_sağ % 2:
                screen.blit(tavsan.karakter_resim_sag,[tavsan.rect.x,tavsan.rect.y])
            else:
                screen.blit(tavsan.karakter_resim_sol,[tavsan.rect.x,tavsan.rect.y])
        elif sayac_üst != 0:
            if zıplama_deg == 1:
                screen.blit(tavsan.karakter_resim_zıpla1,[tavsan.rect.x,tavsan.rect.y])
            else:
                screen.blit(tavsan.karakter_resim_zıpla,[tavsan.rect.x,tavsan.rect.y])
        else:
            if dur_deg == 1:
                screen.blit(tavsan.karakter_resim_dur1,[tavsan.rect.x,tavsan.rect.y])
            else:
                screen.blit(tavsan.karakter_resim_dur,[tavsan.rect.x,tavsan.rect.y])

        screen.blit(fırtına.kasırga_resim,[fırtına.rect.x,fırtına.rect.y])

        fırtına.rect.x += fırtına.kasırga_hızx
        fırtına.rect.y += fırtına.kasırga_hızy
        if fırtına.rect.x > 1330 or fırtına.rect.x < 0:
            fırtına.kasırga_hızx *= -1
        if fırtına.rect.y > 650 or fırtına.rect.y < 0:
            fırtına.kasırga_hızy *= -1


    for j in range(len(snow_list)):
        pygame.draw.circle(screen, lacivert, snow_list[j], 2)
        snow_list[j][1] += 1
        if snow_list[j][1] > 700:
            y = random.randrange(-50, -10)
            snow_list[j][1] = y
            x = random.randrange(0, 1380)
            snow_list[j][0] = x


    pygame.display.flip()
    zaman.tick(60)
pygame.quit ()
