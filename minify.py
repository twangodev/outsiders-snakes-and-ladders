x='fps'
w='Game Quit'
U=type
i=None
T=''
R=print
M=str
L='snake-xoffset'
I=False
H='width'
G='height'
E=True
D=int
C='display'
import pygame as A,json,time,random as b,datetime as c
with open('config.json')as J:B=json.loads(J.read())
A.init()
F=A.display.set_mode((B[C][H],B[C][G]))
A.display.set_caption(B[C]['caption'])
N=A.image.load('./assets/startingbg.png')
O=A.image.load('./assets/startbtn.png')
n=A.image.load('./assets/grid-snakes.png')
o=A.image.load('./assets/snake.png')
p=A.image.load('./assets/announcement.png')
q=A.image.load('./assets/check.png')
r=A.image.load('./assets/xmark.png')
d=A.image.load('./assets/continue.png')
e=A.image.load('./assets/quit.png')
f=[A.image.load('./assets/dice/1.png'),A.image.load('./assets/dice/2.png'),A.image.load('./assets/dice/3.png'),A.image.load('./assets/dice/4.png'),A.image.load('./assets/dice/5.png'),A.image.load('./assets/dice/6.png')]
g=A.time.Clock()
K=A.font.SysFont(i,25)
def P(imageh,imagew):A=B[C][G];E=B[C][H];F=E/2-imagew/2;I=A/2-imageh/2;return[D(F),D(I)]
def s(offset):
	A,C=offset;A+=60
	if A>650:
		A=B[L]
		if C!=540:C+=60
		else:R('You win')
	return[A,C]
def t(offset):A,C=offset;A-=B[L];E=A/60;F=C/60;return[D(E),D(F)]
def h(id,ug_answer):
	C=ug_answer;id=M(id);A=B['answers'][id]
	if U(A)==list:
		for D in A:
			if D.lower()==M(C).lower():return E
		return I
	elif U(A)==M:
		if C.lower()==A.lower():return E
		else:return I
def u(event):
	B=event
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
		elif B.key==A.K_SPACE:return' '
		elif B.key==A.K_MINUS:return'-'
		elif B.key==A.K_KP_MINUS:return'-'
		else:return T
def v(position,offset):
	F=position;D=K.render('You discovered and took a snake!',E,(0,0,0))
	if F==[6-1,0]:A=[6-1,4];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	elif F==[3-1,1]:A=[9-1,6];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	elif F==[2-1,4]:A=[2-1,8];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	D=K.render('You discovered and took a ladder!',E,(0,0,0))
	if F==[1-1,3]:A=[2-1,0];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	elif F==[10-1,5]:A=[9-1,2];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	elif F==[4-1,7]:A=[5-1,4];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	elif F==[9-1,9]:A=[8-1,6];C=[A[0]*60+B[L],A[1]*60];return A,C,D
	else:D=i;return F,offset,D
def Q():
	F.fill([42,42,42]);G=E
	while G==E:
		for D in A.event.get():
			if D.type==A.QUIT:G=I;R(w)
			elif D.type==A.MOUSEBUTTONDOWN:
				if D.pos[0]>=P(30,100)[0]and D.pos[0]<=P(30,100)[0]+100 and D.pos[1]>=P(30,100)[1]and D.pos[1]<=P(30,100)[1]+30:S();G=I
		F.blit(N,[0,0]);F.blit(O,P(30,100));A.display.update();g.tick(B[C][x]);A.display.flip()
def S():
	AA='Your Answer: ';A9='questions';N=[]
	for j in B[A9].keys():N.append(j)
	b.shuffle(N);R('Question Order: {}'.format(N));y=c.datetime.now();O=T;U=T;k=T;Q=[B[L],0];S=[0,0];l=f[0];V=E;Y=I;Z=I;a=E;W=I
	while V==E:
		for J in A.event.get():
			if J.type==A.QUIT:V=I;R(w)
			elif J.type==A.KEYDOWN:
				if J.key==A.K_BACKSPACE:O=O[:-1]
				elif J.key==A.K_RETURN:U=O;O=T;Z=E;a=I
				else:z=M(u(J));O=O+z
			elif J.type==A.MOUSEBUTTONDOWN:
				if W==E:
					if J.pos[0]>=D(B[C][H]/2-180)and J.pos[0]<=D(B[C][H]/2-180+100)and J.pos[1]>=D(B[C][G]/2+40)and J.pos[1]<=D(B[C][G]/2+40+30):V=I
					if J.pos[0]>=D(B[C][H]/2-50)and J.pos[0]<=D(D(B[C][H]/2-50)+200)and J.pos[1]>=D(B[C][G]/2+10)and J.pos[1]<=D(D(B[C][G]/2+40)+30):Z=I;N.pop(0)
		F.fill([255,255,255]);F.blit(n,[0,0]);A0=M(S[0]+S[1]*10+1);A1=K.render('Score: '+A0,E,(0,0,0),(255,255,255));F.blit(A1,[0,0]);A2=M(round((c.datetime.now()-y).total_seconds()));A3=K.render('Seconds Elapsed: '+A2,E,(0,0,0),(255,255,255));F.blit(A3,[0,B[C][G]-20]);F.blit(o,Q)
		try:A4=B[A9][N[0]]
		except Exception:R('Out of questions.');V=I
		A5=K.render('Question: '+A4,E,(0,0,0),(255,255,255));F.blit(A5,[0,B[C][G]-40]);k=K.render(AA+M(O),E,(0,0,0),(255,255,255));F.blit(k,[D(B[C][H]/2-200),D(B[C][G]-20)])
		if Z==E:
			A6=K.render(AA+U,E,(0,0,0));F.blit(p,P(341,604));F.blit(A6,[D(B[C][H]/2-180),D(B[C][G]/2-75)])
			if h(N[0],U)==E:
				F.blit(q,[D(B[C][H]/2),D(B[C][G]/2-70)]);Y=E
				if a==I:
					X=b.randint(1,6);l=f[X-1];R('Random Number: '+M(X))
					for j in range(X):Q=s(Q);S=t(Q)
					S,Q,m=v(S,Q);a=E
				A7=K.render('You rolled a '+M(X),E,(0,0,0));F.blit(A7,[D(B[C][H]/2-180),D(B[C][G]/2-30)])
				if m!=i:F.blit(m,[D(B[C][H]/2-180),D(B[C][G]/2)])
				W=E;F.blit(e,[D(B[C][H]/2-180),D(B[C][G]/2+40)]);F.blit(d,[D(B[C][H]/2-80),D(B[C][G]/2+40)])
			elif h(N[0],U)==I:F.blit(r,[D(B[C][H]/2-180),D(B[C][G]/2-50)]);Y=I;W=E;F.blit(e,[D(B[C][H]/2-180),D(B[C][G]/2+40)]);F.blit(d,[D(B[C][H]/2-50),D(B[C][G]/2+40)])
		else:W=I
		if Y==E:A8=K.render('Previous Roll:',E,(0,0,0));F.blit(A8,[0,40]);F.blit(l,[0,60])
		g.tick(B[C][x]);A.display.update();A.display.flip()
Q()