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
        return FK
    else:
        FK = Forward_kinematic.run(theta1,theta2,theta3,theta4,theta5,theta6,L1,L2,L3,L4,"T07")
        return FK
def Scale_value(theta,upper_limit,lower_limit):
    ans = theta*1.0
    if(theta >= upper_limit):
        ans = upper_limit
    elif (theta <= lower_limit):
        ans = lower_limit
    return ans

#///---- Main program ----- ///////
def run(Px,Py,Pz,alpha,beta,gama,theta_init,L1,L2,L3,L4,upper_limit,lower_limit):
    r11 = cosd(alpha)*cosd(beta)
    r21 = sind(alpha)*cosd(beta)
    r31 = -sind(beta)
    Pf = np.array([Px,Py,Pz])
    Pf_05 = np.array([Pf[0]-L4*r11,Pf[1]-L4*r21,Pf[2]-L4*r31])
    # T05 position and solve CCD for T05 to find theta1, theta2, theta3 and theta4
    Pe = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T05")
    A1 = Distance_Calculated(Pe,Pf_05,"246")
    A2 = Distance_Calculated(Pe,Pf_05,"135")
    while((A1>0.05) or (A2>0.05)):
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
   # T07 position and solve CCD for T57 to find theta5 and theta6
    Pe = Forward_kinematic.run(theta_init[0],theta_init[1],theta_init[2],theta_init[3],theta_init[4],theta_init[5],L1,L2,L3,L4,"T07")
    A1 = Distance_Calculated(Pe,Pf,"246")
    A2 = Distance_Calculated(Pe,Pf,"135")
    while((A1>0.05) or (A2>0.05)):
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
    return theta_init

#///---- Test program ----- //////
if __name__ == "__main__":
    L1,L2,L3,L4 = 170,225,225,215
    theta_init = np.array([45.0,-30.0,0.0,0.0,0.0,0.0])
    upper_limit = np.array([45,45,45,45,45,45])
    lower_limit = np.array([-45,-30,-45,-30,-45,-45])
    Px,Py,Pz = 805,0,10
    theta = run(Px,Py,Pz,0,0,0,theta_init,L1,L2,L3,L4,upper_limit,lower_limit)
    FK = Forward_kinematic.run(theta[0],theta[1],theta[2],theta[3],theta[4],theta[5],L1,L2,L3,L4,"T07")
    print(theta," ", FK)
    pass