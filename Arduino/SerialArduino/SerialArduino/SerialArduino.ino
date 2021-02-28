#define numofvaluereceive 2
#define digitpervaluereceive 3
#define numofvaluesend 2

int valreceive[numofvaluereceive];
int stringlength = numofvaluereceive * digitpervaluereceive + 1;
int valssend[numofvaluesend] = {0, 0};

int counter = 0;
bool counterstart = false;
String receivestring;

void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void receivedata() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '$') {
      counterstart = true;
    }
    if (counterstart) {
      if (counter < stringlength) {
        receivestring = String(receivestring + c);
        counter++;
        //$050255
      }
      if (counter >= stringlength) {
        for (int i = 0; i < numofvaluereceive; i++)
        {
          int num = (i * digitpervaluereceive) + 1;
          valreceive[i] = receivestring.substring(num, num + digitpervaluereceive).toInt();
          //valreceive[0] = receivestring.substring(1,4).toInt();
          //valreceive[1] = receivestring.substring(4,7).toInt();
        }
        receivestring = "";
        counter = 0;
        counterstart = false;
      }
    }
  }
}

void senddata(int myvals[numofvaluesend]){
  String mystring;
  for (int i=0; i<numofvaluesend; i++){
    mystring +=String(myvals[i]) + '#';
  }
  Serial.println(mystring);
}

void loop() {
  //receivedata();

  //sendata
  int sensorval = analogRead(A0);
  valssend[0] = sensorval;
  senddata(valssend);
  delay(100);
  
 // if (valreceive[0] == 0 && valreceive[1] == 255){
 //     digitalWrite(13, HIGH);}
      
 // else  if (valreceive[0] == 0 && valreceive[1] == 0){
 //     digitalWrite(13, LOW);}


}
