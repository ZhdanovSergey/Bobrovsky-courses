using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text.Json;

abstract class Any : General {}

abstract class General
{
    public void ShallowCopyTo<TTarget>(ref TTarget target)
    {
        target = (TTarget) MemberwiseClone();
    }

    public void DeepCopyTo<TTarget>(ref TTarget target)
    {
        target = DeepClone<TTarget>();
    }

    public TResult DeepClone<TResult>()
    {
        using var stream = ToMemoryStream();
        var formatter = new BinaryFormatter();

        return (TResult) formatter.Deserialize(stream);
    }

    public bool Equals(General obj) => base.Equals(obj);

    public bool DeepEquals(General obj)
    {
        using var thisStream = ToMemoryStream();
        using var objStream = obj.ToMemoryStream();

        if (thisStream.Length != objStream.Length)
            return false;

        var thisByteArray = thisStream.ToArray();
        var objByteArray = objStream.ToArray();

        return thisByteArray.SequenceEqual(objByteArray);
    }

    public string Serialize() => JsonSerializer.Serialize(this);

    public TResult? Deserialize<TResult>(string json) => JsonSerializer.Deserialize<TResult>(json);

    public string Print() => Serialize();

    public bool CheckType(Type type) => GetType() == type;
    public new Type GetType() => base.GetType();

    private MemoryStream ToMemoryStream()
    {
        var formatter = new BinaryFormatter();
        var stream = new MemoryStream();

        formatter.Serialize(stream, this);
        stream.Position = 0;

        return stream;
    }
}