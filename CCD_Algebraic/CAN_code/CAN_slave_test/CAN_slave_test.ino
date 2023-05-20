// Đây là code tạm


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
struct can_frame canSendFeedBack;
MCP2515 mcp2515(10);


void setup() {

  Serial.begin(115200);
  SPI.begin();
  
  mcp2515.reset();
  
  mcp2515.setBitrate(CAN_1000KBPS, MCP_8MHZ);
  
  canSend1.can_id = 0xA; 
  canSend1.can_dlc = 2;
  canSendFeedBack.can_id = 0x10; 
  canSendFeedBack.can_dlc = 1;
  
  mcp2515.setNormalMode();

  pinMode(PP, OUTPUT);
  pinMode(PG, OUTPUT);
  pinMode(NP, OUTPUT);
  pinMode(NG, OUTPUT);
}

////////////////////////////////////////////////////////////////////
// chuyển đổi số
////////////////////////////////////////////////////////////////////
void Convert_CanDataToInt(byte D1, byte D2){
  if(D2<100){             // số dương
    number = D1 + D2*256;
  }
  else{
    number = (-(256-D1)-(255-D2)*256);
  }
}
////////////////////////////////////////////////////////////////////
// feed back
////////////////////////////////////////////////////////////////////
void Feedback_to_Mater(int data){
  canSendFeedBack.data[0] = data;
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
        canSend1.data[0] = data1;
        canSend1.data[1] = data2;
        mcp2515.sendMessage(&canSend1);
     }
   }
 
}
