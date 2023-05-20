// Đây là code chinh


#include <Arduino.h>
#include <SPI.h>
#include <mcp2515.h>
#include <TimerOne.h>

#define PP 6
#define PG 7
#define NP 8
#define NG 9



int number,number_pass=0;

struct can_frame canRecieve;
struct can_frame canSend1;
struct can_frame canSendFeedBack1;
struct can_frame canSendFeedBack2;
struct can_frame canSendFeedBack3;
struct can_frame canSendFeedBack4;
struct can_frame canSendFeedBack5;
struct can_frame canSendFeedBack6;

int theta1,theta2,theta3,theta4,theta5,theta6;
MCP2515 mcp2515(10);


void setup() {

  Serial.begin(115200);
  SPI.begin();
  
  mcp2515.reset();
  
  mcp2515.setBitrate(CAN_1000KBPS, MCP_8MHZ);
  
  canSendFeedBack1.can_id = 0x10; 
  canSendFeedBack1.can_dlc = 1;
  canSendFeedBack2.can_id = 0x11; 
  canSendFeedBack2.can_dlc = 1;
  canSendFeedBack3.can_id = 0x12; 
  canSendFeedBack3.can_dlc = 1;
  canSendFeedBack4.can_id = 0x13; 
  canSendFeedBack4.can_dlc = 1;
  canSendFeedBack5.can_id = 0x14; 
  canSendFeedBack5.can_dlc = 1;
  canSendFeedBack6.can_id = 0x15; 
  canSendFeedBack6.can_dlc = 1;  
  mcp2515.setNormalMode();

  pinMode(PP, OUTPUT);
  pinMode(PG, OUTPUT);
  pinMode(NP, OUTPUT);
  pinMode(NG, OUTPUT);
}

////////////////////////////////////////////////////////////////////
// chuyển đổi số
////////////////////////////////////////////////////////////////////
int convertCanDataToInt(byte D1, byte D2){
  if(D2<100){             // số dương
    number = D1 + D2*256;
  }
  else{
    number = (-(256-D1)-(255-D2)*256);
  }
  return number;
}
////////////////////////////////////////////////////////////////////
// feed back
////////////////////////////////////////////////////////////////////
void feedbackToMater(struct can_frame canSendFeedBack){
  canSendFeedBack.data[0] = 1;
  mcp2515.sendMessage(&canSendFeedBack);
}
void loop() {
  if (mcp2515.readMessage(&canRecieve) == MCP2515::ERROR_OK) {
      ////////////////////////////////////////////////////////////////////
      ///////////////////////////////// NHẬN GÓC TỪ MASTER ///////////////
      ////////////////////////////////////////////////////////////////////
     if(canRecieve.can_id == 0x01){
        byte data1 = canRecieve.data[0];
        byte data2 = canRecieve.data[1];
        theta1 = convertCanDataToInt(data1, data2);
        feedbackToMater(canSendFeedBack1);
     }
     else if(canRecieve.can_id == 0x01){
        byte data1 = canRecieve.data[0];
        byte data2 = canRecieve.data[1];
        theta2 = convertCanDataToInt(data1, data2);
        feedbackToMater(canSendFeedBack2);
     }
     else if(canRecieve.can_id == 0x03){
        byte data1 = canRecieve.data[0];
        byte data2 = canRecieve.data[1];
        theta3 = convertCanDataToInt(data1, data2);
        feedbackToMater(canSendFeedBack3);
     }
     else if(canRecieve.can_id == 0x04){
        byte data1 = canRecieve.data[0];
        byte data2 = canRecieve.data[1];
        theta4 = convertCanDataToInt(data1, data2);
        feedbackToMater(canSendFeedBack4);
     }
     else if(canRecieve.can_id == 0x05){
        byte data1 = canRecieve.data[0];
        byte data2 = canRecieve.data[1];
        theta5 = convertCanDataToInt(data1, data2);
        feedbackToMater(canSendFeedBack5);
     }
     else if(canRecieve.can_id == 0x06){
        byte data1 = canRecieve.data[0];
        byte data2 = canRecieve.data[1];
        theta1 = convertCanDataToInt(data1, data2);
        feedbackToMater(canSendFeedBack1);
     }     
     else if(canRecieve.can_id == 0xFF){
        byte data1 = canRecieve.data[0];
        if(data1 == 1){
          // Tien hanh bam xung pwm
        }
        else{
          // khong bam xung pwm
        }
     }
     
   }
 
}
