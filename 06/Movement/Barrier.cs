using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Movement
{
    public class Barrier
    {
        public int X { get; set; }
        public int Y { get; set; }
        public Barrier(int x, int y)
        {
            X = x;
            Y = y;
        }
    }
}
