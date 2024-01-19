using OOAP_1.LinkedList;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1.TwoWayList;

interface IParentList<TValue>
{
    // КОМАНДЫ

    // предусловие: список не пустой
    // постусловие: курсор установлен на первый узел
    void Head(); // установить курсор на первый узел в списке

    // предусловие: список не пустой
    // постусловие: курсор установлен на последний узел
    void Tail(); // установить курсор на последний узел в списке

    // предусловие: правее курсора есть узел
    // постусловие: курсор установлен на узел справа от текущего
    void Right(); // сдвинуть курсор на один узел вправо

    // предусловие: список не пустой
    // постусловие: вставляет новый узел с переданным значением справа от текущего узла
    void PutRight(TValue value); // вставить справа от текущего узла

    // предусловие: список не пустой
    // постусловие: вставляет новый узел с переданным значением слева от текущего узла
    void PutLeft(TValue value); // вставить слева от текущего узла

    // предусловие: список не пустой
    // постусловие: удален текущий узел
    //  если справа от текущего узла есть узел, курсор устанавливается на него, иначе
    //  если слева от текущего узла есть узел, курсор устанавливается на него
    void Remove(); // удалить текущий узел

    // постусловие: все узлы удалены
    void Clear(); // очистить список

    // постусловие: в хвост списка добавлен новый узел с переданным значением
    void AddTail(TValue value); // добавить новый узел в хвост списка

    // предусловие: список не пустой
    // постусловие: значение текущего узла на изменено на новое
    void Replace(TValue value); // заменить значение текущего узла на заданное

    // постусловие: курсор установлен на первый узел с переданным значением, находящийся справа от текущего узла, если такой есть
    void Find(TValue value); // установить курсор на следующий узел с искомым значением (по отношению к текущему узлу)

    // постусловие: все узлы с заданным значением удалены
    void RemoveAll(TValue value); // удалить в списке все узлы с заданным значением

    // ЗАПРОСЫ

    // предусловие: список не пустой
    TValue Get { get; } // получить значение текущего узла
    int Size { get; } // посчитать количество узлов в списке
    bool IsHead { get; } // находится ли курсор в начале списка?
    bool IsTail { get; } // находится ли курсор в конце списка?
    bool IsValue { get; } // установлен ли курсор на какой-либо узел в списке?

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int HeadStatus { get; } // возвращает значение HEAD_*
    int TailStatus { get; } // возвращает значение TAIL_*
    int RightStatus { get; } // возвращает значение RIGHT_*
    int PutRightStatus { get; } // возвращает значение PUT_RIGHT_*
    int PutLeftStatus { get; } // возвращает значение PUT_LEFT_*
    int RemoveStatus { get; } // возвращает значение REMOVE_*
    int ReplaceStatus { get; } // возвращает значение REPLACE_*
    int FindStatus { get; } // возвращает значение FIND_*
}

interface ILinkedList<TValue> : IParentList<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создан новый пустой список
    abstract static ILinkedList<TValue> Create();
}

interface ITwoWayList<TValue> : IParentList<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создан новый пустой список
    abstract static ITwoWayList<TValue> Create();

    // КОМАНДЫ

    // предусловие: левее курсора есть узел
    // постусловие: курсор установлен на узел слева от текущего
    void Left(); // сдвинуть курсор на один узел влево

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ

    int LeftStatus { get; } // возвращает значение LEFT_*
}

class Node<TValue>
{
    public TValue Value { get; set; }
    public Node<TValue>? Prev { get; set; }
    public Node<TValue>? Next { get; set; }
    public Node(TValue value)
    {
        Value = value;
    }
}

abstract class ParentList<TValue> : IParentList<TValue>
{
    protected Node<TValue>? _cursor;
    protected Node<TValue>? _head;
    protected Node<TValue>? _tail;

    public const int HEAD_NIL = 0; // Head() ещё не вызывалась
    public const int HEAD_OK = 1; // последняя Head() отработала нормально
    public const int HEAD_ERR = 2; // список пуст

    public const int TAIL_NIL = 0; // Tail() ещё не вызывалась
    public const int TAIL_OK = 1; // последняя Tail() отработала нормально
    public const int TAIL_ERR = 2; // список пуст

    public const int RIGHT_NIL = 0; // Right() ещё не вызывалась
    public const int RIGHT_OK = 1; // последняя Right() отработала нормально
    public const int RIGHT_ERR = 2; // правее курсора нет узлов

    public const int PUT_RIGHT_NIL = 0; // PutRight() ещё не вызывалась
    public const int PUT_RIGHT_OK = 1; // последняя PutRight() отработала нормально
    public const int PUT_RIGHT_ERR = 2; // список пуст

    public const int PUT_LEFT_NIL = 0; // PutLeft() ещё не вызывалась
    public const int PUT_LEFT_OK = 1; // последняя PutLeft() отработала нормально
    public const int PUT_LEFT_ERR = 2; // список пуст

    public const int REMOVE_NIL = 0; // Remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя Remove() отработала нормально
    public const int REMOVE_ERR = 2; // список пуст

    public const int REPLACE_NIL = 0; // Replace() ещё не вызывалась
    public const int REPLACE_OK = 1; // последняя Replace() отработала нормально
    public const int REPLACE_ERR = 2; // список пуст

    public const int FIND_NIL = 0; // Find() ещё не вызывалась
    public const int FIND_OK = 1; // последняя Find() отработала нормально
    public const int FIND_ERR = 2; // подходящий узел не найден

    // ЗАПРОСЫ

    public TValue Get
    {
        get
        {
            if (_cursor is null)
                throw new InvalidOperationException("List is empty");

            return _cursor.Value;
        }
    }
    public int Size { get; private set; }
    public bool IsHead
    { 
        get => _head is not null && _cursor == _head;
    }
    public bool IsTail
    {
        get => _tail is not null && _cursor == _tail;
    }
    public bool IsValue
    {
        get => _cursor is not null;
    }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ

    public int HeadStatus { get; private set; } = HEAD_NIL;
    public int TailStatus { get; private set; } = TAIL_NIL;
    public int RightStatus { get; private set; } = RIGHT_NIL;
    public int PutRightStatus { get; private set; } = PUT_RIGHT_NIL;
    public int PutLeftStatus { get; private set; } = PUT_LEFT_NIL;
    public int RemoveStatus { get; private set; } = REMOVE_NIL;
    public int ReplaceStatus { get; private set; } = REPLACE_NIL;
    public int FindStatus { get; private set; } = FIND_NIL;

    // КОМАНДЫ

    public void Head()
    {
        if (_head is null)
        {
            HeadStatus = HEAD_ERR;
            return;
        }

        _cursor = _head;
        HeadStatus = HEAD_OK;
    }
    public void Tail()
    {
        if (_tail is null)
        {
            TailStatus = TAIL_ERR;
            return;
        }

        _cursor = _tail;
        TailStatus = TAIL_OK;
    }
    public void Right()
    {
        if (_cursor?.Next is null)
        {
            RightStatus = RIGHT_ERR;
            return;
        }

        _cursor = _cursor.Next;
        RightStatus = RIGHT_OK;
    }
    public void PutRight(TValue value)
    {
        if (_cursor is null)
        {
            PutRightStatus = PUT_RIGHT_ERR;
            return;
        }

        var newNode = new Node<TValue>(value);
        var nextNode = _cursor.Next;

        _cursor.Next = newNode;
        newNode.Prev = _cursor;

        if (nextNode is null)
        {
            _tail = newNode;
        } else
        {
            newNode.Next = nextNode;
            nextNode.Prev = newNode;
        }

        Size += 1;
        PutRightStatus = PUT_RIGHT_OK;
    }
    public void PutLeft(TValue value)
    {
        if (_cursor is null)
        {
            PutLeftStatus = PUT_LEFT_ERR;
            return;
        }

        var prevNode = _cursor.Prev;
        var newNode = new Node<TValue>(value);

        newNode.Next = _cursor;
        _cursor.Prev = newNode;

        if (prevNode is null)
        {
            _head = newNode;
        }
        else
        {
            prevNode.Next = newNode;
            newNode.Prev = prevNode;
        }

        Size += 1;
        PutLeftStatus = PUT_LEFT_OK;
    }
    public void Remove()
    {
        if (_cursor is null)
        {
            RemoveStatus = REMOVE_ERR;
            return;
        }

        var nextCursor = _cursor.Next ?? _cursor.Prev;

        if (_cursor.Prev is null)
            _head = _cursor.Next;
        else
            _cursor.Prev.Next = _cursor.Next;

        if (_cursor.Next is null)
            _tail = _cursor.Prev;
        else
            _cursor.Next.Prev = _cursor.Prev;

        Size -= 1;
        _cursor = nextCursor;
        RemoveStatus = REMOVE_OK;
    }
    public void Clear()
    {
        _cursor = null;
        _head = null;
        _tail = null;
        Size = 0;
    }
    public void AddTail(TValue value)
    {
        var originalCursor = _cursor;
        _cursor = _tail;
        PutRight(value);
        _cursor = originalCursor;
        Size += 1;
    }
    public void Replace(TValue value)
    {
        if (_cursor is null)
        {
            ReplaceStatus = REPLACE_ERR;
            return;
        }

        _cursor.Value = value;
        ReplaceStatus = REPLACE_OK;
    }
    public void Find(TValue value)
    {
        var originalCursor = _cursor;
        Right();

        while (RightStatus == RIGHT_OK)
        {
            if (_cursor.Value.Equals(value))
            {
                FindStatus = FIND_OK;
                return;
            }

            Right();
        }

        _cursor = originalCursor;
        FindStatus = FIND_ERR;
    }
    public void RemoveAll(TValue value)
    {
        _cursor = _head;

        while (_cursor is not null)
        {
            if ( _cursor.Value.Equals(value))
                Remove();
            else
                _cursor = _cursor.Next;
        }
    }
}

class LinkedList<TValue> : ParentList<TValue>, ILinkedList<TValue>
{
    // КОНСТРУКТОР
    public static ILinkedList<TValue> Create() => new LinkedList<TValue>();
}

class TwoWayList<TValue> : ParentList<TValue>, ITwoWayList<TValue>
{
    public const int LEFT_NIL = 0; // Left() ещё не вызывалась
    public const int LEFT_OK = 1; // последняя Left() отработала нормально
    public const int LEFT_ERR = 2; // левее курсора нет узлов

    // КОНСТРУКТОР
    public static ITwoWayList<TValue> Create() => new TwoWayList<TValue>();

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int LeftStatus { get; private set; } = LEFT_NIL;

    // КОМАНДЫ
    public void Left()
    {
        if (_cursor?.Prev is null)
        {
            LeftStatus = LEFT_ERR;
            return;
        }

        _cursor = _cursor.Prev;
        LeftStatus = LEFT_OK;
    }
}