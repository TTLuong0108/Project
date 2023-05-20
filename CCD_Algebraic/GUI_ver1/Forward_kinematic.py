import numpy as np
import math
#////---- Math function -----
def sind(input):
    input = math.radians(input)
    value = math.sin(input)
    value = round(value,4)
    return value
def cosd(input):
    input = math.radians(input)
    value = math.cos(input)
    value = round(value,4)
    return value
def asind(input):
    value = math.asin(input)
    value = round(value*180/math.pi,4)
    return value
def acosd(input):
    value = math.acos(input)
    value = round(value*180/math.pi,4)
    return value
#////---- Sub function ------ /////
def TransMatrix(a,anpha,d,theta):
    DH_matrix = [[cosd(theta),-sind(theta)*cosd(anpha),sind(theta)*sind(anpha) ,a*cosd(theta)],
                 [sind(theta),cosd(anpha)*cosd(theta) ,-cosd(theta)*sind(anpha),a*sind(theta)],
                 [0          ,sind(anpha)             ,cosd(anpha)             ,d           ],
                 [0          ,0                       ,0                       ,1          ]]
    return np.array(DH_matrix)
#///---- Main program ----- ///////
def run(t1,t2,t3,t4,t5,t6,L1,L2,L3,L4,text):
    T01=TransMatrix(L1,0,0,0)
    T12=TransMatrix(0 , 90,0,t1)     
    T23=TransMatrix(L2,-90,0,t2)       
    T34=TransMatrix(0 , 90,0,t3)       
    T45=TransMatrix(L3,-90,0,t4)         
    T56=TransMatrix(0 , 90,0,t5)      
    T67=TransMatrix(L4, -90,0,t6) 
    if text == "T01":
        ans = T01
    elif text == "T02":
        ans = T01 @ T12
    elif text == "T03":
        ans = T01 @ T12 @ T23
    elif text == "T04":
        ans = T01 @ T12 @ T23 @ T34
    elif text == "T05":
        ans = T01 @ T12 @ T23 @ T34 @ T45
    elif text == "T06":
        ans = T01 @ T12 @ T23 @ T34 @ T45 @ T56
    elif text == "T07":
        ans = T01 @ T12 @ T23 @ T34 @ T45 @ T56 @ T67
    return np.array([round(ans[0,3],4),round(ans[1,3],4),round(ans[2,3],4)])
#///---- Test program ----- //////
if __name__ == "__main__":
    theta_init = np.array([0,0,0,0,0,0])
    L1,L2,L3,L4 = 170,225,225,215
    Pc2 = run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T03")
    print(Pc2)