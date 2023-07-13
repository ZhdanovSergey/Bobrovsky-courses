using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tetris
{
    internal class Point
    {
        public int X { get; set; }
        public int Y { get; set; }
        public char C { get; set; }

        public Point(int x, int y, char c)
        {
            this.X = x;
            this.Y = y;
            this.C = c;
        }

        public Point(Point p)
        {
            this.X = p.X;
            this.Y = p.Y;
            this.C = p.C;
        }
        public void Draw()
        {
            Console.SetCursorPosition(X, Y);
            Console.Write(C);
            Console.SetCursorPosition(0, 0);
        }

        public void Hide()
        {
            Console.SetCursorPosition(X, Y);
            Console.Write(" ");
        }

        public void Move(Direction dir)
        {
            switch (dir)
            {
                case Direction.LEFT:
                    this.X -= 1; break;

                case Direction.RIGHT:
                    this.X += 1; break;

                case Direction.DOWN:
                    this.Y += 1; break;
            }
        }
    }
}
