using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tetris
{
    abstract class Figure
    {
        static readonly int LENGHT = 4;
        public Point[] Points = new Point[LENGHT];

        abstract public void Rotate(Point[] points);

        internal Result TryMove(Direction dir)
        {
            Hide();

            var clone = Clone();
            Move(clone, dir);

            var result = VerifyPosition(clone);

            if (result == Result.SUCCESS)
                Points = clone;

            Draw();

            return result;
        }

        internal Result TryRotate()
        {
            Hide();

            var clone = Clone();
            Rotate(clone);

            var result = VerifyPosition(clone);

            if (result == Result.SUCCESS)
                Points = clone;

            Draw();

            return result;
        }

        private void Hide()
        {
            foreach (Point p in Points)
            {
                p.Hide();
            }
        }

        private Point[] Clone()
        {
            Point[] clone = new Point[LENGHT];

            for (int i = 0; i < LENGHT; i++)
            {
                clone[i] = new Point(Points[i]);
            }

            return clone;
        }

        private static void Move(Point[] points, Direction dir)
        {
            foreach (Point p in points)
            {
                p.Move(dir);
            }
        }

        private static Result VerifyPosition(Point[] points)
        {
            foreach (var p in points)
            {
                if (Field.CheckStrike(p) || p.Y >= Field.Height)
                {
                    return Result.HEAP_STRIKE;
                }

                if (p.X < 0 || p.X >= Field.Width || p.Y < 0)
                {
                    return Result.BORDER_STRIKE;
                }
            }

            return Result.SUCCESS;
        }

        protected void Draw()
        {
            foreach (Point p in Points)
            {
                p.Draw();
            }
        }
    }
}
