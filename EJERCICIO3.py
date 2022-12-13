#La secuencia de Fibonacci se usa tradicionalmente para explicar la recursividad del árbol.
function fibonacci(n) {
 if(n==0 || n == 1)
 return n;
 return fibonacci(n-1) + fibonacci(n-2);
}