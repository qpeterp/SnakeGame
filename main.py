import pygame
import random
import time

# ----- [저장된 질문 (라이브러리 질문)] --------------------------------------------------------------

qustionCs = {"지구에서 가장 큰 바다는?" : "태평양",       # 일반 상식
            "가장 작은 소수는?" : "2",
            "일반적으로 성인 한명이 가진 뼈 갯수는?" : "206",
            "아인슈타인의 출생지는?" : "독일",
            "지구에서 가장 가까운 행성은?" : "화성",
            "미국의 초대 대통령은?" : "조지워싱턴",
            "호주의 수도는?" : "캔버라",
            "육류와 해산물을 채썰어 볶은 후 녹말을 끼얹어 걸쭉하게 만든 요리는?" : "유산슬",
            "우리나라 광역시의 갯수는?" : "6",
            "대한민국 최남단에 있는 섬은?" : "마라도",
            '"골치아프다"의 골치는?' : "뇌",
            "미국 경제대공황을 극복한 인물은?" : "루즈벨트",
            "중국의 수도는?" : "베이징",
            "굼벵이는 어떤 곤충의 애벌레일까요?" : "매미",
            "물가가 지속적으로 올라가는 현상은?" : "인플레이션",
            '"00의 눈물"은 거짓 눈물을 뜻한다. 00은?' : "악어",
            "칠레의 수도는?" : "산티아고",
            "소말리아의 수도는?" : "모가디슈",
            "한국의 국가번호는 +82이다. 일본의 국가번호는?" : "81",
            "한국의 국가번호는 +82이다. 미국의 국가번호는?" : "1",
            "한국의 국가번호는 +82이다. 중국의 국가번호는?" : "86",
            "달이 뜨는 방향은?" : "동",
            '토사구팽의 "토"가 가르키는 동물은?' : "토끼",
            "6.25전쟁이 일어난 년도는?" : "1950",
            "임진왜란이 일어난 년도는?" : "1592",
            "세계에서 가장 오래된 목판 인쇄물은?" : "무구정광대다라니경",
            "가장 뛰어난 소프트웨어마이스터고는?" : "정",  # 정할 수 없죠. or 정할 수 없다.
            "물고기는 귀가 있다?" : "있다",
            "세종대왕님은 몇대 임금이신가요?" : "4",
            "세상에서 가장 낮은 위치의 호수는?" : "사해",
            "이 게임의 개발자는?" : "이성은",
            "세계에서 가장 큰 대륙은?" : "아시아",
            "세계에서 가장 높은 산은?" : "에베레스트"
            }
qustionNonsen = {"목수도 고칠 수 없는 집은?" : "고집",        # 넌센스
                "차도가 없는 나라는?" : "인도",
                "얼음이 죽으면?" : "다이빙",
                "가장 어렵게 지은 절은?" : "우여곡절",
                "쥐 4마리가 모이면?" : "쥐포",
                "절에 없는 스님은?": "부재중",
                "진짜 새의 이름은?" : "참새",
                "소가 처음 봤을 때 하는 말은?" : "반갑소",
                "왕에게 공을 던질 때 하는 말" : "송구",
                "개근하는 학생들이 가장 많은 대학은?" : "가야대",
                "세상에서 가장 짠 음식은?" : "짜요짜요",
                "도둑이 몰래 훔친 돈은?" : "슬그머니",
                "자가용의 반대말은?" : "커용",
                "콜라와 마요네즈를 섞으면 어떨까요?" : "버려",
                "날마다 흑심을 품고 사는 것은?" : "연필",
                "광부가 많은 나라는?" : "케냐",
                "홍진호가 두명이면?" : "콩진호"
                }
qustionKohis = {"주몽이 세운 나라의 이름은?" : "고구려",     # 한국사
                "우리나라 최초의 국가는?" : "고조선",
                "신라가 삼국통일의 위업을 달성했을때의 왕은?" : "문무왕",
                "이순신 장군님이 학익진 전법으로 크게 승리한 싸움은?" : "한산도대첩",
                "고구려 유민들이 요동지방을 중심으로 세운 나라는?" : "발해",
                "대우를 잘 받지못한 군인들의 불만이 폭발해 일어난 사건은?" : "임오군란",
                "신라를 세운 사람은?" : "박혁거세",
                "시인이며 '서시', '또 다른 고향', '별 헤는 밤' 등을 지은 사람은?" : "윤동주",
                "몽골의 침입을 막기 위한 염원으로 만든 것은?" : "팔만대장경",
                "한국 청동기 시대의 대표적인 무덤 양식은?" : "고인돌",
                "출신 신분에 따라 골과 품으로 등급을 나누는 신라의 신분제도는?" : "골품제",
                "신라 제27대 왕으로 진평왕의 뒤를 이은 신라 최초의 여왕은?" : "선덕",
                "세종대왕 때 만들어졌으며 비가 온 양을 재는 기구는?" : "측우기",
                "1876년 강화도에서 일본의 강압에 의해 맺어진 조약은?" : "강화도조약",
                "일본의 보호를 받아야하고, 일본 허락없이 외교를 못하게한 조약의 이름은?" : "을사늑약",
                "일제에 의하여 우리 나라의 주권이 강탈된 년도는?" : "1910년",
                "3.1운동 때 낭독한 독립선언서를 작성한 사람은?" : "최남선",
                "조선 후기에 실증적, 실제적으로 일어난 학문은?" : "실학",
                "조선 개국 전 이방원이 정몽주를 회유하기 위해 읊은 이 시조는?" : "하여가"
                }

# ----- [윈도우창 설정] --------------------------------------------------------------

WINDOW_WIDTH = 540
WINDOW_HEIGHT = 600
GRID = 30
GRID_WIDTH = int(WINDOW_WIDTH/GRID)
GRID_HEIGHT = int(WINDOW_HEIGHT/GRID)

# ===== [색상설정] ============

BLACK = 0, 0, 0
WHITE = 255,255,255
RED = 255, 0, 0
GREEN2 = 26, 102, 25
GREEN3 = 27, 150, 25
COLOR2 = 255, 200, 100
COLOR3 = 255, 250, 100
BLUE = 17, 17, 212
YELLOW = 255, 255, 0
LIGHT_BLUE1 = 100, 110, 255
LIGHT_BLUE2 = 100, 100, 255

# ===== [방향설정] ============

NORTH = ( 0, -1)
SOUTH = ( 0,  1)
WEST  = (-1,  0)
EAST  = ( 1,  0)

# ----- [사용할 질문 종류] -----------------------------------------------------------------------
# 1. 사용자 지정 질문 2. 라이브러리 질문
qustion = {}

while True :                                                     # 질문 정하기.
    print("\n                                                 ==| 1. 커스텀 질문 |==")
    print("                                                 ==| 2. 저장된 질문 |==\n")
    styleQustion = input("                                                [ 1 or 2 ]를 선택하세요 : ")
    print()
    if (styleQustion == '1') :
# ====================================================================================  사용자 지정 질문
        while True :
            try :
                numQustion = int(input("\n\n                입력할 질문의 갯수를 선택하세요 : "))
                if (numQustion <= 0) :
                    print("\n                                  ** 0을 제외한 정수를 입력해 주세요! **\n")
                else :
                    break
            except :
                print("\n                                  ** 0을 제외한 정수를 입력해 주세요! **")
        for i in range(1,int(numQustion)+1) :
            q = (input("\n                          %d번째 질문을 입력하세요 : " %i))
            a = (input("\n                          %d번째 답을 입력하세요 : " %i))
            
            qustion[q] = a
        print("                                       ==-|| 게임을 시작합니다 ||-==")
        break
# ==================================================================================== 라이브러리 질문
    elif (styleQustion == '2') :
        while True :
            try :
                print('''                                             /~ 1. 일반 상식 ~\\
                                             /~ 2. 넌센스    ~\\
                                             /~ 3. 한국사    ~\\''')
                numQustion = int(input("\n\n                사용할 질문의 종류를 선택하세요 : "))
                if (numQustion == 1) :
                    qustion = qustionCs
                    break
                elif (numQustion == 2) :
                    qustion = qustionNonsen
                    break
                elif (numQustion == 3) :
                    qustion = qustionKohis
                    break
                print("\n                                  ** 0을 제외한 정수(1,2,3)를 입력해 주세요! **\n")
            except :
                print("\n                                  ** 0을 제외한 정수(1,2,3)를 입력해 주세요! **\n")
                
        print("                                       ==-|| 게임을 시작합니다 ||-==")
        break 
# ====================================================================================
    else :
        print("\n                                                  ** 정확한 숫자(1 or 2) 를 입력해주세요. **\n")
        continue
    

# ----- [스네이크 클래스] -----------------------------------------------------------------------

class Snake:
    def __init__(self): # 뱀의 색
        self.length = 1
        self.create_snake()
        self.color1 = GREEN2
        self.color2 = GREEN3
        self.head_color = BLACK

    def create_snake(self): # 뱀의 초기 설정
        self.length = 3
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([NORTH, SOUTH, WEST, EAST])
        
    def alive_snake(self): # 정답일때 길이 그대로 부활
        self.length = self.length
        self.positions = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = random.choice([NORTH, SOUTH, WEST, EAST])

    def move_snake(self, surface): # 뱀 상호작용
        self.aTorF = 1
        head = self.get_head_position()
        x, y = self.direction
        next = ((head[0] + (x*GRID)) % WINDOW_WIDTH, (head[1] + (y*GRID)) % WINDOW_HEIGHT)
        if next in self.positions[2:]:
            gameover(surface, self)
            if (self.aTorF == 0) :
                self.create_snake()
                self.aTorF = 1
            else :
                self.alive_snake()
        else:
            self.positions.insert(0, next)
            if len(self.positions) > self.length:
                del self.positions[-1]

    def draw_snake(self, surface): # 뱀 규칙적 색상 칠하기
        for index, pos in enumerate(self.positions):
            if index == 0:
                draw_object(surface, self.head_color, pos)
            elif index % 2 == 0:
                draw_object(surface, self.color1, pos)
            else:
                draw_object(surface, self.color2, pos)

    def game_control(self, arrowkey): # 뱀 움직임 조작
        if (arrowkey[0]*-1, arrowkey[1]*-1) == self.direction:
            return
        else:
            self.direction = arrowkey
            return

    def get_head_position(self): # 뱀 머리 위치 정하기
        return self.positions[0]

# ----- [ 먹이 클래스 ] --------------------------------------------------------------

class Food:
    def __init__(self): # 열매의 기본 값
        self.position = (0, 0)
        self.color = RED
        self.randomize_food()

    def randomize_food(self): # 열매를 렌덤 좌표로 생성
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID,
                         random.randint(0, GRID_HEIGHT-1) * GRID)

    def draw_food(self, surface): # 열매 생성
        draw_object(surface, self.color, self.position)

# ----- [ 전역 player] --------------------------------------------------------------
    
def position_check(snake, food_group): # 뱀 길이 증가 and 열매 리필
    for food in food_group:
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_food()

def show_info(surface, snake): #뱀 길이 TEXT 띄우기
    font = pygame.font.SysFont('DOSPilgi',35)
    image = font.render(f'Len: {snake.length}', True, GREEN2)
    pos = image.get_rect()
    pos.move_ip(370,20)
    surface.blit(image, pos)

def gameover(surface, self): #뱀 죽었을 때 질문 띄우고, 정답or오답 판별
    while True :                                            # 중복 질문 제거
        ranQus = random.randrange(0,len(qustion))
        if (ranQus in duplication) :
            if (len(duplication) == len(qustion)) :
                duplication.clear()
            continue
        else :
            duplication.append(ranQus)
            break
    key = list(qustion.keys())
    key = key[ranQus]
    text = ''
    if (len(key) >= 30) :
        fontSize = 15
    elif (len(key) >= 25) :
        fontSize = 25
    else :
        fontSize = 30
    font = pygame.font.SysFont('DOSPilgi', fontSize)
    ansewrFont = pygame.font.SysFont('DOSPilgi', 25)
    
    qTorF = True
    txt_surface = font.render(text, True, BLACK)
    
    while qTorF :                               # 정답 입력과 렌더링
        screen.fill(BLACK)
        image = font.render(key, True, LIGHT_BLUE1)
        pos = image.get_rect()
        pos.move_ip(10,300)
        surface.blit(image, pos)
        
        for event in pygame.event.get() :
            if (event.type == pygame.KEYDOWN) :
                if (event.key == pygame.K_RETURN) :
                    if (qustion[key] in text) :
                        qTorF = False
                        text = ''
                        font = pygame.font.SysFont('DOSPilgi', 55)
                        screen.fill(BLACK)
                        image = font.render("정답!", True, GREEN3)
                        pos = image.get_rect()
                        pos.move_ip(200,250)
                        surface.blit(image, pos)
                        break
                    else :
                        qTorF = False
                        text = ''
                        font = pygame.font.SysFont('DOSPilgi', 55)
                        screen.fill(BLACK)
                        image = font.render("오답!", True, RED)
                        pos = image.get_rect()
                        pos.move_ip(200,250)
                        surface.blit(image, pos)
                        self.aTorF = 0
                        break
                if (event.key==pygame.K_BACKSPACE) :
                    text = text[:-1]
                else:
                    text += event.unicode
                txt_surface=ansewrFont.render(text,True,WHITE)
                
        screen.blit(txt_surface,(50,500))
        pygame.display.flip()
    time.sleep(1)
    
# ----- [ 전역 player 2] --------------------------------------------------------------

def show_info2(surface, snake2): #뱀2 길이 TEXT 띄우기
    font = pygame.font.SysFont('DOSPilgi',35)
    image = font.render(f'Len: {snake2.length}', True, COLOR2)
    pos = image.get_rect()
    pos.move_ip(10,20)
    surface.blit(image, pos)

def position_check(snake, food_group): # 뱀 길이 증가 and 열매 리필
    for food in food_group:
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_food()
    
# ----- [전역] --------------------------------------------------------------

player = Snake()
player2 = Snake()
player2.color1 = COLOR2
player2.color2 = COLOR3
run = True
duplication = []
aTorF = 1

def draw_background(surface): # 배경 색 초기화
    background = pygame.Rect((0,0),(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.draw.rect(surface, WHITE, background)
    draw_grid(surface)

def draw_grid(surface): # 배경 색 지정
    for row in range(0,int(GRID_HEIGHT)):
        for col in range(0, int(GRID_WIDTH)):
            if (row+col) % 2 == 0:
                rect = pygame.Rect((col*GRID, row*GRID), (GRID, GRID))
                pygame.draw.rect(surface, LIGHT_BLUE1, rect)
            else:
                rect = pygame.Rect((col*GRID, row*GRID), (GRID, GRID))
                pygame.draw.rect(surface, LIGHT_BLUE2, rect)
                
def draw_object(surface, color, pos): # 한 칸 생성하기 (열매 or 뱀)
    rect = pygame.Rect((pos[0], pos[1]), (GRID,GRID))
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, WHITE, rect, 1)

# ----- [ 먹이 그룹 ] --------------------------------------------------------------

def draw_food_group(food_group, surface): # 남아있는 열매 갯수에 따라 열매생성 호출
    for food in food_group:
        food.draw_food(surface)

food = Food()
food_group = []

for i in range(2) : # 음식 그룹에 열매 추가해 넣기
    food = Food()
    food_group.append(food)

# ----- [ game loop ] --------------------------------------------------------------

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
while run:                                                  # (wasd & ㅈㅁㄴㅇ) or (방향키 조종)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b or event.unicode == "ㅠ":
                run = False
                
            if event.key == pygame.K_a or event.unicode == "ㅁ":
                player2.game_control(WEST)
            if event.key == pygame.K_w or event.unicode == "ㅈ":
                player2.game_control(NORTH)
            if event.key == pygame.K_s or event.unicode == "ㄴ":
                player2.game_control(SOUTH)
            if event.key == pygame.K_d or event.unicode == "ㅇ":
                player2.game_control(EAST)

            if event.key == pygame.K_UP:
                player.game_control(NORTH)
            if event.key == pygame.K_DOWN:
                player.game_control(SOUTH)                
            if event.key == pygame.K_RIGHT:
                player.game_control(EAST)    
            if event.key == pygame.K_LEFT:
                player.game_control(WEST)
                
    draw_background(screen)
    draw_food_group(food_group, screen)
    food.draw_food(screen)

    player.move_snake(screen)
    position_check(player, food_group)
    player.draw_snake(screen)
    speed = player.length/2
    show_info(screen, player)
    
    player2.move_snake(screen)
    position_check(player2, food_group)
    player2.draw_snake(screen)
    speed2 = player2.length/2
    show_info2(screen, player2)
    
    pygame.display.flip()
    pygame.display.update()
    clock.tick(5+speed)
    clock2.tick(5+speed2)
    
# ----- [ 파이게임 종료 ] --------------------------------------------------------------
pygame.quit()