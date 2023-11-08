using System;

class MainProgram
{
    static double CelsiusToFahrenheit(double celsius)
    {
        return (celsius * 9 / 5) + 32;
    }

    static double FahrenheitToCelsius(double fahrenheit)
    {
        return (fahrenheit - 32) * 5 / 9;
    }

    static double InchesToCentimeters(double inches)
    {
        return inches * 2.54;
    }

    static double CentimetersToInches(double centimeters)
    {
        return centimeters / 2.54;
    }

    static void Main(string[] args)
    {
        Console.WriteLine("Bienvenido al sistema de cálculo y conversión.");
        Console.WriteLine("1. Convertir de Celsius a Fahrenheit");
        Console.WriteLine("2. Convertir de Fahrenheit a Celsius");
        Console.WriteLine("3. Convertir de pulgadas a centímetros");
        Console.WriteLine("4. Convertir de centímetros a pulgadas");

        int choice;
        double result = 0.0;

        if (!int.TryParse(Console.ReadLine(), out choice) || choice < 1 || choice > 4)
        {
            Console.WriteLine("Opción no válida. Por favor, elige 1, 2, 3 o 4.");
        }
        else
        {
            try
            {
                switch (choice)
                {
                    case 1:
                        Console.Write("Ingresa la temperatura en grados Celsius: ");
                        double celsius;
                        if (double.TryParse(Console.ReadLine(), out celsius))
                        {
                            result = CelsiusToFahrenheit(celsius);
                            Console.WriteLine($"Resultado: {result} grados Fahrenheit");
                        }
                        else
                        {
                            Console.WriteLine("Entrada no válida. Debes ingresar un número válido.");
                        }
                        break;

                    case 2:
                        Console.Write("Ingresa la temperatura en grados Fahrenheit: ");
                        double fahrenheit;
                        if (double.TryParse(Console.ReadLine(), out fahrenheit))
                        {
                            result = FahrenheitToCelsius(fahrenheit);
                            Console.WriteLine($"Resultado: {result} grados Celsius");
                        }
                        else
                        {
                            Console.WriteLine("Entrada no válida. Debes ingresar un número válido.");
                        }
                        break;

                    case 3:
                        Console.Write("Ingresa la longitud en pulgadas: ");
                        double inches;
                        if (double.TryParse(Console.ReadLine(), out inches))
                        {
                            result = InchesToCentimeters(inches);
                            Console.WriteLine($"Resultado: {result} centímetros");
                        }
                        else
                        {
                            Console.WriteLine("Entrada no válida. Debes ingresar un número válido.");
                        }
                        break;

                    case 4:
                        Console.Write("Ingresa la longitud en centímetros: ");
                        double centimeters;
                        if (double.TryParse(Console.ReadLine(), out centimeters))
                        {
                            result = CentimetersToInches(centimeters);
                            Console.WriteLine($"Resultado: {result} pulgadas");
                        }
                        else
                        {
                            Console.WriteLine("Entrada no válida. Debes ingresar un número válido.");
                        }
                        break;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Se produjo un error: {ex.Message}");
            }
        }

        Console.WriteLine("Oprime cualquier tecla para salir...");
        Console.ReadKey();
    }
}