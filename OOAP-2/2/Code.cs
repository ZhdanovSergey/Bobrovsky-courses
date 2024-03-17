using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOAP_2._2;

// Я никогда ранее не слышал про наследование как более общий случай класса-родителя,
// в моем понимании такое наследование противоречило бы отношению "is-a".

class Person
{
    public required string Name { get; init; }
}

// уточнение класса Person
class Employee : Person
{
    public required string Profession { get; init; }
}