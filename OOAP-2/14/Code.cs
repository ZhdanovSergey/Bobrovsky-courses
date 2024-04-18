using OOAP_2._9;
using System.Collections;
using System.Security.Cryptography.X509Certificates;
using System.Text.Json;

namespace OOAP_2._14;

abstract class Any : General
{
    public abstract Any? Sum(Any? other);
}

class Primitive : Any
{
    public int Value { get; }

    public Primitive(int value)
    {
        Value = value;
    }

    public override Any? Sum(Any? other)
    {
        var primitiveOther = other as Primitive;

        if (primitiveOther is null)
            return null;

        return new Primitive(Value + primitiveOther.Value);
    }
}

class Vector<TValue> : Any, IEnumerable<TValue> where TValue : Any
{
    readonly TValue[] _array;
    public override Any? Sum(Any? other)
    {
        var leftVector = this;
        var rightVector = other as Vector<TValue>;

        if (rightVector is null || leftVector.Length != rightVector.Length)
            return null;

        var result = new TValue[leftVector.Length];

        for (var i = 0; i < leftVector.Length; i++)
        {
            var sum = (leftVector[i].Sum(rightVector[i])) as TValue;

            if (sum is null)
                return null;

            result[i] = sum;
        }

        return new Vector<TValue>(result);
    }

    public Vector(IEnumerable<TValue> values)
    {
        _array = values.ToArray();
    }

    public int Length { get => _array.Length; }

    public TValue this[int index] { get => _array[index]; }

    public IEnumerator<TValue> GetEnumerator() => ((IEnumerable<TValue>) _array).GetEnumerator();
    IEnumerator IEnumerable.GetEnumerator() => _array.GetEnumerator();
}

class Client
{
    public static void Method()
    {
        var vector1 = new Vector<Primitive>(
            Enumerable.Range(0, 3).Select(num => new Primitive(num)));

        var vector2 = new Vector<Vector<Primitive>>(
            Enumerable.Range(0, 3).Select(num => vector1));

        var vector3 = new Vector<Vector<Vector<Primitive>>>(
            Enumerable.Range(0, 3).Select(num => vector2));

        var result1 = vector1.Sum(vector1);
        // [0, 1, 2] + [0, 1, 2] => [0, 2, 4]

        var result2 = vector2.Sum(vector2);
        // [0, 1, 2]   [0, 1, 2]    [0, 2, 4]
        // [0, 1, 2] + [0, 1, 2] => [0, 2, 4]
        // [0, 1, 2]   [0, 1, 2]    [0, 2, 4]

        var result3 = vector3.Sum(vector3);
        // тоже работает корректно, сложно нарисовать :)
    }
}