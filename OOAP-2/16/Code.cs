namespace OOAP_2._16;

class Parent
{
    public virtual void Print() => Console.WriteLine("I`m a parent");
    public virtual void CheckSameType<T>(T _)
    {
        if (typeof(T) == typeof(Parent))
            Console.WriteLine("Same type");
        else
            Console.WriteLine("Different type");
    }
}

class Child : Parent
{
    public override void Print() => Console.WriteLine("I`m a child");
    public override void CheckSameType<T>(T _)
    {
        if (typeof(T) == typeof(Child))
            Console.WriteLine("Same type");
        else
            Console.WriteLine("Different type");
    }
}

class Client
{
    public static void Method()
    {
        Parent parent = new Parent();
        Child child = new Child();
        Parent childAsParent = child;

        // полиморфный вызов
        childAsParent.Print(); // "I`m a child"

        // ковариантный вызов
        parent.CheckSameType<Parent>(parent); // Same type
        parent.CheckSameType<Parent>(childAsParent); // Same type
        parent.CheckSameType<Child>(child); // Different type

        // полиморфный + ковариантный вызов
        childAsParent.CheckSameType<Parent>(parent); // Different type
        childAsParent.CheckSameType<Parent>(childAsParent); // Different type
        childAsParent.CheckSameType<Child>(child); // Same type
    }
}