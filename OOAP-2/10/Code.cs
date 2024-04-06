// В C# все методы по умолчанию закрытые, но при переопределении закрытого метода ошибки компиляции не возникает, только предупреждение, что если переопределение было намеренным, следует использовать ключевое слово new.
// Использование new считается плохой практикой и допустимо лишь в качестве последнего средства.
// Чтобы определить открытый метод, нужно использовать ключевое слово virtual при объявлении и override при переопределении.

class Parent
{
    public void ClosedMethod() => Console.WriteLine("Parent ClosedMethod");
    public virtual void OpenedMethod() => Console.WriteLine("Parent OpenedMethod");
}

class Child : Parent
{
    public new void ClosedMethod() => Console.WriteLine("Child ClosedMethod");
    public override void OpenedMethod() => Console.WriteLine("Child OpenedMethod");
}