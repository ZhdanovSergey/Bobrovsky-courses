using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1.NativeDictionary;

interface INativeDictionary<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создан пустой словарь
    abstract static INativeDictionary<TValue> Create(int maxSize);

    // КОМАНДЫ
    // предусловие: в словаре нет указанного ключа и есть свободный слот
    // постусловие: в словарь добавлена пара ключ-значение
    void Add(string key, TValue value);

    // предусловие: в словаре существует указанный ключ
    // постусловие: соответствующая пара ключ-значение удалены из словаря
    void Remove(string key);

    // ЗАПРОСЫ
    // предусловие: в словаре есть указанный ключ
    TValue? Get(string key);
    bool ContainsKey(string key);
    int Size { get; }
    int MaxSize { get; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int AddStatus { get; }
    int RemoveStatus { get; }
    int GetStatus {  get; }
}

class NativeDictionary<TValue> : INativeDictionary<TValue>
{
    readonly string?[] keys;
    readonly TValue?[] values;

    public const int STEP = 3;

    public const int ADD_NIL = 0; // Add() ещё не вызывалась
    public const int ADD_OK = 1; // последняя Add() отработала нормально
    public const int ADD_ERR_KEY_EXIST = 2; // указанный ключ уже существует
    public const int ADD_ERR_FULL = 3; // нет свободных слотов

    public const int REMOVE_NIL = 0; // Remove() ещё не вызывалась
    public const int REMOVE_OK = 1; // последняя Remove() отработала нормально
    public const int REMOVE_ERR = 2; // переданного ключа не существует

    public const int GET_NIL = 0; // Get() ещё не вызывалась
    public const int GET_OK = 1; // последняя Get() отработала нормально
    public const int GET_ERR = 2; // переданного ключа не существует

    // КОНСТРУКТОР
    public static INativeDictionary<TValue> Create(int maxSize) => new NativeDictionary<TValue>(maxSize);

    // КОМАНДЫ
    public void Add(string key, TValue value)
    {
        if (Size == MaxSize)
        {
            AddStatus = ADD_ERR_FULL;
            return;
        }

        foreach (var index in GetSlotsIterator(key))
        {
            if (keys[index] == key)
            {
                AddStatus = ADD_ERR_KEY_EXIST;
                return;
            }

            if (keys[index] is null)
            {
                keys[index] = key;
                values[index] = value;
                Size++;
                AddStatus = ADD_OK;
                return;
            }
        }
    }
    public void Remove(string key)
    {
        foreach (var index in GetSlotsIterator(key))
        {
            if (keys[index] == key)
            {
                keys[index] = null;
                values[index] = default(TValue);
                Size--;
                RemoveStatus = REMOVE_OK;
                return;
            }
        }

        RemoveStatus = REMOVE_ERR;
    }

    // ЗАПРОСЫ
    public TValue? Get(string key)
    {
        foreach (var index in GetSlotsIterator(key))
        {
            if (keys[index] == key)
            {
                GetStatus = GET_OK;
                return values[index];
            }
        }

        GetStatus = GET_ERR;
        return default(TValue);
    }
    public bool ContainsKey(string key)
    {
        foreach (var index in GetSlotsIterator(key))
        {
            if (keys[index] == key)
                return true;
        }

        return false;
    }
    public int Size { get; private set; }
    public int MaxSize { get => keys.Length; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int AddStatus { get; private set; } = ADD_NIL;
    public int RemoveStatus { get; private set; } = REMOVE_NIL;
    public int GetStatus { get; private set; } = GET_NIL;

    NativeDictionary (int maxSize)
    {
        if (maxSize % STEP == 0)
            throw new Exception($"{nameof(maxSize)} should not be divisible by {STEP}");

        keys = new string?[maxSize];
        values = new TValue?[maxSize];
    }

    IEnumerable<int> GetSlotsIterator(string key)
    {
        var initIndex = key.GetHashCode() / MaxSize;
        var index = initIndex;

        do
        {
            yield return index;
            index = (index + STEP) % MaxSize;

        } while (index != initIndex);
    }
}