// По тексту урока я вообще не понял что такое динамическое связываение. Судя по тому, что пишут в интернете, динамическое связывание можно представить так:

namespace OOAP_2._7;

abstract class Animal
{
    public virtual void MakeSound() =>
        Console.WriteLine("Some sound");
}

class Dog : Animal
{
    public override void MakeSound() =>
        Console.WriteLine("Bark");
}

class Cat : Animal
{
    public override void MakeSound() =>
        Console.WriteLine("Meow");
}

class Program
{
    static void Main()
    {
        Animal myAnimal;

        // Динамическое связывание - решение о том, какой именно метод MakeSound вызывать, принимается во время выполнения программы
        myAnimal = new Dog();
        myAnimal.MakeSound(); // Вывод: Bark

        myAnimal = new Cat();
        myAnimal.MakeSound(); // Вывод: Meow
    }
}