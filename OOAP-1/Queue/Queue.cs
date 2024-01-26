using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata.Ecma335;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1.Queue;

interface IQueue<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создана пустая очередь
    static abstract IQueue<TValue> Create(int maxSize);

    // КОМАНДЫ
    // предусловие: очередь не заполнена полностью
    // постусловие: значение добавлено в хвост очереди
    void Enqueue(TValue value);

    // предусловие: очередь не пустая
    // постусловие: значение удалено из головы очереди
    void Dequeue();

    // постусловие: все значения удалены
    void Clear();

    // ЗАПРОСЫ
    // предусловие: очередь не пустая
    TValue? Head();
    int Size { get; }
    int MaxSize { get; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int EnqueueStatus { get; }
    int DequeueStatus { get; }
    int HeadStatus { get; }
}

class Queue<TValue> : IQueue<TValue>
{
    readonly TValue?[] array;
    int _headIndex = 0;
    int _tailIndex = 0;
    int headIndex { get => _headIndex; set { _headIndex = value % MaxSize; } }
    int tailIndex { get => _tailIndex; set { _tailIndex = value % MaxSize; } }

    public const int ENQUEUE_NIL = 0;
    public const int ENQUEUE_OK = 1;
    public const int ENQUEUE_ERR = 2;

    public const int DEQUEUE_NIL = 0;
    public const int DEQUEUE_OK = 1;
    public const int DEQUEUE_ERR = 2;

    public const int HEAD_NIL = 0;
    public const int HEAD_OK = 1;
    public const int HEAD_ERR = 2;

    // КОНСТРУКТОР
    public static IQueue<TValue> Create(int maxSize) =>
        new Queue<TValue>(maxSize);

    // КОМАНДЫ
    public void Enqueue(TValue value)
    {
        if (Size == MaxSize)
        {
            EnqueueStatus = ENQUEUE_ERR;
            return;
        }

        array[tailIndex] = value;
        tailIndex++;
        EnqueueStatus = ENQUEUE_OK;
    }
    public void Dequeue()
    {
        if (Size == 0)
        {
            DequeueStatus = DEQUEUE_ERR;
            return;
        }

        array[headIndex] = default;
        headIndex++;
        DequeueStatus = DEQUEUE_OK;
    }
    public void Clear()
    {
        Array.Clear(array, 0, MaxSize);
        headIndex = 0;
        tailIndex = 0;
    }

    // ЗАПРОСЫ
    public TValue? Head()
    {
        if (Size == 0)
        {
            HeadStatus = HEAD_ERR;
            return default;
        }

        HeadStatus = HEAD_OK;
        return array[headIndex];
    }
    public int Size { get => (tailIndex - headIndex + MaxSize) % MaxSize; }
    public int MaxSize { get => array.Length; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int EnqueueStatus { get; private set; } = ENQUEUE_NIL;
    public int DequeueStatus { get; private set; } = DEQUEUE_NIL;
    public int HeadStatus { get; private set; } = HEAD_NIL;
    Queue(int maxSize) => array = new TValue[maxSize];
}