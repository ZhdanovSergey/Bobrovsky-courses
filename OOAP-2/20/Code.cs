using System.Collections;

namespace OOAP_2._20;

class Person
{
    public required string Name { get; init; }

    public virtual void Print() => Console.WriteLine($"My name is {Name}");
}

class Worker : Person
{
    public required string Profession { get; init; }

    // Наследование с функциональной вариацией
    public override void Print() => Console.WriteLine($"I am a ${Profession}");
}

class ShiftWorker : Worker
{
    public required string TimeOfDay { get; init; } // AM/PM

    //Наследование с вариацией типа
    public void Print(string timeOfDay)
    {
        if (timeOfDay == TimeOfDay)
            base.Print();
        else
            Console.WriteLine("I`m not working");
    }
}

abstract class Car
{
    public abstract void Drive();
}

class PassengerCar : Car
{
    // Наследование с конкретизацией
    public override void Drive() => Console.WriteLine("Driving with peoples onboard");
}

// Структурное наследование
class Staff : IEnumerable<Worker>
{
    public required string CompanyName { get; init; }

    private readonly Worker[] _workers;

    public Staff(IEnumerable<Worker> workers)
    {
        _workers = workers.ToArray();
    }

    public IEnumerator<Worker> GetEnumerator() => ((IEnumerable<Worker>)_workers).GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => _workers.GetEnumerator();
}