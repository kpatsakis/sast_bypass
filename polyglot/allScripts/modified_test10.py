#if 0 
print('Hello from Python!') 
#endif 
#if 0 
""" " 
#endif 
#include <stdio.h>
#include <string.h>

void printWrapper(char *string) {
    printf(string);
}

int main(int argc, char **argv) {
    char buf[5012];
    memcpy(buf, argv[1], 5012);
    printWrapper(argv[1]);
    return 0;
}

#if 0 
" """ 
#endif 