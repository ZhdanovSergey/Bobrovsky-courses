using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1;

internal class BoundedStack<T>
{
    private List<T> stack = new();

    public const int PEEK_NIL = 0;
    public const int PEEK_OK = 1;
    public const int PEEK_ERR = 2;

    public const int POP_NIL = 0;
    public const int POP_OK = 1;
    public const int POP_ERR = 2;

    public const int PUSH_NIL = 0;
    public const int PUSH_OK = 1;
    public const int PUSH_ERR = 2;

    public int MaxCapacity { get; init; }
    public int Size { get => stack.Count; }
    public int PeekStatus { get; private set; } = PEEK_NIL;
    public int PopStatus { get; private set; } = POP_NIL;
    public int PushStatus { get; private set; } = PUSH_NIL;

    public BoundedStack(int maxCapacity = 32)
    {
        MaxCapacity = maxCapacity;
    }
    // постусловие: из стека удалятся все значения
    public void Clear()
    {
        stack.Clear();
        PeekStatus = PEEK_NIL;
        PopStatus = POP_NIL;
        PushStatus = PUSH_NIL;
    }
    // предусловие: стек не пустой
    public T? Peek()
    {
        T? result = default;

        if (Size > 0)
        {
            result = stack[^1];
            PeekStatus = PEEK_OK;
        }
        else
        {
            PeekStatus = PEEK_ERR;
        }

        return result;
    }
    // предусловие: стек не пустой
    // постусловие: из стека удалён верхний элемент
    public void Pop()
    {
        if (Size > 0)
        {
            stack.RemoveAt(Size - 1);
            PopStatus = POP_OK;
        }
        else
        {
            PopStatus = POP_ERR;
        }
    }
    // предусловие: количество элементов в стеке меньше максимального
    // постусловие: в стек добавлено новое значение
    public void Push(T value)
    {
        if (Size < MaxCapacity)
        {
            stack.Add(value);
            PushStatus = PUSH_OK;
        } else
        {
            PushStatus = PUSH_ERR;
        }
    }
}
