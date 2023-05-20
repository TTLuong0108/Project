// master
#include <Arduino.h>
#include <SPI.h>
#include <mcp2515.h>
#include <TimerOne.h>

struct can_frame canRecieve;
struct can_frame canSend1;
struct can_frame canSend2;
struct can_frame canSend3;
struct can_frame canSend4;
struct can_frame canSend5;
struct can_frame canSend6;
struct can_frame canSend7;
extern volatile unsigned long timer0_millis;
long data;
String Sdata;
int number;
byte data1,data2;
String theta1,theta2,theta3,theta4,theta5,theta6,t;
byte flag1 = 0;
byte flag2 = 0;
byte flag3 = 0;
byte flag4 = 0;
byte flag5 = 0;
byte flag6 = 0;
MCP2515 mcp2515(10);

void setup() 
{
  Serial.begin(115200);
  SPI.begin();
  mcp2515.reset();
  mcp2515.setBitrate(CAN_1000KBPS, MCP_8MHZ);
  mcp2515.setNormalMode();
  
  canSend1.can_id = 0x01; // CAN id as 0x01
  canSend1.can_dlc = 2; // CAN data length as 2 byte
  canSend2.can_id = 0x02;
  canSend2.can_dlc = 2; 
  canSend3.can_id = 0x03;
  canSend3.can_dlc = 2; 
  canSend4.can_id = 0x04;
  canSend4.can_dlc = 2; 
  canSend5.can_id = 0x05;
  canSend5.can_dlc = 2; 
  canSend6.can_id = 0x06;
  canSend6.can_dlc = 2; 

  canSend7.can_id = 0xFF;
  canSend7.can_dlc = 1; 
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  Serial.setTimeout(3);
}

String splitString(String str, String delim, uint16_t pos){
  String tmp = str;
  for(int i=0; i<pos; i++){
    tmp = tmp.substring(tmp.indexOf(delim)+1);

    
    if(tmp.indexOf(delim)== -1 
    && i != pos -1 )
      return "";
  }
  return tmp.substring(0,tmp.indexOf(delim));
}

void Read_number(byte D1, byte D2){
  if(D2<100){             // số dương
    number = D1 + D2*256;
    //direction_selection = 0;
  }
  else{
    number = (-(256-D1)-(255-D2)*256);
    // direction_selection = 1;
  }
}

void canSend(struct can_frame canSend,int datasend){
  canSend.data[0] = datasend;
  canSend.data[1] = datasend >> 8;
  mcp2515.sendMessage(&canSend);
}

void setFlag(struct can_frame canRecieve){
   if(canRecieve.can_id == 0x10){
    flag1 = canRecieve.data[0];
   }
   else if(canRecieve.can_id == 0x11){
    flag2 = canRecieve.data[0];
   }
   else if(canRecieve.can_id == 0x12){
    flag3 = canRecieve.data[0];
   }
   else if(canRecieve.can_id == 0x13){
    flag4 = canRecieve.data[0];
   }
   else if(canRecieve.can_id == 0x14){
    flag5 = canRecieve.data[0];
   }
   else if(canRecieve.can_id == 0x15){
    flag6 = canRecieve.data[0];
   }
}

void resetFlag(){
  flag1 = 0;
  flag2 = 0;
  flag3 = 0;
  flag4 = 0;
  flag5 = 0;
  flag6 = 0;
}

void synchronousPulse(){
  canSend7.data[0] = 1;
  canSend(canSend7,canSend7.data[0]);
}

void loop()
{
  if(Serial.available()>0){
     String Sdata = Serial.readStringUntil('\n');
     theta1 = splitString(Sdata,":",0);
     theta2 = splitString(Sdata,":",1);
     theta3 = splitString(Sdata,":",2);
     theta4 = splitString(Sdata,":",3);
     theta5 = splitString(Sdata,":",4);
     theta6 = splitString(Sdata,":",5);
     t = splitString(Sdata,":",6);

//     // CAN SEND
     int Itheta1 = theta1.toInt();
     int Itheta2 = theta2.toInt();
     int Itheta3 = theta3.toInt();
     int Itheta4 = theta4.toInt();
     int Itheta5 = theta5.toInt();
     int Itheta6 = theta6.toInt();
     canSend(canSend1,Itheta1);
     canSend(canSend2,Itheta2);
     canSend(canSend3,Itheta3);
     canSend(canSend4,Itheta4);
     canSend(canSend5,Itheta5);
     canSend(canSend6,Itheta6);
     //Serial.print("Du lieu gui: ");
     //Serial.println(Itheta1);   
  }
  else if (mcp2515.readMessage(&canRecieve) == MCP2515::ERROR_OK) {
    setFlag(canRecieve);
    if(flag1*flag2*flag3*flag4*flag5*flag6 == 1){
      synchronousPulse();
      String s = theta1 + ":" + theta2 + ":" + theta3 + ":" + theta4 + ":" + theta5 + ":" + theta6 + ":" + t;
      Serial.println(s);   
    }
    else{
        canSend7.data[0] = 0;
        canSend(canSend7,canSend7.data[0]);
    }
    //Serial.println("Dang cho phan hoi");
//    if(canRecieve.can_id == 0x10){
//        byte data1 = canRecieve.data[0];
//        byte data2 = canRecieve.data[1];
//        Read_number(data1, data2);
//        Serial.print("Du lieu nhan duoc: ");
//        String s = String(number)+ ":" + theta2 + ":" + theta3 + ":" + theta4 + ":" + theta5 + ":" + theta6 + ":" + t;
//        Serial.println(s);   
//      }


  }
}
