using System.Reflection.Emit;

namespace Tetris
{
    internal class Program
    {

        static readonly FigureGenerator generator = new(20, 0, '*');
        static void Main()
        {
            Field.SetConsoleSize();
            var figure = generator.GenerateFigure();

            while (true)
            {
                if (Console.KeyAvailable)
                {
                    var keyInfo = Console.ReadKey();
                    var result = HandleKey(figure, keyInfo);
                    ProcessResult(result, ref figure);
                }
            }
        }

        private static void ProcessResult(Result result, ref Figure figure)
        {
            if (result == Result.HEAP_STRIKE)
            {
                Field.AddFigure(figure);
                figure = generator.GenerateFigure();
            }
        }

        private static Result HandleKey(Figure figure, ConsoleKeyInfo keyInfo) => keyInfo.Key switch
        {
            ConsoleKey.LeftArrow => figure.TryMove(Direction.LEFT),
            ConsoleKey.RightArrow => figure.TryMove(Direction.RIGHT),
            ConsoleKey.DownArrow => figure.TryMove(Direction.DOWN),
            ConsoleKey.Spacebar => figure.TryRotate(),
            _ => Result.SUCCESS,
        };
    }
}