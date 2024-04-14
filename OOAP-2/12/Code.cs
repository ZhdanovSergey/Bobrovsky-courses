using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text.Json;

namespace OOAP_2._12;

abstract class General
{
    public void AssignmentAttempt<TTarget>(ref TTarget? target) where TTarget : class
    {
        target = this as TTarget; // присваивает null в случае неудачи
    }
}

abstract class Any : General
{
    // наследует AssignmentAttempt
}