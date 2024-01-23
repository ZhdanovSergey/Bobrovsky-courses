using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace OOAP_1.DynArray;

internal interface IDynArray<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создан пустой массив с заданным размером буфера
    abstract static IDynArray<TValue> Create(int capacity);

    // КОМАНДЫ

    // постусловие: в конец массива добавлен элемент,
    // Count увеличивается на 1
    // если Count >= Capacity, Capacity увеличивается
    void Append(TValue value);

    // предусловие: index <= Count
    // постусловие: в позицию index вставлен элемент, все последующие элементы сдвинуты вправо
    //   Count увеличивается на 1
    //   если Count >= Capacity, Capacity увеличивается
    void Insert(TValue value, int index);

    // предусловие: index < Count
    // постусловие: из позиции index удален элемент, все поледующие элементы сдвинуты влево
    //   Count уменьшается на 1
    //   если Count < Capacity / 2, Capacity уменьшается (но не меньше минимальной)
    void Remove(int index);

    // ЗАПРОСЫ

    // предусловие: index < Count
    TValue? GetItem(int index);
    int Count { get; }
    int Capacity { get; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ

    int InsertStatus { get; }
    int RemoveStatus { get; }
    int GetItemStatus { get; }
}

class DynArray<TValue> : IDynArray<TValue>
{
    const int MIN_CAPACITY = 16;
    const float MIN_FILLING_RATE = 0.5f;
    const int CAPACITY_INCREASE_FACTOR = 2;
    const float CAPACITY_DECREASE_FACTOR = 1.5f;
    TValue[] _array = new TValue[MIN_CAPACITY];

    public const int INSERT_NIL = 0;
    public const int INSERT_OK = 1;
    public const int INSERT_ERR = 2;

    public const int REMOVE_NIL = 0;
    public const int REMOVE_OK = 1;
    public const int REMOVE_ERR = 2;

    public const int GET_ITEM_NIL = 0;
    public const int GET_ITEM_OK = 1;
    public const int GET_ITEM_ERR = 2;

    // КОНСТРУКТОР
    public static IDynArray<TValue> Create(int capacity = MIN_CAPACITY)
    {
        return new DynArray<TValue>(capacity);
    }

    // КОМАНДЫ
    public void Append(TValue value)
    {
        if (Count >= Capacity)
            IncreaseCapacity();

        _array[Count] = value;
        Count++;
    }
    public void Insert(TValue value, int index)
    {
        if (index > Count)
        {
            InsertStatus = INSERT_ERR;
            return;
        }

        if (Count >= Capacity)
            IncreaseCapacity();

        Array.Copy(_array, index, _array, index + 1, Count - index);
        _array[index] = value;
        Count++;
        InsertStatus = INSERT_OK;
    }
    public void Remove(int index)
    {

        if (index >= Count)
        {
            RemoveStatus = REMOVE_ERR;
            return;
        }

        Array.Copy(_array, index + 1, _array, index, Count - index - 1);
        Count--;

        if (Count < Capacity * MIN_FILLING_RATE)
            DecreaseCapacity();

        RemoveStatus = REMOVE_OK;
    }

    // ЗАПРОСЫ

    public TValue? GetItem(int index)
    {
        if (index >= Count)
        {
            GetItemStatus = GET_ITEM_ERR;
            return default(TValue);
        }

        GetItemStatus = GET_ITEM_OK;
        return _array[index];
    }
    public int Count { get; private set; } = 0;
    public int Capacity
    {
        get => _array.Length;
    }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int InsertStatus { get; private set; } = INSERT_NIL;
    public int RemoveStatus { get; private set; } = REMOVE_NIL;
    public int GetItemStatus { get; private set; } = GET_ITEM_NIL;

    DynArray(int capacity)
    {
        if (capacity < MIN_CAPACITY)
            throw new ArgumentOutOfRangeException($"{nameof(capacity)} should be more or equal {MIN_CAPACITY}");

        _array = new TValue[capacity];
    }

    void IncreaseCapacity()
    {
        var increasedCapacity = Capacity * CAPACITY_INCREASE_FACTOR;
        Array.Resize(ref _array, increasedCapacity);
    }
    void DecreaseCapacity()
    {
        var decreasedCapacity = (int)(Capacity / CAPACITY_DECREASE_FACTOR);
        var guardedDecreasedCapacity = decreasedCapacity < MIN_CAPACITY ? MIN_CAPACITY : decreasedCapacity;
        Array.Resize(ref _array, guardedDecreasedCapacity);
    }
}