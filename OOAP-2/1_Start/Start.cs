using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_2._1_Start;

class Person
{
    public required string Name { get; init; }

    public virtual void PrintInfo() =>
        Console.WriteLine($"Name: {Name}");
}

// Пример наследования: класс Employee содержит унаследованное от Person свойство Name
class Employee : Person
{
    public required string Profession { get; init; }
    public override void PrintInfo() =>
        Console.WriteLine($"Name: {Name}, Profession: {Profession}");
}

// Пример композиции: класс Company содержит Employee как одно из полей
class Company
{
    public readonly Employee BestEmployee = new Employee { Name = "Sergey", Profession = "Programmer" };
}

// Пример полиморфизма: можно использовать экземпляр Employee как экземпляр Person
class PolimorficExample
{
    public void Main()
    {
        Person person = new Employee { Name = "Sergey", Profession = "Programmer" };
        person.PrintInfo();
    }
}