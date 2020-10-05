e='fps'
f='Game Quit'
g='answers'
h=list
Y=None
Z=type
S=''
P=print
K='snake-xoffset'
L=str
I=False
H='width'
G='height'
E=True
D=int
C='display'
import pygame as A,json,time,random as i,datetime as j
with open('config.json')as J:B=json.loads(J.read())
A.init()
F=A.display.set_mode((B[C][H],B[C][G]))
A.display.set_caption(B[C]['caption'])
N=A.image.load('./assets/startingbg.png')
O=A.image.load('./assets/startbtn.png')
w=A.image.load('./assets/grid-snakes.png')
x=A.image.load('./assets/snake.png')
y=A.image.load('./assets/announcement.png')
z=A.image.load('./assets/check.png')
A0=A.image.load('./assets/xmark.png')
k=A.image.load('./assets/continue.png')
l=A.image.load('./assets/quit.png')
m=[A.image.load('./assets/dice/1.png'),A.image.load('./assets/dice/2.png'),A.image.load('./assets/dice/3.png'),A.image.load('./assets/dice/4.png'),A.image.load('./assets/dice/5.png'),A.image.load('./assets/dice/6.png')]
n=A.time.Clock()
M=A.font.SysFont(Y,25)
def Q(imageh,imagew):A=B[C][G];E=B[C][H];F=E/2-imagew/2;I=A/2-imageh/2;return[D(F),D(I)]
def A1(offset):
	A,C=offset;A+=60
	if A>650:
		A=B[K]
		if C!=540:C+=60
		else:P('You win')
	return[A,C]
def A2(offset):A,C=offset;A-=B[K];E=A/60;F=C/60;return[D(E),D(F)]
def o(id,ug_answer):
	C=ug_answer;id=L(id);A=B[g][id]
	if Z(A)==h:
		for D in A:
			if D.lower()==L(C).lower():return E
		return I
	elif Z(A)==L:
		if C.lower()==A.lower():return E
		else:return I
def A3(event):
	C='-';B=event
	if B.type==A.KEYDOWN:
		if B.key==A.K_q:return'q'
		elif B.key==A.K_w:return'w'
		elif B.key==A.K_e:return'e'
		elif B.key==A.K_r:return'r'
		elif B.key==A.K_t:return't'
		elif B.key==A.K_y:return'y'
		elif B.key==A.K_u:return'u'
		elif B.key==A.K_i:return'i'
		elif B.key==A.K_o:return'o'
		elif B.key==A.K_p:return'p'
		elif B.key==A.K_a:return'a'
		elif B.key==A.K_s:return's'
		elif B.key==A.K_d:return'd'
		elif B.key==A.K_f:return'f'
		elif B.key==A.K_g:return'g'
		elif B.key==A.K_h:return'h'
		elif B.key==A.K_j:return'j'
		elif B.key==A.K_k:return'k'
		elif B.key==A.K_l:return'l'
		elif B.key==A.K_QUOTE:return"'"
		elif B.key==A.K_z:return'z'
		elif B.key==A.K_x:return'x'
		elif B.key==A.K_c:return'c'
		elif B.key==A.K_v:return'v'
		elif B.key==A.K_b:return'b'
		elif B.key==A.K_n:return'n'
		elif B.key==A.K_m:return'm'
		elif B.key==A.K_1:return'1'
		elif B.key==A.K_2:return'2'
		elif B.key==A.K_3:return'3'
		elif B.key==A.K_4:return'4'
		elif B.key==A.K_5:return'5'
		elif B.key==A.K_6:return'6'
		elif B.key==A.K_7:return'7'
		elif B.key==A.K_8:return'8'
		elif B.key==A.K_9:return'9'
		elif B.key==A.K_0:return'0'
		elif B.key==A.K_KP_MINUS:return C
		elif B.key==A.K_MINUS:return C
		elif B.key==A.K_SPACE:return' '
		else:return S
def A4(position,offset):
	F=position;D=M.render('You discovered and took a snake!',E,(0,0,0))
	if F==[6-1,0]:A=[6-1,4];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	elif F==[3-1,1]:A=[9-1,6];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	elif F==[2-1,4]:A=[2-1,8];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	D=M.render('You discovered and took a ladder!',E,(0,0,0))
	if F==[1-1,3]:A=[2-1,0];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	elif F==[10-1,5]:A=[9-1,2];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	elif F==[4-1,7]:A=[5-1,4];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	elif F==[9-1,9]:A=[8-1,6];C=[A[0]*60+B[K],A[1]*60];return A,C,D
	else:D=Y;return F,offset,D
def R():
	F.fill([42,42,42]);G=E
	while G==E:
		for D in A.event.get():
			if D.type==A.QUIT:G=I;P(f)
			elif D.type==A.MOUSEBUTTONDOWN:
				if D.pos[0]>=Q(30,100)[0]and D.pos[0]<=Q(30,100)[0]+100 and D.pos[1]>=Q(30,100)[1]and D.pos[1]<=Q(30,100)[1]+30:T();G=I
		F.blit(N,[0,0]);F.blit(O,Q(30,100));A.display.update();n.tick(B[C][e]);A.display.flip()
def T():
	p='Your Answer: ';q='questions';N=[]
	for r in B[q].keys():N.append(r)
	i.shuffle(N);P('Question Order: {}'.format(N));A5=j.datetime.now();O=S;U=S;s=S;R=[B[K],0];T=[0,0];t=m[0];V=E;a=I;b=I;c=E;W=I
	while V==E:
		for J in A.event.get():
			if J.type==A.QUIT:V=I;P(f)
			elif J.type==A.KEYDOWN:
				if J.key==A.K_BACKSPACE:O=O[:-1]
				elif J.key==A.K_RETURN:U=O;O=S;b=E;c=I
				else:A6=L(A3(J));O=O+A6
			elif J.type==A.MOUSEBUTTONDOWN:
				if W==E:
					if J.pos[0]>=D(B[C][H]/2-180)and J.pos[0]<=D(B[C][H]/2-180+100)and J.pos[1]>=D(B[C][G]/2+40)and J.pos[1]<=D(B[C][G]/2+40+30):V=I
					if J.pos[0]>=D(B[C][H]/2-50)and J.pos[0]<=D(D(B[C][H]/2-50)+200)and J.pos[1]>=D(B[C][G]/2+10)and J.pos[1]<=D(D(B[C][G]/2+40)+30):b=I;N.pop(0)
		F.fill([255,255,255]);F.blit(w,[0,0]);A7=L(T[0]+T[1]*10+1);A8=M.render('Score: '+A7,E,(0,0,0),(255,255,255));F.blit(A8,[0,0]);A9=L(round((j.datetime.now()-A5).total_seconds()));AA=M.render('Seconds Elapsed: '+A9,E,(0,0,0),(255,255,255));F.blit(AA,[0,B[C][G]-20]);F.blit(x,R)
		try:AB=B[q][N[0]]
		except Exception:P('Out of questions.');V=I
		AC=M.render('Question: '+AB,E,(0,0,0),(255,255,255));F.blit(AC,[0,B[C][G]-40]);s=M.render(p+L(O),E,(0,0,0),(255,255,255));F.blit(s,[D(B[C][H]/2-200),D(B[C][G]-20)])
		if b==E:
			AD=M.render(p+U,E,(0,0,0));F.blit(y,Q(341,604));F.blit(AD,[D(B[C][H]/2-180),D(B[C][G]/2-75)])
			if o(N[0],U)==E:
				F.blit(z,[D(B[C][H]/2),D(B[C][G]/2-70)]);a=E
				if c==I:
					X=i.randint(1,6);t=m[X-1];P('Random Number: '+L(X))
					for r in range(X):R=A1(R);T=A2(R)
					T,R,u=A4(T,R);c=E
				AE=M.render('You rolled a '+L(X),E,(0,0,0));F.blit(AE,[D(B[C][H]/2-180),D(B[C][G]/2-30)])
				if u!=Y:F.blit(u,[D(B[C][H]/2-180),D(B[C][G]/2)])
				W=E;F.blit(l,[D(B[C][H]/2-180),D(B[C][G]/2+40)]);F.blit(k,[D(B[C][H]/2-80),D(B[C][G]/2+40)])
			elif o(N[0],U)==I:
				F.blit(A0,[D(B[C][H]/2-180),D(B[C][G]/2-50)]);d=B[g][N[0]]
				if Z(d)==h:v='One of the correct answers were: '+d[0]
				else:v='The correct answer was: '+L(d)
				AF=M.render(v,E,(0,0,0));F.blit(AF,[D(B[C][H]/2-180),D(B[C][G]/2-20)]);a=I;W=E;F.blit(l,[D(B[C][H]/2-180),D(B[C][G]/2+40)]);F.blit(k,[D(B[C][H]/2-50),D(B[C][G]/2+40)])
		else:W=I
		if a==E:AG=M.render('Previous Roll:',E,(0,0,0));F.blit(AG,[0,40]);F.blit(t,[0,60])
		n.tick(B[C][e]);A.display.update();A.display.flip()
R()