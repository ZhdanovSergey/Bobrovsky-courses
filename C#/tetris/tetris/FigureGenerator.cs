namespace Tetris
{
    internal class FigureGenerator
    {
        private readonly int x;
        private readonly int y;
        private readonly char c;

        private readonly Random random = new();

        public FigureGenerator(int x, int y, char c)
        {
            this.x = x;
            this.y = y;
            this.c = c;
        }

        public Figure GenerateFigure()
        {
            int r = random.Next(0, 2);

            return r switch
            {
                0 => new Square(x, y, c),
                1 => new Stick(x, y, c),
                _ => throw new Exception($"no figure defined for generated number{r}"),
            };
        }
    }
}