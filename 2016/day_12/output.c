
#include <stdio.h>
int main(int argc, char** argv) {
	int a = 0;
	int b = 0;
	int c = 1;
	int d = 0;
LBL0: a=1;
LBL1: b=1;
LBL2: d=26;
LBL3: if (c) goto LBL5;
LBL4: if (1) goto LBL9;
LBL5: c=7;
LBL6: d++;
LBL7: c--;
LBL8: if (c) goto LBL6;
LBL9: c=a;
LBL10: a++;
LBL11: b--;
LBL12: if (b) goto LBL10;
LBL13: b=c;
LBL14: d--;
LBL15: if (d) goto LBL9;
LBL16: c=13;
LBL17: d=14;
LBL18: a++;
LBL19: d--;
LBL20: if (d) goto LBL18;
LBL21: c--;
LBL22: if (c) goto LBL17;

	printf("a = %d\n", a);
	return 0;
}
