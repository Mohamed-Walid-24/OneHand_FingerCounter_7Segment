int digits [11][8]{
  {1,1,0,1,1,1,1,0}, // digit 0
  {0,0,0,0,0,1,1,0}, // digit 1
  {1,1,1,0,1,1,0,0}, // digit 2
  {1,0,1,0,1,1,1,0}, // digit 3
  {0,0,1,1,0,1,1,0}, // digit 4
  {1,0,1,1,1,0,1,0}, // digit 5
  {1,1,1,1,1,0,1,0}, // digit 6
  {0,0,0,0,1,1,1,0}, // digit 7
  {1,1,1,1,1,1,1,0}, // digit 8
  {1,0,1,1,1,1,1,0}, // digit 9
  {0,0,0,0,0,0,0,1}  // Dot
};

void display_digit(int d){
  if   (digits[d][0]==1) digitalWrite(2, HIGH); else digitalWrite(2, LOW); //D
  if   (digits[d][1]==1) digitalWrite(3, HIGH); else digitalWrite(3, LOW); //E
  if   (digits[d][2]==1) digitalWrite(4, HIGH); else digitalWrite(4, LOW); //G
  if   (digits[d][3]==1) digitalWrite(5, HIGH); else digitalWrite(5, LOW); //F
  if   (digits[d][4]==1) digitalWrite(6, HIGH); else digitalWrite(6, LOW); //A
  if   (digits[d][5]==1) digitalWrite(7, HIGH); else digitalWrite(7, LOW); //B
  if   (digits[d][6]==1) digitalWrite(8, HIGH); else digitalWrite(8, LOW); //C
  if   (digits[d][7]==1) digitalWrite(9, HIGH); else digitalWrite(9, LOW); //DP
  
}
void setup() {
  // put your setup code here, to run once:
   pinMode(2, OUTPUT);// Segment D
   pinMode(3, OUTPUT);// Segment E
   pinMode(4, OUTPUT);// Segment G
   pinMode(5, OUTPUT);// Segment F
   pinMode(6, OUTPUT);// Segment A
   pinMode(7, OUTPUT);// Segment B
   pinMode(8, OUTPUT);// Segment C
   pinMode(9 ,OUTPUT);// Segment DP

   Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while( Serial.available() > 0){
    int number = Serial.parseInt();
    display_digit(number);
    delay(250);
  }
}
