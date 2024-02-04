using OOAP_1.TwoWayList;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1.HashTable;

interface IHashTable<TValue>
{
    // КОНСТРУКТОР
    abstract static IHashTable<TValue> Create(int maxSize);

    // КОМАНДЫ
    // постусловие: если не возникло неразрешимых коллизий, в таблицу добавлено значение
    void Add(TValue value);

    // предусловие: в таблице существует переданное значение
    // постусловие: переданное значение удалено из таблицы
    void Remove(TValue value);

    // ЗАПРОСЫ
    bool Contains(TValue value);
    int MaxSize { get; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int AddStatus { get; }
    int RemoveStatus { get; }
}

class HashTable<TValue> : IHashTable<TValue>
{
    public const int STEP = 3;
    readonly TValue?[] slots;

    public const int ADD_NIL = 0; // Add() ещё не вызывалась
    public const int ADD_OK = 1; // последняя Add() отработала нормально
    public const int ADD_ERR = 2; // неразрешимая коллизия

    public const int REMOVE_NIL = 0; // Remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя Remove() отработала нормально
    public const int REMOVE_ERR = 2; // переданного значения не существует

    // КОНСТРУКТОР
    public static IHashTable<TValue> Create(int maxSize) => new HashTable<TValue>(maxSize);

    // КОМАНДЫ
    public void Add(TValue value)
    {
        foreach (var index in GetSlotsIterator(value))
        {
            if (slots[index].Equals(default(TValue)))
            {
                slots[index] = value;
                AddStatus = ADD_OK;
                return;
            }
        }

        AddStatus = ADD_ERR;
    }
    public void Remove(TValue value)
    {
        foreach (var index in GetSlotsIterator(value))
        {
            if (slots[index].Equals(value))
            {
                slots[index] = default(TValue);
                RemoveStatus = REMOVE_OK;
                return;
            }
        }

        RemoveStatus = REMOVE_ERR;
    }

    // ЗАПРОСЫ
    public int MaxSize { get => slots.Length; }

    public bool Contains(TValue value) =>
        GetSlotsIterator(value)
            .Select(index => slots[index])
            .Contains(value);

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int AddStatus { get; private set; } = ADD_NIL;
    public int RemoveStatus { get; private set; } = REMOVE_NIL;

    HashTable(int maxSize)
    {
        if (maxSize % STEP == 0)
            throw new Exception($"{nameof(maxSize)} should not be divisible by {STEP}");

        slots = new TValue[maxSize];
    }

    IEnumerable<int> GetSlotsIterator(TValue value)
    {
        var initIndex = value.GetHashCode() / MaxSize;
        var index = initIndex;

        do
        {
            yield return index;
            index = (index + STEP) % MaxSize;

        } while (index != initIndex);
    }
}