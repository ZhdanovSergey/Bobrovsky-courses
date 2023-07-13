using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Tetris
{
    internal static class Field
    {
        private static int _width = 40;
        private static int _height = 30;
        private static readonly bool[,] _heap = new bool[Height, Width];

        public static int Width
        {
            get
            {
                return _width;
            }
            set
            {
                _width = value;
                SetConsoleSize();
            }
        }

        public static int Height
        {
            get
            {
                return _height;
            }
            set
            {
                _height = value;
                SetConsoleSize();
            }
        }

        public static void AddFigure(Figure fig)
        {
            foreach (var p in fig.Points)
            {
                _heap[p.Y, p.X] = true;
            }
        }

        public static bool CheckStrike(Point p)
        {
            return _heap[p.Y, p.X];
        }

        public static void SetConsoleSize()
        {         
            Console.SetWindowSize(Width, Height);
            Console.SetBufferSize(Width, Height);
        }
    }
}
