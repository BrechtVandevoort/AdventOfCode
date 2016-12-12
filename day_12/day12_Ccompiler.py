import re

HEADER_CODE = """
#include <stdio.h>
int main(int argc, char** argv) {
	int a = 0;
	int b = 0;
	int c = 1;
	int d = 0;
"""

FOOTER_CODE = """
	printf("a = %d\\n", a);
	return 0;
}
"""

LABEL_PREFIX = 'LBL'

code = ''
for i, instruction in enumerate(open('input.txt').readlines()):
	parts = instruction.split()
	code += LABEL_PREFIX + str(i) + ': '
	if parts[0] == 'cpy':
		code += parts[2] + '=' + parts[1] + ';\n'
	elif parts[0] == 'inc':
		code += parts[1] + '++;\n'
	elif parts[0] == 'dec':
		code += parts[1] + '--;\n'
	elif parts[0] == 'jnz':
		code += 'if (' + parts[1] + ') goto ' + LABEL_PREFIX + str(i + int(parts[2])) + ';\n'

open('output.c', 'w').write(HEADER_CODE + code + FOOTER_CODE)
