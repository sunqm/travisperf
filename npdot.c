#include <stdlib.h>

void NPdgemm(const int n, double *a, double *b, double *c)
{
        const char TransN = 'N';
        const double D1 = 1;
        const double D0 = 0;
        dgemm_(&TransN, &TransN, &n, &n, &n,
               &D1, a, &n, b, &n, &D0, c, &n);
}
