using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Movement
{
    public class Plane
    {
        public int SizeX { get; set; } //розмір площини по осі X
        public int SizeY { get; set; } //розмір площини по осі Y
        public List<Barrier> barriers { get; set; } //список перешкод на площині
        public Barrier StartPoint { get; set; } //початкова точка
        public Barrier EndPoint { get; set; } //кінцева точка
        public Barrier CurrentPoint { get; set; } //поточна позиція
        public string Text { get; set; } //опис руху
        public Plane() 
        {
            barriers = new List<Barrier>();
        }
        //перевірка, чи є вільне місце в координатах (x, y)
        public bool IsEmpty(int x, int y)
        {
            Barrier barrier = new Barrier(x, y);
            return !barriers.Exists(b => b.X == x && b.Y == y);
        }
        //завдання 3
        //рух по площині без перешкод
        public Barrier MoveWithoutBarrier()
        {
            if (EndPoint.X == CurrentPoint.X)
            {
                if (EndPoint.Y == CurrentPoint.Y)
                {
                    //кінцева точка досягнута
                    return null;
                }
                else
                {
                    //рух по осі Y
                    if (EndPoint.Y > CurrentPoint.Y)
                    {
                        CurrentPoint.Y++;
                        Text = "Поворот на 90 градусів ліворуч, рух на одну клітинку";
                        return CurrentPoint;
                    }
                    else
                    {
                        CurrentPoint.Y--;
                        Text = "Поворот на 90 градусів праворуч, рух на одну клітинку";
                        return CurrentPoint;
                    }
                }
            }
            else
            {
                //рух по осі X або діагонально
                if ((EndPoint.X - CurrentPoint.X) >= Math.Abs(EndPoint.Y - CurrentPoint.Y))
                {
                    CurrentPoint.X++;
                    Text = "Рух прямо на одну клітинку";
                    return CurrentPoint;
                }
                else
                {
                    //діагональний рух
                    if (EndPoint.Y < CurrentPoint.Y)
                    {
                        CurrentPoint.X++;
                        CurrentPoint.Y--;
                        Text = "Поворот на 45 градусів праворуч, рух на одну клітинку";
                        return CurrentPoint;
                    }
                    else
                    {
                        CurrentPoint.X++;
                        CurrentPoint.Y++;
                        Text = "Поворот на 45 градусів ліворуч, рух на одну клітинку";
                        return CurrentPoint;
                    }
                }
            }

        }

        //рух з обходом перешкод
        public Barrier Move()
        {
            if (EndPoint.X == CurrentPoint.X)
            {
                if (EndPoint.Y == CurrentPoint.Y)
                {
                    //кінцева точка досягнута
                    return null;
                }
                else
                {
                    //рух по осі Y з перевіркою перешкод
                    if (EndPoint.Y > CurrentPoint.Y)
                    {
                        if (IsEmpty(CurrentPoint.X, CurrentPoint.Y + 1))
                        {
                            CurrentPoint.Y++;
                            Text = "Поворот на 90 градусів ліворуч, рух на одну клітинку";
                            return CurrentPoint;
                        }
                        else
                        {
                            CurrentPoint.Y--;
                            CurrentPoint.X--;
                            Text = "Поворот на 135 градусів праворуч, рух на одну клітинку";
                            return CurrentPoint;
                        }
                    }
                    else
                    {
                        if (IsEmpty(CurrentPoint.X, CurrentPoint.Y - 1))
                        {
                            CurrentPoint.Y--;
                            Text = "Поворот на 90 градусів праворуч, рух на одну клітинку";
                            return CurrentPoint;
                        }
                        else
                        {
                            CurrentPoint.Y--;
                            CurrentPoint.X--;
                            Text = "Поворот на 135 градусів праворуч, рух на одну клітинку";
                            return CurrentPoint;
                        }
                    }
                }
            }
            else
            {
                //рух по осі X або діагонально з перевіркою перешкод
                if ((EndPoint.X - CurrentPoint.X) >= Math.Abs(EndPoint.Y - CurrentPoint.Y) && IsEmpty(CurrentPoint.X + 1, CurrentPoint.Y))
                {
                    CurrentPoint.X++;
                    Text = "Рух прямо на одну клітинку";
                    return CurrentPoint;
                }
                else
                {
                    if (CurrentPoint.Y < EndPoint.Y)
                    {
                        //діагональний рух вгору
                        if (IsEmpty(CurrentPoint.X + 1, CurrentPoint.Y + 1))
                        {
                            CurrentPoint.X++;
                            CurrentPoint.Y++;
                            Text = "Поворот на 45 градусів ліворуч, рух на одну клітинку";
                            return CurrentPoint;
                        }
                        else
                        {
                            if (IsEmpty(CurrentPoint.X + 1, CurrentPoint.Y))
                            {
                                CurrentPoint.X++;
                                Text = "Рух прямо на одну клітинку";
                                return CurrentPoint;
                            }
                            else
                            {
                                //рух в інші напрямки при наявності перешкод
                                if (IsEmpty(CurrentPoint.X, CurrentPoint.Y + 1))
                                {
                                    CurrentPoint.Y++;
                                    Text = "Поворот на 90 градусів ліворуч, рух на одну клітинку";
                                    return CurrentPoint;
                                }
                                else
                                {
                                    if (IsEmpty(CurrentPoint.X, CurrentPoint.Y - 1))
                                    {
                                        CurrentPoint.Y--;
                                        Text = "Поворот на 90 градусів праворуч, рух на одну клітинку";
                                        return CurrentPoint;
                                    }
                                    else
                                    {
                                        CurrentPoint.Y--;
                                        CurrentPoint.X--;
                                        Text = "Поворот на 135 градусів праворуч, рух на одну клітинку";
                                        return CurrentPoint;
                                    }
                                }
                            }
                        }
                    }
                    else
                    {
                        //діагональний рух вниз
                        if (IsEmpty(CurrentPoint.X + 1, CurrentPoint.Y - 1))
                        {
                            CurrentPoint.X++;
                            CurrentPoint.Y--;
                            Text = "Поворот на 45 градусів праворуч, рух на одну клітинку";
                            return CurrentPoint;
                        }
                        else
                        {
                            if (IsEmpty(CurrentPoint.X + 1, CurrentPoint.Y))
                            {
                                CurrentPoint.X++;
                                Text = "Рух прямо на одну клітинку";
                                return CurrentPoint;
                            }
                            else
                            {
                                //рух в інші напрямки при наявності перешкод
                                if (IsEmpty(CurrentPoint.X, CurrentPoint.Y - 1))
                                {
                                    CurrentPoint.Y--;
                                    Text = "Поворот на 90 градусів праворуч, рух на одну клітинку";
                                    return CurrentPoint;
                                }
                                else
                                {
                                    if (IsEmpty(CurrentPoint.X, CurrentPoint.Y + 1))
                                    {
                                        CurrentPoint.Y++;
                                        Text = "Поворот на 90 градусів ліворуч, рух на одну клітинку";
                                        return CurrentPoint;
                                    }
                                    else
                                    {
                                        CurrentPoint.Y++;
                                        CurrentPoint.X--;
                                        Text = "Поворот на 135 градусів ліворуч, рух на одну клітинку";
                                        return CurrentPoint;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
