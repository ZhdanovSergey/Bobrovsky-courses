namespace OOAP_2._21;

// Пример наследования реалиации https://github.com/ZhdanovSergey/Bobrovsky-courses/blob/main/OOAP-1/TwoWayList/TwoWayList.cs

// Если я правильно понял суть льготного наследования, то мне кажется лучше использовать вместо него композицию.
// Но в качестве примера наследования можно привести следующий код:

public class TextEditorLibrary
{
    protected readonly BlockNodeUtils BlockNodeUtils = new();
    protected readonly InlineNodeUtils InlineNodeUtils = new();
}

public class InlineTextEditor : TextEditorLibrary
{
    private object _state = new();
    public void Add(string text) => InlineNodeUtils.InsertNode(_state, text);
    public void Delete(string text) => InlineNodeUtils.DeleteNode(_state, text);
}

public class BlockNodeUtils
{
    public void InsertNode(object state, object node) => Console.WriteLine("Insert block node");
    public void DeleteNode(object state, object node) => Console.WriteLine("Delete block node");
}

public class InlineNodeUtils
{
    public void InsertNode(object state, object node) => Console.WriteLine("Insert inline node");
    public void DeleteNode(object state, object node) => Console.WriteLine("Delete inline node");
}