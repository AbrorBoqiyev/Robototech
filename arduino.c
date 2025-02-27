// Created by Entry
// tugma yordamida led chiroqlarini yoqish kodi

void setup() {
	pinMode(3, OUTPUT);
	pinMode(4, OUTPUT);
	pinMode(2, INPUT);
}

void loop() {
	if (digitalRead(2)) {
		digitalWrite(4, HIGH);
		digitalWrite(3, LOW);
	} else {
		digitalWrite(4, LOW);
		digitalWrite(3, HIGH);
	}
}


// Created by Entry
// mator yurg'azish kodi 

void setup() {
	pinMode(3, OUTPUT);
	pinMode(5, OUTPUT);
}

void loop() {
	analogWrite(5, 255);
	analogWrite(3, 0);
}
