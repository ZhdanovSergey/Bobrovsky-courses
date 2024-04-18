namespace OOAP_2._13;

// C# поддерживает все варианты скрытия методов кроме второго: публичный метод родительского класса нельзя скрыть в потомке.

// 1. метод публичен в родительском классе Parent_1 и публичен в его потомке Child_1;

class Parent_1
{
    public void Print(string message) => Console.WriteLine(message);
}

class Child_1 : Parent_1 {}

class Client_1
{
    void Main() => new Child_1().Print("I`m still a public method");
}


// 3. метод скрыт в родительском классе Parent_3 и публичен в его потомке Child_3;

class Parent_3
{
    protected void Print(string message) => Console.WriteLine(message);
}

class Child_3 : Parent_3
{
    public new void Print(string message) => base.Print(message);
}

class Client_3
{
    void Main() => new Child_3().Print("I`ve become a public method");
}

// 4. метод скрыт в родительском классе Parent_4 и скрыт в его потомке Child_4.

class Parent_4
{
    protected void Print(string message) => Console.WriteLine(message);
}

class Child_4 : Parent_4 {}

class Client_4
{
    //void Main() => new Child_4().Print("I`m a protected method and cannot be called from here");
}