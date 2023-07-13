namespace Tetris
{
    internal class Stick : Figure
    {
        public Stick(int x, int y, char sym)
        {
            this.Points[0] = new Point(x, y, sym);
            this.Points[1] = new Point(x, y + 1, sym);
            this.Points[2] = new Point(x, y + 2, sym);
            this.Points[3] = new Point(x, y + 3, sym);

            Draw();
        }

        public override void Rotate(Point[] points)
        {
            if (points[0].X == points[1].X)
            {
                RotateHorizontal(points);
            }
            else
            {
                RotateVertical(points);
            }
        }

        static void RotateHorizontal(Point[] points)
        {
            for (int i = 0; i < points.Length; i++)
            {
                points[i].X = points[0].X + i;
                points[i].Y = points[0].Y;

            }
        }

        static void RotateVertical(Point[] points)
        {
            for (int i = 0; i < points.Length; i++)
            {
                points[i].X = points[0].X;
                points[i].Y = points[0].Y + i;
            }
        }
    }
}