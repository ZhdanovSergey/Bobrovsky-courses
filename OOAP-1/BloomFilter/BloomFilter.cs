using OOAP_1.TwoWayList;
using System;
using System.Collections.Generic;
using System.Diagnostics.Metrics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace OOAP_1.BloomFilter;

interface IBloomFilter<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создан пустой фильтр
    abstract static IBloomFilter<TValue> Create();

    // КОМАНДЫ
    // предусловие: фильтр не должен быть переполнен
    // постусловие: новое значение добавлено в фильтр
    void Add(TValue value);
    // постусловие: значения в фильтре сброшены
    void Clear();

    // ЗАПРОСЫ
    bool isValue(TValue value);
    int Size { get; }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    int AddStatus {  get; }
}

class BloomFilter<TValue> : IBloomFilter<TValue>
{
    public const int FILTER_LENGTH = 32;
    public const int MAX_SIZE = 10;

    const int HASH_NUMBER_1 = 17;
    const int HASH_NUMBER_2 = 223;

    const int ADD_NIL = 0; // метод Add еще не вызывался
    const int ADD_OK = 1; // метод Add отработал успешно
    const int ADD_OK_OVERLOAD = 2; // максимальный размер фильтра превышен

    int store = 0;

    // КОНСТРУКТОР
    public static IBloomFilter<TValue> Create() => new BloomFilter<TValue>();

    public void Add(TValue value)
    {
        store |= getHash(value, HASH_NUMBER_1);
        store |= getHash(value, HASH_NUMBER_2);
        Size++;

        if (Size <= MAX_SIZE)
            AddStatus = ADD_OK;
        else
            AddStatus = ADD_OK_OVERLOAD;
    }

    public void Clear()
    {
        store = 0;
        Size = 0;
    }

    // ЗАПРОСЫ
    public int Size { get; private set; } = 0;
    public bool isValue(TValue value)
    {
        var hash1 = getHash(value, HASH_NUMBER_1);
        var hash2 = getHash(value, HASH_NUMBER_2);

        return (store & hash1) != 0 && (store & hash2) != 0;
    }

    // ДОПОЛНИТЕЛЬНЫЕ ЗАПРОСЫ
    public int AddStatus { get; private set; } = ADD_NIL;

    int getHash(TValue value, int hashNumber)
    {
        var defaultHash = value.GetHashCode();
        var resultHash = 0;

        while (defaultHash > 0)
        {
            resultHash = (resultHash * hashNumber + defaultHash % 10) % FILTER_LENGTH;
            defaultHash /= 10;
        }

        return 1 << resultHash;
    }
}
