namespace OOAP_2._15;

abstract class Worker
{
    public abstract void DoWork();
}

class Programmer : Worker
{
    public override void DoWork() =>
        Console.WriteLine("Writing programms and stuff");
}

class ConstructionWorker : Worker
{
    public override void DoWork() =>
        Console.WriteLine("Laying bricks, smoke every hour");
}

class Company
{
    Worker[] workers = new Worker[] { new Programmer(), new ConstructionWorker() };
    void StartWorking()
    {
        foreach (Worker worker in workers)
        {
            worker.DoWork();
        }
    }
}