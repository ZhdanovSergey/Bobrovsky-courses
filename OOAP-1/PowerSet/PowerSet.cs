using OOAP_1.HashTable;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_1.PowerSet;

interface IPowerSet<TValue> : IHashTable<TValue>
{
    // КОНСТРУКТОР
    // постусловие: создано пустое множество
    new abstract static IPowerSet<TValue> Create(int maxSize);

    // КОМАНДЫ
    // предусловие: в множестве нет переданного значения и есть свободный слот
    // постусловие: переданное значение добавлено в множество
    // void Add(TValue value);

    // ЗАПРОСЫ
    IPowerSet<TValue> Intersection(IPowerSet<TValue> powerSet);
    IPowerSet<TValue> Union(IPowerSet<TValue> powerSet);
    IPowerSet<TValue> Difference(IPowerSet<TValue> powerSet);
    bool IsSubset(IPowerSet<TValue> powerSet);
}

class PowerSet<TValue> : HashTable<TValue>, IPowerSet<TValue>
{
    public const int ADD_ERR_DUPLICATE = 3; // переданное значение уже есть в множестве
    // КОНСТРУКТОР
    public new static IPowerSet<TValue> Create(int maxSize) => new PowerSet<TValue>(maxSize);

    // КОМАНДЫ
    public new void Add(TValue value)
    {
        if (this.Contains(value))
        {
            AddStatus = ADD_ERR_DUPLICATE;
            return;
        }

        base.Add(value);
    }

    // ЗАПРОСЫ
    public IPowerSet<TValue> Intersection(IPowerSet<TValue> paramSet)
    {
        var result = new PowerSet<TValue>(Math.Min(MaxSize, paramSet.MaxSize));

        foreach (var thisValue in this)
            if (paramSet.Contains(thisValue))
                result.Add(thisValue);

        return result;
    }
    public IPowerSet<TValue> Union(IPowerSet<TValue> paramSet)
    {
        var result = new PowerSet<TValue>(MaxSize + paramSet.MaxSize);

        foreach (var thisValue in this)
            result.Add(thisValue);

        foreach (var paramValue in paramSet)
            result.Add(paramValue);

        return result;
    }
    public IPowerSet<TValue> Difference(IPowerSet<TValue> paramSet)
    {
        var result = new PowerSet<TValue>(MaxSize);

        foreach (var thisValue in this)
            if (!paramSet.Contains(thisValue))
                result.Add(thisValue);

        return result;
    }

    public bool IsSubset(IPowerSet<TValue> paramSet)
    {
        foreach (var paramValue in paramSet)
            if (!this.Contains(paramValue))
                return false;

        return true;
    }

    PowerSet(int maxSize) : base(maxSize) {}
}
