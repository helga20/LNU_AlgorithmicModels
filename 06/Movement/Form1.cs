using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Movement
{
    public partial class Form1 : Form
    {
        bool isBarriers; //змінна, яка визначає, чи є перешкоди на полі
        Plane plane; //об'єкт, що описує рух і перешкоди
        public Form1()
        {
            InitializeComponent();
            plane = new Plane();
        }

        //зчитування даних з файлу та малювання поля з перешкодами
        private void button1_Click(object sender, EventArgs e)
        {
            isBarriers = true; //встановлюємо, що є перешкоди
            Graphics g = pictureBox1.CreateGraphics();
            Pen pen = new Pen(Color.Black, 1);
            //зчитування даних з файлу plane.txt
            using (StreamReader streamReader = new StreamReader(@"plane.txt"))
            {
                //читання розмірів поля
                plane.SizeX = Convert.ToInt32(streamReader.ReadLine().Split(' ')[1]);
                plane.SizeY = Convert.ToInt32(streamReader.ReadLine().Split(' ')[1]);

                //читання початкової точки
                var start = streamReader.ReadLine().Replace("Start:[", "").Replace(";", " ").Replace("]", "").Split(' ');
                plane.StartPoint = new Barrier(Convert.ToInt32(start[0]), Convert.ToInt32(start[1]));
                plane.CurrentPoint = new Barrier(Convert.ToInt32(start[0]), Convert.ToInt32(start[1]));

                //читання кінцевої точки
                var end = streamReader.ReadLine().Replace("End:[", "").Replace(";", " ").Replace("]", "").Split(' ');
                plane.EndPoint = new Barrier(Convert.ToInt32(end[0]), Convert.ToInt32(end[1]));

                //читання перешкод
                var lines = streamReader.ReadToEnd().Replace("[", "").Replace(";", " ").Replace("]", "").Split('\n');
                for (int i = 0; i < lines.Length; i++)
                {
                    var line = lines[i].Split(' ');
                    plane.barriers.Add(new Barrier(Convert.ToInt32(line[0]), Convert.ToInt32(line[1])));
                }
            }

            //малювання сітки на полі
            for (int i = 1; i <= plane.SizeY; i++)
            {
                for (int j = 1; j <= plane.SizeX; j++)
                {
                    g.DrawRectangle(pen, j * 20, i * 20, 20, 20);
                }
            }

            //малювання стартової точки (зеленим кольором)
            SolidBrush startBrush = new SolidBrush(Color.Green);
            g.FillRectangle(startBrush, plane.StartPoint.X * 20, (plane.SizeY - plane.StartPoint.Y + 1) * 20, 20, 20);

            //малювання кінцевої точки (червоним кольором)
            SolidBrush endBrush = new SolidBrush(Color.Red);
            g.FillRectangle(endBrush, plane.EndPoint.X * 20, (plane.SizeY - plane.EndPoint.Y + 1) * 20, 20, 20);

            //малювання перешкод (сірим кольором)
            SolidBrush barrierBrush = new SolidBrush(Color.Gray);
            for (int i = 0; i < plane.barriers.Count; i++)
            {
                g.FillRectangle(barrierBrush, plane.barriers[i].X * 20, (plane.SizeY - plane.barriers[i].Y + 1) * 20, 20, 20);
            }
        }

        //зчитування даних з файлу planeEmpty.txt та малювання поля без перешкод
        private void button2_Click(object sender, EventArgs e)
        {
            isBarriers = false; //встановлюємо, що немає перешкод
            Graphics g = pictureBox1.CreateGraphics(); 
            Pen pen = new Pen(Color.Black, 1); 

            //зчитування даних з файлу planeEmpty.txt
            using (StreamReader streamReader = new StreamReader(@"planeEmpty.txt"))
            {
                //читання розмірів поля
                plane.SizeX = Convert.ToInt32(streamReader.ReadLine().Split(' ')[1]);
                plane.SizeY = Convert.ToInt32(streamReader.ReadLine().Split(' ')[1]);

                //читання початкової точки
                var start = streamReader.ReadLine().Replace("Start:[", "").Replace(";", " ").Replace("]", "").Split(' ');
                plane.StartPoint = new Barrier(Convert.ToInt32(start[0]), Convert.ToInt32(start[1]));
                plane.CurrentPoint = new Barrier(Convert.ToInt32(start[0]), Convert.ToInt32(start[1]));

                //читання кінцевої точки
                var end = streamReader.ReadLine().Replace("End:[", "").Replace(";", " ").Replace("]", "").Split(' ');
                plane.EndPoint = new Barrier(Convert.ToInt32(end[0]), Convert.ToInt32(end[1]));
                var lines = streamReader.ReadToEnd().Replace("[", "").Replace(";", " ").Replace("]", "").Split('\n');

            }

            //малювання сітки на полі
            for (int i = 1; i <= plane.SizeY; i++)
            {
                for (int j = 1; j <= plane.SizeX; j++)
                {
                    g.DrawRectangle(pen, j * 20, i * 20, 20, 20);
                }
            }

            //малювання стартової точки (зеленим кольором)
            SolidBrush startBrush = new SolidBrush(Color.Green);
            g.FillRectangle(startBrush, plane.StartPoint.X * 20, (plane.SizeY - plane.StartPoint.Y + 1) * 20, 20, 20);

            //малювання кінцевої точки (червоним кольором)
            SolidBrush endBrush = new SolidBrush(Color.Red);
            g.FillRectangle(endBrush, plane.EndPoint.X * 20, (plane.SizeY - plane.EndPoint.Y + 1) * 20, 20, 20);
        }

        //рух за перешкодами або без них
        private void button3_Click(object sender, EventArgs e)
        {
            //якщо є перешкоди
            if (isBarriers)
            {
                Barrier barrier = plane.Move(); //викликаємо метод руху з перешкодами
                Graphics g = pictureBox1.CreateGraphics();
                Pen pen = new Pen(Color.Black, 1);
                SolidBrush startBrush = new SolidBrush(Color.Green);

                //якщо рух завершено (досягнуто кінцевої точки)
                if (barrier == null)
                {
                    MessageBox.Show("Кінець. Вітаю!"); //вивести повідомлення
                    g.FillRectangle(startBrush, plane.EndPoint.X * 20, (plane.SizeY - plane.EndPoint.Y + 1) * 20, 20, 20);

                }
                else
                {
                    //вивести нові координати поточної точки
                    textBox1.Text = barrier.X.ToString();
                    textBox2.Text = barrier.Y.ToString();
                    richTextBox1.Text += plane.Text + "\n";
                    g.FillRectangle(startBrush, barrier.X * 20, (plane.SizeY - barrier.Y + 1) * 20, 20, 20);
                }
            }
            //якщо немає перешкод
            else
            {
                Barrier barrier = plane.MoveWithoutBarrier(); //викликаємо метод руху без перешкод
                Graphics g = pictureBox1.CreateGraphics();
                Pen pen = new Pen(Color.Black, 1);
                SolidBrush startBrush = new SolidBrush(Color.Green);

                //якщо рух завершено (досягнуто кінцевої точки)
                if (barrier == null)
                {
                    MessageBox.Show("Кінець. Вітаю!"); //вивести повідомлення
                    g.FillRectangle(startBrush, plane.EndPoint.X * 20, (plane.SizeY - plane.EndPoint.Y + 1) * 20, 20, 20);

                }
                else
                {
                    //вивести нові координати поточної точки
                    textBox1.Text = barrier.X.ToString();
                    textBox2.Text = barrier.Y.ToString();
                    richTextBox1.Text += plane.Text + "\n";
                    g.FillRectangle(startBrush, barrier.X * 20, (plane.SizeY - barrier.Y + 1) * 20, 20, 20);
                }
            }
        }
    }
}
