using OOAP_1.Queue;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1.Deque;

interface IParentQueue<TValue>
{
    // постусловие: все значения удалены
    void Clear();

    // КОМАНДЫ
    // постусловие: значение добавлено в хвост очереди
    void AddTail(TValue value);

    // предусловие: очередь не пустая
    // постусловие: значение удалено из головы очереди
    void RemoveHead();

    // ЗАПРОСЫ
    int Size { get; }
    // предусловие: очередь не пустая
    TValue? GetHead();

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int RemoveHeadStatus { get; }
    int GetHeadStatus { get; }
}

interface IQueue<TValue> : IParentQueue<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создана пустая очередь
    static abstract IQueue<TValue> Create();
}

interface IDeque<TValue> : IParentQueue<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создана пустая двусторонняя очередь
    static abstract IDeque<TValue> Create();

    // КОМАНДЫ
    // постусловие: значение добавлено в голову двусторонней очереди
    void AddHead(TValue value);

    // предусловие: очередь не пустая
    // постусловие: значение удалено из хвоста двусторонней очереди
    void RemoveTail();

    // ЗАПРОСЫ
    // предусловие: очередь не пустая
    TValue? GetTail();

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int RemoveTailStatus { get; }
    int GetTailStatus { get; }
}

abstract class ParentQueue<TValue> : IParentQueue<TValue>
{
    protected readonly List<TValue> list = new();

    public const int REMOVE_HEAD_NIL = 0; // RemoveHead() ещё не вызывалась
    public const int REMOVE_HEAD_OK = 1; // последняя RemoveHead() отработала нормально
    public const int REMOVE_HEAD_ERR = 2; // очередь пуста

    public const int GET_HEAD_NIL = 0; // GetHead() ещё не вызывалась
    public const int GET_HEAD_OK = 1; // последняя GetHead() отработала нормально
    public const int GET_HEAD_ERR = 2; // очередь пуста

    // КОМАНДЫ
    public void Clear() => list.Clear();
    public void AddTail(TValue value) => list.Add(value);
    public void RemoveHead()
    {
        if (Size == 0)
        {
            RemoveHeadStatus = REMOVE_HEAD_ERR;
            return;
        }

        list.RemoveAt(0);
        RemoveHeadStatus = REMOVE_HEAD_OK;
    }

    // ЗАПРОСЫ
    public int Size { get => list.Count; }
    public TValue? GetHead()
    {
        if (Size == 0)
        {
            GetHeadStatus = GET_HEAD_ERR;
            return default(TValue);
        }

        GetHeadStatus = GET_HEAD_OK;
        return list.First();
    }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int RemoveHeadStatus { get; private set; } = REMOVE_HEAD_NIL;
    public int GetHeadStatus { get; private set; } = GET_HEAD_OK;
}

class Queue<TValue> : ParentQueue<TValue>, IQueue<TValue>
{
    // КОНСТРУКТОР
    public static IQueue<TValue> Create() => new Queue<TValue>();
}

class Deque<TValue> : ParentQueue<TValue>, IDeque<TValue>
{
    public const int REMOVE_TAIL_NIL = 0; // RemoveTail() ещё не вызывалась
    public const int REMOVE_TAIL_OK = 1; // последняя RemoveTail() отработала нормально
    public const int REMOVE_TAIL_ERR = 2; // очередь пуста

    public const int GET_TAIL_NIL = 0; // GetTail() ещё не вызывалась
    public const int GET_TAIL_OK = 1; // последняя GetTail() отработала нормально
    public const int GET_TAIL_ERR = 2; // очередь пуста

    // КОНСТРУКТОР
    public static IDeque<TValue> Create() => new Deque<TValue>();

    // КОМАНДЫ
    public void AddHead(TValue value) => list.Insert(0, value);
    public void RemoveTail()
    {
        if (Size == 0)
        {
            RemoveTailStatus = REMOVE_TAIL_ERR;
            return;
        }

        list.RemoveAt(Size - 1);
        RemoveTailStatus = REMOVE_TAIL_OK;
    }

    // ЗАПРОСЫ
    public TValue? GetTail()
    {
        if (Size == 0)
        {
            GetTailStatus = GET_TAIL_ERR;
            return default(TValue);
        }

        GetTailStatus = GET_TAIL_OK;
        return list.Last();
    }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int RemoveTailStatus { get; private set; } = REMOVE_TAIL_NIL;
    public int GetTailStatus { get; private set; } = GET_TAIL_NIL;
}