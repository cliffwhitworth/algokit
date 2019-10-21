using System;
using System.Collections.Generic;

namespace Algokit
{
    class Program
    {
        static void Main(string[] args)
        {
            string s = "Hello World!";
            CharMapper(s);
        }

        private static void StringReversal(string s) 
        {
            char[] arr = s.ToCharArray();
            Array.Reverse(arr);
            Console.WriteLine(new string(arr));
        }

        private static void CharMapper(string s) 
        {
            // char[] arr = s.ToCharArray();
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
    }
}
