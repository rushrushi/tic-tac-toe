print("\n\nWelcome!!!")
print("Here is the format to enter the location")
input_sign = input("which sign do you want \nEnter 'O' for O \nEnter 'X' for X \nEnter here:")
#chart_c with O and X
chart_c=[['7','8','9'],
         ['4','5','6'],
         ['1','2','3']]

#Chart converted into numbers
chart_n=[['7','8','9'],
         ['4','5','6'],
         ['1','2','3']]

#Chart with numbers but for processing only
chart_p=[[1,2,3],
         [4,5,6],
         [7,8,9]]

#Chart with location status
chart_sta=[[0,1,2],
           [3,4,5],
           [6,7,8]]

#Chart with possibility
chart_poss=[[0,0,0],
            [0,0,0],
            [0,0,0]]

player_name=['sonu' , 'monu']
player_sign=[]
if input_sign == 'O' or input_sign == 'o':
    player_turn=0
    player_wait=1
    player_sign.append('O')
    player_sign.append('X')
else:
    player_turn=1
    player_wait=0
    player_sign.append('X')
    player_sign.append('O')
player_score=[0,0]

sum_ln=[0,0,0,0,0,0,0,0]
mul_ln=[0,0,0,0,0,0,0,0]
sta_ln=[0,0,0,0,0,0,0,0]
steps = 0



def clear_chart():
    for i in range(len(chart_c)):
        for j in range(len(chart_c[i])):
            chart_c[i][j]=' '


def print_chart():
        print('{}|{}|{}\n{}|{}|{}\n{}|{}|{}'.format(chart_c[0][0],chart_c[0][1],chart_c[0][2],chart_c[1][0],chart_c[1][1],chart_c[1][2],chart_c[2][0],chart_c[2][1],chart_c[2][2]))


def create_chart_n():
    
    for i in range(3):
        for j in range(3):
            if chart_c[i][j]==' ':
                chart_n[i][j]=10
            if chart_c[i][j]=='O':
                chart_n[i][j]=1
            if chart_c[i][j]=='X':
                chart_n[i][j]=-1


def analyse():

    if player_sign[player_turn]=='O':
        plvl=1
    else:
        plvl=-1
   
    #Create sums and muls
     
    sum_ln[0]=chart_p[0][0]+chart_p[0][1]+chart_p[0][2]
    sum_ln[1]=chart_p[1][0]+chart_p[1][1]+chart_p[1][2]
    sum_ln[2]=chart_p[2][0]+chart_p[2][1]+chart_p[2][2]
    sum_ln[3]=chart_p[0][0]+chart_p[1][0]+chart_p[2][0]
    sum_ln[4]=chart_p[0][1]+chart_p[1][1]+chart_p[2][1]
    sum_ln[5]=chart_p[0][2]+chart_p[1][2]+chart_p[2][2]
    sum_ln[6]=chart_p[0][0]+chart_p[1][1]+chart_p[2][2]
    sum_ln[7]=chart_p[0][2]+chart_p[1][1]+chart_p[2][0]

    mul_ln[0]=chart_p[0][0]*chart_p[0][1]*chart_p[0][2]
    mul_ln[1]=chart_p[1][0]*chart_p[1][1]*chart_p[1][2]
    mul_ln[2]=chart_p[2][0]*chart_p[2][1]*chart_p[2][2]
    mul_ln[3]=chart_p[0][0]*chart_p[1][0]*chart_p[2][0]
    mul_ln[4]=chart_p[0][1]*chart_p[1][1]*chart_p[2][1]
    mul_ln[5]=chart_p[0][2]*chart_p[1][2]*chart_p[2][2]
    mul_ln[6]=chart_p[0][0]*chart_p[1][1]*chart_p[2][2]
    mul_ln[7]=chart_p[0][2]*chart_p[1][1]*chart_p[2][0]

    #Create all line line status

    for i in range(len(sum_ln)):

        #Condition for Win
        if (abs(sum_ln[i]) == 3 and abs(mul_ln[i]) == 1):
            if plvl == mul_ln[i]:
                sta_ln[i] = 1000
            else:
                sta_ln[i] = -1 #dead

        #Condition for Save
        elif (abs(sum_ln[i]) == 1 and abs(mul_ln[i]) == 1):
            if plvl == mul_ln[i]:
                sta_ln[i] = 85
            else:
                sta_ln[i] = -1 #dead

        #Condition for No hope
        elif (abs(sum_ln[i]) == 10 and abs(mul_ln[i]) == 10):
            sta_ln[i] = -1

        #Condition for Dead
        elif (abs(sum_ln[i]) == 10 and abs(mul_ln[i]) == 10):
            sta_ln[i] = -1

        #Condition for Hope
        else:
            sta_ln[i] = 21

    #Create all location wise status

    chart_sta[0][0] = sta_ln[0]+sta_ln[3]+sta_ln[6]
    chart_sta[0][1] = sta_ln[0]+sta_ln[4]
    chart_sta[0][2] = sta_ln[0]+sta_ln[5]+sta_ln[7]

    chart_sta[1][0] = sta_ln[1]+sta_ln[3]
    chart_sta[1][1] = sta_ln[1]+sta_ln[4]+sta_ln[6]+sta_ln[7]      
    chart_sta[1][2] = sta_ln[1]+sta_ln[5]          
 
    chart_sta[2][0] = sta_ln[2]+sta_ln[3]+sta_ln[7]         
    chart_sta[2][1] = sta_ln[2]+sta_ln[4]
    chart_sta[2][2] = sta_ln[2]+sta_ln[5]+sta_ln[6]


def bot():

    chart_poss=[[0,0,0],[0,0,0],[0,0,0]]

 
    for i in range(3):
        for j in range(3):
            
            for t in range(3):
                for y in range(3):
                    chart_p[t][y]=chart_n[t][y]

             
            if chart_p[i][j]!=10:
                chart_poss[i][j]=-1
            else:
                if player_sign[player_turn]=='O':
                    chart_p[i][j]=1
                else:
                    chart_p[i][j]=-1
                analyse()
                chart_poss[i][j]=chart_sta[i][j]


    e=-4
    for i in range(3):
        for j in range(3):
            if chart_poss[i][j] >= e or  ( e == 0 and chart_poss[i][j] != -1):
                e = chart_poss[i][j]
                ei = i
                ej = j
    
    chart_c[ei][ej] = player_sign[player_turn]
    create_chart_n()


def win_check():
    for i in range(3):
        if ((chart_c[i][0] == chart_c[i][1] and chart_c[i][1] == chart_c[i][2]) and (chart_c[i][0] == 'O' or chart_c[i][0] == 'X')):
            return 'win'
        if ((chart_c[0][i] == chart_c[1][i] and chart_c[1][i] == chart_c[2][i]) and (chart_c[0][i] == 'O' or chart_c[0][i] == 'X')):
            return 'win'
    if ((chart_c[0][0] == chart_c[1][1] and chart_c[1][1] == chart_c[2][2]) and (chart_c[0][0] == 'O' or chart_c[0][0] == 'X')):
        return 'win'
    if ((chart_c[0][2] == chart_c[1][1] and chart_c[1][1] == chart_c[2][0]) and (chart_c[0][2] == 'O' or chart_c[0][2] == 'X')):
        return 'win'


def fill():

    try:
        i=int(input('{} Enter {} at location:'.format(player_name[player_turn],player_sign[player_turn])))

        if i>0 and i<10:
            i-=1
            j=2-int(i/3)
            k=i%3
            if (chart_c[j][k]=='O' or chart_c[j][k]=='X'):
                fill()
            else:
                chart_c[j][k]=player_sign[player_turn]
        else:
            fill()
    except:
        fill()

    create_chart_n()


# Program starts here.......

print_chart()
clear_chart()
print("\nLets play")
create_chart_n()
    
    
        
while True:
    a = win_check()
    
    if steps == 9:
        print_chart()
        print("\n\nDraw")
        print('{} score: {}'.format(player_name[player_turn],player_score[player_turn]))
        print('{} score: {}\n\n\n'.format(player_name[player_wait],player_score[player_wait]))
        clear_chart()
        steps = 0

    elif player_turn==0:
        if a == 'win':
            steps = 0
            player_score[player_wait]+=1
            print_chart()
            print('{} won!!!'.format(player_name[player_wait]))
            print('{} score: {}'.format(player_name[player_wait],player_score[player_wait]))
            print('{} score: {}\n\n\n'.format(player_name[player_turn],player_score[player_turn]))
            clear_chart()
        print_chart()
        fill()
        steps+=1

    else:
        if a == 'win':
            steps = 0
            player_score[player_wait]+=1
            print_chart()
            print('{} won!!!'.format(player_name[player_wait]))
            print('{} score: {}'.format(player_name[player_wait],player_score[player_wait]))
            print('{} score: {}\n\n\n'.format(player_name[player_sign],player_score[player_sign]))
            clear_chart()
        bot()
        steps+=1


    if player_turn == 0:
        player_turn=1
        player_wait=0

    else:
        player_turn=0
        player_wait=1