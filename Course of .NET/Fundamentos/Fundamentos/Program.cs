using System;

class Fundamentos
{
    static void Main(string[] args)
    {
        // Tipos de Variables
        int num = 20;
        string nombre = "Sebastian";
        double altura = 1.71;
        bool esEstudiante = true;
        char inicial = 'S';

        // Operadores Aritméticos
        int suma = 5 + 3;
        int resta = 10 - 2;
        int multiplicacion = 4 * 2;
        double division = 10.0 / 2.0;
        int modulo = 10 % 3;

        // Operadores de Comparación
        bool esIgual = (5 == 5);
        bool esDiferente = (5 != 3);
        bool esMayor = (10 > 5);
        bool esMenor = (3 < 5);
        bool esMayorOIgual = (5 >= 5);
        bool esMenorOIgual = (3 <= 5);

        // Estructura de control
        int edad = 19;

        if (edad >= 18)
        {
            Console.WriteLine("Eres mayor de edad.");
        }
        else if (edad >= 13)
        {
            Console.WriteLine("Eres adolescente.");
        }
        else
        {
            Console.WriteLine("Eres un niño.");
        }

        // Bucles
        for (int f = 1; f <= 5; f++)
        {
            Console.WriteLine("Iteración: " + f);
        }

        int i = 0;
        while (i < 3)
        {
            Console.WriteLine("Valor: " + i);
            i++;
        }

        // Arrays
        int[] array = { 10, 20, 30, 40, 50 };
        Console.WriteLine(array[0]);

        for (int j = 0; j < array.Length; j++)
        {
            Console.WriteLine("Número: " + array[j]);
        }

        // Funciones o Métodos
        Saludar("Luis");
        int resultado = Sumar(4, 5);
        Console.WriteLine("Suma: " + resultado);

        // Objetos POO
        Persona p = new Persona();
        p.nombre = "Carlos";
        p.edad = 22;
        p.Presentarse();

        // Entrada y salida por consola
        Console.WriteLine("¿Cuál es tu nombre?");
        string nombreUsuario = Console.ReadLine();
        Console.WriteLine("Hola " + nombreUsuario);
    }

    // Métodos definidos fuera del Main
    static void Saludar(string nombre)
    {
        Console.WriteLine("Hola, " + nombre);
    }

    static int Sumar(int a, int b)
    {
        return a + b;
    }
}

// Clase Persona
class Persona
{
    public string nombre;
    public int edad;

    public void Presentarse()
    {
        Console.WriteLine("Hola, soy " + nombre + " y tengo " + edad + " años.");
    }
}