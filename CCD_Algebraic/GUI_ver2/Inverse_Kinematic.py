import numpy as np
import math
import Forward_kinematic
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
def Theta_calculated(Pe,Pc,Pf,Dimension_text):
    if Dimension_text == "135":
        Pe_x = Pe[0]
        Pe_y = Pe[1]
        Pe_z = 0

        Pc_x = Pc[0]
        Pc_y = Pc[1]
        Pc_z = 0
        
        Pf_x = Pf[0]
        Pf_y = Pf[1]
        Pf_z = 0; 

        Pec = np.array([Pe_x-Pc_x,Pe_y-Pc_y,Pe_z-Pc_z])
        Pec_x = Pec[0]
        Pec_y = Pec[1] 
        Pec_z = Pec[2]
        length_Pec = math.sqrt( (Pec_x)**2 + (Pec_y)**2 + (Pec_z)**2)
        Pfc = [Pf_x-Pc_x,Pf_y-Pc_y,Pf_z-Pc_z]
        Pfc_x = Pfc[0]
        Pfc_y = Pfc[1]
        Pfc_z = Pfc[2]
        length_Pfc = math.sqrt( (Pfc_x)**2 + (Pfc_y)**2 + (Pfc_z)**2)
            # Tich co huong
        Z = (Pec_x/length_Pec)*(Pfc_y/length_Pfc) - (Pec_y/length_Pec)*(Pfc_x/length_Pfc)
            # Calculate theta
        theta = acosd((Pec_x*Pfc_x+Pec_y*Pfc_y)/(length_Pec*length_Pfc))
        Z = np.sign(Z)
    elif Dimension_text == "246":
        Pe_x = Pe[0]
        Pe_y = 0
        Pe_z = Pe[2]

        Pc_x = Pc[0]
        Pc_y = 0
        Pc_z = Pc[2]
        
        Pf_x = Pf[0]
        Pf_y = 0
        Pf_z = Pf[2] 

        Pec = np.array([Pe_x-Pc_x,Pe_y-Pc_y,Pe_z-Pc_z])
        Pec_x = Pec[0]
        Pec_y = Pec[1] 
        Pec_z = Pec[2]
        length_Pec = math.sqrt( (Pec_x)**2 + (Pec_y)**2 + (Pec_z)**2)
        Pfc = [Pf_x-Pc_x,Pf_y-Pc_y,Pf_z-Pc_z]
        Pfc_x = Pfc[0]
        Pfc_y = Pfc[1]
        Pfc_z = Pfc[2]
        length_Pfc = math.sqrt( (Pfc_x)**2 + (Pfc_y)**2 + (Pfc_z)**2)
        # Tich co huong
        Z = -(Pec_z/length_Pec)*(Pfc_x/length_Pfc) + (Pec_x/length_Pec)*(Pfc_z/length_Pfc)
        # Calculate theta
        theta = acosd((Pec_x*Pfc_x+Pec_z*Pfc_z)/(length_Pec*length_Pfc))
        Z = np.sign(Z)
    return np.array([round(theta,4),Z])
def Distance_Calculated(Pe,Pf,Dimension_text):
    if Dimension_text == "135":
        Pe_x = Pe[0]
        Pe_y = Pe[1]
        Pe_z = 0

        Pf_x = Pf[0]
        Pf_y = Pf[1]
        Pf_z = 0
    elif Dimension_text == "246":
        Pe_x = Pe[0]
        Pe_y = 0
        Pe_z = Pe[2]

        Pf_x = Pf[0]
        Pf_y = 0
        Pf_z = Pf[2]
    Distance = math.sqrt( (Pf_x-Pe_x)**2 + (Pf_y-Pe_y)**2 + (Pf_z-Pe_z)**2);        
    return round(Distance,4)
def Theta_Rotation(theta_matrix,L1,L2,L3,L4,theta_change):
    #theta_matrix[theta_change-1] = theta
    theta1 = theta_matrix[0]
    theta2 = theta_matrix[1]
    theta3 = theta_matrix[2]
    theta4 = theta_matrix[3]
    theta5 = theta_matrix[4]
    theta6 = theta_matrix[5]
    if theta_change < 5:
        FK = Forward_kinematic.run(theta1,theta2,theta3,theta4,theta5,theta6,L1,L2,L3,L4,"T05")
        FK[0] = round(FK[0],4)
        FK[1] = round(FK[1],4)
        FK[2] = round(FK[2],4)
        return FK
    else:
        FK = Forward_kinematic.run(theta1,theta2,theta3,theta4,theta5,theta6,L1,L2,L3,L4,"T07")
        FK[0] = round(FK[0],4)
        FK[1] = round(FK[1],4)
        FK[2] = round(FK[2],4)
        return FK
def Scale_value(theta,upper_limit,lower_limit):
    ans = theta*1.0
    if(theta >= upper_limit):
        ans = upper_limit
    elif (theta <= lower_limit):
        ans = lower_limit
    return ans

#///---- Main program ----- ///////
def run(Px,Py,Pz,alpha,beta,gama,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision,interation):
    temp_theta_init = theta_init
    r11 = cosd(alpha)*cosd(beta)
    r21 = sind(alpha)*cosd(beta)
    r31 = -sind(beta)
    Pf = np.array([Px,Py,Pz])
    Pf_05 = np.array([Pf[0]-L4*r11,Pf[1]-L4*r21,Pf[2]-L4*r31])
    # T05 position and solve CCD for T05 to find theta1, theta2, theta3 and theta4
    Pe = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T05")
    A1 = Distance_Calculated(Pe,Pf_05,"246")
    A2 = Distance_Calculated(Pe,Pf_05,"135")
    count_iteration_T05 = 0
    count_iteration_T57 = 0
    while((A1>precision) or (A2>precision)):
        if(count_iteration_T05 >= interation):
            break
        else:
            count_iteration_T05 = count_iteration_T05 + 1
            #**************** 246 frame **********#
            #T03 postion
            Pc2 = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T03")
            theta,Z = Theta_calculated(Pe,Pc2,Pf_05,"246")
            theta_init[3] = Scale_value(Z*theta+theta_init[3],upper_limit[3],lower_limit[3]) #theta4   
            Pe = Theta_Rotation(theta_init,L1,L2,L3,L4,4)
            #T01 position
            Pc1 = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T01")
            theta,Z = Theta_calculated(Pe,Pc1,Pf_05,"246")
            theta_init[1] = Scale_value(Z*theta+theta_init[1],upper_limit[1],lower_limit[1]) #theta2
            Pe = Theta_Rotation(theta_init,L1,L2,L3,L4,2)
            #Distance
            A1 = Distance_Calculated(Pe,Pf_05,"246")
            #**************** 135 frame **********#
            #T03 postion
            Pc2 = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T03")
            theta,Z = Theta_calculated(Pe,Pc2,Pf_05,"135")
            theta_init[2] = Scale_value(Z*theta+theta_init[2],upper_limit[2],lower_limit[2]) #theta3   
            Pe = Theta_Rotation(theta_init,L1,L2,L3,L4,3)
            #T01 position
            Pc1 = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T01")
            theta,Z = Theta_calculated(Pe,Pc1,Pf_05,"135")
            theta_init[0] = Scale_value(Z*theta+theta_init[0],upper_limit[0],lower_limit[0]) #theta1   
            Pe = Theta_Rotation(theta_init,L1,L2,L3,L4,1)
            #Distance
            A2 = Distance_Calculated(Pe,Pf_05,"135")
    if(count_iteration_T05 >= interation):
        return temp_theta_init
    else:
    # T07 position and solve CCD for T57 to find theta5 and theta6
        Pe = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T07")
        A1 = Distance_Calculated(Pe,Pf,"246")
        A2 = Distance_Calculated(Pe,Pf,"135")         
        while((A1>precision) or (A2>precision)):
            if(count_iteration_T57 >= interation):
                return temp_theta_init
            else:
                count_iteration_T57 = count_iteration_T57 + 1
                #**************** 246 frame **********#
                #T05 postion
                Pc3 = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T05")
                theta,Z = Theta_calculated(Pe,Pc3,Pf,"246")
                theta_init[5] = Scale_value(Z*theta+theta_init[5],upper_limit[5],lower_limit[5]) #theta6
                Pe = Theta_Rotation(theta_init,L1,L2,L3,L4,6)
                #Distance
                A1 = Distance_Calculated(Pe,Pf,"246")
                #T05 position
                Pc3 = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T05")
                theta,Z = Theta_calculated(Pe,Pc3,Pf,"135")
                theta_init[4] = Scale_value(Z*theta+theta_init[4],upper_limit[4],lower_limit[4]) #theta5  
                Pe = Theta_Rotation(theta_init,L1,L2,L3,L4,5)
                #Distance
                A2 = Distance_Calculated(Pe,Pf,"135")
        theta_init[0] = round(theta_init[0],5)
        theta_init[1] = round(theta_init[1],5)
        theta_init[2] = round(theta_init[2],5)
        theta_init[3] = round(theta_init[3],5)
        theta_init[4] = round(theta_init[4],5)
        theta_init[5] = round(theta_init[5],5)
        #print(count_iteration)
        return theta_init

def lines(start_Point,end_Point,t,tf):
    mod = divmod(t,2*tf)
    if(mod[1] <= tf):
        floor = divmod(t,2*tf)
        tp = t-floor[0]*2*tf
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
    else:
        temp = start_Point
        start_Point = end_Point
        end_Point = temp

        floor = divmod(t,2*tf)
        tp = t-floor[0]*2*tf - tf 
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
    return np.array([round(Px,4),round(Py,4),round(Pz,4)])

def lines_Home(start_Point,end_Point,theta_home,theta_start,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit):
    if(t <= tf):
        t1 = Joint_space(theta_home[0],theta_start[0],t,tf)
        t2 = Joint_space(theta_home[1],theta_start[1],t,tf)
        t3 = Joint_space(theta_home[2],theta_start[2],t,tf)
        t4 = Joint_space(theta_home[3],theta_start[3],t,tf)
        t5 = Joint_space(theta_home[4],theta_start[4],t,tf)
        t6 = Joint_space(theta_home[5],theta_start[5],t,tf)
        theta = np.array([t1,t2,t3,t4,t5,t6])
    elif(t>tf and t<=2*tf):
        tp = t - tf 
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
        theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
        theta_init = theta
    elif(t>2*tf and t<=3*tf):
        temp = start_Point
        start_Point = end_Point
        end_Point = temp
        tp = t - 2*tf 
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
        theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
        theta_init = theta
    else:
        tp = round(t - 3*tf,2)
        t1 = Joint_space(theta_init[0],theta_home[0],tp,tf)
        t2 = Joint_space(theta_init[1],theta_home[1],tp,tf)
        t3 = Joint_space(theta_init[2],theta_home[2],tp,tf)
        t4 = Joint_space(theta_init[3],theta_home[3],tp,tf)
        t5 = Joint_space(theta_init[4],theta_home[4],tp,tf)
        t6 = Joint_space(theta_init[5],theta_home[5],tp,tf)
        theta = np.array([t1,t2,t3,t4,t5,t6])
    return theta

def Triangle_Home(Point1,Point2,Point3,theta_home,theta_start,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit):
    if(t <= tf):
        t1 = Joint_space(theta_home[0],theta_start[0],t,tf)
        t2 = Joint_space(theta_home[1],theta_start[1],t,tf)
        t3 = Joint_space(theta_home[2],theta_start[2],t,tf)
        t4 = Joint_space(theta_home[3],theta_start[3],t,tf)
        t5 = Joint_space(theta_home[4],theta_start[4],t,tf)
        t6 = Joint_space(theta_home[5],theta_start[5],t,tf)
        theta = np.array([t1,t2,t3,t4,t5,t6])
    elif(t>tf and t<=2*tf):
        tp = t - tf 
        start_Point = Point1
        end_Point = Point2
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
        theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
        theta_init = theta
    elif(t>2*tf and t<=3*tf):
        tp = t - 2*tf 
        start_Point = Point2
        end_Point = Point3
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
        theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
        theta_init = theta
    elif(t>3*tf and t<=4*tf):
        tp = t - 3*tf 
        start_Point = Point3
        end_Point = Point1
        Pz = start_Point[2]+(3.0/(tf**2))*(end_Point[2]-start_Point[2])*(tp**2) - (2.0/(tf**3))*(end_Point[2]-start_Point[2])*(tp**3)
        Py = start_Point[1]+(3.0/(tf**2))*(end_Point[1]-start_Point[1])*(tp**2) - (2.0/(tf**3))*(end_Point[1]-start_Point[1])*(tp**3)
        Px = start_Point[0]+(3.0/(tf**2))*(end_Point[0]-start_Point[0])*(tp**2) - (2.0/(tf**3))*(end_Point[0]-start_Point[0])*(tp**3)
        theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
        theta_init = theta
    else:
        tp = round(t - 4*tf,2)
        t1 = Joint_space(theta_init[0],theta_home[0],tp,tf)
        t2 = Joint_space(theta_init[1],theta_home[1],tp,tf)
        t3 = Joint_space(theta_init[2],theta_home[2],tp,tf)
        t4 = Joint_space(theta_init[3],theta_home[3],tp,tf)
        t5 = Joint_space(theta_init[4],theta_home[4],tp,tf)
        t6 = Joint_space(theta_init[5],theta_home[5],tp,tf)
        theta = np.array([t1,t2,t3,t4,t5,t6])
    return theta

def Circle_Home(Point1,R,theta_home,theta_start,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit):
    if(t <= tf):
        t1 = Joint_space(theta_home[0],theta_start[0],t,tf)
        t2 = Joint_space(theta_home[1],theta_start[1],t,tf)
        t3 = Joint_space(theta_home[2],theta_start[2],t,tf)
        t4 = Joint_space(theta_home[3],theta_start[3],t,tf)
        t5 = Joint_space(theta_home[4],theta_start[4],t,tf)
        t6 = Joint_space(theta_home[5],theta_start[5],t,tf)
        theta = np.array([t1,t2,t3,t4,t5,t6])
    elif(t>tf and t<=3*tf):
        floor = divmod(t,tf)
        tp = t - floor[0]*tf
        f = 1/tf
        Px = Point1[0]
        Py = Point1[1]+R*math.sin(2*math.pi*f*tp)
        Pz = Point1[2]+R*math.cos(2*math.pi*f*tp)
        theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
        theta_init = theta
    else:
        tp = round(t - 3*tf,2)
        t1 = Joint_space(theta_init[0],theta_home[0],tp,tf)
        t2 = Joint_space(theta_init[1],theta_home[1],tp,tf)
        t3 = Joint_space(theta_init[2],theta_home[2],tp,tf)
        t4 = Joint_space(theta_init[3],theta_home[3],tp,tf)
        t5 = Joint_space(theta_init[4],theta_home[4],tp,tf)
        t6 = Joint_space(theta_init[5],theta_home[5],tp,tf)
        theta = np.array([t1,t2,t3,t4,t5,t6])
    return theta


def Joint_space(t1,t2,t,tf):
    if(t1 > t2):
        return round(t1 - (t1-t2)*t/tf,4)
    else:
        return round(t1 + (t2-t1)*t/tf,4)
#///---- Test program ----- //////
if __name__ == "__main__":
    X = []
    Y = []
    Z = []
    L1,L2,L3,L4 = 170.0,225.0,225.0,215.0
    theta_init = np.array([45.0,-30.0,0.0,0.0,0.0,0.0])
    upper_limit = np.array([45,45,45,45,45,45])
    lower_limit = np.array([-45,-30,-45,-30,-45,-45])
    theta = run(780.0,0,0,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
    print(theta)
    FK = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
    print(FK[0],FK[1],FK[2])


    # times = np.arange(0,15+0.05,0.05)
    # theta_init = np.array([45.0,-30.0,0.0,0.0,0.0,0.0])
    # max_error = 0
    # index = 0
    # tf = 5.0
    # start_Point = np.array([780.0,-100,50.0])
    # end_Point = np.array([780.0,100.0,50.0])
    # thetaH2S_start = np.array([0,0,0,0,0,0])
    # thetaH2S_end = run(start_Point[0],start_Point[1],start_Point[2],0,0,0,np.array([45.0,-30.0,0.0,0.0,0.0,0.0]),L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
    # thetaE2H = run(end_Point[0],end_Point[1],end_Point[2],0,0,0,np.array([45.0,-30.0,0.0,0.0,0.0,0.0]),L1,L2,L3,L4,upper_limit,lower_limit,precision=0.05,interation=700)
    # for t in times:
    #     t = round(t,2) 
    #     theta = lines_Home(start_Point,end_Point,thetaH2S_start,thetaH2S_end,thetaE2H,t,tf,L1,L2,L3,L4,theta_init,upper_limit,lower_limit)
    #     theta_init = theta
    #     FK = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
    #     print(t,FK[1])



    