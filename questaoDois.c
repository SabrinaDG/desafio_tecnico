#include <stdio.h>

int fibonacci(int N)
{
    if (N < 0)
    {
        printf("Erro: N deve ser um número inteiro não negativo.\n");
        return -1; // Valor de erro
    }
    else if (N == 0 || N == 1)
    {
        return N;
    }
    else
    {
        return fibonacci(N - 1) + fibonacci(N - 2);
    }
}

int main() {
    int N;

    printf("Informe um número: ");
    scanf("%d", &N);

    int resultado = fibonacci(N);
    if (resultado != -1)
    {
        printf("Fibonacci(%d) = %d\n", N, resultado);
    }
    return 0;
}
