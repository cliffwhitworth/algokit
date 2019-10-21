using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Algokit
{
    class Program
    {
        static void Main(string[] args)
        {
            // string s = "Hello World!";
            // StringReversal(s);
            // CharMapper(s);
            int[] arr = new int[]{1, 2, 3, 4, 5, 6, 7};
            int size = 2;
            ArraySlicer(arr, size);
            // string a1 = "Eleven plus two";
            // string a2 = "Twelve plus one";
            // Console.WriteLine(Anagrams(a1) == Anagrams(a2));
        }

        private static void StringReversal(string s) 
        {
            char[] arr = s.ToCharArray();
            Array.Reverse(arr);
            Console.WriteLine(new string(arr));
        }

        private static void CharMapper(string s) 
        {
            Dictionary<char, int> charmap = new Dictionary<char, int>();
            foreach (char c in s)
            {
                if (charmap.ContainsKey(c))
                {
                    charmap[c]++;
                }
                else
                {
                    charmap.Add(c, 1);
                }
            }

            char maxchar = new Char();
            int max = 0;
            foreach (KeyValuePair<char, int> el in charmap) {
                if (el.Value > max)
                {
                    maxchar = el.Key;
                    max = el.Value;
                }
            }

            Console.WriteLine("Maxchar = {0}", maxchar);
        }

        private static void ArraySlicer(int[] arr, int s)
        {
            // need list for slices (not using c# 8)
            List<int> lst = new List<int>(arr);
            // use t as the size of the slices[][] array
            int t = arr.Length / s;
            if (arr.Length % s != 0)
            {
                t = (int)(arr.Length / s) + 1;
            }

            int[][] slices = new int[t][];
            int index = 0;
            for (int i = 0; i < slices.Length; i++)
            {
                if(i < slices.Length - 1)
                {
                    slices[i] = lst.GetRange(index,s).ToArray();
                    index += s;
                }
                else
                {
                    slices[i] = lst.GetRange(index,arr.Length%s).ToArray();
                }
            }

            for (int i = 0; i < slices.Length; i++)
            {
                Console.Write("[ ");
                for (int j = 0; j < slices[i].Length; j++)
                {
                    Console.Write("{0} ", slices[i][j]);
                }
                Console.Write("] ");
            }
        }

        private static String Anagrams(string s) 
        {
            // Console.WriteLine(Regex.Replace(s, @"s", ""));
            char[] arr = Regex.Replace(s.ToLower(), @"\s+", "").ToCharArray();
            Array.Sort(arr);
            Console.WriteLine(new string(arr));
            return new string(arr);
        }
    }
}
