Ans="""

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Constructor_Overloading
{
    class GameScore
    {
        string user;
        int age;
        //Default Constructor
        public GameScore()
        {
            user = "Steven";
            age = 28;
            Console.WriteLine("Previous User {0} and he was {1} year old", user, age);
        }

        //Parameterized Constructor
        public GameScore(string name, int age1)
        {
            user = name;
            age = age1;
            Console.WriteLine("Current User {0} and he is {1} year old", user, age);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            GameScore gs = new GameScore(); //Default Constructor Called
            GameScore gs1 = new GameScore("Clark", 35); //Overloaded Constructor.
            Console.ReadLine();
        }
    }
}
"""
